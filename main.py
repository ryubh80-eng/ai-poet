# from dotenv import load_dotenv
# load_dotenv()

# from langchain_openai import OpenAI
# llm = OpenAI()
# result = llm.invoke("내가 좋아하는 동물은")
# print(result)

import streamlit as st
from langchain_openai import ChatOpenAI

st.title("인공지능 시인")

content = st.text_input("시의 주제를 제시해주세요.")

if st.button("시 작성 요청하기"):
    if not content.strip():
        st.warning("시의 주제를 입력해주세요.")
    else:
        chat_model = ChatOpenAI(model="gpt-4o-mini")
        result = chat_model.invoke(f"{content}에 대한 시를 써줘").content
        st.write(result)


# title = st.text_input("시의 주제를 제시해주세요.")
# st.write("시의 주제는", title)
