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
        ("8801(三井不動産)","8802(三菱地所)","1925(大和ハウス工業)")
    )

    #ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')
    st.text('「送信」を押すと計算処理が始まります')


    if submit_btn:
        if code == "8801(三井不動産)":
            st.subheader('予想価格は以下の通りになりました。')
            st.text('過去約700日の予想精度')
            image1 = Image.open("./data/ARIMA_8801.png")
            st.image(image1,width=500)
            kekka1 = pd.DataFrame({
            "MAE": [35.83335984435268],
            "MSE": [2172.9300603345782],
            "RMSE": [46.614697900282245]},
            index=["参考値"])

            st.dataframe(kekka1)

            st.subheader("2023-03-20の次の市場の終値は2023-03-20の終値の0.9634331359040047倍になると予想しました")
        
        elif code == "8802(三菱地所)":
            st.subheader('予想価格は以下の通りになりました。')
            st.text("過去約700日の予想精度")
            image1 = Image.open("./data/ARIMA_8802.png")
            st.image(image1,width=500)
            kekka1 = pd.DataFrame({
            "MAE": [21.92008711716755],
            "MSE": [914.7628673494552],
            "RMSE": [30.245046988712964]},
            index=["参考値"])

            st.dataframe(kekka1)

            st.subheader("2023-03-20の次の市場の終値は2023-03-20の終値の0.9779553867010675倍になると予想しました")

        elif code == "1925(大和ハウス工業)":
            st.subheader('予想価格は以下の通りになりました。')
            st.text("過去約700日の予想精度")
            image1 = Image.open("./data/ARIMA_1925.png")
            st.image(image1,width=500)
            kekka1 = pd.DataFrame({
            "MAE": [37.74558700076443],
            "MSE": [2564.1021028343607],
            "RMSE": [50.63696379952456]},
            index=["参考値"])

            st.dataframe(kekka1)

            st.subheader("2023-03-20の次の市場の終値は2023-03-20の終値の0.9806140343896721倍になると予想しました")
        







