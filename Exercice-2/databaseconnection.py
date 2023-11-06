from dataclasses import dataclass
from typing import ClassVar

@dataclass
class DatabaseConnection:
    """Cette classe représente des connexions aux bases de données et compte le nombre de connexions actuelles"""
    type_db: str 
    utilisateur: str
    mot_de_passe: str
    hote: str = "localhost"
    nb_instance: ClassVar[int] = 0
    
    def __post_init__(self):
        # Ajouter chaque nouvelle connexion au compteur des connections actuelles. 
        DatabaseConnection.nb_instance += 1
    
    @staticmethod
    def nombre_instances():
        """Permet d'afficher le nombre de connexions de bases de données instanciées.

        Returns:
            str: Une phrase qui présente le nombre d'instances
        """
        return f"La classe DatabaseConnection possède actuellement {DatabaseConnection.nb_instance} instance(s)."
    
    @classmethod
    def db_factory(cls):
        """Factory pour générer des instances de la Classe Database Connection avec cette configuration :
        type_db = "mariadb", utilisateur = "root", mot_de_passe = "1234", hote = "76.287.872.12"

        Returns:
            DatabaseConnection: instance de la classe DatabaseConnection 
        """
        return DatabaseConnection("mariadb","root","1234","76.287.872.12")
        

        
    
    
    