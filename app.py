import streamlit as st

st.set_page_config(page_title="AI Image Classifier")

st.title("AI Image Classifier")

st.write(
    "This application uses a Teachable Machine model "
    "to classify uploaded images using Artificial Intelligence."
)

st.info(
    "Click the button below to open the live AI classifier."
)

model_url = "PASTE YOUR TEACHABLE MACHINE LINK HERE"

st.link_button("Launch AI Classifier", model_url)
