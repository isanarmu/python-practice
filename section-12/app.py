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


def mostrar_filtros():
    transacciones = st.session_state.transacciones
    fechas = [transaccion["date"] for transaccion in transacciones]
    fecha_desde = min(fechas) if fechas else None
    fecha_hasta = max(fechas) if fechas else None

    categorias_seleccionadas = st.multiselect(
        "Categorías",
        categorias,
        default=categorias,
    )
    desde = st.date_input("Desde", value=fecha_desde)
    hasta = st.date_input("Hasta", value=fecha_hasta)

    return categorias_seleccionadas, desde, hasta


def filtrar_transacciones(transacciones, categorias_seleccionadas, desde, hasta):
    return [
        transaccion
        for transaccion in transacciones
        if transaccion["category"] in categorias_seleccionadas
        and desde <= transaccion["date"] <= hasta
    ]


# Muestra las transacciones registradas o un mensaje informativo si no hay ninguna.
def mostrar_transacciones(transacciones):
    st.subheader("Registered transactions: ")

    if transacciones:
        df = pd.DataFrame(transacciones)
        st.dataframe(df)
    else:
        st.info("No registered transactions")


# Calculates and displays the transaction summary metrics.
def mostrar_resumen(transacciones):
    if not transacciones:
        st.info("No transactions available yet")
        return

    ingresos = sum(
        transaccion["amount"]
        for transaccion in transacciones
        if transaccion["type"] == "Income"
    )
    gastos = [
        transaccion["amount"]
        for transaccion in transacciones
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


# Aggregates and displays expenses by category and date.
def mostrar_analisis(transacciones):
    gastos = []
    for transaccion in transacciones:
        if transaccion["type"] == "Expense":
            gastos.append(transaccion)

    if not gastos:
        st.info("No expense transactions available yet")
        return

    gastos_por_categoria = {}
    for transaccion in gastos:
        categoria = transaccion["category"]
        if categoria not in gastos_por_categoria:
            gastos_por_categoria[categoria] = 0
        gastos_por_categoria[categoria] += transaccion["amount"]

    datos_categoria = []
    for categoria, total in gastos_por_categoria.items():
        datos_categoria.append({"Category": categoria, "Total expenses": total})
    df_categoria = pd.DataFrame(datos_categoria, columns=["Category", "Total expenses"])

    st.subheader("Total expenses by category")
    st.bar_chart(df_categoria, x="Category", y="Total expenses")

    gastos_por_fecha = {}
    for transaccion in gastos:
        fecha = transaccion["date"]
        if fecha not in gastos_por_fecha:
            gastos_por_fecha[fecha] = 0
        gastos_por_fecha[fecha] += transaccion["amount"]

    datos_fecha = []
    for fecha, total in sorted(gastos_por_fecha.items()):
        datos_fecha.append({"Date": fecha, "Total expenses": total})
    df_fecha = pd.DataFrame(datos_fecha, columns=["Date", "Total expenses"])

    st.subheader("Total expenses by date")
    st.line_chart(df_fecha, x="Date", y="Total expenses")


mostrar_titulos()
inicializar_estado()

with st.sidebar:
    mostrar_formulario()
    categorias_seleccionadas, desde, hasta = mostrar_filtros()

transacciones_filtradas = filtrar_transacciones(
    st.session_state.transacciones,
    categorias_seleccionadas,
    desde,
    hasta,
)

tab_resumen, movimientos, analisis = st.tabs(["Resumen", "Movimientos", "Análisis"])

with tab_resumen:
    mostrar_resumen(transacciones_filtradas)

with movimientos:
    mostrar_transacciones(transacciones_filtradas)

with analisis:
    mostrar_analisis(transacciones_filtradas)

