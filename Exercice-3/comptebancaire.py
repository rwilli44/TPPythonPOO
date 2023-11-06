from client import Client
import random
from datetime import datetime, date 

class CompteBancaire: 
    __somme_tous_soldes = 0  # Total de tous les soldes des comptes clients
    
    def __init__(self, date_creation: str, client: Client, solde: float) -> None:
        self.date_creation = self.verifier_date(date_creation) # vérifier le format et validité de la date
        self.client = client
        self.solde = solde
        self.id = self.generer_ID(self.date_creation) # créer un identifiant unique
        CompteBancaire.__somme_tous_soldes += self.solde # augmenter la propriété statique de la somme de tous les comptes
        
    def verifier_date(self, date_creation: str) -> date:
        """Vérifier que la date est dans le format YYYY-MM-DD et que la date n'est pas plus tard qu'aujorud'hui.
        Retourne un objet de type date avec la date de création ou relève une Erreur si la date donnée n'est pas valide.
        Args:
            date_creation (str): date de création de compte en format YYYY-MM-DD
            
        Raises:
            ValueError: La date de création de compte ne peut pas être ultérieur à aujourd'hui.
            
        Returns:
            date: date objet de la date de création
        """
        format_date = "%Y-%m-%d"    
        date_creation_objet = datetime.strptime(date_creation,format_date).date() # Provoque une erreur si le format est erroné
        aujourdhui = date.today()
        if date_creation_objet > aujourdhui: # Vérifie que la date de création n'est pas ultérieur à aujourd'hui
            raise ValueError("La date de création de compte ne peut pas être ultérieur à aujourd'hui.")
        return date_creation_objet
        
    def generer_ID(self, date_creation: date) -> str:
        """Générer un identifiant client avec 4 lettres majuscules aléatoires suivi par l'année, le mois et la jour de la création de compte.

        Args:
            date_creation (date): un objet date de la date de création de compte

        Returns:
            str: un string de 12 characters - 4 lettres majuscules aléatoires + YYYYMMDD (date de création de compte)
        """
        id = ""
        for i in range(0,4):
            # ajoute 4 lettres majuscules aléatoires à id
            id += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") 
        id += f"{date_creation.strftime('%d')}{date_creation.strftime('%m')}{date_creation.strftime('%Y')}" # ajoute la date au bon format
        return id
    
    def __eq__(self, other: object) -> bool:
        # deux comptes sont considérés égaux si leur soldes sont égaux
        return self.solde == other.solde
    
    @classmethod
    def somme_soldes_clients(cls):
        """Affiche la somme de tous les soldes clients. 

        Returns:
            float: l'attribut de classe 'privé' __somme_tous_soldes
        """
        return CompteBancaire.__somme_tous_soldes
    