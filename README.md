# Bharatanatyam Mudra Recognition

A deep learning application that recognizes Bharatanatyam hand mudras using a custom CNN and MobileNetV2 transfer learning. Built with TensorFlow and Streamlit.

## Features
- Upload mudra images.
- Predict mudra class and confidence.
- Compare CNN and MobileNetV2 performance.

## Setup

**1. Clone the repository**
```bash
git clone https://github.com/vidyaldev-tech/bharatanatyam-mudra-detection.git
cd bharatanatyam-mudra-detection
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Configure Hugging Face**

Upload the trained model and `label_encoder.pkl` to Hugging Face, then update the repository ID in `app.py`.

**4. Run the application**
```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

## Technologies
Python, TensorFlow, CNN, MobileNetV2, Streamlit, Hugging Face Hub.

## Author
Vidya L
