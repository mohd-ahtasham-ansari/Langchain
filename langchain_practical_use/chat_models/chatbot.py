import os
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())


from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model ="mistral-small-2506",temperature=0.5)

response = model.invoke("hi")


print(response.content)