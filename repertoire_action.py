
def demander_nom():
    return input("Nom ? ").capitalize()

def demander_num():
    return input("numéro ? ")

def demander_adresse():
    return input("adresse ? ")

def show_contact_table (repertoire):
    liste_des_contacts = [["Noms", "Numéros", "adresses"]]
    for contact in repertoire:
        liste_des_contacts.append([contact["Nom"],contact["Tel"],contact["Adresse"]])
    liste_des_contacts = AsciiTable(liste_des_contacts)
    print(liste_des_contacts.table)

def existe(nouveau_contact, repertoire):
    existe_deja = False
    for contact in repertoire:
        if contact["Nom"].lower() == nouveau_contact.lower():
            existe_deja = True
            return existe_deja
    return existe_deja

def lister_les_contacts():
    if not repertoire:
        print("Le répertoire est vide")
    else:
        print("Liste des contacts du répertoire :")
        show_contact_table (repertoire)

def ajouter_un_contact(nouveau_contact, nouveau_numero, nouvelle_adresse, repertoire):
    if not existe(nouveau_contact, repertoire):
        repertoire.append({'Nom':nouveau_contact, 'Tel':nouveau_numero, 'Adresse':nouvelle_adresse})
        return True
    else:
        return False

def supprimer_un_contact(contact_a_supprimer, repertoire):
    for i, contact in enumerate(repertoire):
        if contact["Nom"].lower() == contact_a_supprimer.lower():
            del repertoire[i]
            return True

def rechercher_par_nom(recherche_contact, repertoire):
    matches = []
    for contact in repertoire:
        if recherche_contact.lower() in contact["Nom"].lower():
            matches.append(contact)
    return matches

def modifier_numero(modifier_contact, nouveau_numero, nouvelle_adresse, repertoire):
    for i, contact in enumerate(repertoire):
        if contact["Nom"].lower() == modifier_contact.lower():
            repertoire[i]=({'Nom':modifier_contact, 'Tel':nouveau_numero, 'Adresse':nouvelle_adresse})
            return True