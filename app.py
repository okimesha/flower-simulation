
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="Flower Simulation", layout="wide")

st.title("Flower Federated Learning Simulation")

html_file = Path("flower_simulation.html")

if html_file.exists():
    html_content = html_file.read_text(encoding="utf-8")
    components.html(html_content, height=700, scrolling=True)
else:
    st.error("File flower_simulation.html tidak ditemukan.")
