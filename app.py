import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Archivo Judicial Logroño", page_icon="⚖️")

st.title("⚖️ Buscador de Archivos - Logroño")
st.markdown("Consulta la ubicación física de los expedientes por Juzgado y Año.")

# 1. BASE DE DATOS DE UBICACIONES
# Definimos los límites y mensajes por juzgado
juzgados_data = {
    1: {"nombre": "INSTANCIA 1", "limite": 2014, "pos": "BLOQUE C PLANTA 1º NORTE C1.4 - DIGITALIZADO", "neg": "PEDIR AL ARCHIVO"},
    2: {"nombre": "INSTANCIA 2", "limite": 2018, "pos": "BLOQUE C PLANTA 1º SUR C1.3 - DIGITALIZADO", "neg": "PEDIR AL ARCHIVO"},
    3: {"nombre": "INSTANCIA 3", "limite": 2017, "pos": "BLOQUE C PLANTA 1º SUR C1.2 - NO DIGITALIZADO", "neg": "PEDIR AL ARCHIVO"},
    4: {"nombre": "INSTANCIA 4", "limite": 2018, "pos": "BLOQUE B PLANTA 1º SUR - DIGITALIZADO", "neg": "PEDIR AL ARCHIVO"},
    5: {"nombre": "INSTANCIA 5", "limite": 2015, "pos": "BLOQUE B PLANTA 1º NORTE B1.4 - DIGITALIZADO", "neg": "PEDIR AL ARCHIVO"},
    6: {"nombre": "INSTANCIA 6", "limite": 2020, "pos": "BLOQUE B PLANTA 2º SUR B2.4 - DIGITALIZADO", "neg": "PEDIR AL ARCHIVO"},
    7: {"nombre": "INSTANCIA 7", "limite": 2019, "pos": "BLOQUE C PLANTA 1º SUR C1.1 - DIGITALIZADO", "neg": "PEDIR AL ARCHIVO"},
    11: {"nombre": "PENAL 1", "limite": 2015, "pos": "BLOQUE B PLANTA 2º NORTE B2.4 - NO DIGITALIZADO", "neg": "PEDIR AL ARCHIVO"},
    12: {"nombre": "PENAL 2", "limite": 2013, "pos": "BLOQUE C PLANTA 2º NORTE C2.4 - NO DIGITALIZADO", "neg": "PEDIR AL ARCHIVO"},
    14: {"nombre": "VIOLENCIA SOBRE LA MUJER", "limite": 2013, "pos": "BLOQUE A PLANTA 1º SUR A1.3- NO DIGITALIZADO", "neg": "PEDIR AL ARCHIVO"},
    15: {"nombre": "MENORES", "limite": 2015, "pos": "BLOQUE A PLANTA 2º SUR A2.3- DIGITALIZADO", "neg": "PEDIR AL ARCHIVO"},
    16: {"nombre": "SOCIAL 1", "limite": 2017, "pos": "BLOQUE A PLANTA 2º SUR A2.1- NO DIGITALIZADO", "neg": "PEDIR AL ARCHIVO"},
    17: {"nombre": "SOCIAL 2", "limite": 2019, "pos": "BLOQUE A PLANTA 2º SUR A2.2- NO DIGITALIZADO", "neg": "PEDIR AL ARCHIVO"},
    18: {"nombre": "SOCIAL 3", "limite": 2017, "pos": "BLOQUE C PLANTA 2º SUR C2.1- DIGITALIZADO", "neg": "PEDIR AL ARCHIVO"},
    19: {"nombre": "CONT. ADM 1", "limite": 2017, "pos": "BLOQUE B PLANTA 2º SUR B2.2- NO DIGITALIZADO", "neg": "PEDIR AL ARCHIVO"},
    20: {"nombre": "CONT. ADM 2", "limite": 2014, "pos": "BLOQUE B PLANTA 2º SUR B2.3- NO DIGITALIZADO", "neg": "PEDIR AL ARCHIVO"},
}

# 2. INTERFAZ DE USUARIO (WIDGETS)
with st.container(border=True):
    # Desplegable de Juzgados
    opciones_juzgado = {f"{k} - {v['nombre']}": k for k, v in juzgados_data.items()}
    # Añadimos los casos especiales manualmente
    opciones_juzgado["8 - INSTRUCCIÓN 1"] = 8
    opciones_juzgado["9 - INSTRUCCIÓN 2"] = 9
    opciones_juzgado["10 - INSTRUCCIÓN 3 / VIGILANCIA"] = 10
    opciones_juzgado["13 - PENAL 3"] = 13
    opciones_juzgado["21 - AUDIENCIA PROV."] = 21

    seleccion = st.selectbox("Selecciona el Juzgado:", list(opciones_juzgado.keys()))
    id_j = opciones_juzgado[seleccion]

    # Desplegable de Año (desde 1990 hasta el actual)
    año_actual = 2024
    año = st.selectbox("Selecciona el Año:", list(range(año_actual, 1989, -1)))

# 3. LÓGICA DE RESPUESTA
st.subheader("Ubicación del Archivo:")

if id_j in juzgados_data:
    datos = juzgados_data[id_j]
    if año > datos["limite"]:
        st.success(datos["pos"])
    else:
        st.info(datos["neg"])

# Casos especiales con lógica compleja
elif id_j == 8:
    if 2013 < año < 2019: st.success("BLOQUE B PLANTA 1º SUR B1.3 - NO DIGITALIZADO")
    elif año > 2020: st.warning("COLEGIO DE ABOGADOS")
    else: st.info("PEDIR AL ARCHIVO")

elif id_j == 9:
    st.warning("BLOQUE B PLANTA 1º SUR B1.2 - NO DIGITALIZADO. SI ES MUY NUEVO COLEGIO DE ABOGADOS. SI ES MUY ANTIGUO PEDIR A ARCHIVO. CONSULTAR A CRISTINA")

elif id_j == 10:
    if 2014 < año < 2022: st.success("BLOQUE B PLANTA 1º SUR B1.3 - NO DIGITALIZADO")
    elif año > 2021: st.warning("COLEGIO DE ABOGADOS")
    else: st.info("PEDIR AL ARCHIVO")

elif id_j == 13:
    st.success("EJECUTORIAS BLOQUE B PLANTA 2º NORTE / RESTO EN COLEGIO DE ABOGADOS - DIGITALIZADO")

elif id_j == 21:
    st.success("BLOQUE C PLANTA 3º NORTE - DIGITALIZADO")

st.divider()
st.caption("Para una nueva consulta, simplemente cambia los valores en los desplegables.")