from entreprise import Entreprise

def main():
    """ Cette fonction teste la classe Entreprise"""
    
    # Créer un objet Entreprise pour les testes
    test_entreprise = Entreprise("Test et Cie.", "55 Rue du Faubourg Saint-Honoré, 75008 Paris", "12345678901214")
    
    # Print l'objet teste pour vérifier son __str__
    print("\n\n\n  **************** Voici le print de l'objet entreprise **************** \n")
    print(test_entreprise)
    
    # Print le nom de l'entreprise
    print("\n\n\n  **************** Voici le print du nom de l'entreprise **************** \n")
    print(test_entreprise.nom)
    
    # Changer le siret de l'entreprise
    test_entreprise.siret = "14120987654321"

    # Print l'objet pour vérifier que le siret a changé
    print("\n\n\n  **************** Voici le print de l'objet entreprise avec un nouveau siret **************** \n")
    print(test_entreprise)
    
    #### Tests Bonus ####
    # Tester la vérification du siret avec un siret non-conforme
    # Devrait afficher un message d'erreur mais continuer le code
    print("\n\n\n  **************** Voici un print bonus de l'erreur reçu si on utilise un siret non valide - lettre **************** \n")

    test_entreprise.siret = "L4120987654321" # L = pas un chiffre
    
    # Print l'entreprise test pour vérifier que le siret n'a pas changé et le code continue
    print("\n\n\n  **************** Voici le print de l'objet entreprise pour vérifier que le siret n'a pas changé **************** \n")
    print(test_entreprise)
    
    # Tester la vérification du siret par le setter avec un siret non-conforme
    # Devrait afficher un message d'erreur mais continuer le code
    print("\n\n\n  **************** Voici un print bonus de l'erreur reçu si on utilise un siret non valide - 13 chiffres **************** \n")
    test_entreprise.siret = "0130987654321" # pas 14 chiffres
     
    # Print l'entreprise test pour vérifier que le siret n'a pas changé et le code continue
    print("\n\n\n  **************** Voici le print de l'objet entreprise pour vérifier que le siret n'a pas changé **************** \n")
    print(test_entreprise)

    # Essayer d'initialiser une instance avec un mauvais siret, le programme plante pour ne pas créer un objet
    # qui n'est pas valide, mais affiche le message d'erreur en fin du Traceback
    print("\n\n\n  ***************** Une tentative de créer un objet avec un mauvais siret devrait provoquer une erreur **************** \n **************** et terminer le programme avec un message après le TraceBack pour expliquer le problème  **************** \n")

    test_mauvais_siret = Entreprise("Unreal Entreprise ","123 Bad Street","NoGood123")
    
        
main()