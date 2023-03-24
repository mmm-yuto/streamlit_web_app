import streamlit as st
from PIL import Image
import pandas as pd

st.title('不動産業社')
st.caption('不動産業についての株価を分析')
st.subheader('LSTMモデルを用いて明日の株価予想値を確認することができます。')

#判断材料と正解率の詳細を表示
st.text("株価の予想の判断には不動産会社77社の\n「前日からの終値の変化率」を用いました。")
st.text("LSTMは、時系列データや自然言語処理のような連続的なデータを扱う深層学習モデルの一種です。\nRNNよりも長期的な依存関係を学習しやすく、入力の一部を忘れたり、\n新しい情報を加えたりすることができます。\nこれによって、テキストの生成や時系列データの予測など、様々なタスクに適用できます。\nLSTMは、入力ゲート、出力ゲート、忘却ゲートと呼ばれる3つの仕組みで、情報の取捨選択を行います。")


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
            st.text('過去約400日の予想精度')
            image1 = Image.open("./data/LSTM_8801.png")
            st.image(image1,width=500)
            kekka1 = pd.DataFrame({
            "MAE": [45.627224198190795],
            "MSE": [436.574050841363],
            "RMSE": [58.62229994499843]},
            index=["参考値"])

            st.dataframe(kekka1)

            st.subheader("2023-03-23の次の市場の終値は2023-03-23の終値の0.9907976倍になると予想しました")
        
        elif code == "8802(三菱地所)":
            st.subheader('予想価格は以下の通りになりました。')
            st.text("過去約400日の予想精度")
            image1 = Image.open("./data/LSTM_8802.png")
            st.image(image1,width=500)
            kekka1 = pd.DataFrame({
            "MAE": [27.099531763980263],
            "MSE": [1232.9539533063669],
            "RMSE": [35.11344405361523]},
            index=["参考値"])

            st.dataframe(kekka1)

            st.subheader("2023-03-23の次の市場の終値は2023-03-23の終値の0.99128675倍になると予想しました")

        elif code == "1925(大和ハウス工業)":
            st.subheader('予想価格は以下の通りになりました。')
            st.text("過去約400日の予想精度")
            image1 = Image.open("./data/LSTM_1925.png")
            st.image(image1,width=500)
            kekka1 = pd.DataFrame({
            "MAE": [47.74080555098683],
            "MSE": [3619.363810274465],
            "RMSE": [60.161148678149964]},
            index=["参考値"])

            st.dataframe(kekka1)

            st.subheader("2023-03-23の次の市場の終値は2023-03-23の終値の1.0055104倍になると予想しました")

