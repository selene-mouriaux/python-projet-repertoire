from terminaltables import AsciiTable
repertoire = {'Contact 1':'04.94.36.12.95', 'Contact 2':'04.75.17.85.43'}
saisie = True
liste_choix_possibles = ["L","A","S","R","M"]

def show_contact_table (repertoire):
    liste_de_listes = [["Noms", "Numéros"]] + [[key, value] for key, value in repertoire.items()]
    tableau_du_repertoire = AsciiTable(liste_de_listes)
    print(tableau_du_repertoire.table)



def lister_les_contacts():
    if not repertoire:
        print("Le répertoire est vide")
    else:
        print("Liste des contacts du répertoire :")
        show_contact_table (repertoire)

def ajouter_un_contact(nouveau_contact, nouveau_numero):
    existe_deja = False
    for key in repertoire.keys():
        test_key = key.lower()
        if nouveau_contact.lower() == test_key:
            print("Contact déjà existant, veuillez supprimer pour recréer ")
            existe_deja = True
    if not existe_deja:
        repertoire[nouveau_contact] = nouveau_numero
    print("contact créé avec succès")
    print("{} est désormais disponible dans le répertoire".format (nouveau_contact))

def supprimer_un_contact():
    recherche_existe = False
    contact_a_supprimer = input("Quel contact voulez-vous supprimer ? ").capitalize()
    for key in repertoire.keys():
        test_key = key.capitalize()
        if contact_a_supprimer == test_key:
            recherche_existe = True
    if recherche_existe:
        del repertoire[contact_a_supprimer]
    else:
        print("Aucune correspondance, suppression impossible ")

def rechercher_par_nom():
    recherche_contact = input("De qui recherchez-vous le numéro ? ").lower()
    for key in repertoire.keys():
        test_key = key.lower()
        if recherche_contact in test_key:
            print("Le numéro de {} est : {}".format(key, repertoire[key]))
    print("Aucune correspondance trouvée")

def modifier_numero():
    modifier_contact = input("Modifier le numéro de qui ? ").capitalize()
    nouveau_numero = input("Son nouveau numéro ? ")
    for key in repertoire.keys():
        test_key = key.lower()
        if modifier_contact.lower() == test_key:
            repertoire[modifier_contact] = nouveau_numero
            print("Numéro mis à jour ")
            return ""
    print("Contact non trouvé, modification impossible ")

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
        nouveau_nom = input("Nom ? ").capitalize()
        nouveau_num = input("numéro ? ")
        ajouter_un_contact(nouveau_nom, nouveau_num, repertoire)
    elif choix.upper() == "S":
        supprimer_un_contact()
    elif choix.upper() == "R":
        rechercher_par_nom()
    elif choix.upper() == "M":
        modifier_numero()

print("fin provisoire")