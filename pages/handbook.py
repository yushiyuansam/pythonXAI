import os
import streamlit as st

files = os.listdir("markdown")
print(files)

files.sort()
print(files)

for f in files:
    with open(f"markdown/{f}", "r", encoding="utf-8") as file:
        content = file.read()

    with st.expander(f[:-3]):
        st.write(content)
