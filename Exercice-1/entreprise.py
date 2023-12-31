class Entreprise:
    def __init__(self, nom: str, adresse: str, siret: str) -> None:
        self.nom = nom
        self.adresse = adresse
        self.__siret = self.verify_siret(siret) #si le siret n'est pas conforme, le programme plante pour ne pas créer un objet sans siret
            
    def __str__(self):
        return f"L'entreprise {self.nom}, ayant son siège social au {self.adresse}, possède le numéro de SIRET {self.__siret}"
        
    def verify_siret(self,nouveau_siret: str) -> bool:
        """Vérifier que le numero SIRET est de 14 chiffres. 
           Raise ValueError avec message précis le cas échéant

        Args:
            nouveau_siret (str): le nouveau numéro siret de 14 chiffres

        Raises:
            ValueError: Le numéro SIRET doit être de 14 chiffres

        Returns:
            str: Si valide le nouveau siret est retourné
        """
        if nouveau_siret.isdigit() and (len(nouveau_siret) == 14):
            return nouveau_siret
        else:
            raise ValueError("ERREUR : Le numéro SIRET doit être de 14 chiffres.")
            
    @property
    def siret(self):
        return self.__numero_SIRET
    
    @siret.setter
    def siret(self, nouveau_siret: str):
        try:
            if self.verify_siret(nouveau_siret): # vérifier que le format est valide
                self.__siret = nouveau_siret
        except ValueError as e:
            print(e) # en cas d'erreur un message s'affiche et l'ancien siret est gardé
        
            
    
            