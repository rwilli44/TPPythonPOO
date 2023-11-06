from client import Client
from comptebancaire import CompteBancaire

def main():
    """Cette fonctionne sert à tester les classes Client et Compte Bancaire.
    """
    
    # Créations de comptes clients avec NIR érronés pour montrer que ça provoque une erreur
    print("Voici les erreurs générées par les mauvais nombres de sécu:\n")
    try:
        client_error2 = Client("Palpatine","Rey","Jakku","1234567890") # manque 5 chiffres
    except ValueError as e:
        print(e)
    try:
        client_error2 = Client("Organa","Leia","Alderaan","12345123456789J") # contient une lettre
    except ValueError as e:
        print(e)
        
    # Création de comptes clients corrects
    client1 = Client("Bobinson","Bob","home addy","123456789012345")
    client2 = Client("Alisson","Alice","home address","123451234567890")
    print("\nDeux objets Clients crées\n")
    
    # Création de comptes client avec dates éronnés pour monter que ça provoque une erreur
    print("\nVoici les erreurs générées par les mauvaises dates de création de compte:\n")

    try:
        compte1 = CompteBancaire("2012/12/12", client1, 10_000.5) # mauvaise séparateur
    except ValueError as e:
        print(e)
    try:
        compte2 = CompteBancaire("2011-30-11", client2, 10_000_000.5) # date et jour renversés
    except ValueError as e:
        print(e)
    try:
        compte2 = CompteBancaire("2025-11-11", client2, 10_000_000.5) # date après aujourd'hui
    except ValueError as e:
        print(e)
        
    # Création de deux objets de la classe CompteBancaires avec données valides
    
    compte1 = CompteBancaire("2012-12-12", client1, 10_000.5)
    compte2 = CompteBancaire("2011-11-11", client2, 10_000_000.5)
    print("\n\nDeux comtes bancaires crées\n")
    
    # print l'identifiant crée pour chaque compte
    print(f"Le compte1 a l'identifiant {compte1.id}\n")
    print(f"Le compte2 a l'identifiant {compte2.id}\n")

    # print pour comparer les soldes, devrait afficher False
    print("\nLes soldes de ces comptes, sont-ils égaux ? \n")
    print(compte1 == compte2)
    
    # print la somme des soldes de tous les comptes
    print(f"\n\nLa solde totale de tous les comptes clients est: {CompteBancaire.somme_soldes_clients()}\n\n")
    
main()
    