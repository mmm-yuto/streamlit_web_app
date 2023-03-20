import streamlit as st
from PIL import Image
import pandas as pd
st.title('不動産業社')
st.caption('不動産業についての株価を分析')
st.text('明日の株価予想値を確認することができます。')

#判断材料と正解率の詳細を表示
st.text("会社の終値データを用いて、ARIMAモデルにて、株価を予測しました")
st.text("ARIMAモデルは、ある時系列データに潜在する、トレンドや季節性などのパターンを分析し、\n未来のデータを予測するための手法です。\nARIMAとは、「自己回帰和移動平均モデル」を意味し、\n時間の推移に伴って発生する自己相関や移動平均などを組み合わせたモデルです。")


st.subheader('予想価格は以下の通りになりました。')
image1 = Image.open("./data/ARIMA_1.png")
st.image(image1,width=500)

kekka1 = pd.DataFrame({
    "MAE": 35.56140532155124,
    "MSE": 2133.7651921476527,
    "RMSE": 46.19269630739964,},
    index=["参考値"])

st.dataframe(kekka1)
