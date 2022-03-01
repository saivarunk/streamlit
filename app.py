import pandas as pd
import streamlit as st

# Load Data
df = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv")

st.title('Streamlit Dataframe')

# Write Dataframe to UI
st.dataframe(df)