import repertoire_utils_text as repertoire_utils

def get_rep():
    return repertoire_utils.get_rep()

def existe(nouveau_contact, repertoire):
    existe_deja = False
    for contact in repertoire:
        if contact["nom"].lower() == nouveau_contact.lower():
            existe_deja = True
            return existe_deja
    return existe_deja

def ajouter_personne(repertoire, nom, telephone, adresse):
    if not existe(nom, repertoire):
        personne = {'nom': nom, 'telephone': telephone, 'adresse': adresse}
        repertoire_utils.append_rep(repertoire, personne)
        return True
    else:
        return False

def supprimer_personne(repertoire, nom):
    repertoire_utils.del_rep(repertoire, nom)
    return True

def chercher_personne(repertoire, nom, telephone, adresse):
    matches = []
    for contact in repertoire:
        if nom.lower() in contact["nom"].lower() or telephone in contact["telephone"] or adresse in contact["adresse"]:
            matches.append(contact)
    return matches

def modifier_personne(repertoire, nom, telephone, adresse):
    if repertoire_utils.modif_rep(repertoire, nom, telephone, adresse):
        return True
