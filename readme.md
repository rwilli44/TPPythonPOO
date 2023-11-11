# TP Python POO - Rachel WILLIAMS 11/06/2023

Merci beaucoup Robin pour ta disponibilité et ton écoute. J'ai pris beaucoup de plaisir à travailler le RPG et à compléter ce TP. Voici quelques précisions sur mon travail.

Pour chaque exercice j'ai créé un fichier **main.py** pour la côté test ou interaction.

## Exercice 1

J'ai ajouté quelques tests supplémentaires pour montrer comment l'erreur est géré au cas où l'utilisateur tente de changer le numéro SIRET pour un numéro qui n'est pas valide. Si l'utilisateur essaie de créer un objet Entreprise avec un mauvais numéro au départ, le programme plante pour éviter de créer un objet sans numéro SIRET. Le dernier test qui vérifie ça est commenté.

## Exercice 2

Rien en particulier à signaler sur le travail. Le TP m'a permis de comprendre quelques différences clés entre Classes et DataClasses comme la manque de getter/setters ou la méthode magique post init.

## Exercice 3

En lisant le doc j'ai vu que .isdigit() peut retourner vrai avec des choses comme l'unicode pour un chiffre ou exposant. Pour cet exercice ce n'est pas grave, mais au cas où dans l'avenir il faut être hyper précis, j'ai voulu tester le regex cette fois pour vérifier le numéro sécu.

Pour la classe CompteBancaire, je me suis amusée à vérifier que la date n'était pas plus tard que le jour même.

Pour les tests, j'ai montré les différents erreurs provoqués par les mauvais dates ou numéros sécu. J'ai également créé un 3e compte pour pouvoir tester la comparision d'égalité entre deux comptes aux soldes différents et deux comptes aux soldes égaux.

## Exercice 4

Après avoir réussi le MVP, je me suis permis de bien m'amuser avec cet exercice. J'ai ajouté des fonctionnalités pour vérifier que les dates ne sont pas seulement au bon format, mais aussi logique. Pour la date limite, j'ai mis aujourd'hui + 1 an en disant que selon le but de la collection, ça pourrait être intéressant d'inclure les films qui sort bientôt mais surtout pour tester comment créer un objet Date pour une date à venir.

J'ai aussi ajouté une fonctionnalité pour éviter d'avoir deux objets Movie avec les mêmes titres et dates.

J'ai testé le tout avec un json vide, un json rempli, et un json inexistant. Du coup, je te laissi ici le JSON rempli et pour créer ces données j'ai donné le format JSON à ChatGPT et l'a demandé de me faire une liste de films avec le même format (pour éviter de perdre mon temps à chercher des années de sorti ou avoir un JSON avec les titres et dates imaginaires).

**_Comme j'ai travaillé avec mon dossier de base 'WILLIAMSRachel-TPPoo' ouvert comme Workspace en VS Code donc pour le chemin du fichier JSON "." fait référence à ce dossier._**

### Merci encore et bon courage pour les corrections !
