import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Configuración de la página
st.set_page_config(page_title="PetFinder Cute Predictor 🐾", page_icon="💖", layout="wide")

# --- 🎀 INYECCIÓN DE ESTILO CUSTOM CSS (AESTHETIC / PASTEL REFINADO) 🎀 ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap');

    .stApp {
        background: #FDF6FB;
        background-image: radial-gradient(circle at 20% 20%, #F8E8F5 0%, transparent 50%),
                          radial-gradient(circle at 80% 80%, #EAF0FB 0%, transparent 50%);
    }

    h1, h2, h3, h4, h5, h6, p, label, span, div {
        font-family: 'Nunito', sans-serif !important;
        color: #4A3560 !important;
    }

    .titulo-magico {
        text-align: center;
        background: linear-gradient(135deg, #C97AB5 0%, #8B6BB1 50%, #6A8FD8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 2.8rem !important;
        font-weight: 800 !important;
        letter-spacing: -0.5px;
        margin-top: -10px;
        line-height: 1.2;
    }

    .subtitulo {
        text-align: center;
        font-size: 1.1rem !important;
        color: #9B8AB4 !important;
        font-weight: 600 !important;
        margin-top: -8px;
    }

    /* Formulario principal */
    [data-testid="stForm"] {
        background: linear-gradient(160deg, #FFFFFF 0%, #FBF5FF 100%) !important;
        border: 1.5px solid #E8D5F5 !important;
        border-radius: 24px !important;
        padding: 32px !important;
        box-shadow: 0px 12px 40px rgba(180, 120, 200, 0.12),
                    0px 2px 8px rgba(180, 120, 200, 0.08) !important;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #F5EEF8 0%, #EEF2FB 100%) !important;
        border-right: 1.5px solid #E2D4F0 !important;
    }

    [data-testid="stSidebar"] * {
        font-family: 'Nunito', sans-serif !important;
    }

    /* Botón principal */
    div.stButton > button {
        background: linear-gradient(135deg, #C97AB5 0%, #9B7FD4 50%, #7B9ED9 100%) !important;
        color: white !important;
        font-size: 17px !important;
        font-weight: 700 !important;
        font-family: 'Nunito', sans-serif !important;
        border-radius: 50px !important;
        border: none !important;
        padding: 14px 28px !important;
        box-shadow: 0px 6px 20px rgba(180, 110, 190, 0.35) !important;
        letter-spacing: 0.3px;
        transition: all 0.25s cubic-bezier(0.34, 1.56, 0.64, 1);
        width: 100%;
    }

    div.stButton > button:hover {
        transform: translateY(-2px) scale(1.02);
        box-shadow: 0px 10px 28px rgba(180, 110, 190, 0.45) !important;
        background: linear-gradient(135deg, #B868A3 0%, #8B6FC4 50%, #6B8EC9 100%) !important;
    }

    div.stButton > button:active {
        transform: translateY(0px) scale(0.99);
    }

    /* Selectboxes e inputs */
    [data-testid="stSelectbox"] > div,
    [data-testid="stNumberInput"] > div {
        border-radius: 12px !important;
    }

    /* Separadores */
    hr {
        border-color: #E8D5F5 !important;
        opacity: 0.7;
    }

    /* Headers de sección dentro del form */
    .section-header {
        font-size: 0.95rem !important;
        font-weight: 700 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #9B7FD4 !important;
        margin-bottom: 12px;
        padding-bottom: 6px;
        border-bottom: 2px solid #EAD8FA;
    }

    /* Resultado */
    [data-testid="stAlert"] {
        border-radius: 16px !important;
        border-left-width: 5px !important;
        font-family: 'Nunito', sans-serif !important;
        font-size: 1.05rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 🗂️ BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    st.markdown("""
        <div style='text-align: center; padding: 10px 0 4px;'>
            <span style='font-size: 2.8rem;'>🐈‍⬛</span>
            <h2 style='font-size: 1.2rem; font-weight: 800; color: #7B5EA7 !important; margin: 8px 0 0;'>Menú Mágico</h2>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
        <div style='background: white; border-radius: 16px; padding: 16px 18px;
                    border: 1.5px solid #E8D5F5; margin-bottom: 12px;'>
            <p style='font-size: 0.78rem; font-weight: 700; text-transform: uppercase;
                      letter-spacing: 1px; color: #B09ACA !important; margin: 0 0 10px;'>
                📝 Datos del Alumno
            </p>
            <p style='margin: 4px 0; font-size: 0.92rem; color: #5A4070 !important;'>
                💝 <strong>Estudiante:</strong><br>
                <span style='color: #7B5EA7 !important;'>Richelle Rodriguez Jurado</span>
            </p>
            <p style='margin: 8px 0 0; font-size: 0.92rem; color: #5A4070 !important;'>
                🆔 <strong>Código ISIL:</strong>
                <span style='color: #7B5EA7 !important;'> 6816</span>
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style='background: white; border-radius: 16px; padding: 16px 18px;
                    border: 1.5px solid #E8D5F5;'>
            <p style='font-size: 0.78rem; font-weight: 700; text-transform: uppercase;
                      letter-spacing: 1px; color: #B09ACA !important; margin: 0 0 10px;'>
                🔗 Entregables
            </p>
            <a href='https://colab.research.google.com/drive/18xubbLLMhc8WTvMQvtOf5dkPirWD0o3t?usp=sharing'
               style='display: inline-flex; align-items: center; gap: 6px;
                      background: linear-gradient(135deg, #C97AB5, #8B6BB1);
                      color: white !important; text-decoration: none;
                      font-size: 0.88rem; font-weight: 700;
                      padding: 8px 14px; border-radius: 50px;'>
                🍓 Ver Google Colab
            </a>
        </div>
    """, unsafe_allow_html=True)

# --- ✨ CUERPO PRINCIPAL APP ✨ ---
st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
st.markdown("<h1 class='titulo-magico'>✨ PetFinder Cute Predictor ✨</h1>", unsafe_allow_html=True)
st.markdown(
    "<p class='subtitulo'>Calculamos el tiempo de adopción con estrellas y arcoíris 🌈</p>",
    unsafe_allow_html=True
)
st.markdown(
    "<div style='text-align: center; font-size: 3rem; margin: 8px 0 24px;'>🐶🐱</div>",
    unsafe_allow_html=True
)

# --- 🧠 CARGA DEL MODELO ---
ruta_modelo = 'modelos/modelo_random_forest.pkl'
if os.path.exists(ruta_modelo):
    model = joblib.load(ruta_modelo)
else:
    st.error("❌ ¡Oh no, linda! No encontré tu modelo en 'modelos/modelo_random_forest.pkl'.")
    st.stop()

# --- 📜 DICCIONARIO DE RAZAS MÁGICAS ---
diccionario_razas = {
    "Sin Raza / Mestizo ✨": 307,
    "Poodle 🐩": 179,
    "Persa 🐱": 285,
    "Siames 🐈": 292,
    "Golden Retriever 🦮": 109,
    "Pastor Alemán 🐕": 115,
    "Chihuahua 🐕‍🦺": 65,
    "Labrador 🐕": 141,
    "Angora 🐈‍⬛": 241,
    "Bengala 🐯": 247
}

# --- 🎈 FORMULARIO PRINCIPAL 🎈 ---
st.markdown(
    "<p style='font-size: 1rem; font-weight: 700; color: #9B7FD4 !important;"
    " margin-bottom: 12px;'>💌 Rellena los datos mágicos de la mascota:</p>",
    unsafe_allow_html=True
)

with st.form("formulario_lindo"):
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("<p class='section-header'>🪵 Características Básicas</p>", unsafe_allow_html=True)
        type_pet = st.selectbox("🌸 Tipo de Animalito", options=[1, 2],
                                format_func=lambda x: "Perrito 🐶" if x == 1 else "Gatito 🐱")
        age = st.number_input("🍼 Edad (en meses)", min_value=0, max_value=250, value=3, step=1)
        gender = st.selectbox("🎀 Género", options=[1, 2, 3],
                              format_func=lambda x: "Macho ♂️" if x == 1 else "Hembra ♀️" if x == 2 else "Grupo / Mixto 📦")
        raza_seleccionada = st.selectbox("🧬 Selección de Raza", options=list(diccionario_razas.keys()))

    with col2:
        st.markdown("<p class='section-header'>🏥 Cuidados y Salud</p>", unsafe_allow_html=True)
        vaccinated = st.selectbox("💉 ¿Tiene sus Vacunas?", options=[1, 2, 3],
                                  format_func=lambda x: "Sí, protegido ✨" if x == 1 else "No" if x == 2 else "No se sabe")
        dewormed = st.selectbox("💊 ¿Está Desparasitado?", options=[1, 2, 3],
                                format_func=lambda x: "Sí, sano 🌱" if x == 1 else "No" if x == 2 else "No se sabe")
        sterilized = st.selectbox("✂️ ¿Está Esterilizado?", options=[1, 2, 3],
                                  format_func=lambda x: "Sí, operado ✅" if x == 1 else "No" if x == 2 else "No se sabe")
        health = st.selectbox("❤️ Estado de Salud actual", options=[1, 2, 3],
                              format_func=lambda x: "Súper Sano 💕" if x == 1 else "Lesión Ligera 🩹" if x == 2 else "Lesión Grave 🚑")

    st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)
    boton_predecir = st.form_submit_button("✨ ¡Calcular Tiempo de Adopción con Magia! 🔮")

if boton_predecir:
    breed1_val = diccionario_razas[raza_seleccionada]
    breed2_val = 0
    color1_val = 1
    maturity_size_val = 2
    fur_length_val = 1
    quantity_val = 1
    fee_val = 0
    video_amt_val = 0
    photo_amt_val = 2

    lista_valores = [
        type_pet, age, breed1_val, breed2_val, gender,
        color1_val, maturity_size_val, fur_length_val,
        vaccinated, dewormed, sterilized, health, quantity_val
    ]

    matriz_pura = np.array([lista_valores])

    try:
        if hasattr(model, 'best_estimator_'):
            clase_predicha = model.best_estimator_.predict(matriz_pura)[0]
        else:
            clase_predicha = model.predict(matriz_pura)[0]

        categorias_adopcion = {
            0: "⚡ ¡Adopción Flash! Se irá a casa hoy mismo 💖",
            1: "🚗 ¡Súper Rápido! Conseguirá familia en menos de una semanita 🏠✨",
            2: "🏡 ¡Adopción Rápida! Tarda entre 8 y 30 días en enamorar a alguien 🥰",
            3: "⏳ Adopción Moderada. Tarda de 1 a 3 meses, ¡pero el amor llega! 🌸",
            4: "🧸 Adopción Difícil. Requiere un poquito más de tiempo y paciencia (+100 días) 💕"
        }

        resultado_final = categorias_adopcion.get(clase_predicha, "¡Categoría misteriosa! ✨")

        st.balloons()
        st.snow()

        st.markdown("""
            <p style='font-size: 1rem; font-weight: 700;
                      color: #9B7FD4 !important; margin: 24px 0 8px;'>
                💌 La Respuesta de las Estrellas:
            </p>
        """, unsafe_allow_html=True)
        st.success(f"**{resultado_final}**")

    except Exception as e:
        st.error(f"⚠️ Error al procesar la predicción: {e}")
