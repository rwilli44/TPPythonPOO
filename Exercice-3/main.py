from client import Client
from comptebancaire import CompteBancaire

def main():
    """Fonction pour tester les classes Client et Compte Bancaire.
    """
    
    # Créations de comptes clients avec NIR érronés pour montrer que ça provoque une erreur
    print("Voici les erreurs générées par les mauvais nombres de sécu:\n")
    try:
        client_error1 = Client("Palpatine","Rey","Jakku","1234567890") # manque 5 chiffres
    except ValueError as e:
        print(e)
    try:
        client_error2 = Client("Organa","Leia","Alderaan","12345123456789J") # contient une lettre
    except ValueError as e:
        print(e)
        
    # Création de comptes clients corrects
    test_client1 = Client("Bobinson","Bob","home addy","123456789012345")
    test_client2 = Client("Alisson","Alice","home address","123451234567890")
    print("\nDeux objets Clients crées\n")
    
    # Création de comptes client avec dates éronnés pour monter que ça provoque une erreur
    print("\nVoici les erreurs générées par les mauvaises dates de création de compte:\n")

    try:
        compte_error1 = CompteBancaire("2012/12/12", test_client1, 10_000.5) # mauvaise séparateur
    except ValueError as e:
        print(e)
    try:
        compte_error2 = CompteBancaire("2011-30-11", test_client2, 10_000_000.5) # date et jour renversés
    except ValueError as e:
        print(e)
    try:
        compte_error3 = CompteBancaire("2025-11-11", test_client2, 10_000_000.5) # date après aujourd'hui
    except ValueError as e:
        print(e)
        
    # Création de deux objets de la classe CompteBancaires avec données valides
    test_compte1 = CompteBancaire("2012-12-12", test_client1, 10_000.5)
    test_compte2 = CompteBancaire("2011-11-11", test_client2, 10_000_000.5)
    print("\n\nDeux comptes bancaires crées\n")
    
    # print l'identifiant crée pour chaque compte
    print(f"Le compte 'test_compte1' a l'identifiant {test_compte1.id}\n")
    print(f"Le compte 'test_compte2' a l'identifiant {test_compte2.id}\n")

    # print pour comparer les soldes, devrait afficher False
    print("\nLes soldes de ces comptes, sont-ils égaux ? Réponse attendu: False\n")
    print(test_compte1 == test_compte2)
    
    # créer une 3e compte avec une solde égal à test_compte1 pour vérifier qu'ils affichent égaux
    test_compte3 = CompteBancaire("2002-12-12", test_client2, 10_000.5)
    print("\nLes comptes 1 et 3, sont-ils égaux ? Réponse attendu: True \n")
    print(test_compte1 == test_compte3)
    
    
    # print la somme des soldes de tous les comptes (10_020_001.5)
    print(f"\n\nLa solde totale de tous les comptes clients est: {CompteBancaire.somme_soldes_clients()}\n\n")
    
main()
    