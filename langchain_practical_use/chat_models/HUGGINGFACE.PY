import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# LangChain's HuggingFaceEndpoint expects the environment variable HUGGINGFACEHUB_API_TOKEN.
# We map your existing HUGGINGFACEHUB_ACCESS_TOKEN from .env to it.
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.environ.get("HUGGINGFACEHUB_ACCESS_TOKEN", "")

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
)
model = ChatHuggingFace(llm=llm)

response = model.invoke("write poem on  alps! in stoic tone ")
print(response.content)