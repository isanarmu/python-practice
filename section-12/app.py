import streamlit as st

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
                                            "type": tipo,
                                            "send": enviado})
    st.success("Transaction added succesfully")
st.write("Acumulated transactions: ")
for transaccion in st.session_state.transacciones:
    st.write(transaccion)

st.write("Summary: ")
st.write(f"{tipo} of ${cantidad} in {categoria} - {descripcion} the {fecha} ")

if "contador" not in st.session_state:
    st.session_state.contador = 0

if st.button("Incrementar"):
    st.session_state.contador += 1
    st.write("contador : ", st.session_state.contador)