import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:5000/predict"

st.set_page_config(page_title="Détection Alzheimer - UI Avancée", layout="wide")

# Sidebar for model selection and instructions
with st.sidebar:
    st.header("🔧 Réglages")
    model_name = st.selectbox("Choisir un modèle :", [
        "svc_model", "logreg_model", "xgb_model", "rf_model"
    ])
    st.markdown("---")
    st.markdown("**Instructions**")
    st.write(
        "1. Sélectionnez un modèle.\n"
        "2. Remplissez les informations du patient.\n"
        "3. Cliquez sur _Prédire_ pour obtenir le résultat."
    )
    if st.button("À propos"):
        st.info("MLOps Alzheimer Prediction App\nVersion: 1.0\nAuteur: Votre Nom")

st.title("🧠 Prédiction de la maladie d'Alzheimer")
st.markdown("### Remplissez les informations du patient")

# Layout in 3 columns for inputs
col1, col2, col3 = st.columns(3)

with col1:
    Country = st.text_input("Pays", value="France")
    Age = st.slider("Âge", 0, 100, 65)
    Gender = st.selectbox("Sexe", ["Male", "Female"])
    Education_Level = st.slider("Niveau d'éducation", 0, 20, 12)
    BMI = st.slider("BMI", 10, 50, 22)

with col2:
    Physical_Activity_Level = st.slider("Activité physique", 0, 10, 5)
    Smoking_Status = st.selectbox("Tabagisme", ["Never", "Former", "Current"])
    Alcohol_Consumption = st.selectbox("Alcool", ["Yes", "No"])
    Diabetes = st.selectbox("Diabète", ["Yes", "No"])
    Hypertension = st.selectbox("Hypertension", ["Yes", "No"])

with col3:
    Cholesterol_Level = st.slider("Cholestérol", 100, 300, 180)
    Family_History = st.selectbox("Antécédents familiaux", ["Yes", "No"])
    Cognitive_Test_Score = st.slider("Score cognitif", 0, 100, 50)
    Depression_Level = st.slider("Niveau dépression", 0, 10, 5)
    Sleep_Quality = st.selectbox("Qualité du sommeil", ["Poor", "Average", "Good"])

# Advanced info in expander
with st.expander("Informations avancées"):
    col4, col5 = st.columns(2)
    with col4:
        Dietary_Habits = st.selectbox("Habitudes alimentaires", ["Unhealthy", "Average", "Healthy"])
        Air_Pollution_Exposure = st.slider("Pollution", 0, 10, 5)
        Employment_Status = st.selectbox("Statut emploi", ["Employed", "Unemployed", "Retired"])
        Marital_Status = st.selectbox("État civil", ["Single", "Married", "Widowed", "Divorced"])
    with col5:
        Genetic_Risk = st.selectbox("Facteur génétique APOE-ε4", ["Yes", "No"])
        Social_Engagement_Level = st.selectbox("Engagement social", ["Low", "Medium", "High"])
        Income_Level = st.selectbox("Niveau de revenu", ["Low", "Medium", "High"])
        Stress_Levels = st.slider("Stress", 0, 10, 5)
        Urban_Rural = st.selectbox("Urbain/Rural", ["Urban", "Rural"])

# Prepare input payload
input_data = {
    "model_name": model_name,
    "Country": Country,
    "Age": Age,
    "Gender": Gender,
    "Education Level": Education_Level,
    "BMI": BMI,
    "Physical Activity Level": Physical_Activity_Level,
    "Smoking Status": Smoking_Status,
    "Alcohol Consumption": Alcohol_Consumption,
    "Diabetes": Diabetes,
    "Hypertension": Hypertension,
    "Cholesterol Level": Cholesterol_Level,
    "Family History of Alzheimer’s": Family_History,
    "Cognitive Test Score": Cognitive_Test_Score,
    "Depression Level": Depression_Level,
    "Sleep Quality": Sleep_Quality,
    "Dietary Habits": Dietary_Habits,
    "Air Pollution Exposure": Air_Pollution_Exposure,
    "Employment Status": Employment_Status,
    "Marital Status": Marital_Status,
    "Genetic Risk Factor (APOE-ε4 allele)": Genetic_Risk,
    "Social Engagement Level": Social_Engagement_Level,
    "Income Level": Income_Level,
    "Stress Levels": Stress_Levels,
    "Urban vs Rural Living": Urban_Rural
}

# Prediction and display
if st.button("🔍 Prédire"):
    with st.spinner("Prédiction en cours..."):
        try:
            response = requests.post("http://localhost:5000/predict", json=input_data)
            result = response.json()
            if "prediction" in result:
                pred = result["prediction"]
                if pred == 1:
                    st.error("⚠️ Risque élevé d'Alzheimer")
                else:
                    st.success("✅ Pas de signes d'Alzheimer")
            else:
                st.warning(f"Erreur API: {result.get('error')}")
        except Exception as e:
            st.error(f"Erreur lors de la requête: {e}")

# Footer
st.markdown("---")
st.markdown("© 2025 Alzheimer Prediction App")
