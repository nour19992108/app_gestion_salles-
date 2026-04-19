class Salle:

    def _init_(self, code, description, categorie, capacite):
        self.code = code
        self.description = description
        self.categorie = categorie
        self.capacite = capacite

    def afficher_infos(self):
        print(f"Code : {self.code}")
        print(f"Description : {self.description}")
        print(f"Categorie : {self.categorie}")
        print(f"Capacite : {self.capacite}")