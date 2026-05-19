import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Configuración de la página con estilo adorable
st.set_page_config(page_title="PetFinder Cute Predictor 🐾", page_icon="💖", layout="wide")

# --- 🎀 INYECCIÓN DE ESTILO CUSTOM CSS (AESTHETIC / PASTEL) 🎀 ---
st.markdown("""
    <style>
    /* Fondo general y fuentes */
    .stApp {
        background-color: #FFF0F5; /* Lavender Blush - Rosa pastel precioso */
    }
    
    h1, h2, h3, h4, h5, h6, p, label, span {
        color: #5D4037 !important; /* Marrón chocolate suave */
        font-family: 'Comic Sans MS', 'Arial', sans-serif;
    }
    
    /* Título principal con brillo */
    .titulo-magico {
        text-align: center;
        color: #FF6B8B !important;
        font-size: 3rem !important;
        font-weight: bold;
        text-shadow: 3px 3px 0px #FFFFFF;
        margin-top: -20px;
    }
    
    /* Contenedor del formulario principal */
    [data-testid="stForm"] {
        background-color: #FFFFFF !important;
        border: 4px dashed #FFB7B2 !important; /* Borde de galleta/pastel */
        border-radius: 25px !important;
        padding: 30px !important;
        box-shadow: 0px 8px 20px rgba(255, 183, 178, 0.5) !important;
    }
    
    /* Barra lateral estilo barrita de dulces */
    [data-testid="stSidebar"] {
        background-color: #FFE5EC !important;
        border-right: 3px solid #FFC2D1;
    }
    
    /* Botón mágico */
    div.stButton > button {
        background: linear-gradient(135deg, #FF85A2 0%, #FFA6C9 100%) !important;
        color: white !important;
        font-size: 20px !important;
        font-weight: bold !important;
        border-radius: 30px !important;
        border: 2px solid #FFFFFF !important;
        padding: 12px !important;
        box-shadow: 0px 5px 15px rgba(255, 133, 162, 0.4) !important;
        transition: all 0.3s ease-in-out;
    }
    
    div.stButton > button:hover {
        transform: scale(1.05) rotate(1deg);
        background: linear-gradient(135deg, #FF5C8A 0%, #FF85A2 100%) !important;
        box-shadow: 0px 8px 20px rgba(255, 92, 138, 0.6) !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 🗂️ BARRA LATERAL (SIDEBAR) PERSONALIZADA ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>🌸 Menú Mágico 🌸</h2>", unsafe_allow_html=True)
    st.markdown("<center><h1 style='font-size: 5rem; margin: 0;'>🐈‍⬛</h1></center>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 📝 Datos del Alumno")
    st.write("💝 **Estudiante:** Richelle Rodriguez Jurado")
    st.write("🆔 **Código ISIL:** 6816")
    
    st.markdown("---")
    st.markdown("### 🔗 Entregables")
    # REQUISITO: Cambia el enlace de abajo por tu link real de Colab en modo lector
    st.markdown("[🍓 Ver Google Colab](https://colab.research.google.com/drive/18xubbLLMhc8WTvMQvtOf5dkPirWD0o3t?usp=sharing)", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("<p style='text-align: center; font-size: 0.8rem;'>Hecho con amor para los animalitos rescatados 🐾</p>", unsafe_allow_html=True)

# --- ✨ CUERPO PRINCIPAL APP ✨ ---
st.markdown("<h1 class='titulo-magico'>✨ PetFinder Cute Predictor ✨</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2rem; font-weight: bold;'>¡Vamos a calcular la velocidad de adopción con estrellas y arcoíris! 🌈🧸</p>", unsafe_allow_html=True)
st.markdown("<center><h1 style='font-size: 4rem; margin: 0;'>🐶✨🐱</h1></center>", unsafe_allow_html=True)

# --- 🧠 CARGA DEL MODELO ---
ruta_modelo = 'modelos/modelo_random_forest.pkl'

if os.path.exists(ruta_modelo):
    model = joblib.load(ruta_modelo)
else:
    st.error("❌ ¡Oh no, linda! No encontré tu modelo en 'modelos/modelo_random_forest.pkl'.")
    st.stop()

# --- 🎈 FORMULARIO PRINCIPAL ADORABLE 🎈 ---
st.markdown("### 💌 Rellena los datos mágicos de la mascota:")

with st.form("formulario_lindo"):
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🪵 Datos Físicos Básicos")
        type_pet = st.selectbox("🌸 Tipo de Animalito", options=[1, 2], format_func=lambda x: "Perrito 🐶" if x == 1 else "Gatito 🐱")
        age = st.number_input("🍼 Edad (en meses)", min_value=0, max_value=250, value=3, step=1)
        gender = st.selectbox("🎀 Género", options=[1, 2, 3], format_func=lambda x: "Macho ♂️" if x == 1 else "Hembra ♀️" if x == 2 else "Grupo / Mixto 📦")
        breed1 = st.number_input("📜 Código Raza Principal", min_value=0, value=307, step=1)
        breed2 = st.number_input("📜 Código Raza Secundaria", min_value=0, value=0, step=1)
        color1 = st.number_input("🎨 Código Color Principal (1-7)", min_value=1, max_value=7, value=1, step=1)
        maturity_size = st.selectbox("📏 Tamaño esperado de grande", options=[1, 2, 3, 4], format_func=lambda x: ["Pequeñito", "Mediano", "Grandecito", "Gigante"][x-1])
        fur_length = st.selectbox("💇 Largo de su Pelaje", options=[1, 2, 3], format_func=lambda x: ["Cortito", "Medio", "Larguito"][x-1])
        
    with col2:
        st.markdown("#### 🏥 Cuidados y Salud")
        vaccinated = st.selectbox("💉 ¿Tiene sus Vacunas?", options=[1, 2, 3], format_func=lambda x: "Sí, protegido ✨" if x == 1 else "No" if x == 2 else "No se sabe")
        dewormed = st.selectbox("💊 ¿Está Desparasitado?", options=[1, 2, 3], format_func=lambda x: "Sí, sano 🌱" if x == 1 else "No" if x == 2 else "No se sabe")
        sterilized = st.selectbox("✂️ ¿Está Esterilizado?", options=[1, 2, 3], format_func=lambda x: "Sí, operado ✅" if x == 1 else "No" if x == 2 else "No se sabe")
        health = st.selectbox("❤️ Estado de Salud actual", options=[1, 2, 3], format_func=lambda x: "Súper Sano 💕" if x == 1 else "Lesión Ligera 🩹" if x == 2 else "Lesión Grave 🚑")
        
        st.markdown("#### 📸 Datos de la Publicación")
        quantity = st.number_input("👪 Cantidad de Mascotas juntas", min_value=1, value=1, step=1)
        fee = st.number_input("💵 Costo de Adopción ($)", min_value=0, value=0, step=1)
        photo_amt = st.number_input("📸 Fotos en el post", min_value=0, value=2, step=1)
        video_amt = st.number_input("🎥 Videos en el post", min_value=0, value=0, step=1)

    st.markdown("<br>", unsafe_allow_html=True)
    # Botón interactivo animado por CSS
    boton_predecir = st.form_submit_button("✨ ¡Calcular Tiempo de Adopción con Magia! 🔮")

# --- 🔮 SOLUCIÓN DEL ERROR Y RESULTADO ANIMADO 🔮 ---
if boton_predecir:
    # Creamos la matriz de entrada numérica pura en lugar de un DataFrame con nombres
    # Esto soluciona de raíz el ValueError de nombres de columnas (feature_names)
    matriz_entrada = np.array([[
        type_pet, age, breed1, breed2, gender, color1,
        maturity_size, fur_length, vaccinated, dewormed,
        sterilized, health, quantity, fee, video_amt, photo_amt
    ]])
    
    # Predecir ignorando las etiquetas del dataset original para evitar choques
    clase_predicha = model.predict(matriz_entrada)[0]
    
    # Categorías adorables
    categorias_adopcion = {
        0: "⚡ ¡Adopción Flash! Se irá a casa hoy mismo 💖",
        1: "🚗 ¡Súper Rápido! Conseguirá familia en menos de una semanita 🏠✨",
        2: "🏡 ¡Adopción Rápida! Tarda entre 8 y 30 días en enamorar a alguien 🥰",
        3: "⏳ Adopción Moderada. Tarda de 1 a 3 meses, ¡pero el amor llega! 🌸",
        4: "🧸 Adopción Difícil. Requiere un poquito más de tiempo y paciencia (+100 días) 💕"
    }
    
    resultado_final = categorias_adopcion.get(clase_predicha, "¡Categoría misteriosa! ✨")
    
    # 🌟 ANIMACIONES SIMULTÁNEAS 🌟
    st.balloons() # Globos de abajo hacia arriba
    st.snow()     # Efecto de estrellas/nieve cayendo
    
    st.markdown("### 💌 La Respuesta de las Estrellas:")
    st.success(f"**{resultado_final}**")
