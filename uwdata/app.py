import streamlit as st
from multiapp import MultiApp
from apps import mgmteng
from apps import residence

app = MultiApp()

st.markdown("""
# Waterloo Engineering Admission Stats & Residence Preferences 
Kevin Lau 
""")

# Add all your application here
app.add_app("Admission Statistics", mgmteng.app)
app.add_app("Residence Statistics", residence.app)

# The main app
app.run()