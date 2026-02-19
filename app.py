import streamlit as st

st.set_page_config(page_title="Archivo Logroño", page_icon="📚")

st.title("📚 UBICACIÓN EXPEDIENTES 📚")

# Selector de juzgados con nombres completos
opciones = [
    "1 INSTANCIA 1", "2 INSTANCIA 2", "3 INSTANCIA 3", "4 INSTANCIA 4",
    "5 INSTANCIA 5", "6 INSTANCIA 6", "7 INSTANCIA 7", "8 INSTRUCCIÓN 1",
    "9 INSTRUCCIÓN 2", "10 INSTRUCCIÓN 3 / VIGILANCIA PENITENCIARIA",
    "11 PENAL 1", "12 PENAL 2", "13 PENAL 3 (Creado en 2020)", "14 VIOLENCIA SOBRE LA MUJER",
    "15 MENORES", "16 SOCIAL 1", "17 SOCIAL 2", "18 SOCIAL 3",
    "19 CONT. ADM 1", "20 CONT. ADM. 2", "21 AUDIENCIA PROV."
]

seleccion = st.selectbox("SELECCIONA JUZGADO:", opciones)
juzgado_num = int(seleccion.split()[0])

año_input = st.text_input("TECLEA AÑO (4 DÍGITOS):", value="")

# Botón de reinicio
if st.button("🔄 NUEVA CONSULTA"):
    st.rerun()

st.divider()

if año_input.isdigit():
    año = int(año_input)
    st.subheader("📍 UBICACIÓN:")
    
    # 1 al 7
    if juzgado_num == 1:
        if año > 2014: st.success("BLOQUE C PLANTA 1º NORTE C1.4 - DIGITALIZADO")
        else: st.info("PEDIR AL ARCHIVO")
    elif juzgado_num == 2:
        if año > 2018: st.success("BLOQUE C PLANTA 1º SUR C1.3 - DIGITALIZADO")
        else: st.info("PEDIR AL ARCHIVO")
    elif juzgado_num == 3:
        if año > 2017: st.success("BLOQUE C PLANTA 1º SUR C1.2 - NO DIGITALIZADO")
        else: st.info("PEDIR AL ARCHIVO")
    elif juzgado_num == 4:
        if año > 2018: st.success("BLOQUE B PLANTA 1º SUR B1.1- DIGITALIZADO")
        else: st.info("PEDIR AL ARCHIVO")
    elif juzgado_num == 5:
        if año > 2015: st.success("BLOQUE B PLANTA 1º NORTE B1.4 - DIGITALIZADO")
        else: st.info("PEDIR AL ARCHIVO")
    elif juzgado_num == 6:
        if año > 2020: st.success("BLOQUE B PLANTA 2º SUR B2.1 - DIGITALIZADO")
        else: st.info("PEDIR AL ARCHIVO")
    elif juzgado_num == 7:
        if año > 2019: st.success("BLOQUE C PLANTA 1º SUR C1.1 - DIGITALIZADO")
        else: st.info("PEDIR AL ARCHIVO")
    
    # Casos Especiales 8, 9, 10
    elif juzgado_num == 8:
        if 2013 < año < 2021: st.success("BLOQUE B PLANTA 1º SUR B1.3 - NO DIGITALIZADO")
        elif año >= 2021: st.warning("🏛️ COLEGIO DE ABOGADOS")
        else: st.info("PEDIR AL ARCHIVO")
    elif juzgado_num == 9:
        st.warning("BLOQUE B PLANTA 1º SUR B1.2 - NO DIGITALIZADO. SI ES MUY NUEVO COLEGIO DE ABOGADOS. SI ES MUY ANTIGUO PEDIR A ARCHIVO. CONSULTAR A CRISTINA")
    elif juzgado_num == 10:
        if 2014 < año < 2022: st.success("BLOQUE A PLANTA 1º SUR A1.1 - NO DIGITALIZADO 🦥")
        elif año >= 2022: st.warning("🏛️ COLEGIO DE ABOGADOS")
        else: st.info("PEDIR AL ARCHIVO")
    
    # 11 al 21
    elif juzgado_num == 11:
        if año > 2015: st.success("BLOQUE B PLANTA 2º NORTE B2.4 - NO DIGITALIZADO")
        else: st.info("PEDIR AL ARCHIVO")
    elif juzgado_num == 12:
        if año > 2013: st.success("BLOQUE C PLANTA 2º NORTE C2.4 (Si EJEC ANTERIOR A 225/2014 PEDIR ARCHIVO - NO DIGITALIZADO")
        else: st.info("PEDIR AL ARCHIVO")
    elif juzgado_num == 13:
        st.success("EJECUTORIAS BLOQUE B PLANTA 2º NORTE / RESTO EN COLEGIO DE ABOGADOS - DIGITALIZADO")
    elif juzgado_num == 14:
        if año > 2013: st.success("BLOQUE A PLANTA 1º SUR A1.3- NO DIGITALIZADO")
        else: st.info("PEDIR AL ARCHIVO")
    elif juzgado_num == 15:
        if año > 2015: st.success("BLOQUE A PLANTA 2º SUR A2.3- DIGITALIZADO")
        else: st.info("PEDIR AL ARCHIVO")
    elif juzgado_num == 16:
        if año > 2017: st.success("BLOQUE A PLANTA 2º SUR A2.1- NO DIGITALIZADO")
        else: st.info("PEDIR AL ARCHIVO")
    elif juzgado_num == 17:
        if año > 2019: st.success("BLOQUE A PLANTA 2º SUR A2.2- NO DIGITALIZADO")
        else: st.info("PEDIR AL ARCHIVO")
    elif juzgado_num == 18:
        if año > 2017: st.success("BLOQUE C PLANTA 2º SUR C2.1- DIGITALIZADO")
        else: st.info("PEDIR AL ARCHIVO")
    elif juzgado_num == 19:
        if año > 2017: st.success("BLOQUE B PLANTA 2º SUR B2.2- NO DIGITALIZADO")
        else: st.info("PEDIR AL ARCHIVO")
    elif juzgado_num == 20:
        if año > 2014: st.success("BLOQUE B PLANTA 2º SUR B2.3- NO DIGITALIZADO")
        else: st.info("PEDIR AL ARCHIVO")
    elif juzgado_num == 21:
        st.success("BLOQUE C PLANTA 3º NORTE - DIGITALIZADO")

elif año_input != "":
    st.error("⚠️ Por favor, introduce un año válido con números.")

st.divider()
st.caption("Base de datos realizada según el folio que andaba pegado a un armario.")


