import streamlit as st
import sqlite3
import os



st.set_page_config(page_title='MOCOMOCA', 
                   page_icon=':smiley:',
                   initial_sidebar_state="auto",
                   layout='wide'
                   )


databasepath = os.path.join(os.getcwd(),'agolo.db')

connect = sqlite3.connect(databasepath)

cur = connect.cursor()

st.title('Okada/Agolo Drivers Registration Form')

with st.form('agoloform',clear_on_submit=True):
    name = st.text_input('Drivers Full Name')
    phone = st.text_input('Drivers Phone Number')
    address= st.text_input('Drivers Adrress')
    vtype= st.selectbox('Vehicle Type',['Agolo','Okada'])
    platenumber = st.text_input(' Vehicle Plate Number')
    vin =st.text_input('Vehicle Identification Number')
    
    submitted = st.form_submit_button()
    
    if submitted:
        cur.execute('''INSERT INTO vehicle (vtype, plate_number, vin) 
                VALUES (?, ?, ?)''', (vtype, platenumber, vin))

        # Get the last inserted vehicle id
        vid = cur.lastrowid

        # Insert data into Driver table
        cur.execute('''INSERT INTO driver (name, phone_number, address, vid) 
                        VALUES (?, ?, ?, ?)''', (name, phone, address, vid))

        connect.commit()
        connect.close()
        st.snow()






    
    
    
    



