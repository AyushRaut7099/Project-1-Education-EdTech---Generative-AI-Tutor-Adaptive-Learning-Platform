import streamlit as st
import base64

st.set_page_config(
    page_title="AI Tutor Pro",
    page_icon="🎓",
    layout="wide"
)
st.title("🎓 AI Tutor Pro")
# ==========================
# HERO IMAGE
# ==========================

st.image(
    "assets/ai_tutor.gif",
    use_container_width=True
)

st.caption("Retrieval-Augmented Learning Assistant")

st.success("✅ Project Status: Fully Operational")

st.markdown("---")

# ==========================
# LIVE STATUS
# ==========================

st.subheader("🚀 System Status")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📄 PDF Processing", "Ready")

with col2:
    st.metric("🧠 RAG Engine", "Active")

with col3:
    st.metric("📝 Quiz Module", "Enabled")

with col4:
    st.metric("💾 Memory", "Running")

st.markdown("---")

# ==========================
# FEATURES
# ==========================

st.subheader("✨ Core Features")

col1, col2 = st.columns(2)

with col1:
    st.success("""
### 🤖 Intelligent Question Answering

Ask questions directly from uploaded PDFs.

Uses Retrieval-Augmented Generation (RAG) to provide context-aware answers while reducing hallucinations.
""")

with col2:
    st.info("""
### 📝 AI Quiz Generator

Generate MCQs automatically from uploaded study material.

Includes scoring, answer validation, and explanations.
""")

st.markdown("---")

# ==========================
# WORKFLOW
# ==========================

st.subheader("⚙️ System Workflow")

st.code("""
PDF Upload
     ↓
Text Extraction
     ↓
Chunking
     ↓
Embeddings
     ↓
ChromaDB
     ↓
Retriever
     ↓
OpenRouter LLM
     ↓
Answer Generation
     ↓
Quiz Generation
""")

st.markdown("---")

# ==========================
# TECH STACK
# ==========================

st.subheader("🛠️ Technology Stack")

tech1, tech2 = st.columns(2)

with tech1:
    st.markdown("""
- Streamlit
- FastAPI
- Python
- ChromaDB
""")

with tech2:
    st.markdown("""
- OpenRouter
- Sentence Transformers
- Session Memory
- Retrieval-Augmented Generation (RAG)
""")

st.markdown("---")

# ==========================
# OBJECTIVE
# ==========================

st.subheader("🎯 Project Objective")

st.write("""
Traditional chatbots often generate responses without reliable context, which may lead to hallucinations.

This AI Tutor leverages Retrieval-Augmented Generation (RAG) to retrieve relevant information directly from uploaded documents before generating responses.

The platform also includes an AI-powered Quiz Generation module to support active learning and knowledge assessment.
""")

st.markdown("---")

# ==========================
# PROJECT STATS
# ==========================

st.subheader("📊 Project Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Weeks Completed", "4")

with col2:
    st.metric("Modules Built", "5")

with col3:
    st.metric("Project Status", "100%")

st.markdown("---")

# ==========================
# FOOTER
# ==========================

st.info(
    "🎓 AI Tutor Pro | Generative AI Internship Project | RAG + ChromaDB + FastAPI + Streamlit"
)