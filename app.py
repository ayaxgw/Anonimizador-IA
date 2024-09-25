import streamlit as st
import os
import tempfile
from anonimizacion import anonimizacion

st.set_page_config(page_title="IA APP", page_icon=":camera", layout="centered", initial_sidebar_state="collapsed")

st.image("incognito.jpg", use_column_width=True)
st.header("Anonimización de imágenes con IA")    
st.subheader("Sube una imagen")
uploaded_image = st.file_uploader("Elige una imagen...", type=["jpg", "jpeg", "png"], accept_multiple_files=False)

file_name = "processed_image.png"   

if uploaded_image is not None:
    st.image(uploaded_image, caption="Imagen subida", use_column_width=True)
    anonymisation_button = st.button(label="Anonimizar")

    if anonymisation_button:
        try:
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(uploaded_image.read())
                file_path = temp_file.name

            temp_final_img = anonimizacion(file_name, file_path)    

            st.image(temp_final_img, caption="Imagen anonimizada", use_column_width=True)

            with open(file_name, "rb") as f:
                image_data = f.read()

            st.download_button("Descargar imagen anonimizada", data=image_data, file_name=file_name)
            os.remove(file_name)

        except Exception as e:
            st.error(f"Ha ocurrido un error: {e}")
    


# Implementando algoritmo de IA, utilizando libreria de opencv de computervision.