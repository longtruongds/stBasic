#!/usr/bin/env python
# coding: utf-8


import streamlit as st
import numpy as np

# Insert elements using "with" notation
with st.container():
    st.write("This is inside the container")
    st.bar_chart(np.random.randn(50, 3))  # You can call any Streamlit command

# Elements can also be inserted out of order
container = st.container()
container.write("This is inside the container")
st.write("This is outside the container")

# Now insert some more elements in the container
container.write("This is inside too")

