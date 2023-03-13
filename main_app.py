import streamlit as st
from PIL import Image

st.title('AIによる株分析サイト')
st.caption('「ニュース分析」、「業種別の株価変動予測を」扱っています')


st.header("項目")

st.subheader("「Aチャートを見る」")
st.text("指定した区間の株価チャートをみることができます")

st.subheader("「Bニュース解析」")
st.text("特定のニュースに関連性のある企業を知ることができます")

st.subheader("「G業種別株価予想AI」")
st.text("業種別に今後の株価予想を行います")
