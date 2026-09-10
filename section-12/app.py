import streamlit as st

# st.title("I'm gonna find a programmer J O B")
st.title("Personal Finance Tracker")
st.write("Track all your expenses and earnings simple and visual")
st.caption("Version 1.0")

categorias = ["Food", "Transportation", "Essentials", "Leisure", "Home", "Health", "Other"]

descripcion = st.text_input("Description of the expense or income", placeholder="Write the description of the operation")
cantidad = st.number_input("Amount", step=1.0, min_value=0.0, format="%0.2f")
fecha = st.date_input("Date")
categoria = st.selectbox("Category", categorias)
tipo = st.radio("Type", ["Income", "Expense"], horizontal=True)

st.write("Summary: ")
st.write(f"{tipo} of ${cantidad} in {categoria} - {descripcion} the {fecha} ")