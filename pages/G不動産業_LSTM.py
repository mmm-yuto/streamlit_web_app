import streamlit as st
from PIL import Image
import pandas as pd

st.title('不動産業社')
st.caption('不動産業についての株価を分析')
st.subheader('LSTMモデルを用いて明日の株価予想値を確認することができます。')

#判断材料と正解率の詳細を表示
st.text("株価の予想の判断には不動産会社77社の\n「前日からの終値の変化率」を用いました。")
st.text("LSTMは、時系列データや自然言語処理のような連続的なデータを扱う深層学習モデルの一種です。\nRNNよりも長期的な依存関係を学習しやすく、入力の一部を忘れたり、\n新しい情報を加えたりすることができます。\nこれによって、テキストの生成や時系列データの予測など、様々なタスクに適用できます。\nLSTMは、入力ゲート、出力ゲート、忘却ゲートと呼ばれる3つの仕組みで、情報の取捨選択を行います。")


st.subheader('予想価格は以下の通りになりました。')
image1 = Image.open("./data/LSTM.png")
st.image(image1,width=500)
kekka1 = pd.DataFrame({
    "MAE": [64.08723798532196],
    "MSE": [6817.40708021852],
    "RMSE": [82.56759097986642]},
    index=["参考値"])

st.dataframe(kekka1)


st.subheader("移動平均を用いて予測した結果です")
image2 = Image.open("./data/LSTM_2.png")
st.image(image2,width=500)
kekka2 = pd.DataFrame({
    "MAE": [45.203428072676104],
    "MSE": [3343.776788042613],
    "RMSE": [57.82539916025321]},
    index=["参考値"])

st.dataframe(kekka2)

