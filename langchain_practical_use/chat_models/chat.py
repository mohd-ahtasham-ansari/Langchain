from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model="mistral-small-latest") # or "mistral-small-latest"

print(model)

response = model.invoke("what is alps?")
print(response.content)