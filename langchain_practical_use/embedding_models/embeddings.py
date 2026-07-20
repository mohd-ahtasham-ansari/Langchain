from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    dimensions = 64
)
text = [
    "hello  i am a student , from glbajaj",
    "my course is btech csaiml",
    "i am excited about genrative ai agentic ai, ai , llm and ml dl etc"
]

vector = embeddings.embed_documents(text)
print(vector)