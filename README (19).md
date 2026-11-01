# 📘 AI Learning Coach – Chat with Multiple PDFs Using Generative AI

An intelligent **AI-powered PDF Learning Assistant** built using Python, Streamlit, LangChain, LangGraph, Groq AI, and Google Gemini Embeddings.

AI Learning Coach allows users to upload multiple PDF documents and interact with them through a conversational AI chatbot. Users can ask questions about their uploaded documents and receive relevant, context-aware answers using Retrieval-Augmented Generation (RAG).

Learn smarter by turning your PDF documents into an interactive AI-powered knowledge base!

---

## 🚀 Project Overview

**AI Learning Coach** is a Generative AI application that uses Retrieval-Augmented Generation (RAG) to answer questions based on uploaded PDF documents.

Instead of manually searching through lengthy documents, users can upload multiple PDFs and ask questions in natural language.

The application processes PDF files, extracts text, splits it into smaller chunks, converts the text into vector embeddings, and stores them in an in-memory vector database.

When a user asks a question, the AI retrieves relevant document content and generates an answer using the Groq-powered language model.

**The main objective is to make document learning, information retrieval, and studying easier and faster.**

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 📂 Multiple PDF Upload | Upload multiple PDF documents simultaneously. |
| 📖 PDF Text Extraction | Extracts text using PyPDFLoader. |
| ✂️ Text Chunking | Splits documents into manageable text chunks. |
| 🧠 Gemini Embeddings | Converts document text into vector embeddings. |
| 🗂️ Vector Database | Stores embeddings using InMemoryVectorStore. |
| 🔍 Semantic Search | Retrieves relevant document information based on user queries. |
| 🤖 Groq AI Integration | Uses GPT-OSS-20B for AI-powered responses. |
| 🔗 LangChain Agent | Connects the language model with the PDF retrieval tool. |
| 💬 Interactive Chatbot | Ask questions and receive answers from uploaded PDFs. |
| 🧠 Conversation Memory | Maintains conversation state using LangGraph MemorySaver. |
| 🎨 Streamlit UI | Provides a clean and interactive user interface. |

---

## 🛠️ Technologies Used

- **Python** – Core programming language.
- **Streamlit** – Interactive web application development.
- **LangChain** – LLM integration, document retrieval, and agent development.
- **LangGraph** – Agent workflow and conversation memory.
- **Groq AI** – Large Language Model integration.
- **GPT-OSS-20B** – Language model used for generating responses.
- **Google Gemini Embeddings** – Converts text into numerical vector representations.
- **PyPDFLoader** – Extracts content from PDF documents.
- **RecursiveCharacterTextSplitter** – Splits documents into smaller chunks.
- **InMemoryVectorStore** – Stores and retrieves document embeddings.
- **Python-dotenv** – Manages environment variables.

---

## 🏗️ Project Architecture

```text
                 USER
                   |
                   ▼
           Streamlit Interface
                   |
                   ▼
             Upload PDFs
                   |
                   ▼
             PyPDFLoader
            (Text Extraction)
                   |
                   ▼
       RecursiveCharacterTextSplitter
              (Text Chunking)
                   |
                   ▼
        Google Gemini Embeddings
            (Vector Creation)
                   |
                   ▼
           InMemoryVectorStore
             (Vector Storage)
                   |
                   ▼
             PDF Retriever
              (Top 4 Chunks)
                   |
                   ▼
            LangChain Agent
                   |
             ┌─────┴─────┐
             ▼           ▼
          Groq AI     PDF Search
        GPT-OSS-20B     Tool
             |           |
             └─────┬─────┘
                   |
                   ▼
          LangGraph MemorySaver
                   |
                   ▼
          Context-A
