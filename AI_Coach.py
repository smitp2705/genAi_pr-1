"""
app.py
-------------------------
AI Learning Coach - RAG Chatbot
 
Features
---------
• Multiple PDF Upload
• Chat with PDFs
• Google Gemini Embeddings
• Groq GPT-OSS-20B
• LangChain Agent (create_agent)
• Conversation Memory
 
Run
----
streamlit run app.py
"""
 
from dotenv import load_dotenv
load_dotenv()
 
import os
import uuid
import tempfile
 
import streamlit as st
 
from langchain_groq import ChatGroq
from langchain_google_genai import GoogleGenerativeAIEmbeddings
 
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
 
from langchain_core.tools import create_retriever_tool
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
 
# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="AI Learning Coach",
    page_icon="📘",
    layout="wide"
)
 
# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>
.main{
    background:#F5F7FA;
}
.title{
    text-align:center;
    font-size:45px;
    font-weight:bold;
    color:#6C63FF;
}
.subtitle{
    text-align:center;
    font-size:18px;
    color:gray;
    margin-bottom:20px;
}
.stButton>button{
    width:100%;
    height:50px;
    background:#6C63FF;
    color:white;
    border-radius:10px;
    font-size:18px;
}
.card{
    padding:20px;
    background:white;
    border-radius:12px;
    box-shadow:0px 0px 10px rgba(0,0,0,.15);
}
</style>
""", unsafe_allow_html=True)
 
# -----------------------------
# Heading
# -----------------------------
st.markdown('<p class="title">📘 AI Learning Coach</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Chat With Multiple PDF Documents Using AI</p>', unsafe_allow_html=True)
st.divider()
 
# -----------------------------
# Models
# -----------------------------
llm = ChatGroq(model="openai/gpt-oss-20b")
 
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
 
# -----------------------------
# Session State
# -----------------------------
if "agent" not in st.session_state:
    st.session_state.agent = None
 
if "ready" not in st.session_state:
    st.session_state.ready = False
 
if "messages" not in st.session_state:
    st.session_state.messages = []
 
if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())
 
# -----------------------------
# Layout
# -----------------------------
left, right = st.columns([2, 1])
 
with left:
    st.markdown("## 📂 Upload PDF Files")
 
    uploaded_files = st.file_uploader(
        "Choose one or more PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )
 
    build = st.button("🚀 Build Knowledge Base")
 
with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
 
    st.markdown("### 📚 Features")
    st.write("📄 Multiple PDF Upload")
    st.write("📖 PDF Reading")
    st.write("✂️ Text Chunking")
    st.write("🧠 Gemini Embeddings")
    st.write("🗂️ InMemory Vector Store")
    st.write("🔍 Semantic Search")
    st.write("🤖 Groq GPT-OSS-20B")
    st.write("💬 AI Chat")
    st.write("🧠 Conversation Memory")
 
    st.markdown("---")
 
    st.markdown("### 💡 Tips")
    st.write("✔ Upload multiple PDFs")
    st.write("✔ Ask document-related questions")
    st.write("✔ AI answers only from uploaded PDFs")
 
    st.markdown("</div>", unsafe_allow_html=True)
 
# -----------------------------
# Build Knowledge Base
# -----------------------------
if build:
 
    if not uploaded_files:
        st.error("Please upload at least one PDF.")
 
    else:
        documents = []
        temp_paths = []
 
        # ---- Read PDFs ----
        with st.spinner("Reading PDF files..."):
            for pdf in uploaded_files:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                    tmp.write(pdf.read())
                    temp_path = tmp.name
 
                temp_paths.append(temp_path)
 
                loader = PyPDFLoader(temp_path)
                docs = loader.load()
                documents.extend(docs)
 
        # ---- Split Documents ----
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        chunks = splitter.split_documents(documents)
 
        # ---- Create Vector Store ----
        with st.spinner("Creating Vector Database..."):
            vector_store = InMemoryVectorStore.from_documents(
                documents=chunks,
                embedding=embeddings
            )
 
        # ---- Clean up temp PDF files ----
        for path in temp_paths:
            try:
                os.remove(path)
            except OSError:
                pass
 
        # ---- Retriever ----
        retriever = vector_store.as_retriever(search_kwargs={"k": 4})
 
        retriever_tool = create_retriever_tool(
            retriever,
            "pdf_search",
            """
Search information from uploaded PDF documents.
 
Always answer only using the uploaded PDFs.
 
If the answer is not present inside the PDFs,
reply:
 
'I could not find that information in the uploaded documents.'
"""
        )
 
        # ---- Agent ----
        agent = create_agent(
            model=llm,
            tools=[retriever_tool],
            system_prompt="""
You are an expert AI Learning Coach.
 
Help the user understand the content of their uploaded PDF documents.
Always use the pdf_search tool to find relevant information before answering.
Explain concepts clearly and simply, like a patient tutor.
""",
            checkpointer=MemorySaver()
        )
 
        st.session_state.agent = agent
        st.session_state.ready = True
        st.session_state.messages = []  # fresh chat for the new knowledge base
 
        st.success("✅ Knowledge Base Created Successfully.")
 
# -----------------------------
# Chat Interface
# -----------------------------
if st.session_state.ready:
 
    st.divider()
    st.markdown("## 💬 Chat With Your PDFs")
 
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
 
    question = st.chat_input("Ask your question...")
 
    if question:
        st.session_state.messages.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.markdown(question)
 
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.agent.invoke(
                    {"messages": [{"role": "user", "content": question}]},
                    {"configurable": {"thread_id": st.session_state.thread_id}}
                )
                answer = response["messages"][-1].content
                st.markdown(answer)
 
        st.session_state.messages.append({"role": "assistant", "content": answer})