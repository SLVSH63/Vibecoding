from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


APP_HTML = Path(__file__).parent / "bank-app" / "index.html"

st.set_page_config(
    page_title="NOVA Bank",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        [data-testid="stHeader"],
        [data-testid="stToolbar"],
        [data-testid="stSidebar"],
        footer {
            display: none;
        }
        [data-testid="stMainBlockContainer"] {
            max-width: 100%;
            padding: 0;
        }
        [data-testid="stAppViewContainer"],
        [data-testid="stMain"] {
            background: #07070f;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

if not APP_HTML.is_file():
    st.error(f"Fichier de l’application introuvable : {APP_HTML}")
    st.stop()

components.html(
    APP_HTML.read_text(encoding="utf-8"),
    height=880,
    scrolling=True,
)
