# Vibecoding — NOVA Bank

*Dernière mise à jour : 28 octobre 2026*

## Présentation

Ce dépôt contient **NOVA Bank**, un prototype interactif d’application bancaire mobile, présenté dans une coque de téléphone et conçu en français. Il explore un parcours d’accueil personnalisé autour de profils clients, de questions sur des abonnements et de la répartition de points entre des offres partenaires.

Le projet est volontairement léger : l’application est réalisée dans un seul fichier HTML, sans framework, dépendance à installer, serveur applicatif ni service bancaire connecté.

> **Prototype uniquement :** les soldes, transactions, coordonnées, points et confirmations de virement sont des données de démonstration. Aucun compte réel, paiement ou virement bancaire n’est effectué.

## Fonctionnalités présentes

### Parcours de personnalisation

1. **Choix d’un profil** parmi quatre personas : Étudiant économe, Grand voyageur, Abonné fidèle et Pro premium.
2. **Questions de profil** : l’utilisateur indique s’il dispose d’un abonnement Revolut Premium et d’une machine à café Nespresso.
3. **Répartition de 10 points** entre sept offres : Airline Miles, Revolut Pay discounts, Stays, Experiences, Gift Cards, Coffee Explorer et Point Multiplier. Les contrôles empêchent de dépasser le total ou d’allouer un nombre négatif de points.
4. **Motivations** : sélection de raisons prédéfinies et saisie facultative d’un commentaire.
5. **Accueil personnalisé** : affichage du profil, du statut et des offres sélectionnées. Les réponses Revolut et Nespresso déterminent également l’affichage des points, des multiplicateurs et de l’offre café.

### Écrans de démonstration

- **Accueil** : solde et cartes fictifs, raccourcis, quelques transactions récentes et offres personnalisées.
- **Transactions** : liste statique de transactions et boutons de filtre qui permettent de modifier le filtre visuellement.
- **Virement** : contacts prédéfinis, pavé numérique, saisie du montant et écran de confirmation simulé.
- **Profil** : informations fictives, statistiques, options de compte et bouton de déconnexion qui réinitialise le parcours.

La navigation principale donne accès à l’accueil, aux transactions, aux virements et au profil. Des notifications temporaires illustrent certaines actions rapides.

## Démarrer

Aucune installation n’est nécessaire. Ouvrir [`bank-app/index.html`](bank-app/index.html) directement dans un navigateur moderne.

Pour servir le fichier localement, si Python est déjà installé :

```bash
python -m http.server 8000
```

Puis ouvrir <http://localhost:8000/bank-app/>. Depuis la racine du dépôt, cette commande sert le dossier du projet ; il est également possible de lancer le serveur depuis `bank-app/` pour ouvrir l’application sur <http://localhost:8000/>.

## Structure du dépôt

```text
.
├── README.md
└── bank-app/
    └── index.html    # Application complète : HTML, CSS et JavaScript
```

Il n’y a actuellement ni `package.json`, ni configuration de build, ni suite de tests automatisés, ni backend.

## Repères dans le code

Tout le code de l’application se trouve dans [`bank-app/index.html`](bank-app/index.html) :

- **Lignes 1–445 environ — styles CSS** : mise en page de la coque mobile, composants et apparence des écrans.
- **À partir d’environ la ligne 446 — structure HTML** : écrans d’accueil initial, questions, offres, motivations, accueil, transactions, virements et profil.
- **À partir d’environ la ligne 888 — JavaScript** : données de démonstration, état en mémoire et interactions.

Les numéros de ligne sont indicatifs et peuvent changer avec les modifications. Repères JavaScript utiles :

- `OFFERS`, `PERSONAS` et `S` : offres, profils et état courant de l’application.
- `selectPersona`, `pickQ`, `buildOffers`, `addPts` et `goOb3` : parcours de personnalisation et allocation des points.
- `finishOnboarding`, `applyPersonalization` et `buildHomeHighlights` : application des choix à l’interface.
- `navigate` et `resetAll` : navigation entre écrans et remise à zéro.
- `selectContact`, `numIn`, `numDel`, `doTransfer` et `closeSuccess` : simulation de virement.
- `setPill` et `showToast` : filtres visuels et notifications temporaires.

## Limites actuelles

- L’état est conservé uniquement en mémoire JavaScript ; recharger la page le réinitialise.
- Les noms, soldes, cartes, IBAN, transactions, statistiques et points affichés sont fictifs et codés en dur.
- Le virement ne contacte aucune banque, ne débite pas de solde et ne crée pas de transaction ; il affiche seulement une confirmation.
- Les filtres de transactions changent l’apparence du bouton sélectionné, mais ne filtrent pas la liste.
- Plusieurs éléments de l’interface (paramètres, menus, échanges de points et certaines actions rapides) sont illustratifs et ne déclenchent pas de fonctionnalité métier.
- Les offres et leur personnalisation ne sont pas sauvegardées ni transmises à un service externe.
- Le document contient des textes français et des descriptions d’offres en anglais.

## Guide rapide pour un agent IA

Avant toute modification :

1. Lire ce README, puis examiner le fichier [`bank-app/index.html`](bank-app/index.html) concerné par la demande ; toute l’application est regroupée dans ce fichier.
2. Repérer l’écran avec son identifiant `screen-*`, les éléments DOM utilisés et les fonctions JavaScript associées. Les interactions HTML appellent actuellement les fonctions via des attributs `onclick`.
3. Conserver le fonctionnement autonome : pas de framework, de dépendance ou de backend à introduire sans besoin explicite.
4. Préserver la distinction entre **simulation** et **fonction bancaire réelle**. Ne pas présenter les exemples comme des données ou opérations financières réelles.
5. Après un changement d’interface, vérifier le parcours concerné dans un navigateur, notamment les étapes d’accueil, la personnalisation, la navigation et la remise à zéro si elles sont affectées. Il n’existe pas de tests automatisés dans le dépôt.
6. Mettre à jour ce README lorsqu’une modification change les fonctionnalités, les commandes de démarrage, l’architecture ou les limites du prototype.

Pour ajouter une fonctionnalité, vérifier ses dépendances avec l’état `S`, ses règles d’affichage dans `applyPersonalization` et les transitions d’écran via `navigate`. Éviter de supposer qu’une carte, un bouton ou une donnée illustrative est déjà relié à un service.
