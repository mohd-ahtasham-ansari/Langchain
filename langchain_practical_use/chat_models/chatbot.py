import os
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

from langchain_core.messages import AIMessage , HumanMessage ,  SystemMessage
from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model ="mistral-small-2506",temperature=0.5,max_tokens=200)

print("------------WELCOME - type 'exit' to exit the application-------------")
print("\n")

messages = [
    SystemMessage(content ="You are a intellectual agent with high iq and sense of humour but calm nature also sometimes bully , your goal is to help the user"),

]

while True:
    prompt = input(" You : ")
    messages.append(HumanMessage(content =prompt))
    if prompt.lower() == "exit":
        break
    response = model.invoke(messages)
    messages.append(AIMessage(content = response.content))
    print("AI :",response.content) 
    print("\n")

print(messages)