import streamlit as st
import pandas as pd
st.title('my first app')
data=pd.read_csv('Loan_data.csv')
st.dataframe(data)
