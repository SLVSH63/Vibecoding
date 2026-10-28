# Vibecoding — NOVA Bank

*Dernière mise à jour : 28 octobre 2026*

## Présentation

Ce dépôt contient **NOVA Bank**, un prototype interactif d’application bancaire mobile, présenté dans une coque de téléphone et conçu en français. Il explore un parcours d’accueil personnalisé autour de profils clients, de questions sur des abonnements et de la répartition de points entre des offres partenaires.

L’interface et ses interactions sont réalisées dans un fichier HTML autonome. Un petit point d’entrée Python l’intègre dans Streamlit pour permettre son déploiement sur Streamlit Community Cloud. Aucun service bancaire n’est connecté.

> **Prototype uniquement :** les soldes, transactions, coordonnées, points et confirmations de virement sont des données de démonstration. Aucun compte réel, paiement ou virement bancaire n’est effectué.

## Fonctionnalités présentes

### Parcours de personnalisation

1. **Choix d’un profil** parmi quatre personas : Étudiant économe, Grand voyageur, Abonné fidèle et Pro premium.
2. **Questions de profil** : l’utilisateur indique s’il dispose d’un abonnement Revolut Premium et d’une machine à café Nespresso.
3. **Répartition de 10 points** entre sept offres : Airline Miles, Revolut Pay discounts, Stays, Experiences, Gift Cards, Coffee Explorer et Point Multiplier. Les contrôles empêchent de dépasser le total ou d’allouer un nombre négatif de points.
4. **Motivations** : sélection de raisons prédéfinies et saisie facultative d’un commentaire.
5. **Accueil personnalisé** : affichage du profil, du statut et des offres sélectionnées. Les réponses Revolut et Nespresso déterminent également l’affichage des points, des multiplicateurs et de l’offre café.

### Écrans de démonstration

- **Code d’accès** : écran initial demandant un code avant d’afficher le parcours de personnalisation.
- **Accueil** : solde et cartes fictifs, raccourcis, quelques transactions récentes et offres personnalisées.
- **Transactions** : liste statique de transactions et boutons de filtre qui permettent de modifier le filtre visuellement.
- **Virement** : contacts prédéfinis, pavé numérique, saisie du montant et écran de confirmation simulé.
- **Profil** : informations fictives, statistiques, options de compte et bouton de déconnexion qui réinitialise le parcours.

La navigation principale donne accès à l’accueil, aux transactions, aux virements et au profil. Des notifications temporaires illustrent certaines actions rapides.

## Démarrer localement

### Dans un navigateur

Aucune installation n’est nécessaire pour ouvrir [`bank-app/index.html`](bank-app/index.html) directement dans un navigateur moderne.

### Avec Streamlit

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Streamlit affiche l’application à l’adresse indiquée dans le terminal, généralement <http://localhost:8501/>.

## Déployer sur Streamlit Community Cloud

1. Pousser ce dépôt GitHub avec `app.py`, `requirements.txt` et `bank-app/index.html`.
2. Dans [Streamlit Community Cloud](https://share.streamlit.io/), créer une application et sélectionner ce dépôt ainsi que la branche à déployer.
3. Définir `app.py` comme fichier principal, puis lancer le déploiement.

Streamlit lit le fichier HTML depuis le dépôt et l’affiche dans un composant intégré. Toute modification de l’interface doit donc rester dans `bank-app/index.html`, à côté du point d’entrée `app.py`.

## Structure du dépôt

```text
.
├── README.md
├── app.py            # Point d’entrée Streamlit Cloud
├── requirements.txt  # Dépendance Python pour Streamlit
└── bank-app/
    └── index.html    # Application complète : HTML, CSS et JavaScript
```

Il n’y a actuellement ni `package.json`, ni configuration de build front-end, ni suite de tests automatisés, ni backend.

## Repères dans le code

Le rendu Streamlit est géré par [`app.py`](app.py), qui charge [`bank-app/index.html`](bank-app/index.html) dans un composant HTML. Le code de l’interface elle-même se trouve dans ce fichier HTML :

- **Lignes 1–422 environ — styles CSS** : mise en page de la coque mobile, composants et apparence des écrans.
- **À partir d’environ la ligne 423 — structure HTML** : code d’accès, parcours d’accueil, questions, offres, motivations, accueil, transactions, virements et profil.
- **À partir d’environ la ligne 892 — JavaScript** : données de démonstration, état en mémoire et interactions.

Les numéros de ligne sont indicatifs et peuvent changer avec les modifications. Repères JavaScript utiles :

- `OFFERS`, `PERSONAS` et `S` : offres, profils et état courant de l’application.
- `selectPersona`, `pickQ`, `buildOffers`, `addPts` et `goOb3` : parcours de personnalisation et allocation des points.
- `finishOnboarding`, `applyPersonalization` et `buildHomeHighlights` : application des choix à l’interface.
- `navigate` et `resetAll` : navigation entre écrans et remise à zéro.
- `selectContact`, `numIn`, `numDel`, `doTransfer` et `closeSuccess` : simulation de virement.
- `setPill` et `showToast` : filtres visuels et notifications temporaires.

## Limites actuelles

- L’état est conservé uniquement en mémoire JavaScript ; recharger la page le réinitialise.
- Le code d’accès est vérifié côté navigateur et figure dans le code source. Cet écran est uniquement un verrou de démonstration : il ne protège pas réellement l’application ni ses données.
- Les noms, soldes, cartes, IBAN, transactions, statistiques et points affichés sont fictifs et codés en dur.
- Le virement ne contacte aucune banque, ne débite pas de solde et ne crée pas de transaction ; il affiche seulement une confirmation.
- Les filtres de transactions changent l’apparence du bouton sélectionné, mais ne filtrent pas la liste.
- Plusieurs éléments de l’interface (paramètres, menus, échanges de points et certaines actions rapides) sont illustratifs et ne déclenchent pas de fonctionnalité métier.
- Les offres et leur personnalisation ne sont pas sauvegardées ni transmises à un service externe.
- Le document contient des textes français et des descriptions d’offres en anglais.

## Guide rapide pour un agent IA

Avant toute modification :

1. Lire ce README, puis examiner le fichier [`bank-app/index.html`](bank-app/index.html) concerné par la demande ; toute l’application est regroupée dans ce fichier.
2. Pour une modification du chargement ou de l’intégration Streamlit, examiner [`app.py`](app.py) et conserver le chemin du fichier HTML ainsi que l’encodage UTF-8.
3. Repérer l’écran avec son identifiant `screen-*`, les éléments DOM utilisés et les fonctions JavaScript associées. Les interactions HTML appellent actuellement les fonctions via des attributs `onclick`.
4. Conserver l’architecture légère : HTML/CSS/JavaScript pour l’interface et Streamlit comme conteneur de déploiement. Ajouter des dépendances uniquement si nécessaire, et mettre à jour `requirements.txt`.
5. Préserver la distinction entre **simulation** et **fonction bancaire réelle**. Ne pas présenter les exemples comme des données ou opérations financières réelles.
6. Après un changement, lancer l’application avec `python -m streamlit run app.py` et vérifier le parcours concerné dans un navigateur, notamment les étapes d’accueil, la personnalisation, la navigation et la remise à zéro si elles sont affectées. Il n’existe pas de tests automatisés dans le dépôt.
7. Mettre à jour ce README lorsqu’une modification change les fonctionnalités, les commandes de démarrage, l’architecture ou les limites du prototype.

Pour ajouter une fonctionnalité, vérifier ses dépendances avec l’état `S`, ses règles d’affichage dans `applyPersonalization` et les transitions d’écran via `navigate`. Éviter de supposer qu’une carte, un bouton ou une donnée illustrative est déjà relié à un service.
