# 📚 Smart Study Buddy – AI-Powered Learning Assistant

An intelligent **Generative AI-powered Study Assistant** built using Python, Streamlit, LangChain, Groq AI, and Google Serper API. It helps students learn any topic by generating structured, easy-to-understand study materials according to their selected difficulty level.

Whether you are a beginner or an advanced learner, Smart Study Buddy makes learning easier, faster, and more effective.

---

## 🚀 Project Overview

**Smart Study Buddy** is an AI-based educational application that generates personalized study materials for any user-provided topic.

Users simply enter a topic, select a difficulty level (Easy, Medium, or Hard), and click the Generate Study Material button.

The AI assistant automatically generates:

- 📖 Detailed Topic Explanation
- ✏️ Simple Beginner-Friendly Example
- 🌍 Real-Life Example
- ❓ 5 Multiple Choice Questions (MCQs)
- 💼 5 Interview Questions
- 📝 Short Topic Summary

The application also integrates Google Serper search to support access to updated information when required.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 📖 Topic Explanation | Generates clear and structured explanations. |
| ✏️ Simple Examples | Provides beginner-friendly examples. |
| 🌍 Real-Life Examples | Connects theoretical concepts with practical applications. |
| ❓ MCQ Generator | Generates exactly 5 MCQs with 4 options each. |
| 💼 Interview Preparation | Generates exactly 5 interview questions. |
| 📝 Smart Summary | Provides a short and useful topic summary. |
| 🎯 Difficulty Selection | Supports Easy, Medium, and Hard levels. |
| 🌐 Web Search | Uses Google Serper for updated information when needed. |
| 🧠 Conversation Memory | Uses LangGraph MemorySaver for conversation state management. |
| 🎨 Interactive UI | Provides a clean and user-friendly Streamlit interface. |

---

## 🛠️ Technologies Used

- **Python** – Core programming language.
- **Streamlit** – Interactive web application development.
- **Groq AI** – Large Language Model integration.
- **LangChain** – AI agent and tool integration.
- **LangGraph** – Agent workflow and conversation memory.
- **Google Serper API** – Web search integration.
- **Python-dotenv** – Environment variable management.

---

## 🏗️ Project Architecture

```text
             USER
               |
               ▼
       Streamlit Web Interface
               |
               ▼
       Enter Topic & Difficulty
               |
               ▼
          AI Agent
          (LangChain)
               |
         ┌─────┴─────┐
         ▼           ▼
      Groq AI    Google Serper
      (LLM)      (Web Search)
         |           |
         └─────┬─────┘
               |
               ▼
       LangGraph MemorySaver
               |
               ▼
       Generate Study Material
               |
               ▼
       Display AI Response
               |
               ▼
    Explanation, Examples, MCQs,
    Interview Questions & Summary
```

---

## 📂 Project Structure

```text
GenAi_PR1/
│
├── SMART_STUDY_Buddy.py
├── README.md
├── .env
└── requirements.txt
```

---

## ⚙️ Installation & Setup

Follow these steps to run the project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/Mant-0957/GenAi_PR1.git
```

### 2. Navigate to the Project Folder

```bash
cd GenAi_PR1
```

### 3. Create a Virtual Environment (Recommended)

```bash
python -m venv env
```

Activate the environment:

**Windows:**
```bash
env\Scripts\activate
```

**Mac/Linux:**
```bash
source env/bin/activate
```

### 4. Install Required Libraries

```bash
pip install streamlit python-dotenv langchain langchain-groq langchain-community langgraph
```

### 5. Configure API Keys

Create a `.env` file in the project root directory.

Add your API keys:

```env
GROQ_API_KEY=your_groq_api_key
SERPER_API_KEY=your_serper_api_key
```

**Get API Keys:**

- Groq API: https://console.groq.com/keys
- Google Serper API: https://serper.dev/

**Important:** Never upload your actual API keys or `.env` file to GitHub. Add `.env` to your `.gitignore` file.

### 6. Run the Application

```bash
streamlit run SMART_STUDY_Buddy.py
```

The application will open in your default browser.

---
