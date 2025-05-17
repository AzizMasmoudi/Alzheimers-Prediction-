# 🧠 Alzheimer Prediction App

Une application MLOps complète pour prédire la probabilité qu'un patient développe la maladie d’Alzheimer à partir de données médicales, comportementales et sociales.

![Streamlit UI](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)

---

## 📊 À propos du projet

Cette application combine :
- ✅ **API Flask** pour la prédiction avec un modèle XGBoost
- ✅ **Interface utilisateur Streamlit** pour l’entrée des données
- ✅ **Pipeline de prétraitement** pour convertir les champs textuels

---


```

---

## 🧠 Modèle ML

- **Type** : XGBoostClassifier
- **Données** : 24 variables issues de `ml.csv`
- **Encodage** : prétraitement manuel dans `utils/preprocess.py`
- **Sortie** : 0 = Pas Alzheimer, 1 = Risque Alzheimer

---


---

## 📚 Ressources utiles

- [Streamlit](https://docs.streamlit.io)
- [Flask](https://flask.palletsprojects.com/)
- [scikit-learn](https://scikit-learn.org/)
- [XGBoost](https://xgboost.readthedocs.io/)

---

## 📬 Contact

Projet réalisé par Aziz Masmoudi  
