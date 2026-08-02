# legal

Les pages légales des applications QLAG, publiées via GitHub Pages.

Ce dépôt est **public** parce que Google Play exige une URL de politique de
confidentialité accessible sans compte, et que GitHub Pages ne dessert pas les dépôts
privés sur un plan gratuit. Il ne contient aucun code : uniquement des pages HTML
statiques.

## Adresses

| Application | Page | URL publique |
|---|---|---|
| Quelle est la marque ? | `qelm/index.html` | https://qlag.github.io/legal/qelm/ |

C'est cette URL qu'attend la Play Console, à deux endroits : *Règles › Contenu de
l'application › Règles de confidentialité*, et le champ « Politique de confidentialité »
de la fiche Store.

## Mettre à jour une politique

La source de vérité vit avec l'application concernée — pour QELM, dans
`Quelle est la marque/Android/fiche-play-store/`. On y modifie le Markdown, on
régénère le HTML, et on recopie le résultat ici.

Un commit sur `master` suffit à republier : l'URL ne change jamais. Toute modification
substantielle mérite d'être signalée dans les notes de version de l'application.

## Ajouter une application

Un dossier par application, avec un `index.html` dedans, plus une ligne dans le tableau
ci-dessus et dans la liste de la page d'accueil.
