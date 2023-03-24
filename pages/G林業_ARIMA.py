import pandas as pd
import pandas_datareader.data as data
import streamlit as st
from PIL import Image

st.title('不動産業社')
st.caption('不動産業についての株価を分析')
st.subheader('ARIMAモデルを用いて明日の株価予想値を確認することができます。')

#判断材料と正解率の詳細を表示
st.text("株価の終値データを用いて、ARIMAモデルにて、株価を予測しました")
st.text("ARIMAモデルは、ある時系列データに潜在する、トレンドや季節性などのパターンを分析し、\n未来のデータを予測するための手法です。\nARIMAとは、「自己回帰和移動平均モデル」を意味し、\n時間の推移に伴って発生する自己相関や移動平均などを組み合わせたモデルです。")


#自動でリロードされないようにする
with st.form(key='profile_form'):
    #銘柄を指定
    #セレクトボックス
    code = st.radio(
        '銘柄を選択',
        ("1911(住友林業)","6250(やまびこ)","9514(エフオン)")
    )

    #ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')
    st.text('「送信」を押すと計算処理が始まります')


    if submit_btn:
        if code == "1911(住友林業)":
            st.subheader('予想価格は以下の通りになりました。')
            st.text('過去約700日の予想精度')
            image1 = Image.open("./data/ARIMA_1911.png")
            st.image(image1,width=500)
            kekka1 = pd.DataFrame({
            "MAE": [30.196633840395187],
            "MSE": [1675.5472249171391],
            "RMSE": [40.933448729824114]},
            index=["参考値"])

            st.dataframe(kekka1)

            st.subheader("2023-03-23の次の市場の終値は2023-03-23の終値の0.9882147129105205倍になると予想しました")
        
        elif code == "6250(やまびこ)":
            st.subheader('予想価格は以下の通りになりました。')
            st.text("過去約700日の予想精度")
            image1 = Image.open("./data/ARIMA_6250.png")
            st.image(image1,width=500)
            kekka1 = pd.DataFrame({
            "MAE": [17.30566021888185],
            "MSE": [619.9966844106985],
            "RMSE": [24.89973261725311]},
            index=["参考値"])

            st.dataframe(kekka1)

            st.subheader("2023-03-23の次の市場の終値は2023-03-23の終値の0.993093858569969倍になると予想しました")

        elif code == "9514(エフオン)":
            st.subheader('予想価格は以下の通りになりました。')
            st.text("過去約700日の予想精度")
            image1 = Image.open("./data/ARIMA_9514.png")
            st.image(image1,width=500)
            kekka1 = pd.DataFrame({
            "MAE": [17.095352358873836],
            "MSE": [761.740185169827],
            "RMSE": [27.599641033350906]},
            index=["参考値"])

            st.dataframe(kekka1)

            st.subheader("2023-03-23の次の市場の終値は2023-03-23の終値の0.9771256198597856倍になると予想しました")
        







