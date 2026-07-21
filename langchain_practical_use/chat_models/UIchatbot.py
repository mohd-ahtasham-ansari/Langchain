import os
import streamlit as st
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_mistralai import ChatMistralAI

st.set_page_config(page_title="Shikamaru AI Chatbot")
st.title("WELCOME - Shikamaru AI Chatbot")

model = ChatMistralAI(model="mistral-small-2506", temperature=0.5, max_tokens=200)

if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a intellectual agent with high iq and sense of humour but calm nature also sometimes bully , your goal is to help the user, your personality is like shikamaru nara in naruto shippuden"),
    ]

# display chat history (skip system message)
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

prompt = st.chat_input("You :")

if prompt:
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.write(prompt)

    response = model.invoke(st.session_state.messages)
    st.session_state.messages.append(AIMessage(content=response.content))
    with st.chat_message("assistant"):
        st.write(response.content)