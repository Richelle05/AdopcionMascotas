import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Configuración de la página
st.set_page_config(page_title="PetFinder Cute Predictor 🐾", page_icon="💖", layout="wide")

# --- 🎀 INYECCIÓN DE ESTILO CUSTOM CSS (AESTHETIC / PASTEL) 🎀 ---
st.markdown("""
    <style>
    .stApp {
        background-color: #FFF0F5; 
    }
    h1, h2, h3, h4, h5, h6, p, label, span {
        color: #5D4037 !important; 
        font-family: 'Comic Sans MS', 'Arial', sans-serif;
    }
    .titulo-magico {
        text-align: center;
        color: #FF6B8B !important;
        font-size: 3rem !important;
        font-weight: bold;
        text-shadow: 3px 3px 0px #FFFFFF;
        margin-top: -20px;
    }
    [data-testid="stForm"] {
        background-color: #FFFFFF !important;
        border: 4px dashed #FFB7B2 !important; 
        border-radius: 25px !important;
        padding: 30px !important;
        box-shadow: 0px 8px 20px rgba(255, 183, 178, 0.5) !important;
    }
    [data-testid="stSidebar"] {
        background-color: #FFE5EC !important;
        border-right: 3px solid #FFC2D1;
    }
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
        width: 100%;
    }
    div.stButton > button:hover {
        transform: scale(1.05) rotate(1deg);
        background: linear-gradient(135deg, #FF5C8A 0%, #FF85A2 100%) !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 🗂️ BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>🌸 Menú Mágico 🌸</h2>", unsafe_allow_html=True)
    st.markdown("<center><h1 style='font-size: 5rem; margin: 0;'>🐈‍⬛</h1></center>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### 📝 Datos del Alumno")
    st.write("💝 **Estudiante:** Richelle Rodriguez Jurado")
    st.write("🆔 **Código ISIL:** 6816")
    st.markdown("---")
    st.markdown("### 🔗 Entregables")
    st.markdown("[🍓 Ver Google Colab](https://colab.research.google.com/drive/18xubbLLMhc8WTvMQvtOf5dkPirWD0o3t?usp=sharing)", unsafe_allow_html=True)

# --- ✨ CUERPO PRINCIPAL APP ✨ ---
st.markdown("<h1 class='titulo-magico'>✨ PetFinder Cute Predictor ✨</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2rem; font-weight: bold;'>¡Calculamos el tiempo de adopción con estrellas y arcoíris! 🌈🧸</p>", unsafe_allow_html=True)
st.markdown("<center><h1 style='font-size: 4rem; margin: 0;'>🐶✨🐱</h1></center>", unsafe_allow_html=True)

# --- 🧠 CARGA DEL MODELO ---
ruta_modelo = 'modelos/modelo_random_forest.pkl'
if os.path.exists(ruta_modelo):
    model = joblib.load(ruta_modelo)
else:
    st.error("❌ ¡Oh no, linda! No encontré tu modelo en 'modelos/modelo_random_forest.pkl'.")
    st.stop()

# --- 📜 DICCIONARIO DE RAZAS MÁGICAS ---
# Mapeamos los nombres reales con los códigos numéricos que pide el modelo
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

# --- 🎈 FORMULARIO PRINCIPAL RENOVADO 🎈 ---
st.markdown("### 💌 Rellena los datos mágicos de la mascota:")

with st.form("formulario_lindo"):
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🪵 Características Básicas")
        type_pet = st.selectbox("🌸 Tipo de Animalito", options=[1, 2], format_func=lambda x: "Perrito 🐶" if x == 1 else "Gatito 🐱")
        age = st.number_input("🍼 Edad (en meses)", min_value=0, max_value=250, value=3, step=1)
        gender = st.selectbox("🎀 Género", options=[1, 2, 3], format_func=lambda x: "Macho ♂️" if x == 1 else "Hembra ♀️" if x == 2 else "Grupo / Mixto 📦")
        
        # Selección de Raza Bonita sin usar códigos numéricos directos
        raza_seleccionada = st.selectbox("🧬 Selección de Raza", options=list(diccionario_razas.keys()))
        
    with col2:
        st.markdown("#### 🏥 Cuidados y Salud")
        vaccinated = st.selectbox("💉 ¿Tiene sus Vacunas?", options=[1, 2, 3], format_func=lambda x: "Sí, protegido ✨" if x == 1 else "No" if x == 2 else "No se sabe")
        dewormed = st.selectbox("💊 ¿Está Desparasitado?", options=[1, 2, 3], format_func=lambda x: "Sí, sano 🌱" if x == 1 else "No" if x == 2 else "No se sabe")
        sterilized = st.selectbox("✂️ ¿Está Esterilizado?", options=[1, 2, 3], format_func=lambda x: "Sí, operado ✅" if x == 1 else "No" if x == 2 else "No se sabe")
        health = st.selectbox("❤️ Estado de Salud actual", options=[1, 2, 3], format_func=lambda x: "Súper Sano 💕" if x == 1 else "Lesión Ligera 🩹" if x == 2 else "Lesión Grave 🚑")

    st.markdown("<br>", unsafe_allow_html=True)
    boton_predecir = st.form_submit_button("✨ ¡Calcular Tiempo de Adopción con Magia! 🔮")



if boton_predecir:
    # 1. Obtener el código de la raza elegida
    breed1_val = diccionario_razas[raza_seleccionada]
    
    # 2. Definir los valores fijos para las variables ocultas
    breed2_val = 0         
    color1_val = 1         
    maturity_size_val = 2  
    fur_length_val = 1     
    quantity_val = 1       
    fee_val = 0            
    video_amt_val = 0      
    photo_amt_val = 2      
    
    # 3. Crear una lista pura con los 16 valores en el orden exacto del dataset
    # Al usar .predict() directamente sobre una lista de Python (dentro de una matriz de numpy), 
    # removemos por completo el uso de DataFrames y evitamos que scikit-learn valide letras.
    lista_valores = [
        type_pet, age, breed1_val, breed2_val, gender, color1_val,
        maturity_size_val, fur_length_val, vaccinated, dewormed,
        sterilized, health, quantity_val, fee_val, video_amt_val, photo_amt_val
    ]
    
    # Convertimos a una matriz de numpy de dos dimensiones (1 fila, 16 columnas)
    matriz_pura = np.array([lista_valores])
    
    try:
        # Extraemos el estimador interno de la búsqueda bayesiana para saltarnos la regla estricta de nombres
        # Si el objeto guardado es un BayesSearchCV, usamos .best_estimator_.predict()
        if hasattr(model, 'best_estimator_'):
            clase_predicha = model.best_estimator_.predict(matriz_pura)[0]
        else:
            # Si guardaste el RandomForestClassifier directo, usamos la propiedad subyacente para evadir feature_names
            if hasattr(model, 'estimators_'):
                # Forzamos la predicción pura sobre el modelo base
                clase_predicha = model.predict(matriz_pura)[0]
            else:
                clase_predicha = model.predict(matriz_pura)[0]
        
        # Mapeo de respuestas tiernas
        categorias_adopcion = {
            0: "⚡ ¡Adopción Flash! Se irá a casa hoy mismo 💖",
            1: "🚗 ¡Súper Rápido! Conseguirá familia en menos de una semanita 🏠✨",
            2: "🏡 ¡Adopción Rápida! Tarda entre 8 y 30 días en enamorar a alguien 🥰",
            3: "⏳ Adopción Moderada. Tarda de 1 a 3 meses, ¡pero el amor llega! 🌸",
            4: "🧸 Adopción Difícil. Requiere un poquito más de tiempo y paciencia (+100 días) 💕"
        }
        
        resultado_final = categorias_adopcion.get(clase_predicha, "¡Categoría misteriosa! ✨")
        
        # ¡Animaciones!
        st.balloons()
        st.snow()
        
        st.markdown("### 💌 La Respuesta de las Estrellas:")
        st.success(f"**{resultado_final}**")
        
    except Exception as e:
        st.error(f"⚠️ Error al procesar la predicción: {e}")
        st.info("Por favor, asegúrate de hacer un 'Reboot App' en el panel de Streamlit para aplicar los cambios.")
