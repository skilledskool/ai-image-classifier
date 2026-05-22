import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# Load model
model = load_model("keras_model.h5", compile=False)

# Load labels
class_names = open("labels.txt", "r").readlines()

# App title
st.title("AI Image Classifier")

st.write("Upload an image and let AI predict it.")

# Upload image
uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    # Open image
    image = Image.open(uploaded_file).convert("RGB")

    # Show image
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Resize image
    image = image.resize((224, 224))

    # Convert image to array
    image_array = np.asarray(image)

    # Normalize image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Create batch
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    data[0] = normalized_image_array

    # Predict
    prediction = model.predict(data)

    index = np.argmax(prediction)

    class_name = class_names[index]

    confidence_score = prediction[0][index]

    # Display result
    st.success(f"Prediction: {class_name}")

    st.write(f"Confidence Score: {confidence_score:.2f}")