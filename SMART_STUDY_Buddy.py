"""
app.py
------
Smart Study Buddy - A Streamlit + Groq AI app that generates
complete study material for any topic.

Features:
- Topic Explanation
- Simple Example
- Real-life Example
- MCQs
- Interview Questions
- Summary

Run with:
    streamlit run app.py
"""

from dotenv import load_dotenv

load_dotenv()

import streamlit as st

from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver

model = ChatGroq(
    model="openai/gpt-oss-20b"
)

search = GoogleSerperAPIWrapper()

agent = create_agent(

    model=model,

    tools=[
        search.run
    ],

    system_prompt="""
You are an expert AI teacher and study assistant.

Whenever the user provides a topic and difficulty level,
generate complete and well-structured study material.

The study material must include:

1. A clear explanation of the topic
2. A simple beginner-friendly example
3. A real-life example
4. Exactly 5 MCQs with 4 options each
5. Exactly 5 interview questions
6. A short summary

Adjust the explanation according to the difficulty level:

Easy:
Use simple language and beginner-friendly explanations.

Medium:
Give moderate technical depth and explain important concepts.

Hard:
Give an in-depth technical explanation with advanced concepts,
edge cases, and interview-level details.

Use web search when current or updated information is required.

Always provide the answer in a professional and easy-to-understand format.
""",

    checkpointer=MemorySaver()
)

st.set_page_config(
    page_title="Smart Study Buddy",
    page_icon="📚",
    layout="wide"
)

st.markdown(
    """
    <style>

    .main {
        background-color: #F5F7FA;
    }

    .title {
        text-align: center;
        color: #6C63FF;
        font-size: 45px;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        color: gray;
        font-size: 18px;
        margin-bottom: 20px;
    }

    .stButton > button {
        width: 100%;
        background: #6C63FF;
        color: white;
        border-radius: 10px;
        height: 50px;
        font-size: 18px;
    }

    .card {
        padding: 20px;
        border-radius: 12px;
        background: white;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '<p class="title">📚 Smart Study Buddy</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">'
    'Learn Any Topic with AI'
    '</p>',
    unsafe_allow_html=True
)

st.divider()

col1, col2 = st.columns([2, 1])

with col1:

    st.markdown("### 📝 Study Details")

    topic = st.text_input(
        "Enter Topic",
        placeholder="Example: Python Functions"
    )

    difficulty = st.selectbox(
        "Select Difficulty",
        [
            "Easy",
            "Medium",
            "Hard"
        ]
    )

    if st.button(
        "🚀 Generate Study Material"
    ):

        if not topic.strip():

            st.error(
                "❌ Please enter a topic first."
            )

        else:

            prompt = f"""
Create complete study material for the following topic.

Topic: {topic}

Difficulty Level: {difficulty}

Please include:

1. Explanation
2. Simple Example
3. Real-life Example
4. Exactly 5 MCQs with 4 options each
5. Exactly 5 Interview Questions
6. Summary

Make the explanation suitable for the selected difficulty level.
Use simple formatting and clear headings.
"""

            with st.spinner(
                "🤖 AI is preparing your study material..."
            ):

                response = agent.invoke(

                    {
                        "messages": [
                            {
                                "role": "user",
                                "content": prompt
                            }
                        ]
                    },

                    {
                        "configurable": {
                            "thread_id": "1"
                        }
                    }

                )


            st.success(
                "🎉 Study Material Generated Successfully!"
            )


            st.markdown(
                response["messages"][-1].content
            )

with col2:

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.markdown(
        "## 📚 Study Kit Includes"
    )

    st.write(
        "📖 Topic Explanation"
    )

    st.write(
        "✏️ Simple Example"
    )

    st.write(
        "🌍 Real-life Example"
    )

    st.write(
        "❓ 5 MCQs"
    )

    st.write(
        "💼 Interview Questions"
    )

    st.write(
        "🧾 Summary"
    )

    st.markdown(
        "---"
    )

    st.markdown(
        "## 💡 Study Tips"
    )

    st.write(
        "✔️ Understand concepts first"
    )

    st.write(
        "✔️ Practice with examples"
    )

    st.write(
        "✔️ Solve MCQs regularly"
    )

    st.write(
        "✔️ Prepare interview questions"
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )