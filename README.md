# LangChain Learning Journey 🚀

Welcome to my LangChain learning repository! This project documents my journey exploring and mastering **LangChain** and **LangGraph**, from foundational concepts and multi-provider model integration to advanced agent middleware, Human-in-the-Loop (HITL) workflows, and production guardrails.

---

## 📁 Repository Structure

```text
├── 1-mini_project_aiChatbot.png     # Screenshot of the Streamlit Shikamaru AI Chatbot
├── README.md                        # Project documentation and learning log
├── main.py                          # Entry point script
├── pyproject.toml                   # Project dependencies and environment metadata
├── requirements.txt                 # Pip dependency definitions
├── updatedlangchain/                # Core concepts & interactive Jupyter notebooks
│   ├── 1-langchain_intro.ipynb      # LangChain basics & architecture
│   ├── 2-modelintegration.ipynb     # Connecting OpenAI, Groq, Mistral, Google GenAI
│   ├── 3-tools.ipynb                # Tool binding & function calling
│   ├── 4-messages.ipynb             # Message types (Human, AI, System, Tool) & memory
│   ├── 5-structuredOutput.ipynb     # Typed & validated schemas via Pydantic & JSON
│   ├── 6-middleware.ipynb           # Summarization & Human-in-the-loop agent middleware
│   └── langchain_gaurdrails.ipynb   # Deterministic & model-based guardrails, PII & hooks
└── langchain_practical_use/         # Hands-on scripts & mini-applications
    ├── chat_models/
    │   ├── UIchatbot.py             # Streamlit-based Shikamaru Persona Chatbot
    │   ├── chatbot.py               # Interactive CLI persona chatbot
    │   ├── chat.py                  # Direct Mistral AI chat completion script
    │   ├── localmodel.py            # Local HuggingFace pipeline with TinyLlama
    │   └── HUGGINGFACE.PY           # HuggingFace Endpoint integration (DeepSeek)
    └── embedding_models/
        ├── embeddings.py            # Google Generative AI vector embeddings
        └── huggingfaceembedding.py  # HuggingFace MiniLM vector embeddings
```

---

## 📚 Topics Covered

The `updatedlangchain/` directory contains interactive walkthroughs diving deep into core abstractions and modern agent patterns:

1. **Introduction to LangChain** (`1-langchain_intro.ipynb`)
   - Overview of the LangChain ecosystem and core design principles.
   - Initializing prompts, runnables, and chain pipelines.

2. **Model Integration** (`2-modelintegration.ipynb`)
   - Multi-provider setup across **OpenAI**, **Groq**, **Mistral AI**, and **Google GenAI**.
   - Comparing streaming, temperature control, and provider parameters.

3. **Tools & Function Calling** (`3-tools.ipynb`)
   - Defining custom tools with the `@tool` decorator.
   - Binding tools to models and handling structured tool calls and execution outputs.

4. **Messages & Chat History** (`4-messages.ipynb`)
   - Managing conversational state using `HumanMessage`, `AIMessage`, `SystemMessage`, and `ToolMessage`.
   - Handling multi-turn dialogues and context retention.

5. **Structured Output** (`5-structuredOutput.ipynb`)
   - Forcing models to adhere to strictly typed schemas using **Pydantic** models.
   - Validating fields, parsing JSON responses, and preventing schema hallucinations.

6. **Agent Middleware & Context Management** (`6-middleware.ipynb`)
   - **SummarizationMiddleware**: Automatically truncating or summarizing conversation histories using token limits, message counts, or fraction triggers to prevent context window overflow.
   - State checkpointing with LangGraph's `InMemorySaver` for multi-turn persistence.

7. **Agent Guardrails & Safety Middleware** (`langchain_gaurdrails.ipynb`) 🛡️
   - **Architectural Approaches**: Comparing deterministic (regex/keyword) filtering vs. model-based LLM safety evaluators.
   - **Built-in `PIIMiddleware`**:
     - Redacting sensitive information (e.g. emails with `strategy="redact"`).
     - Masking confidential numbers (e.g. credit cards with `strategy="mask"`).
     - Blocking requests containing credentials via custom detectors and universal API key regex (`strategy="block"`).
   - **Human-in-the-Loop Middleware (`HumanInTheLoopMiddleware`)**:
     - Intercepting high-stakes tool executions (sending emails, modifying databases) with `interrupt_on`.
     - Resuming paused workflows using `Command(resume={"decisions": [...]})` with review actions (approve, reject, edit).
   - **Custom Middleware Hooks**:
     - *Inbound Defense (`before_agent`)*: Deterministic keyword filtering using `@hook_config(can_jump_to=["end"])` to abort unsafe prompts at zero LLM token cost.
     - *Outbound Defense (`after_agent`)*: Model-based safety judge verifying LLM outputs before they reach the user.

---

## 🛠️ LangChain Practical Use (Mini Projects)

The `langchain_practical_use/` directory demonstrates how these foundational concepts translate into standalone scripts and interactive applications.

### 1. Shikamaru AI Chatbot (`langchain_practical_use/chat_models/UIchatbot.py`)
A web-based conversational application built with **Streamlit** and **LangChain** featuring the persona of Shikamaru Nara from *Naruto*.
- **Streamlit UI**: Clean chat layout using `st.chat_message` and `st.chat_input`.
- **Session State Persistence**: Uses `st.session_state.messages` to preserve conversational history across Streamlit reruns.
- **Persona Prompting**: Persistent character guidance via a foundational `SystemMessage`.

<img width="1919" height="827" alt="1-mini_project_aiChatbot" src="1-mini_project_aiChatbot.png" />

### 2. Terminal Persona Chatbot (`langchain_practical_use/chat_models/chatbot.py`)
A CLI-based chatbot allowing users to choose dynamic conversational tones (Motivational, Sad, Angry, Normal) driven by `ChatMistralAI` and configurable system instructions.

### 3. Stoic Poetry Generator (`langchain_practical_use/chat_models/chat.py`)
A minimal testing script demonstrating parameterized completions using `ChatMistralAI` with strict `max_tokens` limits and temperature tuning.

### 4. Local & Remote Hugging Face Models
- **Offline Inference (`localmodel.py`)**: Runs local models on device (e.g., `TinyLlama/TinyLlama-1.1B-Chat-v1.0`) using `HuggingFacePipeline` without cloud API latency or costs.
- **Serverless Hub Endpoint (`HUGGINGFACE.PY`)**: Connects to hosted Hugging Face endpoints (such as `deepseek-ai/DeepSeek-R1`) using `HuggingFaceEndpoint` and `ChatHuggingFace`.

### 5. Vector Embeddings (`langchain_practical_use/embedding_models/`)
Techniques for embedding generation essential for vector search and RAG systems:
- **Google GenAI Embeddings (`embeddings.py`)**: Vector generation with dimensionality control (`gemini-embedding-001`).
- **Hugging Face Sentence Transformers (`huggingfaceembedding.py`)**: Lightweight, local embeddings using `sentence-transformers/all-MiniLM-L6-v2`.

---

## 🚧 Errors Faced & Lessons Learned

Hands-on development with cutting-edge agent frameworks naturally brings hurdles. Here is what went wrong and how it was resolved:

- **`RateLimitError` (OpenAI 429 Insufficient Quota)**:
  - *The Error*: Exhausted OpenAI credits when testing models and safety evaluators.
  - *The Learning*: Built resilience into the codebase by introducing fast, generous fallback providers such as **Groq** (`llama-3.1-8b-instant`, `llama-3.3-70b-versatile`, `gpt-oss-20b`), decoupling development from single-vendor downtime or quotas.

- **Agent Interrupts & Checkpointing in HITL Middleware**:
  - *The Error*: Attempting to use `HumanInTheLoopMiddleware` or interrupt commands without persistent state resulted in errors or lost agent memory.
  - *The Learning*: Interventions and approval loops require a checkpointer (e.g. `InMemorySaver()`) along with thread-specific configurations (`configurable={"thread_id": "..."}`) so LangGraph can store interrupted state and resume via `Command(resume=...)`.

- **PII Detection Nuances & Strategy Enforcement**:
  - *The Error*: Default detection patterns failed to detect diverse API key formats, or sensitive strings bypassed naive filters.
  - *The Learning*: Implemented comprehensive regex (`UNIVERSAL_API_KEY_REGEX`) covering provider prefixes (OpenAI, Groq, Google, AWS, Slack, GitHub) and mastered different enforcement strategies (`strategy="redact"`, `"mask"`, or `"block"`).

- **Output Parsing & Schema Inconsistencies**:
  - *The Error*: LLMs occasionally returned Markdown wrappers around JSON or missing schema properties, triggering parsing errors.
  - *The Learning*: Switched to Pydantic-based structured outputs with `with_structured_output` and explicit schemas, adding guardrails to ensure clean, type-validated data objects.

- **Local Pipeline Environment & Torch Dependencies**:
  - *The Error*: Running local Hugging Face pipelines triggered `PyTorch was not found` and missing wheel warnings.
  - *The Learning*: Configured local virtual environments with matching `torch`, `transformers`, and `langchain-huggingface` package versions for seamless offline execution.

- **HTTP 422 Unprocessable Entity (Parameter Typos)**:
  - *The Error*: Misspelled kwargs (such as `temprature` instead of `temperature`) were passed straight to provider endpoints.
  - *The Learning*: Understood that LangChain keyword dictionaries route directly to underlying client SDKs. Verified strict keyword spelling and validation against model specifications.

- **Streamlit State Management Across Re-runs**:
  - *The Error*: Conversational context vanished after each user message submission in Streamlit.
  - *The Learning*: Leveraged Streamlit's `st.session_state` to store message arrays, synchronizing web UI state with LangChain message histories.

---

## ⚙️ Environment & Setup

### Prerequisites
- Python `>= 3.11` (Repository tested on `3.14`)
- Virtual environment manager (`uv` or `venv`)

### 1. Installation
Using `uv`:
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
```

Or using standard `pip`:
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Environment Variables
Create a `.env` file in the root directory:
```env
# Primary LLM API Keys
GROQ_API_KEY=your_groq_api_key_here
MISTRAL_API_KEY=your_mistral_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
GEMINI_API_KEY=your_google_gemini_api_key_here

# Hugging Face
HUGGINGFACEHUB_ACCESS_TOKEN=your_hf_token_here
```

### 3. Running the Mini-Projects
- **Launch the Streamlit Chatbot:**
  ```bash
  streamlit run langchain_practical_use/chat_models/UIchatbot.py
  ```
- **Run the CLI Persona Chatbot:**
  ```bash
  python langchain_practical_use/chat_models/chatbot.py
  ```
- **Run Embeddings:**
  ```bash
  python langchain_practical_use/embedding_models/embeddings.py
  ```

---

## 💪 Confidence in LangChain

Mastering LangChain has demonstrated the immense power of having a unified, composable interface over diverse AI providers. 

From effortless provider swapping (switching from OpenAI to Groq seamlessly) to orchestrating stateful agents with deterministic input filters, PII redactors, and human approval interrupts, LangChain and LangGraph provide the robust scaffolding needed to build production-grade, reliable AI systems.
