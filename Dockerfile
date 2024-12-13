# Étape 1 : Image de construction (builder)
FROM maven:3.9.5-eclipse-temurin-17 AS builder

# Définit le répertoire de travail
WORKDIR /app

# Copie le fichier de configuration Maven (optionnel)
COPY pom.xml .

# Télécharge les dépendances de Maven (caching)
RUN mvn dependency:go-offline

# Copie tout le code source dans le conteneur
COPY src ./src

# Compile le projet et crée le fichier JAR
RUN mvn clean package -DskipTests

# Étape 2 : Image d'exécution (runtime)
FROM eclipse-temurin:17-jdk

# Définit le répertoire de travail
WORKDIR /app

# Copie le fichier JAR depuis l'image builder
COPY --from=builder /app/target/*.jar app.jar

# Commande de lancement de l'application
ENTRYPOINT ["java", "-jar", "app.jar"]
