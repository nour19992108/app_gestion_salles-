from services.service_salle import ServiceSalle
from models.salle import Salle
from views.view_salle import ViewSalle

def main():
    service = ServiceSalle()
    view = ViewSalle()

    while True:
        view.afficher_menu()
        choix = input("Choix : ")

        if choix == "1":
            code, description, categorie, capacite = view.saisir_salle()
            salle = Salle(code, description, categorie, capacite)
            succes, message = service.ajouter_salle(salle)
            view.afficher_message(message)

        elif choix == "2":
            salles = service.get_salles()
            view.afficher_salles(salles)

        elif choix == "3":
            code, description, categorie, capacite = view.saisir_salle()
            salle = Salle(code, description, categorie, capacite)
            succes, message = service.modifier_salle(salle)
            view.afficher_message(message)

        elif choix == "4":
            code = view.saisir_code()
            succes, message = service.supprimer_salle(code)
            view.afficher_message(message)

        elif choix == "5":
            print("Au revoir")
            break

        else:
            print("Choix invalide")

main()