import streamlit as st

st.title("AI Image Classifier")

st.markdown("""
## Teachable Machine Model

Click below to open the live AI classifier.
""")

model_url = "PASTE_YOUR_MODEL_LINK_HERE"

st.link_button("Open AI Model", model_url)
