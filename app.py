import streamlit as st
import tensorflow as tf
import pickle
import numpy as np
from PIL import Image

@st.cache_resource
def load_model():
    return tf.keras.models.load_model(
        "mudra_cnn_model.keras"
    )

@st.cache_resource
def load_encoder():
    with open("label_encoder.pkl", "rb") as f:
        return pickle.load(f)

model = 
import streamlit as st
import tensorflow as tf
import numpy as np
import pickle

from PIL import Image
from huggingface_hub import hf_hub_download

st.title("Bharatanatyam Mudra Recognition")
st.write("Upload an image to identify the mudra.")

# Load model only once
@st.cache_resource
def load_model():
    model_path = hf_hub_download(
        repo_id="vidya-l/mudra-cnn-model",
        filename="mudra_cnn_model.keras"
    )

    model = tf.keras.models.load_model(model_path)
    return model

# Load label encoder
@st.cache_resource
def load_encoder():
    encoder_path = hf_hub_download(
        repo_id="vidya-l/mudra-cnn-model",
        filename="label_encoder.pkl"
    )

    with open(encoder_path, "rb") as f:
        encoder = pickle.load(f)

    return encoder

try:
    model = load_model()
    encoder = load_encoder()
    st.success("Model loaded successfully!")
except Exception as e:
    st.error(f"Could not load model: {e}")
    st.stop()

# Upload image
uploaded_file = st.file_uploader(
    "Choose a mudra image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded image", width=300)

    # Preprocess image as during training
    resized_image = image.resize((224, 224))
    image_array = np.array(resized_image, dtype=np.float32) / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    # Predict
    if st.button("Predict Mudra"):
        probabilities = model.predict(image_array, verbose=0)
        predicted_index = np.argmax(probabilities[0])
        confidence = float(probabilities[0][predicted_index])

        predicted_label = encoder.inverse_transform(
            [predicted_index]
        )[0]

        st.subheader(f"Predicted Mudra: {predicted_label}")
        st.write(f"Confidence: {confidence:.2%}")
load_model()
encoder = load_encoder()

st.title("Mudra Recognition")

uploaded_file = st.file_uploader(
    "Upload a mudra image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded Image")

    img = img.resize((224, 224))
    img_array = np.array(img, dtype=np.float32) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array, verbose=0)
    class_index = np.argmax(predictions[0])

    label = encoder.inverse_transform([class_index])[0]
    confidence = predictions[0][class_index] * 100

    st.success(f"Predicted Mudra: {label}")
    st.write(f"Confidence: {confidence:.2f}%")
