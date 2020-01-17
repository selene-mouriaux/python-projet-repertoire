from terminaltables import AsciiTable
from utils.repertoire_action import *

entrees_par_contact = 3
repertoire = [{'Nom':'Adrien', 'Tel':'04.94.36.12.95', 'Adresse':'12 Rue du yahourt'},\
              {'Nom':'Dobby', 'Tel':'04.94.36.12.95', 'Adresse':'325 chemin du train des pignes'},\
              {'Nom':'Bob', 'Tel':'01.44.99.10.32', 'Adresse':'38 Avenue Victor Hugo'}]

def menu():
    choix = input("\nVeuillez sélectionner une option : \n(L)ister les contacts du répertoire \n" \
                  + "(A)jouter un contact au répertoire \n(S)upprimer un contact du répertoire \n" \
                  + "(R)echercher un contact par nom \n(M)odifier un numéro \n")
    return choix

def add_contact():
    if ajouter_un_contact(demander_nom(), demander_num(), demander_adresse(), repertoire):
        print("contact créé avec succès")
    else:
        print("Echec de la quête ! ")

def delete_contact():
    if not supprimer_un_contact(demander_nom(), repertoire):
        print("Suppression échouée, contact non trouvé ")
    else:
        print("Suppression effectuée ")

def look_for():
    matches = rechercher_par_nom(demander_nom(), repertoire)
    if matches:
        for match in matches:
            print("correspondance trouvée :\n {} : {}, domicilié(e) au {}.".format(match["Nom"], \
                                                                                   match["Tel"], \
                                                                                   match["Adresse"]))

def modify_contact():
    if not modifier_numero(demander_nom(), demander_num(), demander_adresse(), repertoire):
        print("Modification non effectuée, contact non trouvé ")
    else:
        print("Modification effectuée ")

while True:
    choix = menu()
    if choix.upper() == "L":
        lister_les_contacts()
    elif choix.upper() == "A":
        add_contact()
    elif choix.upper() == "S":
        delete_contact()
    elif choix.upper() == "R":
        look_for()
    elif choix.upper() == "M":
        modify_contact()