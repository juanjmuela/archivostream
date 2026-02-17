import streamlit as st

# Configuración visual
st.set_page_config(page_title="Archivo Logroño", page_icon="⚖️")

st.title("⚖️ Localizador de Archivos - Logroño")
st.info("Consulta la planta y bloque según el Juzgado y Año.")

# --- ENTRADA DE DATOS ---
with st.container(border=True):
    opcion = st.selectbox("SELECCIONA JUZGADO:", [
        "1 INSTANCIA 1", "2 INSTANCIA 2", "3 INSTANCIA 3", "4 INSTANCIA 4", 
        "5 INSTANCIA 5", "6 INSTANCIA 6", "7 INSTANCIA 7", "8 INSTRUCCIÓN 1", 
        "9 INSTRUCCIÓN 2", "10 INSTRUCCIÓN 3 / VIGILANCIA PENITENCIARIA", 
        "11 PENAL 1", "12 PENAL 2", "13 PENAL 3", "14 VIOLENCIA SOBRE LA MUJER", 
        "15 MENORES", "16 SOCIAL 1", "17 SOCIAL 2", "18 SOCIAL 3", 
        "19 CONT. ADM 1", "20 CONT. ADM. 2", "21 AUDIENCIA PROV."
    ])
    
    # Extraer el número del juzgado
    id_j = int(opcion.split()[0])
    
    año = st.number_input("TECLEA AÑO (CUATRO DÍGITOS):", min_value=1900, max_value=2030, value=2024)

st.divider()

# --- LÓGICA DE UBICACIÓN ---
st.subheader("📍 UBICACIÓN:")

if id_j == 1:
    st.success("BLOQUE C PLANTA 1º NORTE C1.4 - DIGITALIZADO") if año > 2014 else st.info("PEDIR AL ARCHIVO")
elif id_j == 2:
    st.success("BLOQUE C PLANTA 1º SUR C1.3 - DIGITALIZADO") if año > 2018 else st.info("PEDIR AL ARCHIVO")
elif id_j == 3:
    st.success("BLOQUE C PLANTA 1º SUR C1.2 - NO DIGITALIZADO") if año > 2017 else st.info("PEDIR AL ARCHIVO")
elif id_j == 4:
    st.success("BLOQUE B PLANTA 1º SUR - DIGITALIZADO") if año > 2018 else st.info("PEDIR AL ARCHIVO")
elif id_j == 5:
    st.success("BLOQUE B PLANTA 1º NORTE B1.4 - DIGITALIZADO") if año > 2015 else st.info("PEDIR AL ARCHIVO")
elif id_j == 6:
    st.success("BLOQUE B PLANTA 2º SUR B2.4 - DIGITALIZADO") if año > 2020 else st.info("PEDIR AL ARCHIVO")
elif id_j == 7:
    st.success("BLOQUE C PLANTA 1º SUR C1.1 - DIGITALIZADO") if año > 2019 else st.info("PEDIR AL ARCHIVO")
elif id_j == 8:
    if 2013 < año < 2019: st.success("BLOQUE B PLANTA 1º SUR B1.3 - NO DIGITALIZADO")
    elif año >= 2019: st.warning("COLEGIO DE ABOGADOS")
    else: st.info("PEDIR AL ARCHIVO")
elif id_j == 9:
    st.warning("BLOQUE B PLANTA 1º SUR B1.2 - NO DIGITALIZADO. SI ES MUY NUEVO COLEGIO DE ABOGADOS. SI ES MUY ANTIGUO PEDIR A ARCHIVO. CONSULTAR A CRISTINA")
elif id_j == 10:
    if 2014 < año < 2022: st.success("BLOQUE B PLANTA 1º SUR B1.3 - NO DIGITALIZADO")
    elif año >= 2022: st.warning("COLEGIO DE ABOGADOS")
    else: st.info("PEDIR AL ARCHIVO")
elif id_j == 11:
    st.success("BLOQUE B PLANTA 2º NORTE B2.4 - NO DIGITALIZADO") if año > 2015 else st.info("PEDIR AL ARCHIVO")
elif id_j == 12:
    st.success("BLOQUE C PLANTA 2º NORTE C2.4 - NO DIGITALIZADO") if año > 2013 else st.info("PEDIR AL ARCHIVO")
elif id_j == 13:
    st.success("EJECUTORIAS BLOQUE B PLANTA 2º NORTE / RESTO EN COLEGIO DE ABOGADOS - DIGITALIZADO")
elif id_j == 14:
    st.success("BLOQUE A PLANTA 1º SUR A1.3- NO DIGITALIZADO") if año > 2013 else st.info("PEDIR AL ARCHIVO")
elif id_j == 15:
    st.success("BLOQUE A PLANTA 2º SUR A2.3- DIGITALIZADO") if año > 2015 else st.info("PEDIR AL ARCHIVO")
elif id_j == 16:
    st.success("BLOQUE A PLANTA 2º SUR A2.1- NO DIGITALIZADO") if año > 2017 else st.info("PEDIR AL ARCHIVO")
elif id_j == 17:
    st.success("BLOQUE A PLANTA 2º SUR A2.2- NO DIGITALIZADO") if año > 2019 else st.info("PEDIR AL ARCHIVO")
elif id_j == 18:
    st.success("BLOQUE C PLANTA 2º SUR C2.1- DIGITALIZADO") if año > 2017 else st.info("PEDIR AL ARCHIVO")
elif id_j == 19:
    st.success("BLOQUE B PLANTA 2º SUR B2.2- NO DIGITALIZADO") if año > 2017 else st.info("PEDIR AL ARCHIVO")
elif id_j == 20:
    st.success("BLOQUE B PLANTA 2º SUR B2.3- NO DIGITALIZADO") if año > 2014 else st.info("PEDIR AL ARCHIVO")
elif id_j == 21:
    st.success("BLOQUE C PLANTA 3º NORTE - DIGITALIZADO")

st.divider()
st.caption("Cualquier duda, consulte con el responsable del archivo.")
