#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import networkx as nx
import matplotlib.pyplot as plt
import streamlit as st

# Generate a random graph with 1000 nodes
G = nx.random_geometric_graph(1000, 0.1)

# Create a Streamlit app
st.title("Graph Visualization")
st.sidebar.header("Graph Settings")

# Add options to customize the graph (e.g., layout, node color, etc.)
layout = st.sidebar.selectbox("Choose layout", ["spring", "circular", "random"])
node_color = st.sidebar.color_picker("Node color", "#1f78b4")

# Set graph layout
pos = nx.spring_layout(G) if layout == "spring" else nx.circular_layout(G)

# Draw the graph
nx.draw(G, pos, node_color=node_color, with_labels=False, node_size=10)
plt.axis("off")

# Display the graph in Streamlit
st.pyplot(plt)

