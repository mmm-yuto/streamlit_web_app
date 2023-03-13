# モジュールのインポート
import numpy as np
import pandas as pd
import pandas_datareader.data as data
from matplotlib import pyplot as plt
import datetime

import streamlit as st


st.title('チャートを見る')
st.caption('日時と銘柄を指定してチャートを見る')

start = "2023-01-01"
end = datetime.datetime.today()

st.text("7203.JP\n" + str(start) + "から現在(" + str(end) + ")")
df = data.DataReader('4689.JP', 'stooq', start, end) 
st.line_chart(df["Close"])


#自動でリロードされないようにする
with st.form(key='profile_form'):
    #銘柄を指定
    code = st.text_input(
        "銘柄コードを入力（例:7203)"
    )

    #見たい範囲を指定
    start = st.date_input(
        "開始日"
    )
    end = st.date_input(
        "終了日"
    )

    #ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')

    if submit_btn:
        #データのインポート
        df = data.DataReader(str(code)+'.JP', 'stooq', start, end) 
        st.line_chart(df["Close"])






