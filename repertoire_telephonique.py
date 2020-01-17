from terminaltables import AsciiTable
repertoire = {'Contact 1':'04.94.36.12.95', 'Contact 2':'04.75.17.85.43'}
saisie = True
liste_choix_possibles = ["L","A","S","R","M"]

def demander_nom():
    nouveau_nom = input("Nom ? ").capitalize()
    return nouveau_nom

def demander_num():
    nouveau_num = input("numéro ? ")
    return nouveau_num

def show_contact_table (repertoire):
    liste_de_listes = [["Noms", "Numéros"]] + [[key, value] for key, value in repertoire.items()]
    tableau_du_repertoire = AsciiTable(liste_de_listes)
    print(tableau_du_repertoire.table)

def existe(nouveau_contact, repertoire):
    existe_deja = False
    for key in repertoire.keys():
        test_key = key.lower()
        if nouveau_contact.lower() == test_key:
            existe_deja = True
            return existe_deja
    return existe_deja

def lister_les_contacts():
    if not repertoire:
        print("Le répertoire est vide")
    else:
        print("Liste des contacts du répertoire :")
        show_contact_table (repertoire)

def ajouter_un_contact(nouveau_contact, nouveau_numero, repertoire):
    if not existe(nouveau_contact, repertoire):
        repertoire[nouveau_contact] = nouveau_numero
        print("contact créé avec succès")
        print("{} est désormais disponible dans le répertoire".format (nouveau_contact))

def supprimer_un_contact(contact_a_supprimer, repertoire):
    if existe(nouveau_contact, repertoire):
        del repertoire[contact_a_supprimer]
        print("Contact supprimé avec succès")

def rechercher_par_nom(recherche_contact, repertoire):
    if repertoire:
        for key in repertoire.keys():
            test_key = key.lower()
            if recherche_contact.lower() in test_key:
                print("Le numéro de {} est : {}".format(key, repertoire[key]))
        print("Aucune correspondance trouvée")

def modifier_numero(modifier_contact, nouveau_numero, repertoire):
    if not existe(modifier_contact, repertoire):
        print("Modification impossible, contact non trouvé")
    if existe(modifier_contact, repertoire):
        for key in repertoire.keys():
            test_key = key.lower()
            if modifier_contact.lower() == test_key:
                repertoire[modifier_contact] = nouveau_numero
                print("Numéro mis à jour ")
                return ""

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
        ajouter_un_contact(demander_nom(), demander_num(), repertoire)
    elif choix.upper() == "S":
        supprimer_un_contact(demander_nom(), repertoire)
    elif choix.upper() == "R":
        rechercher_par_nom(demander_nom(), repertoire)
    elif choix.upper() == "M":
        modifier_numero(demander_nom(), demander_num(), repertoire)

print("fin provisoire")