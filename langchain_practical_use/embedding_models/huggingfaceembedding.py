from langchain_huggingface import HuggingFaceEmbeddings

embedding=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2" 
)
text = [
    "hello  i am a student , from glbajaj",
    "my course is btech csaiml",
    "i am excited about genrative ai agentic ai, ai , llm and ml dl etc"
]

vector = embedding.embed_documents(text)
print(vector)