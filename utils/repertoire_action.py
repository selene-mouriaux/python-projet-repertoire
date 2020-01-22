import repertoire_utils_dict as repertoire_utils

def existe(nouveau_contact, repertoire):
    existe_deja = False
    for contact in repertoire:
        if contact["nom"].lower() == nouveau_contact.lower():
            existe_deja = True
            return existe_deja
    return existe_deja

def ajouter_personne(repertoire, nom, telephone, adresse):
    if not existe(nom, repertoire):
        repertoire.append({'nom': nom, 'telephone': telephone, 'adresse': adresse})
        return True
    else:
        return False

def supprimer_personne(repertoire, nom):
    for i, contact in enumerate(repertoire):
        if contact["nom"].lower() == nom.lower():
            del repertoire[i]
            return True

def chercher_personne(repertoire, nom, telephone, adresse):
    matches = []
    for contact in repertoire:
        if nom.lower() in contact["nom"].lower() or telephone in contact["telephone"] or adresse in contact["adresse"]:
            matches.append(contact)
    return matches

def modifier_personne(repertoire, nom, telephone, adresse):
    for i, contact in enumerate(repertoire):
        if contact["nom"].lower() == nom.lower():
            repertoire[i]=({'nom':nom, 'telephone':telephone, 'adresse':adresse})
            return True