from data.dao_salle import DataSalle

class ServiceSalle:
    def _init_(self):
        self.dao = DataSalle()

def ajouter_salle(self, salle):
    if not salle.code or not salle.description or not salle.categorie or not salle.capacite:
        return False, "❌ Données manquantes"

    if salle.capacite < 1:
        return False, "❌ Capacité invalide"

    self.dao.insert_salle(salle)
    return True, "✅ Salle ajoutée"
def modifier_salle(self, salle):
    if not salle.code or not salle.description or not salle.categorie or not salle.capacite:
        return False, "❌ Données manquantes"

    if salle.capacite < 1:
        return False, "❌ Capacité invalide"

    self.dao.update_salle(salle)
    return True, "✅ Salle modifiée"

def supprimer_salle(self, code):
    self.dao.delete_salle(code)
    return True, "🗑️ Salle supprimée"