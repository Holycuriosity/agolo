import streamlit as st 
import sqlite3
import pandas as pd
import os

st.title('AGOLO DB')


databasepath = os.path.join(os.getcwd(),'agolo.db')

connect = sqlite3.connect(databasepath)

vehicle_df = pd.read_sql_query("SELECT * from vehicle", connect)
driver_df = pd.read_sql_query("SELECT * from driver", connect)

connect.close()

st.markdown('Vehicle Table :blush:')
st.dataframe(vehicle_df)

st.markdown('Driver Table :blush:')

st.dataframe(driver_df)
