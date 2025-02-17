import streamlit as st 
import pandas as pd
import numpy as np

st.title("Zara Dashboard")
st.sidebar.title("Menu")

st.markdown(" This app is for training purpose to analyze the zara data from kaggle. 🚀")
st.sidebar.markdown(" Here will be the Navigation")

# load data
data_url = "data/zara.csv"

@st.cache_data(persist=True) #store data on disk to avoid compute every time we deploy
def load_data():
    data = pd.read_csv(data_url)
    return data

data = load_data()
