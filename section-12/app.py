import streamlit as st
import pandas as pd

# st.title("I'm gonna find a programmer J O B")
st.title("Personal Finance Tracker")
st.write("Track all your expenses and earnings simple and visual")
st.caption("Version 1.0")

categorias = ["Food", "Transportation", "Essentials", "Leisure", "Home", "Health", "Other"]

if "transacciones" not in st.session_state:
    st.session_state.transacciones = []

with st.form("New transaction"):
    descripcion = st.text_input("Description of the expense or income", placeholder="Write the description of the operation")
    cantidad = st.number_input("Amount", step=1.0, min_value=0.0, format="%0.2f")
    fecha = st.date_input("Date")
    categoria = st.selectbox("Category", categorias)
    tipo = st.radio("Type", ["Income", "Expense"], horizontal=True)
    enviado = st.form_submit_button("Submit")

if enviado:
    st.session_state.transacciones.append({"Description": descripcion,
                                            "amount": cantidad,
                                            "date": fecha,
                                            "category": categoria,
                                            "type": tipo})
    st.success("Transaction added succesfully")

st.subheader("Registered transactions: ")

if st.session_state.transacciones:
    df = pd.DataFrame(st.session_state.transacciones)
    st.dataframe(df)
else:
    st.info("No registered transactions")


