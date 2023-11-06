from databaseconnection import DatabaseConnection
def main():
    
    # Initialiser une instance de Databaseconnection sans spécifier l'hôte
    new_connection = DatabaseConnection("PostgreSQL","admin","Password1!")
    
    # Print la nouvelle instance pour vérifier que "hôte a la valeur par défaut 'localhost'"
    print(new_connection)
    
    # Initialiser une instance de Databaseconnection en appelant le factory
    newer_connection = DatabaseConnection.db_factory()
    
    # Print la nouvelle instance pour vérifier l'information attendu (mariadb, root, 1234, et 76.287.872.12)
    print(newer_connection)
    
    # Utiliser la méthode statique pour voir le nombre total d'instances
    print(DatabaseConnection.nombre_instances())
    
main()