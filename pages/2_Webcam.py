import streamlit as st
from ultralytics import YOLO
import cv2
from PIL import Image

st.title("🎥 Live Webcam Detection")

MODEL_PATH = "best.pt"

@st.cache_resource
def load_model():
    return YOLO(MODEL_PATH)

model = load_model()

start_cam = st.button("▶ Start Webcam", use_container_width=True)

if start_cam:
    cap = cv2.VideoCapture(0)
    stframe = st.empty()

    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Could not access camera.")
            break
        
        res = model.predict(frame, conf=0.5)[0]
        annotated = res.plot()
        stframe.image(annotated, channels="BGR")

        if st.button("⏹ Stop Camera"):
            break

    cap.release()
