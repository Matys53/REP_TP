# 1️⃣ Utiliser une image de base Python
FROM python:3.9-slim

# 2️⃣ Mettre à jour et installer les dépendances système
RUN apt-get update && apt-get install -y \
    python3-pip \
    && pip3 install jupyter

# 3️⃣ Copier les fichiers du projet dans le container
WORKDIR /app
COPY . .

# 5️⃣ Exposer le port de Jupyter Notebook
EXPOSE 8888

# 6️⃣ Lancer Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]