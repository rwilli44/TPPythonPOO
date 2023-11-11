from databaseconnection import DatabaseConnection

def main():
    """Fonction pour tester la classe DatabaseConnection"""
    
    # Initialiser une instance de Databaseconnection sans spécifier l'hôte
    test_connection = DatabaseConnection("PostgreSQL","admin","Password1!")
    
    # Print la nouvelle instance pour vérifier que "hôte a la valeur par défaut 'localhost'"
    print("\n\n********** Résultat attendu : affiche un objet DatabaseConnection avec hote='localhost' **********\n")
    print(test_connection)
    
    # Initialiser une instance de Databaseconnection en appelant le factory
    test_connection2 = DatabaseConnection.db_factory()
    
    # Print la nouvelle instance pour vérifier l'information attendu (mariadb, root, 1234, et 76.287.872.12)
    print("\n\n\n********** Résultat attendu : affiche un objet DatabaseConnection avec 'mariadb','root','1234', '76.287.872.12' **********\n")
    print(test_connection2)
    
    # Utiliser la méthode statique pour voir le nombre total d'instances
    print("\n\n\n********** Résultat attendu : une phrase qui indique 2 connexions actuelles **********\n")
    print(DatabaseConnection.nombre_instances())
    
main()