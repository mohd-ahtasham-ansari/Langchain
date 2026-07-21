import os
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

from langchain_core.messages import AIMessage , HumanMessage ,  SystemMessage
from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model ="mistral-small-2506",temperature=0.5,max_tokens=200)

print("------------WELCOME - type 'exit' to exit the application-------------")
print("\n")

print("Choose your ai mode!")
print(" press 1 for motivational mode , 2 for sad mode , 3 for angry mode , 4 for normal mode")

choice = int(input(" Enter your mode :"))
if choice == 1:
    mode ="You are a motivational speaker, and you will always try to motivate the user and make them feel happy and positive."
elif choice == 2:
    mode = "You are a sad speaker, and you will always try to make the user feel sad and negative."
elif choice == 3:
    mode = "You are an angry speaker, and you will always try to make the user feel angry and negative."
elif choice == 4:
    mode = "You are a normal speaker, and you will always try to make the user feel normal and positive."

messages = [
    SystemMessage(content =mode),

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