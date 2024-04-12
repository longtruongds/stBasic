#!/usr/bin/env python
# coding: utf-8

# admin
#


import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

def creds_entered():
    if st.session_state["user"].strip() == "admin" and st.session_state ["passwd"].strip() == "admin":
        st.session_state["authenticated"] = True
    else:
        st.session_state["authenticated"] = False
        if not st.session_state["passwd"]:
            st.warning("Please enter password.")
        elif not st.session_state["user"]:
            st.warning("Please enter username.")
        else:
            st.error("Invalid Username/Password:face_with_raised_eyebrow:")
def authenticate_user():
    if "authenticated" not in st.session_state:
        st.text_input(label="Username:", value="", key="user", on_change=creds_entered)
        st.text_input(label="Password", value="", key="passwd", type="password", on_change=creds_entered)
        return False
    else:
        if st.session_state["authenticated"]:
            return True
        else:
            st.text_input(label="Username:", value="", key="user", on_change=creds_entered)
            st.text_input(label="Password", value="", key="passwd", type="password", on_change=creds_entered)
            return False
        
if authenticate_user():
    # Create a DataFrame with random integers
    df = pd.DataFrame(np.random.randint(0, 100, size=(10, 2)), columns=['Column1', 'Column2'])
    
    # Create a line chart using Plotly Express
    fig = px.line(df, x=df.index, y=['Column1', 'Column2'], title='Random Data Line Chart')
    
    # Display the chart in Streamlit
    st.plotly_chart(fig)


# In[ ]:




