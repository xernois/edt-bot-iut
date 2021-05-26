import json
import requests


# =======================
# Fonction qui ouvre le json
# ======================
def data():
    data = {}
    with open('donnees.json') as json_data:
        data = json.load(json_data)
    return data

def lecteurEDT(indiceGroupe, semaine):
    if indiceGroupe <=5:
        annee = 1
    if indiceGroupe > 5 and indiceGroupe <=9:
        annee = 2
    if indiceGroupe > 9:
        annee = 3
    semaine = int(semaine)+ 1
    stringRequete = str(f'http://109.220.5.61/api/edt/a{annee}?s={semaine}')
    try:
        res = requests.get(stringRequete)
        print(res.text)
        return(json.loads(res.text))
    except:
        print("L'EDT de la semaine "+str(semaine)+" est introuvable")
        return False


data  = data()