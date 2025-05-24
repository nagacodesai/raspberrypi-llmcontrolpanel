import streamlit as st
import numpy as np
import pandas as pd 


st.set_page_config(page_title="LLM Control Panel", page_icon=":robot_face:", layout="wide")

st.title("LLM Control Panel")
st.write("This is a control panel for managing and monitoring LLMs (Large Language Models). We use this to upload the documents, content on which  we want to train the LLM. we do the RAG (Retrieval Augmented Generation) and then we can use the LLM to answer questions based on the uploaded documents.")

slider_value = st.slider("Select a value", 0, 100, 10)
st.write(f"Selected value: {slider_value}")

