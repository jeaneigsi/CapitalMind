import streamlit as st
import streamlit.components.v1 as components
from Utils import widget_finance


with st.sidebar:
    st.title("CapitalMind")
    st.write("The best financial Advisor powered by AI")

st.markdown("#  **CapitalMind**")
st.write("Welcome to CapitalMind, the best financial advisor powered by AI. We are here to help you make the best financial decisions for your future. Please enter your details below to get started.")
components.html(widget_finance,height=700)