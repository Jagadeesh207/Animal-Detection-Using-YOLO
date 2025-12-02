import streamlit as st
from ultralytics import YOLO
from PIL import Image
import time
import io

st.title("📸 Upload Image Detection")

MODEL_PATH = "best.pt"

@st.cache_resource
def load_model():
    return YOLO(MODEL_PATH)

model = load_model()

st.sidebar.header("⚙️ Settings")
confidence = st.sidebar.slider("Confidence", 0.1, 1.0, 0.45)

st.markdown('<div class="neon-box">', unsafe_allow_html=True)
uploaded = st.file_uploader("Upload Image", type=["jpg","jpeg","png"])
st.markdown("</div>", unsafe_allow_html=True)

if uploaded:
    img = Image.open(uploaded)
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(img)

    with col2:
        if st.button("🚀 Run Detection", use_container_width=True):
            with st.spinner("Detecting..."):
                start = time.time()
                r = model.predict(img, conf=confidence)
                plot = r[0].plot()
                output_img = Image.fromarray(plot[..., ::-1])
                end = time.time()

                st.subheader("Detection Result")
                st.image(output_img)

                st.success(f"Inference Time: {end - start:.3f}s")

                # Convert image to buffer for download
                buf = io.BytesIO()
                output_img.save(buf, format="PNG")
                byte_data = buf.getvalue()

                st.download_button(
                    label="⬇ Download Result",
                    data=byte_data,
                    file_name="detection_result.png",
                    mime="image/png",
                    use_container_width=True
                )
