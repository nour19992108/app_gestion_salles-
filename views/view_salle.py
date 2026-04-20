import customtkinter as ctk
from services.service_salle import ServiceSalle

class ViewSalle(ctk.CTk):
    def _init_(self):
        super()._init_()

        self.title("Gestion des salles")
        self.geometry("900x600")

        self.service_salle = ServiceSalle()
import customtkinter as ctk
from services.service_salle import ServiceSalle

class ViewSalle(ctk.CTk):
    def _init_(self):
        super()._init_()

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