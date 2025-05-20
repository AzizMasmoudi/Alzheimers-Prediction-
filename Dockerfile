FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Copier les fichiers nécessaires
COPY ./app/api/app_dynamic.py /app/app/api/
COPY ./app/model/ /app/app/model/
COPY ./requirements.txt /app/

# Créer le fichier __init__.py pour que app.api soit reconnu comme un module
RUN mkdir -p /app/app/api && touch /app/app/__init__.py && touch /app/app/api/__init__.py

# Installer les dépendances
RUN pip3 install -r requirements.txt

# Exposer le port Flask
EXPOSE 5000

# Vérification de santé
HEALTHCHECK CMD curl --fail http://localhost:5000/ || exit 1

# Définir les variables d'environnement
ENV FLASK_APP=app/api/app_dynamic.py
ENV FLASK_ENV=production

# Démarrer l'application
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]