import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI Image Classifier",
    page_icon="🤖",
    layout="centered"
)

# Custom background and styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #ff9966, #ff5e62);
        color: white;
    }

    h1 {
        color: white;
        text-align: center;
        font-size: 50px;
    }

    p {
        color: white;
        font-size: 18px;
        text-align: center;
    }

    .stButton button {
        background-color: white;
        color: #ff5e62;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 18px;
        font-weight: bold;
    }

    .stButton button:hover {
        background-color: #ffe6e6;
        color: #ff5e62;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🤖 AI Image Classifier")

# Description
st.write(
    "This application uses a Teachable Machine AI model "
    "to classify uploaded images."
)

st.write("Click the button below to launch the AI model.")

# Your Teachable Machine model link
model_url = "PASTE YOUR TEACHABLE MACHINE LINK HERE"

# Button
st.link_button("🚀 Launch AI Classifier", model_url)
