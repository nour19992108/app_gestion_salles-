import customtkinter as ctk
from services.service_salle import ServiceSalle
from tkinter import ttk


class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestion des salles")
        self.geometry("900x600")

        self.service_salle = ServiceSalle()

        # Cadre Informations Salle
        self.frame_info = ctk.CTkFrame(self)
        self.frame_info.pack(pady=10, padx=10, fill="x")

        # Code
        self.label_code = ctk.CTkLabel(self.frame_info, text="Code")
        self.label_code.grid(row=0, column=0, padx=5, pady=5)

        self.entry_code = ctk.CTkEntry(self.frame_info)
        self.entry_code.grid(row=0, column=1, padx=5, pady=5)

        # Description
        self.label_description = ctk.CTkLabel(self.frame_info, text="Description")
        self.label_description.grid(row=1, column=0, padx=5, pady=5)

        self.entry_description = ctk.CTkEntry(self.frame_info)
        self.entry_description.grid(row=1, column=1, padx=5, pady=5)

        # Catégorie
        self.label_categorie = ctk.CTkLabel(self.frame_info, text="Catégorie")
        self.label_categorie.grid(row=2, column=0, padx=5, pady=5)

        self.entry_categorie = ctk.CTkEntry(self.frame_info)
        self.entry_categorie.grid(row=2, column=1, padx=5, pady=5)

        # Capacité
        self.label_capacite = ctk.CTkLabel(self.frame_info, text="Capacité")
        self.label_capacite.grid(row=3, column=0, padx=5, pady=5)

        self.entry_capacite = ctk.CTkEntry(self.frame_info)
        self.entry_capacite.grid(row=3, column=1, padx=5, pady=5)

        # Cadre Actions
        self.frame_actions = ctk.CTkFrame(self)
        self.frame_actions.pack(pady=10, padx=10, fill="x")

        self.btn_ajouter = ctk.CTkButton(
            self.frame_actions,
            text="Ajouter",
            command=self.ajouter_salle
        )
        self.btn_ajouter.grid(row=0, column=0, padx=10, pady=10)

        self.btn_modifier = ctk.CTkButton(self.frame_actions, text="Modifier")
        self.btn_modifier.grid(row=0, column=1, padx=10, pady=10)

        self.btn_supprimer = ctk.CTkButton(self.frame_actions, text="Supprimer")
        self.btn_supprimer.grid(row=0, column=2, padx=10, pady=10)

        self.btn_rechercher = ctk.CTkButton(self.frame_actions, text="Rechercher")
        self.btn_rechercher.grid(row=0, column=3, padx=10, pady=10)


        # Cadre Liste des salles
        self.cadreList = ctk.CTkFrame(self, corner_radius=10, width=400)
        self.cadreList.pack(pady=10, padx=10)

        self.treeList = ttk.Treeview(
            self.cadreList,
            columns=("code", "description", "categorie", "capacite"),
            show="headings"
        )

        # En-têtes
        self.treeList.heading("code", text="CODE")
        self.treeList.heading("description", text="Description")
        self.treeList.heading("categorie", text="Catégorie")
        self.treeList.heading("capacite", text="Capacité")

        # Largeur des colonnes
        self.treeList.column("code", width=50)
        self.treeList.column("description", width=150)
        self.treeList.column("categorie", width=100)
        self.treeList.column("capacite", width=100)

        self.treeList.pack(expand=True, fill="both", padx=10, pady=10)
        self.lister_salles()

    def ajouter_salle(self):
        code = self.entry_code.get()
        description = self.entry_description.get()
        categorie = self.entry_categorie.get()
        capacite = int(self.entry_capacite.get())

        from models.salle import Salle
        salle = Salle(code, description, categorie, capacite)

        print("avant service")
        try:
            resultat = self.service_salle.ajouter_salle(salle)
            print("resultat =", resultat)

            success, message = resultat
            print(message)

            if success:
                self.lister_salles()

        except Exception as e:
            print("ERREUR AJOUT =", e)

    def lister_salles(self):
        self.treeList.delete(*self.treeList.get_children())
        liste = self.service_salle.get_salles()
        for s in liste:
            self.treeList.insert("", "end", values=(s.code, s.description, s.categorie, s.capacite))
