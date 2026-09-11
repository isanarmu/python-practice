import streamlit as st
import pandas as pd


categorias = ["Food", "Transportation", "Essentials", "Leisure", "Home", "Health", "Other"]
categorias_ingresos = ["Salary", "Sale", "Stocks", "Other"]

def mostrar_titulos():
    st.title("Personal Finance Tracker")
    st.write("Track all your expenses and earnings simple and visual")
    st.caption("Version 1.0")
    # st.title("I'm gonna find a programmer J O B") 
    


# Inicializa la lista de transacciones si todavía no existe.
def inicializar_estado():
    if "transacciones" not in st.session_state:
        st.session_state.transacciones = []


# Muestra el formulario y guarda la transacción cuando se envía.
def mostrar_formulario():
    with st.sidebar:
        # para ocultar texto sueprpuesto con placeholder
        st.markdown(
            """
            <style>
            div[data-testid="InputInstructions"] {
                display: none;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        
        tipo = st.radio("Type", ["Income", "Expense"], horizontal=True)
        with st.form("New transaction"):
            descripcion = st.text_input("Description of the expense or income", placeholder="Write the description of the operation")
            cantidad = st.number_input("Amount", step=1.0, min_value=0.0, format="%0.2f")
            fecha = st.date_input("Date")
            opciones_categoria = categorias_ingresos if tipo == "Income" else categorias
            categoria = st.selectbox("Category", opciones_categoria)
            enviado = st.form_submit_button("Submit")

        if enviado:
            st.session_state.transacciones.append({"Description": descripcion,
                                                    "amount": cantidad,
                                                    "date": fecha,
                                                    "category": categoria,
                                                    "type": tipo})
            st.success("Transaction added succesfully")


# Muestra las transacciones registradas o un mensaje informativo si no hay ninguna.
def mostrar_transacciones():
    st.subheader("Registered transactions: ")

    if st.session_state.transacciones:
        df = pd.DataFrame(st.session_state.transacciones)
        st.dataframe(df)
    else:
        st.info("No registered transactions")


# Calculates and displays the transaction summary metrics.
def mostrar_resumen():
    if not st.session_state.transacciones:
        st.info("No transactions available yet")
        return

    ingresos = sum(
        transaccion["amount"]
        for transaccion in st.session_state.transacciones
        if transaccion["type"] == "Income"
    )
    gastos = [
        transaccion["amount"]
        for transaccion in st.session_state.transacciones
        if transaccion["type"] == "Expense"
    ]
    total_gastos = sum(gastos)
    balance = ingresos - total_gastos
    gasto_promedio = total_gastos / len(gastos) if gastos else 0

    metricas = st.columns(4)
    metricas[0].metric("Income", f"€{ingresos:.2f}")
    metricas[1].metric("Expenses", f"€{total_gastos:.2f}")
    metricas[2].metric("Balance", f"€{balance:.2f}")
    metricas[3].metric("Average expense", f"€{gasto_promedio:.2f}")


mostrar_titulos()
inicializar_estado()
mostrar_formulario()

tab_resumen, movimientos, analisis = st.tabs(["Resumen", "Movimientos", "Análisis"])

with tab_resumen:
    mostrar_resumen()

with movimientos:
    mostrar_transacciones()

with analisis:
    st.info("Próximamente")

