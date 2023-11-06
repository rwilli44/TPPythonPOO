from entreprise import Entreprise

def main():
    
    # Créer un objet Entreprise pour les testes
    test_entreprise = Entreprise("Test et Cie.", "55 Rue du Faubourg Saint-Honoré, 75008 Paris", "12345678901214")
    
    # Print l'objet teste pour vérifier son __str__
    print("\n\n\n  **************** Voici le print de l'objet entreprise **************** \n")
    print(test_entreprise)
    
    # Print le nom de l'entreprise teste
    print("\n\n\n  **************** Voici le print du nom de l'entreprise **************** \n")
    print(test_entreprise.nom)
    
    # Changer le siret via un setter et envoyer un int pour montrer que la Classe a prévu de le changer en string
    # en cas de besoin
    test_entreprise.siret = 14120987654321

    # Print l'objet pour vérifier que le siret a changé
    print("\n\n\n  **************** Voici le print de l'objet entreprise avec un nouveau siret **************** \n")
    print(test_entreprise)
    
    #### Tests Bonus ####
    # Tester la vérification du siret par le setter avec un siret non-conforme
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

    # Essayer d'initialiser une instance avec un mauvais siret, l'instance sera créer mais sans siret
    # Je n'ai pas trouvé de moyen de ne pas créer l'objet de tout 
    print("\n\n\n  ***************** Une tentative de créer un objet avec un mauvais siret devrait provoquer une erreur **************** \n **************** et terminer le programme avec un message après le TraceBack pour expliquer le problème  **************** \n")

    bad_entreprise = Entreprise("Unreal Entreprise ","123 Bad Street","NoGood123")
    
    print("\n\n\n  **************** Voici le print de l'objet sans siret qui devrait provoquer une **************** \n **************** erreur et terminer le programme car il n'a pas de siret **************** \n")

    print(bad_entreprise)
    
    
        
main()