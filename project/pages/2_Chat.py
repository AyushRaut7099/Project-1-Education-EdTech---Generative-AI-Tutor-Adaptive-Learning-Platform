import streamlit as st
from backend.retrieval import retrieve_chunks #importing the fxn to retrieve the relevant chunks froom VectorDB
from backend.llm import generate_response #importing the fxn to generate response using Gemini free model
st.set_page_config(page_title="AI Chat", layout="wide")
st.title(" AI Tutor Chat")
user_question = st.text_input("Ask your question")
if user_question:
    results = retrieve_chunks(user_question)
    retrieved_docs = results["documents"][0]

    context = "\n".join(retrieved_docs) # Combine retrieved chunks into a single context string
    answer = generate_response(context, user_question) # Generate answer using the context and user question
    st.subheader("AI Answer") #
    st.write(answer) # Display the generated answer
    st.subheader("Source Chunks") # Display the retrieved chunks as sources
    for i, doc in enumerate(retrieved_docs): #
        st.markdown(f"### Source {i+1}")
        st.write(doc) # Display each retrieved chunk as a source
        st.divider()