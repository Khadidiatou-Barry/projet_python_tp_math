# GeoSolve – Projet personnel

## 1. Présentation

GeoSolve est un programme développé en Python dans le cadre du cours d'Outils fondamentaux de mathématiques en première année de BUT Informatique.

Son objectif est de réaliser plusieurs calculs mathématiques et géométriques et d'étudier les limites des calculs numériques avec les nombres flottants.

Une attention particulière est portée au calcul de l'intersection de deux droites et aux erreurs de précision.

## 2. Fonctionnalités

Le programme propose un menu avec les fonctionnalités suivantes :

- Calculer la distance entre deux points.
- Calculer le milieu d'un segment.
- Résoudre une équation du second degré.
- Calculer l'intersection de deux droites.
- Lancer plusieurs expériences numériques.

## 3. Notions mathématiques utilisées

Le projet mobilise plusieurs notions étudiées en cours :

- **Géométrie plane :** distance entre deux points, milieu d'un segment et intersection de droites.
- **Algèbre :** résolution d'une équation du second degré.
- **Systèmes linéaires :** calcul de l'intersection de deux droites à partir de leurs équations.
- **Déterminant :** utilisation du déterminant pour distinguer les droites sécantes des droites parallèles.
- **Nombres flottants :** prise en compte des approximations numériques et de la précision des calculs.

## 4. Étude de la précision numérique

Pour calculer l'intersection de deux droites, le programme utilise un déterminant.

Lorsque ce déterminant est nul, les droites peuvent être parallèles ou confondues.

Cependant, les nombres flottants peuvent produire de petites valeurs qui ne sont pas exactement nulles.

Pour tenir compte de ce problème, le programme utilise une tolérance numérique avec une valeur epsilon de `1e-10`.

Une expérience porte sur deux droites presque parallèles. Le programme peut alors les classer comme parallèles ou presque parallèles, même si elles possèdent mathématiquement une intersection.

Cela montre qu'une tolérance améliore la gestion des approximations, mais qu'elle peut aussi entraîner une classification approximative.

## 5. Organisation des fichiers

- `main.py` : contient le programme et ses différentes fonctionnalités.
- `tests.py` : contient les tests automatiques.

## 6. Installation et lancement

Python doit être installé sur l'ordinateur.

Pour lancer le programme, ouvrir un terminal dans le dossier `geosolve` et exécuter :

```bash
python main.py
```

Pour exécuter les tests :

```bash
python -m unittest -v
```

## 7. Tests réalisés

Le programme possède huit tests automatiques qui vérifient notamment :

- Le calcul d'une distance.
- Le calcul du milieu d'un segment.
- La résolution d'une équation du second degré.
- L'intersection de droites sécantes.
- La détection de droites parallèles et confondues.
- Le fonctionnement de la tolérance numérique.
- Le cas de droites presque parallèles.

## 8. Limites du projet

La tolérance `1e-10` est un choix effectué pour cette expérimentation. Elle n'est pas adaptée à toutes les situations.

Le programme ne distingue donc pas toujours parfaitement deux droites parallèles de deux droites presque parallèles.

La résolution de l'équation du second degré utilise également une méthode classique qui ne traite pas toutes les difficultés possibles liées à la précision numérique.

Ces limites montrent qu'il est important de vérifier les résultats d'un programme de calcul.

## 9. Utilisation de l'intelligence artificielle

Une intelligence artificielle a été utilisée comme aide à l'apprentissage pour obtenir des explications sur certaines notions mathématiques et informatiques, réfléchir à l'organisation du programme et préparer des tests.

Le code a été étudié, exécuté et testé dans le but de comprendre son fonctionnement. Cette aide ne remplace pas la compréhension personnelle du travail.

## 10. Conclusion

GeoSolve m'a permis de mettre en pratique plusieurs notions mathématiques avec Python et de découvrir l'importance de la précision numérique.

Ce projet m'a également permis de travailler sur les fonctions, les conditions, les tests et l'organisation d'un programme.
