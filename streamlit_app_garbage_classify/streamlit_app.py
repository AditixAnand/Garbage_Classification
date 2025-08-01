import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image

# Constants
MODEL_PATH = "C:/Users/diyab/Garbage_Classification/Waste_classifier_v2.h5"
IMG_SIZE = (224, 224)
CLASS_LABELS = ['battery', 'biological', 'cardboard']

# Load trained model
@st.cache_resource
def load_trained_model():
    return load_model(MODEL_PATH)

model = load_trained_model()

# Image preprocessing
def preprocess_image(img: Image.Image) -> np.ndarray:
    img = img.convert("RGB").resize(IMG_SIZE)
    img_array = img_to_array(img) / 255.0
    return np.expand_dims(img_array, axis=0)

# Prediction
def predict_image(img: Image.Image):
    processed = preprocess_image(img)
    predictions = model.predict(processed)
    class_idx = np.argmax(predictions)
    confidence = np.max(predictions)
    return CLASS_LABELS[class_idx], confidence

# Streamlit App
# st.set_page_config(page_title="Waste Classifier", layout="centered")
st.title("♻️ Smart Waste Classification")
st.markdown("Upload an image of waste to classify it into one of the categories.")

st.subheader("📤 Upload Waste Image")
uploaded_file = st.file_uploader("Choose an image (JPG/PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", width=300)


    if st.button("🔍 Classify"):
        label, confidence = predict_image(img)
        st.success(f"🧠 **Predicted**: `{label}` \n💯 **Confidence**: `{confidence * 100:.2f}%`")


