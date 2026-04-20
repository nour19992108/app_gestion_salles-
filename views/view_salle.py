class ViewSalle:
    def afficher_menu(self):
        print("\n--- Gestion des salles ---")
        print("1. Ajouter une salle")
        print("2. Afficher les salles")
        print("3. Modifier une salle")
        print("4. Supprimer une salle")
        print("5. Quitter")

    def saisir_salle(self):
        code = input("Code : ")
        description = input("Description : ")
        categorie = input("Catégorie : ")
        capacite = int(input("Capacité : "))
        return code, description, categorie, capacite

    def saisir_code(self):
        return input("Code de la salle : ")

    def afficher_message(self, message):
        print(message)

    def afficher_salles(self, salles):
        if not salles:
            print("Aucune salle trouvée")
        else:
            for s in salles:
                print(f"{s.code} - {s.description} - {s.categorie} - {s.capacite}")