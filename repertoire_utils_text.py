import json

repertoire = [{'nom':'Adrien', 'telephone':'04.94.36.12.95', 'adresse':'12 Rue du yahourt'},\
              {'nom':'Dobby', 'telephone':'04.94.36.12.95', 'adresse':'325 chemin du train des pignes'},\
              {'nom':'Bob', 'telephone':'01.44.99.10.32', 'adresse':'38 Avenue Victor Hugo'}]

def get_rep():
    data = open("Json.txt", "r")
    repertoire = json.loads(data.read())
    data.close()
    return repertoire

def append_rep(repertoire, personne):
    repertoire.append(personne)
    with open("Json.txt", "w") as data:
        data.write(json.dumps(repertoire))
    return repertoire

def del_rep(repertoire, personne):
    for i, contact in enumerate(repertoire):
        if contact["nom"].lower() == personne.lower():
            del repertoire[i]

def modif_rep(repertoire, nom, telephone, adresse):
    for i, contact in enumerate(repertoire):
        if contact["nom"].lower() == nom.lower():
            repertoire[i]=({'nom':nom, 'telephone':telephone, 'adresse':adresse})
            return True