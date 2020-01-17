from terminaltables import AsciiTable
entrees_par_contact = 3
repertoire = [{'Nom':'Adrien', 'Tel':'04.94.36.12.95', 'Adresse':'12 Rue du yahourt'},\
              {'Nom':'Dobby', 'Tel':'04.94.36.12.95', 'Adresse':'325 chemin du train des pignes'},\
              {'Nom':'Bob', 'Tel':'01.44.99.10.32', 'Adresse':'38 Avenue Victor Hugo'}]
saisie = True
liste_choix_possibles = ["L","A","S","R","M"]

def demander_nom():
    nouveau_nom = input("Nom ? ").capitalize()
    return nouveau_nom

def demander_num():
    nouveau_num = input("numéro ? ")
    return nouveau_num

def demander_adresse():
    nouvelle_adresse = input("adresse ? ")
    return nouvelle_adresse

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

while saisie:
    choix = input("\nVeuillez sélectionner une option : \n(L)ister les contacts du répertoire \n" \
                      + "(A)jouter un contact au répertoire \n(S)upprimer un contact du répertoire \n"\
                        +"(R)echercher un contact par nom \n(M)odifier un numéro \n")
    if choix.upper() not in liste_choix_possibles:
        print("Merci de se cantonner aux options existantes... ")
        continue
    elif choix.upper() == "L":
        lister_les_contacts()
    elif choix.upper() == "A":
        if ajouter_un_contact(demander_nom(), demander_num(), demander_adresse(), repertoire):
            print("contact créé avec succès")
        else:
            print("Echec de la quête ! ")
    elif choix.upper() == "S":
        if not supprimer_un_contact(demander_nom(), repertoire):
            print("Suppression échouée, contact non trouvé ")
        else:
            print("Suppression effectuée ")
    elif choix.upper() == "R":
        matches = rechercher_par_nom(demander_nom(), repertoire)
        if matches:
            for match in matches:
                print("correspondance trouvée :\n {} : {}, domicilié(e) au {}.".format(match["Nom"], \
                                                                                   match["Tel"], \
                                                                                   match["Adresse"]))
    elif choix.upper() == "M":
        if not modifier_numero(demander_nom(), demander_num(), demander_adresse(), repertoire):
            print("Modification non effectuée, contact non trouvé ")
        else:
            print("Modification effectuée ")

print("fin provisoire")