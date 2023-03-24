import streamlit as st
from PIL import Image
import pandas as pd

st.title('林業')
st.caption('林業についての株価を分析')
st.subheader('LSTMモデルを用いて明日の株価予想値を確認することができます。')

#判断材料と正解率の詳細を表示
st.text("株価の予想の判断には会社の\n「前日からの終値の変化率」を用いました。")
st.text("LSTMは、時系列データや自然言語処理のような連続的なデータを扱う深層学習モデルの一種です。\nRNNよりも長期的な依存関係を学習しやすく、入力の一部を忘れたり、\n新しい情報を加えたりすることができます。\nこれによって、テキストの生成や時系列データの予測など、様々なタスクに適用できます。\nLSTMは、入力ゲート、出力ゲート、忘却ゲートと呼ばれる3つの仕組みで、情報の取捨選択を行います。")


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
            st.text('過去約400日の予想精度')
            image1 = Image.open("./data/LSTM_1911.png")
            st.image(image1,width=500)
            kekka1 = pd.DataFrame({
            "MAE": [63.57793715049341],
            "MSE": [6083.924301324036],
            "RMSE": [77.99951475056776]},
            index=["参考値"])

            st.dataframe(kekka1)

            st.subheader("2023-03-23の次の市場の終値は2023-03-23の終値の0.9976123倍になると予想しました")
        
        elif code == "6250(やまびこ)":
            st.subheader('予想価格は以下の通りになりました。')
            st.text("過去約400日の予想精度")
            image1 = Image.open("./data/LSTM_6250.png")
            st.image(image1,width=500)
            kekka1 = pd.DataFrame({
            "MAE": [27.400918378906248],
            "MSE": [1408.7859832598033],
            "RMSE": [37.53379787950859]},
            index=["参考値"])

            st.dataframe(kekka1)

            st.subheader("2023-03-23の次の市場の終値は2023-03-23の終値の1.010911倍になると予想しました")

        elif code == "9514(エフオン)":
            st.subheader('予想価格は以下の通りになりました。')
            st.text("過去約400日の予想精度")
            image1 = Image.open("./data/LSTM_9514.png")
            st.image(image1,width=500)
            kekka1 = pd.DataFrame({
            "MAE": [23.6924844140625],
            "MSE": [1590.9509443889456],
            "RMSE": [39.886726418558666]},
            index=["参考値"])

            st.dataframe(kekka1)

            st.subheader("2023-03-23の次の市場の終値は2023-03-23の終値の1.0155993倍になると予想しました")

