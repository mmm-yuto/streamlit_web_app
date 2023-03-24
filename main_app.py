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
st.text("回帰分析")
st.markdown("[不動産業(LSTMモデル)](G不動産業_LSTM)")
st.markdown("[不動産業(ARIMAモデル)](G不動産業_ARIMA)")
st.text("分類分析")
st.markdown("[不動産業(ランダムフォレスト)](G不動産業_ランダムフォレスト)")
st.markdown("[不動産業(勾配ブースティング木)](G不動産業_GBDT)")

st.subheader("林業")
st.text("回帰分析")
st.markdown("[林業(LSTMモデル)](G林業_LSTM)")
st.markdown("[林業(ARIMAモデル)](G林業_ARIMA)")


st.text("分類分析")
st.markdown("[林業(ランダムフォレスト)](G林業_ランダムフォレスト)")
st.markdown("[林業(勾配ブースティング木)](G林業_GBDT)")



st.header('以下の業種はまだ実装していない')
st.subheader("サービス業")
st.subheader("小売飲食業")
st.subheader("建設業")
st.subheader("水産業")
st.subheader("製造業")
st.subheader("運搬通信業")
st.subheader("金融保険業")
st.subheader("鉱業")
st.subheader("電気ガス業")
