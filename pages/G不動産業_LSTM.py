import streamlit as st
from PIL import Image

st.title('不動産業社')
st.caption('不動産業についての株価を分析')
st.subheader('明日の株価予想値を確認することができます。')

#判断材料と正解率の詳細を表示
st.text("株価の予想の判断には不動産会社77社の\n「前日からの終値の変化率」を用いました。")



st.subheader('予想価格は以下の通りになりました。')
image = Image.open("./data/LSTM.png")
st.image(image,width=500)



