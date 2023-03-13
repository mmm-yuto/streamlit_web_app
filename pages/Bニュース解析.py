import streamlit as st
from PIL import Image

st.title('ニュース解析')
st.caption('ニュースを解析し、関連のある企業情報を提供します')
st.text("これはGPTを用いて関連性のある企業を考えています。したがって出力結果が確実性のあるものではありません。")

#gptの関数
def gpt(text):
    import openai

    openai.api_key = "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"

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= "次の記事から「企業名」と「材料名」を抽出してください。" + text,
    temperature=0.7,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    ans1 = response["choices"][0]["text"]
    ans = ans1.replace("\n","").replace("-","")
    

    material = ans[:ans.find("企業名")-1].replace("材料名:","").replace(" ","")
    enterprise = ans[ans.find("企業名"):].replace("企業名:","").replace(" ","")
    material = material.split("、")

    for mate in material:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt= "「" + mate + "」が含まれる業種の日本企業において、「" + mate + "」との関連性が高い企業を10社まで答えてください",
        temperature=0.7,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        ans = response["choices"][0]["text"].replace("\n","").replace("。","")
        

    return "記事内に書いてある企業名、材料名（モノ）" + str(ans1) + "\n材料名と関連性が高い企業\n" + str(ans)




#自動でリロードされないようにする
with st.form(key='profile_form'):


    #テキストボックス
    news_data = st.text_input('ニュース記事をコピペしてください')


    #ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')

    if submit_btn:
        st.text(gpt(news_data))