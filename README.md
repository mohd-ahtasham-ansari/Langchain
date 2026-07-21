# LangChain Learning Journey 🚀

Welcome to my LangChain learning repository! This project documents my phase of exploring and mastering LangChain, a powerful framework for developing applications powered by language models.

## 📚 Topics Covered

Throughout this learning phase, I've dived deep into various core components of LangChain, as structured in the `updatedlangchain` directory:
1. **Introduction to LangChain** (`1-langchain_intro.ipynb`) - Understanding the basics and core philosophy.
2. **Model Integration** (`2-modelintegration.ipynb`) - Connecting to different LLMs (OpenAI, Groq, etc.).
3. **Tools & Function Calling** (`3-tools.ipynb`) - Empowering models to take actions and use external tools.
4. **Messages & Chat History** (`4-messages.ipynb`) - Managing conversation state with Human, AI, and System messages.
5. **Structured Output** (`5-structuredOutput.ipynb`) - Forcing LLMs to return predictable, structured data (e.g., JSON).
6. **Middleware & Advanced Chains** (`6-middleware.ipynb`) - Building complex workflows and handling middleware concepts.
## 🛠️ LangChain Practical Use (Mini Projects)

While the initial tutorials focused on understanding core concepts, the `langchain_practical_use` directory is where these concepts are put into practice. This folder demonstrates real-world applications of LangChain by building standalone scripts and full mini-projects. It is structured to separate different practical implementations, such as chat models and embedding models, showing how to integrate everything from UIs (Streamlit) to specific persona prompting.

### 1. Shikamaru AI Chatbot (`langchain_practical_use/chat_models/UIchatbot.py`)
A web-based conversational AI built using **Streamlit** and **LangChain**. It leverages the `Mistral` model (via `ChatMistralAI`) and is instructed via a `SystemMessage` to act like Shikamaru Nara from Naruto—highly intelligent but strategically lazy.

<img width="1919" height="827" alt="1-mini_project_aiChatbot" src="https://github.com/user-attachments/assets/20d013b8-5da2-465d-887d-6ebef992f476" />


**Key Features:**
- **Streamlit UI**: Created an interactive chat interface using `st.chat_message` and `st.chat_input`.
- **Session State Memory**: Streamlit re-runs the script on every user interaction. I learned how to use `st.session_state` to persist the conversation history so the LangChain model maintains context.
- **Persona Prompting**: Set up a persistent character using a `SystemMessage` at the start of the chat history.

### 2. Terminal Persona Chatbot (`langchain_practical_use/chat_models/chatbot.py`)
A CLI-based conversational AI where users can select the AI's mood/persona before starting the chat (e.g., Motivational, Sad, Angry, or Normal). Built using the `Mistral` model, it dynamically adjusts behavior using a `SystemMessage`.

### 3. Local Model & HuggingFace Integrations (`langchain_practical_use/chat_models/`)
Explorations into connecting with the HuggingFace Hub and running models locally to reduce API dependency. Includes scripts like `HUGGINGFACE.PY` and `localmodel.py`.

### 4. Text Embeddings (`langchain_practical_use/embedding_models/`)
Practical examples of generating vector embeddings for text data, which is essential for RAG (Retrieval-Augmented Generation) applications. 
- **Google GenAI Embeddings** (`embeddings.py`)
- **HuggingFace MiniLM Embeddings** (`huggingfaceembedding.py`)

## 🚧 Errors Faced & Lessons Learned

Learning LangChain involved hands-on debugging. Here are some key errors I encountered and what I learned from them:

- **`RateLimitError` (OpenAI 429 Insufficient Quota)**: 
  - **The Error**: Encountered `openai.RateLimitError` due to exceeding current API quotas (`insufficient_quota`).
  - **The Learning**: I learned how to handle API limits gracefully and the importance of having fallback models. This led to exploring and integrating alternative, fast providers like **Groq** (using `llama-3.1-8b-instant`) to keep development moving without friction.
  
- **Output Parsing Errors**:
  - **The Error**: Issues where the LLM's response didn't perfectly match the expected schema, resulting in parsing exceptions (e.g., tracking `parsing_error` when using structured outputs).
  - **The Learning**: I realized that LLMs can be unpredictable. I learned how to use LangChain's structured output parsers, how to write robust prompts to enforce JSON structures, and how to handle edge cases where the LLM deviates from instructions.

- **Environment & Key Management**:
  - **The Learning**: Safely managing multiple API keys using `.env` files is critical. LangChain's seamless integration with environment variables makes it easy to manage configurations securely.

- **Parameter Typos (`422 Unprocessable Entity`)**:
  - **The Error**: Encountered a 422 HTTP error when initializing models (like Mistral) because of a typo in the parameters, specifically `temprature` instead of `temperature`.
  - **The Learning**: LangChain often passes unexpected kwargs directly to the underlying API providers. A small typo in model parameters can lead to hard-to-debug HTTP errors. It is crucial to verify parameter spelling and valid ranges.

- **Local LLMs & Dependencies (`PyTorch was not found` / `ImportError`)**:
  - **The Error**: When trying to run models locally via `HuggingFacePipeline` or `HuggingFaceEmbeddings`, I encountered missing dependencies or `PyTorch was not found` errors.
  - **The Learning**: Using local models requires a properly configured environment. Installing specific integrations like `langchain-huggingface` and backend dependencies like `sentence-transformers` or `torch` is essential.

- **Invalid Model IDs & Authentication**:
  - **The Error**: Encountered `BadRequestError: 400 - invalid model ID` and HuggingFace API token authentication errors.
  - **The Learning**: Always verify the exact model name required by the specific provider and ensure environment variables (e.g., `HUGGINGFACEHUB_API_TOKEN`) are correctly loaded.
- **Streamlit Execution & Session Management**:
  - **The Error**: The Streamlit server would sometimes stop unexpectedly (exit code 1) or fail to start properly in the terminal.
  - **The Learning**: I learned that running local web servers like Streamlit requires stable terminal environments. Additionally, dealing with Streamlit's stateless nature taught me the absolute necessity of using `st.session_state` to store message history; otherwise, the LangChain model loses the entire conversation context upon every new input.

## 💪 Confidence in LangChain

Despite the initial learning curve and the errors encountered along the way, I am **highly confident** in LangChain as my go-to framework. 

It provides an incredibly robust and flexible abstraction layer over raw LLM APIs. By standardizing how we interact with models, tools, and prompts, LangChain makes it remarkably easy to swap out components (like smoothly switching from OpenAI to Groq when hitting rate limits) and build complex, reliable AI applications. The framework handles the heavy lifting, allowing me to focus on building the actual logic of the AI agents. I am excited to leverage this framework to build production-ready applications!
