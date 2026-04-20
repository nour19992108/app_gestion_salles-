from data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()

# Test connexion
con = dao.get_connection()
if con.is_connected():
    print("Connexion OK")
con.close()

# Test ajout
salle = Salle("A5", "Salle Python", "Lab", 30)
dao.insert_salle(salle)
print("Salle ajoutée")

# Test affichage
print("\nListe des salles :")
salles = dao.get_salles()
for s in salles:
    s.afficher_infos()
