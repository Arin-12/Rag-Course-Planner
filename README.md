# 📚 Agentic RAG Course Planning Assistant

## 🚀 Overview
This project implements a **Retrieval-Augmented Generation (RAG)** system that helps students with course planning using academic catalog data.

The assistant answers:
- 📌 Prerequisite queries  
- 📌 Course eligibility decisions  
- 📌 Program requirement questions  
- 📌 Safely abstains when information is missing  

All responses are **strictly grounded in catalog documents with citations**.

---

## 🧠 Features

- ✅ Grounded answers with citations  
- ✅ Prerequisite reasoning (Eligible / Not Eligible / Need info)  
- ✅ Handles prerequisite chains (multi-step reasoning)  
- ✅ Safe abstention for missing information  
- ✅ Structured output format (Answer, Why, Citations, etc.)

---

## 🏗️ Architecture

### 🔹 Pipeline
1. **Data Ingestion**
   - Web scraping using catalog URLs

2. **Text Processing**
   - Chunking using RecursiveCharacterTextSplitter  
   - Chunk size: 500  
   - Overlap: 100  

3. **Embeddings**
   - Model: `all-MiniLM-L6-v2`

4. **Vector Store**
   - FAISS (similarity search)

5. **Retriever**
   - Top-K retrieval (`k=5`)

6. **LLM**
   - Gemini (`models/gemini-2.5-flash`)

---

## 📂 Project Structure

```
rag-course-planner/
│
├── main.py # Main pipeline (RAG + LLM)
├── utils.py # Loading, splitting, embeddings, FAISS
├── evaluation.py # Evaluation script
├── requirements.txt # Dependencies
├── README.md # Project documentation
└── .gitignore
```


---

## 📊 Evaluation Results

| Metric               | Score |
|--------------------|------|
| Citation Coverage   | 100% |
| Abstention Accuracy | 100% |

### ✔ Observations
- All answers include **verifiable citations**
- Model correctly avoids hallucination
- Proper handling of prerequisite conditions (AND / OR)

---

## 🧪 Sample Output

### 🔹 Question
**What are prerequisites for database systems?**

### 🔹 Answer
```
The prerequisites for 6.5831 Database Systems are
((6.1210 or 6.1220[J]) and (6.1800 or 6.1810))
or permission of instructor.

Why:
This is directly stated in the catalog.

Citations:
[Source: https://catalog.mit.edu/subjects/6/
]

Assumptions / Not in catalog:
None
```


---

## 📚 Data Sources

- https://catalog.mit.edu/subjects/6/
- https://catalog.mit.edu/subjects/18/
- https://catalog.mit.edu/degree-charts/computer-science-engineering-course-6-3/
- https://guide.berkeley.edu/courses/compsci/
- https://guide.berkeley.edu/undergraduate/degree-programs/computer-science/

📅 Date accessed: March 2026

---

## ⚙️ Installation & Setup

```bash
pip install -r requirements.txt
```
