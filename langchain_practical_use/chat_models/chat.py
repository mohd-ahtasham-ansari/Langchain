from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model="mistral-small-latest",temperature=0.7) # or "mistral-large-latest"

print(model)

response = model.invoke("write poem on  alps! in stoic tone ")
print(response.content)