import streamlit as st
import pandas as pd
from datetime import date as fecha_date


categorias = ["Food", "Transportation", "Essentials", "Leisure", "Home", "Health", "Other"]
categorias_ingresos = ["Salary", "Sale", "Stocks", "Other"]
ARCHIVO_DATOS = "transacciones.csv"
tipos_transaccion = {
    "income": "Income",
    "ingreso": "Income",
    "expense": "Expense",
    "gasto": "Expense",
}


class Transaccion:
    def __init__(self, Description, amount, date, category, type):
        self.Description = Description
        self.amount = float(amount)
        self.date = date if isinstance(date, fecha_date) else fecha_date.fromisoformat(str(date))
        self.category = category
        self.type = tipos_transaccion.get(str(type).strip().lower(), type)

    def es_gasto(self):
        return self.type == "Expense"

    def es_ingreso(self):
        return self.type == "Income"

    def to_dict(self):
        return {
            "Description": self.Description,
            "amount": self.amount,
            "date": self.date,
            "category": self.category,
            "type": self.type,
        }


class Cartera:
    def __init__(self, transacciones=None):
        self.transacciones = []
        for transaccion in transacciones or []:
            self.agregar(transaccion)

    def __iter__(self):
        return iter(self.transacciones)

    def __len__(self):
        return len(self.transacciones)

    def __bool__(self):
        return bool(self.transacciones)

    def agregar(self, transaccion):
        if not isinstance(transaccion, Transaccion):
            transaccion = Transaccion(**transaccion)
        self.transacciones.append(transaccion)

    def ingresos_totales(self):
        return sum(transaccion.amount for transaccion in self if transaccion.es_ingreso())

    def gastos_totales(self):
        return sum(transaccion.amount for transaccion in self if transaccion.es_gasto())

    def balance(self):
        return self.ingresos_totales() - self.gastos_totales()

    def gasto_promedio(self):
        gastos = [transaccion for transaccion in self if transaccion.es_gasto()]
        return self.gastos_totales() / len(gastos) if gastos else 0

    def filtrar(self, categorias_seleccionadas, desde, hasta):
        return Cartera(
            transaccion
            for transaccion in self
            if transaccion.category in categorias_seleccionadas
            and desde <= transaccion.date <= hasta
        )

    def gastos_por_categoria(self):
        gastos = {}
        for transaccion in self:
            if transaccion.es_gasto():
                gastos[transaccion.category] = gastos.get(transaccion.category, 0) + transaccion.amount
        return gastos

    def gastos_por_fecha(self):
        gastos = {}
        for transaccion in self:
            if transaccion.es_gasto():
                gastos[transaccion.date] = gastos.get(transaccion.date, 0) + transaccion.amount
        return gastos

    def a_dataframe(self):
        return pd.DataFrame([transaccion.to_dict() for transaccion in self])

    def guardar_csv(self, archivo=ARCHIVO_DATOS):
        self.a_dataframe().to_csv(archivo, index=False)

    @classmethod
    def cargar_csv(cls, archivo=ARCHIVO_DATOS):
        try:
            df = pd.read_csv(archivo)
            return cls(df.to_dict(orient="records"))
        except Exception:
            return cls()

    @classmethod
    def desde_dataframe_importado(cls, df):
        columnas_esperadas = ["descripcion", "monto", "fecha", "categoria", "tipo"]
        if not all(columna in df.columns for columna in columnas_esperadas):
            raise ValueError(
                "El CSV debe contener las columnas: "
                + ", ".join(columnas_esperadas)
            )

        transacciones = []
        for _, fila in df.iterrows():
            transacciones.append(
                Transaccion(
                    fila["descripcion"],
                    float(fila["monto"]),
                    fecha_date.fromisoformat(str(fila["fecha"])),
                    fila["categoria"],
                    fila["tipo"],
                )
            )
        return cls(transacciones)

def mostrar_titulos():
    st.title("Personal Finance Tracker")
    st.write("Track all your expenses and earnings simple and visual")
    st.caption("Version 1.0")
    # st.title("I'm gonna find a programmer J O B") 
    


# Inicializa la lista de transacciones si todavía no existe.
def inicializar_estado():
    if "transacciones" not in st.session_state:
        st.session_state.transacciones = Cartera.cargar_csv()
    elif not isinstance(st.session_state.transacciones, Cartera):
        st.session_state.transacciones = Cartera(st.session_state.transacciones)


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
            st.session_state.transacciones.agregar(
                Transaccion(descripcion, cantidad, fecha, categoria, tipo)
            )
            st.success("Transaction added succesfully")


def importar_csv():
    with st.expander("Importar desde CSV"):
        archivo = st.file_uploader("Selecciona un archivo CSV", type=["csv"])
        importar = st.button("Importar transacciones")

        if importar:
            if archivo is None:
                st.warning("Primero sube un archivo CSV")
                return

            try:
                df = pd.read_csv(archivo)
            except Exception:
                st.error("El archivo no es un CSV válido")
                return

            try:
                cartera_importada = Cartera.desde_dataframe_importado(df)
            except ValueError as error:
                if str(error).startswith("El CSV debe contener"):
                    st.error(str(error))
                else:
                    st.error("El CSV contiene un monto o una fecha no válida")
                return

            except (TypeError, KeyError):
                st.error("El CSV contiene un monto o una fecha no válida")
                return

            for transaccion in cartera_importada:
                st.session_state.transacciones.agregar(transaccion)
            st.success(f"Se importaron {len(cartera_importada)} transacciones")


def mostrar_filtros():
    transacciones = st.session_state.transacciones
    fechas = [transaccion.date for transaccion in transacciones]
    fecha_desde = min(fechas) if fechas else None
    fecha_hasta = max(fechas) if fechas else None
    categorias_disponibles = sorted(
        set(categorias)
        | {transaccion.category for transaccion in transacciones}
    )

    categorias_seleccionadas = st.multiselect(
        "Categorías",
        categorias_disponibles,
        default=categorias_disponibles,
    )
    desde = st.date_input("Desde", value=fecha_desde)
    hasta = st.date_input("Hasta", value=fecha_hasta)

    return categorias_seleccionadas, desde, hasta


# Muestra las transacciones registradas o un mensaje informativo si no hay ninguna.
def mostrar_transacciones(transacciones):
    st.subheader("Registered transactions: ")

    if transacciones:
        df = transacciones.a_dataframe()
        st.dataframe(df)
        st.download_button(
            "Descargar transacciones",
            data=df.to_csv(index=False),
            file_name="mis_transacciones.csv",
            mime="text/csv",
        )
    else:
        st.info("No registered transactions")


# Calculates and displays the transaction summary metrics.
def mostrar_resumen(transacciones):
    if not transacciones:
        st.info("No transactions available yet")
        return

    ingresos = transacciones.ingresos_totales()
    total_gastos = transacciones.gastos_totales()
    balance = transacciones.balance()
    gasto_promedio = transacciones.gasto_promedio()

    metricas = st.columns(4)
    metricas[0].metric("Income", f"€{ingresos:.2f}")
    metricas[1].metric("Expenses", f"€{total_gastos:.2f}")
    metricas[2].metric("Balance", f"€{balance:.2f}")
    metricas[3].metric("Average expense", f"€{gasto_promedio:.2f}")


# Aggregates and displays expenses by category and date.
def mostrar_analisis(transacciones):
    gastos_por_categoria = transacciones.gastos_por_categoria()
    gastos_por_fecha = transacciones.gastos_por_fecha()

    if not gastos_por_categoria:
        st.info("No expense transactions available yet")
        return

    datos_categoria = []
    for categoria, total in gastos_por_categoria.items():
        datos_categoria.append({"Category": categoria, "Total expenses": total})
    df_categoria = pd.DataFrame(datos_categoria, columns=["Category", "Total expenses"])

    st.subheader("Total expenses by category")
    st.bar_chart(df_categoria, x="Category", y="Total expenses")

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
    importar_csv()
    categorias_seleccionadas, desde, hasta = mostrar_filtros()

transacciones_filtradas = st.session_state.transacciones.filtrar(
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

st.session_state.transacciones.guardar_csv()