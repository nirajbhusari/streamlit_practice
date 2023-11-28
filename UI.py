import streamlit as st

st.markdown("<h1 style='color:#808080;font-family: Arial;text-align: Left'>Welcome to Password Generator</h1>",
            unsafe_allow_html=True)
st.markdown("<h1 style='color: #808080;font-size:20px;font-family: Arial;text-align: Left'><i>Generate passwords, copy, use. Remember to save it somewhere!</i></h1>",
            unsafe_allow_html=True)
st.markdown("<h1 style='color: #808080;font-size:16px;font-family: Arial;text-align: Left'><i>Choose an option:</i></h1>",
            unsafe_allow_html=True)
st.checkbox("Numbers")
st.checkbox("Alphabets")
st.checkbox("I don't want to understand what is written")

st.button("Generate!")
st.button("Copy")

