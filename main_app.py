import streamlit as st
from PIL import Image

st.title('AIによる株分析サイト')
st.caption('「ニュース分析」、「業種別の株価変動予測を」扱っています')


st.header("項目一覧")

st.subheader("Aチャートを見る")
st.text("指定した区間の株価チャートをみることができます")
st.markdown("[チャートを見る](Aチャートを見る)")


# st.subheader("「Bニュース解析」")
# st.text("特定のニュースに関連性のある企業を知ることができます")

st.subheader("業種別に今後の株価予想を行います")

st.subheader("不動産業")
st.markdown("[不動産業(LSTMモデル)](G不動産業_LSTM)")
st.markdown("[不動産業(ARIMAモデル)](G不動産業_ARIMA)")
st.markdown("[不動産業(ランダムフォレストモデル)](G不動産業_ランダムフォレスト)")

