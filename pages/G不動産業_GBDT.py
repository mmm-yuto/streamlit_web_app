import pandas as pd
import numpy as np
import datetime
import pandas_datareader as data
import streamlit as st
from PIL import Image

st.title('不動産業社')
st.caption('不動産業についての株価を分析')
st.subheader('GBDT(勾配ブースティング木)を用いて指定された不動産業社の「株価平均」が来年上昇するかを判定します')
st.text("勾配ブースティング木(Gradient Boosting Tree)は、\n機械学習のアルゴリズムの一つであり、複数の決定木を組み合わせて予測を行う手法です。\n各決定木は前の決定木の予測結果の誤差を学習し、次の決定木でそれを補正することで、\n精度を向上させます。このように、複数の決定木を順番に構築していくことで、\n予測の精度が向上することが特徴です。")
#判断材料と正解率の詳細を表示
st.text("判断に使った変数と依存度は以下の通りになっています。\n判断には「人口」「取引量の合計」「取引量の平均」「1年間の平均株価」を用いました。\n2005~2015年のデータで学習、テストしています")
image = Image.open("./data/importance_GBDT.png")
st.image(image,width=500)

st.header("正解率は55~59%ほどのモデルです\n指定された年の平均株価が前年よりも上がるか、下がるかについて予想します。")



#自動でリロードされないようにする
with st.form(key='profile_form'):
    #銘柄を指定
    code = st.text_input(
        "銘柄コードを入力（例:1878)"
    )

    #調べたい年を入力
    target_year = st.text_input(
        "調べたい年を入力(2024年の平均株価を調べたいなら:2024)"
    )

    #調べたい年の前年の人口を入力
    people_math = st.text_input(
        "調べたい年の前年の日本の人口を入力(例:120000000)"
    )

    #ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')
    st.text('「送信」を押すと計算処理が始まります')


    if submit_btn:
        x_column_list_for_multi = ["all_people","Volume_sum","Volume_mean","train_year_stooq"]
        y_column_list_for_multi = ["UpDown"]
        x_col = np.array(x_column_list_for_multi)

        #all_dataのインポート
        all_data = pd.read_csv("./data/all_people_stock_data.csv",index_col=0)

        x = all_data[x_column_list_for_multi].to_numpy()
        Y = all_data[y_column_list_for_multi].to_numpy()

        y = []
        for i in Y:
            if i[0] == -1:
                y.append(0)
            else:
                y.append(i[0])
        y = np.array(y)

        import xgboost as xgb
        from sklearn.model_selection import cross_validate,cross_val_predict, StratifiedKFold
        
        splits = 5
        skf = StratifiedKFold(n_splits=splits, shuffle=False)
        score_funcs = ["accuracy","precision_macro","recall_macro","f1_macro"]
        
        clf = xgb.XGBClassifier(max_depth=10,objective="binary:logistic")
        
        score = cross_validate(clf, x, y, cv=skf, scoring=score_funcs,return_estimator=True)

        #予測
        #ある年の人口、ある不動産会社の指定された年の取引量合計、平均、その年の株価平均がわかれば良い
        today = datetime.date.today()
        start = '2005-01-01'
        end = today

        #データのインポート
        #企業名コード

        df = data.DataReader(str(code)+".jp", 'stooq', start, end) 

        if len(df.columns) != 0:

            #終値のみを取り出す
            df = df.drop(['Open', 'Low', 'High'], axis=1)

            #年が小さいのを一番最初に並び替え
            df.sort_values(by='Date', ascending=True, inplace=True)

            #抽出したい年を指定
            i = int(target_year)-1

            #終値の平均
            memo1 = (df[df.index.year == i].mean()["Close"])
            #取引量の合計
            memo3 = (df[df.index.year == i].sum()["Volume"])
            #取引量の平均
            memo4 = df[df.index.year == i].mean()["Volume"]
            #指定された年の次の年の終値の平均
            memo2 = (df[df.index.year == i+1].mean()["Close"])

            ans = score["estimator"][0].predict([[int(people_math),memo3,memo4,memo1]])
            if ans == 1:
                st.subheader("指定年は株価平均は上昇すると予想しました")
            elif ans == 0:
                st.subheader("指定年は株価平均は下降すると予想しました")
            else:
                st.subheader("予想できませんでした")


            
        else:
            st.subheader('データが収取できず、予想できませんでした')

        







