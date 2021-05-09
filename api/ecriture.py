import json

# =====================
# Fonction qui ecrit dans un fichier  /!\ FICHIER SEUL CONSEILLE /!\
# 
# Entree: Le dictionnaire avec les donnees
# Sortie: RIEN
# =====================
def ecrire(donnee,nomFichier):
    with open("edt/"+nomFichier, 'w') as f:
        json.dump(donnee,f, indent=2, ensure_ascii=False, sort_keys=False )


# Listes des coordonnées des 4 pipettes
pipetteCoordonnees = { "A1":{
    "X": [208, 290, 371, 453, 534, 616, 697, 779, 860, 942, 1023, 1105, 1186, 1268, 1349, 1431, 1512, 1594, 1675, 1757, 1838, 1920, 2001, 2083],
    "Y": [216, 252, 288, 326, 362, 398, 436, 472, 508, 546, 582, 618, 656, 692, 728, 766, 802, 838, 876, 912, 948, 986, 1022, 1058, 1096, 1132, 1168, 1206, 1242, 1278, 1316, 1352, 1388, 1426, 1462, 1498]
},"A3":{
    "X": [208, 290, 371, 453, 534, 616, 697, 779, 860, 942, 1023, 1105, 1186, 1268, 1349, 1431, 1512, 1594, 1675, 1757, 1838, 1920, 2001, 2083],
    "Y": [215, 326, 437, 550, 661, 772, 885, 996, 1107, 1220, 1331, 1442]
},"A2":{
    "X": [208, 290, 371, 453, 534, 616, 697, 779, 860, 942, 1023, 1105, 1186, 1268, 1349, 1431, 1512, 1594, 1675, 1757, 1838, 1920, 2001, 2083],
    "Y": [216, 267, 320, 371, 424, 475, 528, 579, 632, 683, 736, 787, 840, 891, 944, 995, 1048, 1099, 1152, 1203, 1256, 1307, 1360, 1411]
}}