# Politique de confidentialité — « Quelle est la question ? »

**Dernière mise à jour : 24 août 2026**
**Éditeur : Quentin Lagarde — qlag.ae@gmail.com**

Cette politique décrit ce que l'application « Quelle est la question ? » fait — et ne fait
pas — des données de ses utilisateurs.

---

## En résumé

L'application ne demande aucun compte, aucune inscription et aucune autorisation système.
Le jeu lui-même se joue hors ligne : les questions sont embarquées dans l'application, et
votre progression ne quitte jamais votre téléphone.

Trois services de Google sont en revanche utilisés, et eux communiquent avec l'extérieur :
**AdMob** pour les publicités qui financent le jeu, **Firebase Analytics** pour comprendre
comment le jeu est utilisé, et **Firebase Crashlytics** pour être averti des plantages.

Si vous vous trouvez dans l'Espace économique européen, au Royaume-Uni ou en Suisse, un
écran de consentement vous est présenté au premier lancement, et **votre choix détermine ce
qui est transmis**. Vous pouvez y revenir à tout moment depuis *Réglages ›
Confidentialité des annonces*.

---

## 1. Données que l'application enregistre sur votre appareil

Les informations suivantes restent **uniquement sur votre téléphone**, dans l'espace de
stockage privé de l'application. Elles ne sont transmises à personne, ne sont pas
sauvegardées sur un serveur, et disparaissent définitivement à la désinstallation :

- votre progression (questions trouvées, packs débloqués) ;
- votre nombre de pièces, les réponses révélées et les indices déjà achetés sur chaque
  question ;
- vos réglages (musique, effets sonores, vibrations) ;
- le fait que vous ayez acheté ou non la suppression des publicités ;
- votre choix de consentement publicitaire.

Aucun identifiant de compte n'y est associé : ces données ne permettent pas de vous
identifier.

## 2. Votre consentement

Au premier lancement, si vous êtes situé dans une zone où la réglementation l'exige
(Espace économique européen, Royaume-Uni, Suisse), l'application affiche un écran de
consentement fourni par la plateforme de gestion du consentement de Google. Il est présenté
**avant** que le moindre service publicitaire ou de mesure ne soit démarré.

Votre choix est conservé sur l'appareil et respecté par les trois services décrits
ci-dessous. Vous pouvez le modifier à tout moment, sans réinstaller le jeu, depuis
**Réglages › Confidentialité des annonces**.

Si vous refusez, le jeu reste **intégralement jouable** : aucune fonction, aucun niveau et
aucun indice n'est réservé à ceux qui acceptent. Les publicités continuent d'être
affichées, mais en mode non personnalisé.

## 3. Publicité — Google AdMob

L'application affiche des publicités fournies par **Google AdMob** (Google Ireland
Limited). Deux formats sont utilisés : des interstitiels périodiques, et des vidéos
récompensées que vous choisissez vous-même de lancer pour payer une révélation ou un
indice à la place de vos pièces.

Pour afficher une annonce, le SDK AdMob transmet à Google des informations techniques
qui échappent au contrôle de l'application, notamment :

- l'identifiant publicitaire de l'appareil et des identifiants techniques associés ;
- le modèle d'appareil, la version d'Android, la langue et le pays approximatif
  (déduit de l'adresse IP) ;
- des événements liés aux annonces (affichage, clic, vidéo terminée).

**Le caractère personnalisé ou non des annonces dépend de votre consentement.** Si vous
l'accordez, Google peut utiliser vos centres d'intérêt pour choisir l'annonce. Si vous le
refusez, ou si vous n'avez pas été sollicité parce que votre pays ne l'impose pas, les
annonces sont demandées en mode **non personnalisé** : elles sont alors sélectionnées à
partir du contexte et du pays seulement. Dans les deux cas, Google peut utiliser ces
informations pour des finalités de mesure, de facturation et de lutte contre la fraude, qui
lui sont propres.

- Règles de confidentialité de Google : https://policies.google.com/privacy
- Fonctionnement des données dans les services publicitaires Google :
  https://policies.google.com/technologies/partner-sites

Vous pouvez à tout moment réinitialiser ou supprimer votre identifiant publicitaire
depuis **Paramètres › Google › Annonces** sur votre téléphone Android.

## 4. Mesure d'usage — Firebase Analytics

L'application utilise **Firebase Analytics** (Google Ireland Limited) pour comprendre
comment le jeu est utilisé, et rien d'autre. Concrètement, cela sert à savoir quelles
questions sont trop difficiles et si le prix des indices est juste — c'est ce qui permet de
corriger l'équilibre du jeu sans avoir à le deviner.

Sept événements sont enregistrés, et il n'y en a pas d'autres :

- l'ouverture d'une question et le fait qu'elle ait été trouvée, avec le pack, le numéro et
  le thème ;
- l'achèvement d'un pack ;
- une réponse révélée, avec son rang et son prix ;
- un indice acheté, lequel et à quel prix ;
- si l'un ou l'autre a été payé en pièces ou par une vidéo ;
- l'ouverture de la boutique ;
- une vidéo récompensée, et si elle a été regardée jusqu'au bout.

À ces événements, le SDK associe des informations techniques : un identifiant d'instance
d'application, propre à cette installation et non à vous, le modèle d'appareil, la version
d'Android, la langue et le pays.

**Ce qui n'est jamais enregistré** : aucun texte que vous saisissez, aucun contenu de
formulation proposée, aucun identifiant de compte, aucune adresse, aucune position
géographique précise.

## 5. Rapports de plantage — Firebase Crashlytics

Si l'application se ferme brutalement, **Firebase Crashlytics** (Google Ireland Limited) en
transmet un rapport : la trace d'exécution au moment du plantage, le modèle d'appareil, la
version d'Android et de l'application, l'état de la mémoire, et le numéro de la question en
cours — ce dernier pour pouvoir reproduire le problème sans avoir à vous le demander.

Un identifiant d'installation anonyme accompagne le rapport, afin de ne pas compter dix
fois le même plantage survenu dix fois sur le même appareil. Il ne permet pas de vous
identifier et disparaît à la désinstallation.

Aucun rapport n'est envoyé si l'application ne plante pas.

## 6. Achats intégrés — Google Play

L'application propose des achats : la suppression des publicités, et des recharges de
pièces. Ces paiements sont traités **entièrement par Google Play**.

L'application ne voit, ne reçoit et n'enregistre **aucune donnée de paiement** — ni
numéro de carte, ni adresse, ni identité. Elle reçoit uniquement de Google la
confirmation qu'un achat a abouti, afin de créditer ce qui a été acheté. La gestion de
ces transactions relève des conditions d'utilisation de Google Play.

## 7. Ce que l'application ne fait pas

- Aucun compte, aucune inscription, aucune adresse e-mail demandée.
- Aucun accès à vos contacts, votre position GPS, votre appareil photo, votre
  microphone, vos photos ou vos fichiers.
- Aucun traceur tiers en dehors des trois services de Google décrits ci-dessus.
- Aucune notification, aucun envoi de courrier électronique.
- Aucune revente ni partage de données à des tiers.
- Aucune donnée de jeu envoyée à l'éditeur : les statistiques sont agrégées par Google, et
  l'éditeur ne consulte que des totaux, jamais le parcours d'une personne.

## 8. Enfants

L'application n'est pas destinée aux enfants de moins de 13 ans et ne leur est pas
adressée. Aucune donnée n'est sciemment collectée auprès d'eux, et le formulaire de
consentement comporte une déclaration d'âge lorsque la réglementation l'exige.

## 9. Vos droits (RGPD)

Les données conservées par l'application sur votre appareil le sont localement, sans
identifiant personnel. Vous pouvez les effacer intégralement en désinstallant
l'application, ou en vidant ses données depuis **Paramètres › Applications › Quelle est
la question ? › Stockage**.

Les données transmises à Google — publicité, mesure d'usage, rapports de plantage,
paiement — sont traitées par Google en tant que responsable de traitement. Les demandes
d'accès, de rectification, d'effacement ou d'opposition doivent lui être adressées, selon
les modalités décrites dans ses règles de confidentialité.

Le retrait de votre consentement se fait directement dans le jeu, depuis **Réglages ›
Confidentialité des annonces**, et prend effet immédiatement sur les annonces suivantes.

Pour toute question sur cette politique, vous pouvez écrire à
**qlag.ae@gmail.com**.

## 10. Contenu du jeu et sources

Les questions du jeu portent sur des connaissances générales : listes, classements et
faits établis. Chaque question est rédigée à partir de sources publiques, dont
l'adresse et la date de relevé sont conservées avec le contenu.

Les noms propres cités — œuvres, marques, personnes publiques, institutions — le sont à
titre culturel et ludique, dans le cadre d'un jeu de connaissances, sans lien
commercial, partenariat ni approbation de leur part.

## 11. Modifications

Cette politique peut évoluer si l'application change. La date en tête de document
indique la dernière révision. Une modification substantielle sera signalée dans les
notes de version sur Google Play.
