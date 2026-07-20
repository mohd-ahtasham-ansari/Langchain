import os
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())


from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model ="mistral-small-2506",temperature=0.5)


while True:
    prompt = input("you : ")
    if prompt.lower() == "exit":
        break
    response = model.invoke(prompt)
    print("AI :",response.content) 
    print("\n")