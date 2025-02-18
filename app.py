import streamlit as st 
import pandas as pd
import numpy as np

st.title("Dashboard")
st.sidebar.title("Menu")

st.markdown(" This app is for training purpose to analyze the zara data from kaggle. 🚀")
st.sidebar.markdown(" Here will be the Navigation")

# load data
data_url = "data/zara.csv"

@st.cache_data(persist=True) #store data on disk to avoid compute every time we deploy
def load_data():
    data = pd.read_csv(data_url, sep=";")
    return data

df = load_data()

import plotly.express as px
# Create two columns for side-by-side pie charts
col1, col2 = st.columns(2)

# First Pie Chart: Product Position Distribution
with col1:
    st.subheader("Product Position Distribution")
    
    position_counts = df["Product Position"].value_counts().reset_index()
    position_counts.columns = ["Product Position", "Count"]

    fig1 = px.pie(position_counts, 
                 names="Product Position", 
                 values="Count", 
                 title="Distribution of Product Position",
                 color_discrete_sequence=px.colors.qualitative.Set2)

    st.plotly_chart(fig1)

# 📊 Second Pie Chart: Sales by Section (MAN vs. WOMEN)
with col2:
    st.subheader("Total Sales Volume by Section")

    section_sales = df.groupby("section")["Sales Volume"].sum().reset_index()

    fig2 = px.pie(section_sales, 
                 names="section", 
                 values="Sales Volume", 
                 title="Sales Distribution by Section",
                 color_discrete_sequence=px.colors.qualitative.Pastel)

    st.plotly_chart(fig2)

st.markdown('# Filter the Data by Category')
category = st.selectbox("Select Product Category", df["terms"].unique())
promo_filter = st.radio("Promotion Status", ["All", "Yes", "No"])

# Apply Filters
filtered_df = df[df["terms"] == category]
if promo_filter != "All":
    filtered_df = filtered_df[filtered_df["Promotion"] == promo_filter]

st.write(filtered_df)
