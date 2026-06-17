import json

path = r'c:\Users\hp\Desktop\Ai and agents\Langchain\updatedlangchain\2-modelintegration.ipynb'
with open(path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell.get('cell_type') == 'code':
        source = "".join(cell.get('source', []))
        if 'gpt-4.1' in source or 'init_chat_model(model="gpt' in source:
            cell['source'] = [
                "from langchain.chat_models import init_chat_model\n",
                "model=init_chat_model(model=\"llama3-8b-8192\", model_provider=\"groq\")\n",
                "model"
            ]
            cell['outputs'] = []
            cell['execution_count'] = None
        elif 'response=model.invoke' in source:
            cell['outputs'] = []
            cell['execution_count'] = None

with open(path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)
