import streamlit as st
from PIL import Image

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import datetime
import pandas_datareader as data

st.title('不動産業社')
st.caption('不動産業についての株価を分析')
st.subheader('ランダムフォレストを用いて\n指定された不動産業社の「株価平均」が来年上昇するかを判定します')
st.text("ランダムフォレストは、多数の決定木を組み合わせて構成されるアンサンブル学習の一種です。\n各決定木は、データのランダムサブセットを用いてトレーニングされ、それぞれが独立に予測を行います。\n最終的な予測は、各決定木の予測結果を多数決することで決定されます。\nランダムフォレストは、高い予測精度と汎化能力を持ち、データの欠損値や外れ値の扱いに強いため、\n様々な分野で広く利用されています。")
#判断材料と正解率の詳細を表示
st.text("判断に使った変数と依存度は以下の通りになっています。\n判断には「人口」「取引量の合計」「取引量の平均」「1年間の平均株価」を用いました。\n2005~2015年のデータで学習、テストしています")
image = Image.open("./data/importance.png")
st.image(image,width=500)

st.header("正解率は59~65%ほどのモデルです\n指定された年の平均株価が前年よりも上がるか、下がるかについて予想します。")



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
        memo = []

        clf = RandomForestClassifier(n_estimators=105,max_depth=4)
        x_column_list_for_multi = ["all_people","Volume_sum","Volume_mean","train_year_stooq"]
        y_column_list_for_multi = ["UpDown"]

        #all_dataのインポート
        all_data = pd.read_csv("./data/all_people_stock_data.csv",index_col=0)


        x_train = all_data[x_column_list_for_multi]
        y_train = all_data[y_column_list_for_multi]

        clf = RandomForestClassifier(n_estimators=105,max_depth=4)

        #予測
        clf.fit(x_train,y_train.values.ravel())

        #指定された年の企業の平均株価と取引量の合計を出す

        today = datetime.date.today()
        start = '2005-01-01'
        end = today

        #データのインポート
        #企業名コード
        code = code + '.JP'

        df = data.DataReader(code, 'stooq', start, end) 

        if len(df.columns) != 0:

            #終値のみを取り出す
            df = df.drop(['Open', 'Low', 'High'], axis=1)

            #年が小さいのを一番最初に並び替え
            df.sort_values(by='Date', ascending=True, inplace=True)

            
            #終値の平均
            memo1 = (df[df.index.year == int(target_year)-1].mean()["Close"])
            #取引量の合計
            memo3 = (df[df.index.year == int(target_year)-1].sum()["Volume"])
            #取引量の平均
            memo4 = df[df.index.year == int(target_year)-1].mean()["Volume"]


            y_pred = clf.predict([[people_math,memo3,memo4,memo1]])
            if y_pred == -1:
                st.subheader("指定年の次の年は株価平均は下降すると予想しました")
            elif y_pred == 1:
                st.subheader("指定年の次の年は株価平均は上昇すると予想しました")

        
        else:
            st.subheader("データが収取できず、予想できませんでした")

        



