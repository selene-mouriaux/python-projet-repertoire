from terminaltables import AsciiTable
from repertoire_action import *


def demander_nom():
    return input("Nom ? ").capitalize()

def demander_num():
    return input("numéro ? ")

def demander_adresse():
    return input("adresse ? ")

def lister_les_contacts(repertoire):
    if not repertoire:
        print("Le répertoire est vide")
    else:
        print("Liste des contacts du répertoire :")
        show_contact_table (repertoire)

def show_contact_table (repertoire):
    liste_des_contacts = [["Noms", "Numéros", "Adresses"]]
    for contact in repertoire:
        liste_des_contacts.append([contact["nom"],contact["telephone"],contact["adresse"]])
    liste_des_contacts = AsciiTable(liste_des_contacts)
    print(liste_des_contacts.table)

def menu():
    choix = input("\nVeuillez sélectionner une option : \n(L)ister les contacts du répertoire \n" \
                  + "(A)jouter un contact au répertoire \n(S)upprimer un contact du répertoire \n" \
                  + "(R)echercher un contact par nom \n(M)odifier un numéro \n")
    return choix

def add_contact(repertoire):
    if ajouter_personne(repertoire, demander_nom(), demander_num(), demander_adresse()):
        print("contact créé avec succès")
    else:
        print("Echec de la quête ! ")

def delete_contact(repertoire):
    if not supprimer_personne(repertoire, demander_nom()):
        print("Suppression échouée, contact non trouvé ")
    else:
        print("Suppression effectuée ")

def look_for(repertoire):
    matches = chercher_personne(repertoire, demander_nom(), demander_num(), demander_adresse())
    if matches:
        for match in matches:
            print("correspondance trouvée :\n {} : {}, domicilié(e) au {}.".format(match["nom"], \
                                                                                   match["telephone"], \
                                                                                   match["adresse"]))

def modify_contact(repertoire):
    if not modifier_personne(repertoire, demander_nom(), demander_num(), demander_adresse()):
        print("Modification non effectuée, contact non trouvé ")
    else:
        print("Modification effectuée ")

while True:
    repertoire = get_rep()
    choix = menu()
    if choix.upper() == "L":
        lister_les_contacts(repertoire)
    elif choix.upper() == "A":
        add_contact(repertoire)
    elif choix.upper() == "S":
        delete_contact(repertoire)
    elif choix.upper() == "R":
        look_for(repertoire)
    elif choix.upper() == "M":
        modify_contact(repertoire)