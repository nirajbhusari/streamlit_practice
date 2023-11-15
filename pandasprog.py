import streamlit as st
import pandas as pd

def load_data():
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    return pd.read_csv(url)

df = load_data()

st.title("Simple Pandas Program.")
st.markdown("This program loads a sample dataset and performs some basic analysis.")

st.subheader("1. Displaying Data")
st.dataframe(df.head())

st.subheader("2. Basic Statistics")
st.write("Summary statistics of the dataset:")
st.write(df.describe())

st.subheader("Data Visualization")
st.bar_chart(df["Age"].value_counts())

st.subheader("4. Filtering and Display")
selected_gender = st.selectbox("Select a Gender:", df["Age"].unique())
filtered_data = df[df["Sex"]== selected_gender]
st.write(f"Displaying data for {selected_gender} only:")
st.dataframe(filtered_data.head())

st.subheader("5. Group By")
grouped_data = df.groupby("Pclass")["Fare"].mean()
st.write("Average Fare by Passenger Class:")
st.bar_chart(grouped_data)


