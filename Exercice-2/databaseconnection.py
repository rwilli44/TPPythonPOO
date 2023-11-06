from dataclasses import dataclass
from typing import ClassVar

@dataclass
class DatabaseConnection:
    type_db: str 
    utilisateur: str
    mot_de_passe: str
    hote: str = "localhost"
    nb_instance: ClassVar[int] = 0
    
    def __post_init__(self):
        """Cette fonctionne est appélé après l'initialisation de l'instance. Pour cette classe elle est utiliser pour ajouter la nouvelle connection au comptage de la variable statique nb_instance.        
        """
        DatabaseConnection.nb_instance += 1
    
    @staticmethod
    def nombre_instances():
        """Permet d'afficher le nombre de connections de bases de données instanciées.

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
        

        
    
    
    