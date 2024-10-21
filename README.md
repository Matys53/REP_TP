# REP TP2

## Code Java

Ce code permet de tester l'associativité de l'addition en Java en vérifiant l'efficacité de l'égalite suivante :

- (x+y) + z = x + (y+z) avec x,y et z des flottants aléatoires.

Le code génère 1 000 000 de tests avec des nombres aléatoires. Ensuite, il effectue le calcul mentionné ci-dessus et teste l'égalité. Le pourcentage de bonnes réponses est indiqué à l'issue de tous les calculs.

### Résultats

Avec des nombres aléatoires entre -1000 et 1000, le résultat obtenu est de **93.1 %** de bonnes réponses.
Si on limite les nombres aléatoires entre 0 et 1000, le résultat est de **74%**.
En utilisant des double au lieu de float, le résultat est de **100%**.

test github action

## Aligning

Afin de comparer notre approche et nos résultats avec ceux des autres groupes, nous avons écrit un script Python 'script.py'. Projet par projet, son objectif est de :

- cloner le repo
- récupérer le résultat contenu dans le fichier 'answer_associativity'
- comparer avec notre propre résultat
