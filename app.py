import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
import cv2

# Load model
model = load_model('models/action_image_model.h5')

class_names = ['calling', 'clapping', 'cycling', 'dancing', 'drinking', 'eating',
               'fighting', 'hugging', 'laughing', 'listening_to_music', 'running',
               'sitting', 'sleeping', 'texting', 'using_laptop']

st.title("Human Action Recognition Demo")

uploaded_file = st.file_uploader("Upload an action image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Convert uploaded file to OpenCV image
   file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
   img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

# Resize to match model’s expected input
   img_resized = cv2.resize(img, (128, 128))

# Normalize only for prediction
   img_input = img_resized / 255.0
   img_input = np.expand_dims(img_input, axis=0)

# Predict
   prediction = model.predict(img_input)
   predicted_class = class_names[np.argmax(prediction)]

# Display original image safely
   st.image(cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB), caption="Uploaded Image")
   st.write(f"**Predicted Action:** {predicted_class}")

