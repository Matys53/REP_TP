# REP TP2

## Description

Ce projet explore l'impact des facteurs de variabilité dans les calculs d'associativité de l'addition en Java et Python, en utilisant des nombres flottants aléatoires. L'objectif est d'identifier les facteurs influençant la précision des calculs.

## Expériences et analyse

Le projet est divisé en plusieurs étapes :

1. **Tests en Java** : Ce code permet de tester l'associativité de l'addition en Java en vérifiant l'efficacité de l'égalite suivante :

- (x+y) + z = x + (y+z) avec x,y et z des flottants aléatoires.

Le code génère 1 000 000 de tests avec des nombres aléatoires. Ensuite, il effectue le calcul mentionné ci-dessus et teste l'égalité. Le pourcentage de bonnes réponses est indiqué à l'issue de tous les calculs.

### Résultats

Avec des nombres aléatoires entre -1000 et 1000, le résultat obtenu est de **93.1 %** de bonnes réponses.
Si on limite les nombres aléatoires entre 0 et 1000, le résultat est de **74%**.
En utilisant des double au lieu de float, le résultat est de **100%**.

2. **Comparaison inter-groupe** : Afin de comparer notre approche et nos résultats avec ceux des autres groupes, nous avons écrit un script Python 'script.py'. Projet par projet, son objectif est de :

- cloner le repo
- récupérer le résultat contenu dans le fichier 'answer_associativity'
- comparer avec notre propre résultat

Pour vérifier que le langage de programmation n'est pas un facteur déterminant pour expliquer la différence de résultats obtenus, nous avons récupéré le code source d'un autre groupe et nous avons appliqué les mêmes modifications que pour notre code. Nous avons ensuite vérifié que les résultats obtenus étaient similaires. Le code source récupéré est en C contrairement à notre code source Java. Le résultat obtenu pour le code de base est similaire à celui obtenu pour notre code Java (93.07% contre 93.14%). Les résultats obtenus après modification du range des valeurs aléatoires est également similaire (74.54% contre 74.53%) et montre de bien meilleurs résultats pour des valeurs aléatoires positives et négatives que pour des valeurs uniquement positives. Les résultats obtenus après modification du type de données utilisé, en passant de float à double est cependant différent pour Java et C (100% contre 92.68%). Cette modification en C ne traduit pas une augmentation des résultats contrairement à Java.

3. **Analyse de la variabilité** (avec Jinja)

## Guide d'utilisation

### Prérequis

- Docker pour exécuter le projet dans un environnement contrôlé.
- Python 3 et Jupyter Notebook pour l'analyse des résultats et l'exécution des scripts.

### Installation et exécution

1. **Construire l'image Docker :**

```bash
docker build -t answer_associativity .
```

2. **Lancer le conteneur Docker :**

```bash
docker run answer_associativity
```

3. **Exécuter les scripts pour générer les résultats :**

- Génération de fichiers CSV avec cli.py :

```bash
python cli.py
```

- Exécution du modèle Jinja pour tester différents facteurs de variabilité :

```bash
python jinja_call.py
```

4. **Exécution automatique de Github Actions**

## Rapport d'analyse (Jupyter Notebook)

Le dossier contient un fichier Jupyter Notebook pour l'analyse des résultats (expériences, facteurs de variabilité, recommandations).
