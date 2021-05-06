import json


# =======================
# Fonction qui ouvre le json
# ======================
def data():
    data = {}
    with open('donnees.json') as json_data:
        data = json.load(json_data)
    return data

def lecteurEDT(data, indice):
    donneeEDT = {}
    nomFichier = str(data[indice]+".json")
    try:
        with open(nomFichier) as json_data:
            donneeEDT = json.load(json_data)
        return donneeEDT
    except :
        sem = indice+1
        print("L'EDT de la semaine "+str(sem)+" est introuvable")
        return False


data  = data()