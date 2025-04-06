import streamlit as st
import pandas as pd

# Load features from module
from trait_module import trait_viewer, trait_downloader, trait_comparer

# Load data
df = pd.read_csv("trait_summary.csv")

# Streamlit page config
st.set_page_config(
    page_title="Australian Plant Traits Dashboard",
    layout="wide"
)

# App Title
st.title("🌿 Australian Plant Traits Dashboard")

# Sidebar navigation
selected_page = st.sidebar.radio(
    "Select a feature",
    [
        "🔍 View Traits",
        "📤 Download Traits",
        "🔬 Compare Species"
    ]
)

# Feature router
if selected_page == "🔍 View Traits":
    trait_viewer(df)

elif selected_page == "📤 Download Traits":
    trait_downloader(df)

elif selected_page == "🔬 Compare Species":
    trait_comparer(df)
