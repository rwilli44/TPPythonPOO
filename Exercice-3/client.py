import re

class Client:
    """Cette classe représente des clients d'une banque"""
    
    def __init__(self, nom: str, prenom: str, adresse: str, numero_secu: str) -> None:
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.numero_secu = self.verifier_secu(numero_secu) # doit être 15 chiffres
        
    def verifier_secu(self, numero_secu: str) -> str:
        """Vérifier que le numéro de sécu est 15 chiffres [0-9]. 
        Si le numéro est valide, il est retourné. Relève une erreur le cas échéant. 

        Args:
            numero_secu (str): numéro de sécurité sociale

        Raises:
            ValueError: Le numéro de sécurité sociale doit être composé de 15 chiffres.

        Returns:
            str: le numéro de sécurité social validé
        """
        if re.match("^[0-9]{15}$", numero_secu): 
            return numero_secu
        else:
            raise ValueError("Le numéro de sécurité sociale doit être composé de 15 chiffres.")