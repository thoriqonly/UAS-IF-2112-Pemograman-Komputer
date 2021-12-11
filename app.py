import streamlit as st
from multiapp import MultiApp
from apps import home, produksi, data, model # import your app modules here

app = MultiApp()

st.markdown("""
# SOAL UAS IF 2112 PEMROGAMAN KOMPUTER

Nama : Siapa saja

Nim : 00000000000

""")

# Add all your application here
app.add_app("home", home.app)
app.add_app("SOAL 1 A", produksi.app)
app.add_app("SOAL 1 B", data.app)
app.add_app("SOAL 1 C", model.app)
# The main app
app.run()