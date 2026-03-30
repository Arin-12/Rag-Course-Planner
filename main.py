import os
from google import genai

from utils import load_docs, split_docs, get_embeddings, create_db, get_retriever
from prompts import build_prompt

# 🔑 Load API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY not set")

# 🤖 Initialize Gemini 2 client
client = genai.Client(api_key=GEMINI_API_KEY)

# 📡 LLM call
def call_llm(prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text


# 🌐 URLs (ADD MORE → 25+)
urls = [
    "https://catalog.mit.edu/subjects/6/",
    "https://catalog.mit.edu/subjects/18/",
    "https://guide.berkeley.edu/courses/compsci/"
]

# 🔄 RAG Pipeline
docs = load_docs(urls)
chunks = split_docs(docs)

embeddings = get_embeddings()
db = create_db(chunks, embeddings)

retriever = get_retriever(db)


# 🔍 Main function
def generate_answer(query):
    docs = retriever.invoke(query)

    context = "\n\n".join([
        f"[Source: {d.metadata.get('source', 'unknown')}]\n{d.page_content}"
        for d in docs
    ])

    prompt = build_prompt(context, query)

    return call_llm(prompt)


# 🧪 Test
print(generate_answer("What are prerequisites for database systems?"))