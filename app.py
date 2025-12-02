import streamlit as st

st.set_page_config(
    page_title="BioSense Wildlife Detector",
    page_icon="🦌",
    layout="wide"
)

# GLOBAL DARK + NEON THEME CSS
st.markdown("""
<style>

html, body {
    background-color: #0d0f17 !important;
}

[data-testid="stAppViewContainer"] {
    background-color: #0d0f17 !important;
}

h1, h2, h3, h4, h5 {
    color: #32fbe2 !important;
    text-shadow: 0px 0px 8px #32fbe2;
}

.sidebar .sidebar-content {
    background: #11131c !important;
}

.uploadButton {
    background: #11131c !important;
}

.block-container {
    padding-left: 2rem;
    padding-right: 2rem;
}

.neon-box {
    border: 1px solid #32fbe2;
    padding: 20px;
    border-radius: 18px;
    background: #0f111a;
    box-shadow: 0px 0px 15px rgba(50,251,226,0.4);
}

.neon-button {
    background: linear-gradient(90deg, #00f5ff, #00ffa6);
    color: black !important;
    font-weight: 800;
    border-radius: 10px;
    padding: 12px 20px;
    box-shadow: 0px 0px 12px #00f5ff;
}

</style>
""", unsafe_allow_html=True)

st.title("🦌 BioSense Wildlife Detector (Dashboard)")
st.write("Select a page from the left menu.")
