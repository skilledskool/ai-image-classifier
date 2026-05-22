import streamlit as st

# Page title
st.set_page_config(page_title="AI Image Classifier")

# Title
st.title("🤖 AI Image Classifier")

# Description
st.write(
    "This application uses a Teachable Machine AI model "
    "to classify images."
)

# Teachable Machine link
model_url = "https://teachablemachine.withgoogle.com/models/wgj1oaU0f/"

# Open link in new tab
st.markdown(
    f"""
    <a href="{model_url}" target="_blank">
        <button style="
            background-color:#ff6600;
            color:white;
            padding:15px 25px;
            border:none;
            border-radius:10px;
            font-size:18px;
            cursor:pointer;
        ">
            🚀 Launch AI Classifier
        </button>
    </a>
    """,
    unsafe_allow_html=True
)
