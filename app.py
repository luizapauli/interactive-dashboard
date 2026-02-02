import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Salary Dashboard in the Data Field",
    page_icon=":bar_chart:",
    layout="wide",
)

df = pd.read_csv("https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv")

st.sidebar.header("🔍 Filters")

