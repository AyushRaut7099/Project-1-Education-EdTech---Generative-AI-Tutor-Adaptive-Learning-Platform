import streamlit as st
from backend.retrieval import retrieve_chunks #importing the fxn to retrieve the relevant chunks froom VectorDB
from backend.llm import generate_response #importing the fxn to generate response using Gemini free model
st.set_page_config(page_title="AI Chat", layout="wide")
st.title(" AI Tutor Chat")
if "chat_history" not in st.session_state:#it creates memory when the chat starts and it will be used to store the conversation history between the user and the AI.
    st.session_state.chat_history = [] # It will create empty memory chat_history[]--
user_question = st.text_input("Ask your question")
if user_question:
    results = retrieve_chunks(user_question)
    retrieved_docs = results["documents"][0]

    context = "\n".join(retrieved_docs) # Combine retrieved chunks into a single context string
    chat_history = st.session_state.chat_history# get previous conversation from history memory---
    #answer = generate_response(context, user_question) # Generate answer using the context and user question // it was before adding memory in the next line we will add chathistory aswell
    answer=generate_response(context, user_question, chat_history)
    st.subheader("AI Answer") 
    st.write(answer) # Display the generated answer
    #after generating the answer we'll update the chat history with new question and answer
    st.session_state.chat_history.append(
        {
            "user":user_question,
            "assistant":answer
        }
    )
    # st.subheader("Source Chunks") # Display the retrieved chunks as sources
    # for i, doc in enumerate(retrieved_docs): #
    #     st.markdown(f"### Source {i+1}")
    #     #st.write(doc) # Display each retrieved chunk as a source
    #     st.divider() 