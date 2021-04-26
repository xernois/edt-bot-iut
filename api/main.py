from PIL import Image
import ecriture, getModule

# =====================
# Fonction qui detect si une couleur est dans un intervalle
# 
# Entree: 3 tuples de couleurs au format (RVB)
# Sortie: Booleen
# =====================
def intervalleCouleur(cdColor,borneInf, borneSup):
    intervalle =  True
    for x in range (0,2,1):
        if cdColor[x] <= borneSup[x] and cdColor[x] >= borneInf[x]:
            intervalle = True
        else:
            intervalle = False
            break
    return intervalle


# =====================
# Fonction qui detecte 4 couleurs
# 
# Entree: 4 tuples de couleurs au format (RVB)
# Sortie: Une chaine de caractere (Rose, Jaune, Beige, Bleu, Violet, None)
# =====================
def getColor(codeColor, codeColor2,codeColor3,codeColor4, codeColor5):
    if (intervalleCouleur(codeColor,(245, 226,245),(255,246,255)) or intervalleCouleur(codeColor2,(245, 226,245),(255,246,255)) or
     intervalleCouleur(codeColor3,(245, 226,245),(255,246,255)) or intervalleCouleur(codeColor4,(245, 226,245),(255,246,255))or 
     intervalleCouleur(codeColor5,(245, 226,245),(255,246,255))):
        return "Rose"
    if (intervalleCouleur(codeColor,(235, 235,1),(255,255,60)) or intervalleCouleur(codeColor2,(235, 235,1),(255,255,60)) or
     intervalleCouleur(codeColor3,(235, 235,1),(255,255,60)) or intervalleCouleur(codeColor4,(235, 235,1),(255,255,60)) or 
     intervalleCouleur(codeColor5,(235, 235,1),(255,255,60))):
        return "Jaune"
    if (intervalleCouleur(codeColor,(235, 167,160),(255,207,200)) or intervalleCouleur(codeColor2,(235, 167,160),(255,207,200)) or
     intervalleCouleur(codeColor3,(235, 167,160),(255,207,200)) or intervalleCouleur(codeColor4,(235, 167,160),(255,207,200)) or
      intervalleCouleur(codeColor5,(235, 167,160),(255,207,200))):
        return "Beige"
    if (intervalleCouleur(codeColor,(160, 235,235),(200,255,255)) or intervalleCouleur(codeColor2,(160, 235,235),(200,255,255)) or
     intervalleCouleur(codeColor3,(160, 235,235),(200,255,255)) or intervalleCouleur(codeColor4,(160, 235,235),(200,255,255)) or 
     intervalleCouleur(codeColor5,(160, 235,235),(200,255,255))):
        return "Bleu"
    if (intervalleCouleur(codeColor,(223, 42,147),(263,82,187)) or intervalleCouleur(codeColor2,(223, 42,147),(263,82,187)) or
     intervalleCouleur(codeColor3,(223, 42,147),(263,82,187)) or intervalleCouleur(codeColor4,(223, 42,147),(263,82,187)) or
      intervalleCouleur(codeColor4,(223, 42,147),(263,82,187))):
        return "Violet"
    return "None"


# =====================
# Fonction qui traite l'EDT en groupe de TP
# 
# Entree: Image de l'EDT
# Sortie: Rien
# =====================
def engine(edtImage, niveau):
    im = Image.open(edtImage)
    # imgScinde = ["fond1.jpg","fond2.jpg","fond3.jpg","fond4.jpg","fond5.jpg","fond6.jpg","fond7.jpg","fond8.jpg","fond9.jpg","fond10.jpg","fond11.jpg",
    # "fond12.jpg","fond13.jpg","fond14.jpg","fond15.jpg","fond16.jpg","fond17.jpg","fond18.jpg","fond19.jpg","fond20.jpg","fond21.jpg","fond22.jpg","fond23.jpg","fond24.jpg"]
    compteur = 1
    height = 5
    width = 79

    # Dictionnaire de données L1
    edt3 = {"L1A" : {"Lundi" : {"Cours" :  []},"Mardi" : {"Cours" :  []},"Mercredi" : {"Cours" :  []},"Jeudi" : {"Cours" :  []},"Vendredi" : {"Cours" :  []},"Samedi" : {"Cours" :  []}},
        "L1B" : {"Lundi" : {"Cours" :  [] }, "Mardi" : { "Cours" :  []},"Mercredi" : {"Cours" :  []},"Jeudi" : {"Cours" :  []},"Vendredi" : {"Cours" :  []},"Samedi" : {"Cours" :  []}}}

    # Dictionnaire de données A2
    edt2 = {"G4A" : {"Lundi" : {"Cours" :  []},"Mardi" : {"Cours" :  []},"Mercredi" : {"Cours" :  []},"Jeudi" : {"Cours" :  []},"Vendredi" : {"Cours" :  []},"Samedi" : {"Cours" :  []}},
        "G4B" : {"Lundi" : {"Cours" :  [] }, "Mardi" : { "Cours" :  []},"Mercredi" : {"Cours" :  []},"Jeudi" : {"Cours" :  []},"Vendredi" : {"Cours" :  []},"Samedi" : {"Cours" :  []}},
        "G5A" : {"Lundi" : {"Cours" :  [] }, "Mardi" : { "Cours" :  []},"Mercredi" : {"Cours" :  []},"Jeudi" : {"Cours" :  []},"Vendredi" : {"Cours" :  []},"Samedi" : {"Cours" :  []}},
        "G5B" : {"Lundi" : {"Cours" :  [] }, "Mardi" : { "Cours" :  []},"Mercredi" : {"Cours" :  []},"Jeudi" : {"Cours" :  []},"Vendredi" : {"Cours" :  []},"Samedi" : {"Cours" :  []}}}
    
    # Dictionnaire de données A1
    edt1 = {"G1A" : {"Lundi" : {"Cours" :  []},"Mardi" : {"Cours" :  []},"Mercredi" : {"Cours" :  []},"Jeudi" : {"Cours" :  []},"Vendredi" : {"Cours" :  []},"Samedi" : {"Cours" :  []}},
        "G1B" : {"Lundi" : {"Cours" :  [] }, "Mardi" : { "Cours" :  []},"Mercredi" : {"Cours" :  []},"Jeudi" : {"Cours" :  []},"Vendredi" : {"Cours" :  []},"Samedi" : {"Cours" :  []}},
        "G2A" : {"Lundi" : {"Cours" :  [] }, "Mardi" : { "Cours" :  []},"Mercredi" : {"Cours" :  []},"Jeudi" : {"Cours" :  []},"Vendredi" : {"Cours" :  []},"Samedi" : {"Cours" :  []}},
        "G2B" : {"Lundi" : {"Cours" :  [] }, "Mardi" : { "Cours" :  []},"Mercredi" : {"Cours" :  []},"Jeudi" : {"Cours" :  []},"Vendredi" : {"Cours" :  []},"Samedi" : {"Cours" :  []}},
        "G3A" : {"Lundi" : {"Cours" :  [] }, "Mardi" : {"Cours" :  []}, "Mercredi" : {"Cours" :  []},"Jeudi" : {"Cours" :  []},"Vendredi" : {"Cours" :  []},"Samedi" : {"Cours" :  []}},
        "G3B" : {"Lundi" : {"Cours" :  [] }, "Mardi" : {"Cours" :  []}, "Mercredi" : {"Cours" :  []},"Jeudi" : {"Cours" :  []},"Vendredi" : {"Cours" :  []},"Samedi" : {"Cours" :  []}}}


    groupe1 = ["G1A","G1B","G2A","G2B","G3A","G3B"]
    groupe2 = ["G4A","G4B","G5A","G5B"]
    groupe3 = ["L1A","L1B"]
    jour = ["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi"]
    compteurGr = 0
    CompteurJr = 0
    for y in range (0,len(ecriture.pipetteCoordonnees[niveau]["Y"]),1): 
        h = 8
        for x in range (0,len(ecriture.pipetteCoordonnees[niveau]["X"])-1,1):
            compteur += 1
            if niveau == 'A1':
                pipette1 = im.getpixel((ecriture.pipetteCoordonnees[niveau]["X"][x]+16,ecriture.pipetteCoordonnees[niveau]["Y"][y]+5))
                pipette2 = im.getpixel((ecriture.pipetteCoordonnees[niveau]["X"][x]+66,ecriture.pipetteCoordonnees[niveau]["Y"][y]+5))
                pipette3 = im.getpixel((ecriture.pipetteCoordonnees[niveau]["X"][x]+16,ecriture.pipetteCoordonnees[niveau]["Y"][y]+28))
                pipette4 = im.getpixel((ecriture.pipetteCoordonnees[niveau]["X"][x]+66,ecriture.pipetteCoordonnees[niveau]["Y"][y]+28))
                pipette5 = im.getpixel((ecriture.pipetteCoordonnees[niveau]["X"][x]+31,ecriture.pipetteCoordonnees[niveau]["Y"][y]+16))

            if niveau == 'A2':
                pipette1 = im.getpixel((ecriture.pipetteCoordonnees[niveau]["X"][x]+16,ecriture.pipetteCoordonnees[niveau]["Y"][y]+13))
                pipette2 = im.getpixel((ecriture.pipetteCoordonnees[niveau]["X"][x]+66,ecriture.pipetteCoordonnees[niveau]["Y"][y]+13))
                pipette3 = im.getpixel((ecriture.pipetteCoordonnees[niveau]["X"][x]+16,ecriture.pipetteCoordonnees[niveau]["Y"][y]+38))
                pipette4 = im.getpixel((ecriture.pipetteCoordonnees[niveau]["X"][x]+66,ecriture.pipetteCoordonnees[niveau]["Y"][y]+38))
                pipette5 = im.getpixel((ecriture.pipetteCoordonnees[niveau]["X"][x]+31,ecriture.pipetteCoordonnees[niveau]["Y"][y]+25))

            if niveau == 'A3':
                pipette1 = im.getpixel((ecriture.pipetteCoordonnees[niveau]["X"][x]+16,ecriture.pipetteCoordonnees[niveau]["Y"][y]+5))
                pipette2 = im.getpixel((ecriture.pipetteCoordonnees[niveau]["X"][x]+66,ecriture.pipetteCoordonnees[niveau]["Y"][y]+5))
                pipette3 = im.getpixel((ecriture.pipetteCoordonnees[niveau]["X"][x]+16,ecriture.pipetteCoordonnees[niveau]["Y"][y]+102))
                pipette4 = im.getpixel((ecriture.pipetteCoordonnees[niveau]["X"][x]+66,ecriture.pipetteCoordonnees[niveau]["Y"][y]+102))
                pipette5 = im.getpixel((ecriture.pipetteCoordonnees[niveau]["X"][x]+31,ecriture.pipetteCoordonnees[niveau]["Y"][y]+49))

            if (int(h)==h):
                heure = str(int(h)) +"h00"
            else:
                heure = str(int(h)) +"h30"
# -------- Pas de Cours
            if getColor(pipette1, pipette2, pipette3, pipette4, pipette5) == "Rose":
                if niveau == "A1":
                    edt1[groupe1[compteurGr]][jour[CompteurJr]]["Cours"].append(("",""))
                    print(heure," - ", groupe1[compteurGr],jour[CompteurJr])
                if niveau == "A2":
                    edt2[groupe2[compteurGr]][jour[CompteurJr]]["Cours"].append(("",""))
                    print(heure," - ", groupe2[compteurGr],jour[CompteurJr])
                if niveau == "A3":
                    edt3[groupe3[compteurGr]][jour[CompteurJr]]["Cours"].append(("",""))
                    print(heure," - ", groupe3[compteurGr],jour[CompteurJr])
            else:
# --------- Cours de CM
                if getColor(pipette1, pipette2, pipette3, pipette4, pipette5) == "Jaune":
                    if niveau == "A1":                        
                        if groupe1[compteurGr] == "G1A":
                            module = str(getModule.decoupeCM(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y], niveau))
                        if groupe1[compteurGr] == "G1B":
                            module = str(getModule.decoupeCM(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y-1], niveau))
                        if groupe1[compteurGr] == "G2A":
                            module = str(getModule.decoupeCM(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y-2], niveau))
                        if groupe1[compteurGr] == "G2B":
                            module = str(getModule.decoupeCM(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y-3], niveau))
                        if groupe1[compteurGr] == "G3A":
                            module = str(getModule.decoupeCM(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y-4], niveau))
                        if groupe1[compteurGr] == "G3B":
                            module = str(getModule.decoupeCM(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y-5], niveau))
                        if (module!=""):
                            edt1[groupe1[compteurGr]][jour[CompteurJr]]["Cours"].append((module, "CM"))
                        else:
                            edt1[groupe1[compteurGr]][jour[CompteurJr]]["Cours"].append(("", ""))
                        print(heure, " - CM ", groupe1[compteurGr],jour[CompteurJr])
                    if niveau == "A2":
                        if groupe2[compteurGr] == "G4A":
                            module = str(getModule.decoupeCM(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y], niveau))
                        if groupe2[compteurGr] == "G4B":
                            module = str(getModule.decoupeCM(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y-1], niveau))
                        if groupe2[compteurGr] == "G5A":
                            module = str(getModule.decoupeCM(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y-2], niveau))
                        if groupe2[compteurGr] == "G5B":
                            module = str(getModule.decoupeCM(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y-3], niveau))
                        if (module!=""):
                            edt2[groupe2[compteurGr]][jour[CompteurJr]]["Cours"].append((module, "CM"))
                        else:
                            edt2[groupe2[compteurGr]][jour[CompteurJr]]["Cours"].append(("", ""))
                        print(heure, " - CM ", groupe2[compteurGr],jour[CompteurJr])
                    if niveau == "A3":
                        if groupe3[compteurGr] == "L1A":
                            module = str(getModule.decoupeCM(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y], niveau))
                        if groupe3[compteurGr] == "L1B":
                            module = str(getModule.decoupeCM(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y-1], niveau))
                        if (module!=""):
                            edt3[groupe3[compteurGr]][jour[CompteurJr]]["Cours"].append((module, "CM"))
                        else:
                            edt3[groupe3[compteurGr]][jour[CompteurJr]]["Cours"].append(("", ""))
                        print(heure, " - CM ", groupe3[compteurGr],jour[CompteurJr])
# ----- Cours de TD
                elif getColor(pipette1, pipette2, pipette3, pipette4, pipette5) == "Beige":
                    if niveau == "A1":
                        if groupe1[compteurGr] == "G1A":
                            module = getModule.decoupeTD(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y], niveau)
                        if groupe1[compteurGr] == "G1B":
                            module = getModule.decoupeTD(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y-1], niveau)
                        if groupe1[compteurGr] == "G2A":
                            module = getModule.decoupeTD(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y], niveau)
                        if groupe1[compteurGr] == "G2B":
                            module = getModule.decoupeTD(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y-1], niveau)
                        if groupe1[compteurGr] == "G3A":
                            module = getModule.decoupeTD(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y], niveau)
                        if groupe1[compteurGr] == "G3B":
                            module = getModule.decoupeTD(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y-1], niveau)
                        if (module!=""):
                            edt1[groupe1[compteurGr]][jour[CompteurJr]]["Cours"].append((module, "TD"))
                        else:
                            edt1[groupe1[compteurGr]][jour[CompteurJr]]["Cours"].append(("", ""))
                        print(heure, " - TD", groupe1[compteurGr],jour[CompteurJr])

                    if niveau == "A2":
                        if groupe2[compteurGr] == "G4A":
                            module = getModule.decoupeTD(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y], niveau)
                        if groupe2[compteurGr] == "G4B":
                            module = getModule.decoupeTD(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y-1], niveau)
                        if groupe2[compteurGr] == "G5A":
                            module = getModule.decoupeTD(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y], niveau)
                        if groupe2[compteurGr] == "G5B":
                            module = getModule.decoupeTD(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y-1], niveau)
                        if (module!=""):
                            edt2[groupe2[compteurGr]][jour[CompteurJr]]["Cours"].append((module, "TD"))
                        else:
                            edt2[groupe2[compteurGr]][jour[CompteurJr]]["Cours"].append(("", ""))
                        print(heure, " - TD", groupe2[compteurGr],jour[CompteurJr])

                    if niveau == "A3":
                        if groupe2[compteurGr] == "L1A":
                            module = getModule.decoupeTD(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y], niveau)
                        if groupe2[compteurGr] == "L1B":
                            module = getModule.decoupeTD(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y-1], niveau)
                        if (module!=""):
                            edt3[groupe3[compteurGr]][jour[CompteurJr]]["Cours"].append((module, "TD"))
                        else:
                            edt3[groupe3[compteurGr]][jour[CompteurJr]]["Cours"].append(("", ""))
                        print(heure, " - TD", groupe3[compteurGr],jour[CompteurJr])

# ------- Cours de TP
                elif getColor(pipette1, pipette2, pipette3, pipette4, pipette5) == "Bleu":
                    if niveau == "A1":
                        if groupe1[compteurGr] == "G1A":
                            module = getModule.decoupeTP(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y], niveau)
                        if groupe1[compteurGr] == "G1B":
                            module = getModule.decoupeTP(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y], niveau)
                        if groupe1[compteurGr] == "G2A":
                            module = getModule.decoupeTP(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y], niveau)
                        if groupe1[compteurGr] == "G2B":
                            module = getModule.decoupeTP(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y], niveau)
                        if groupe1[compteurGr] == "G3A":
                            module = getModule.decoupeTP(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y], niveau)
                        if groupe1[compteurGr] == "G3B":
                            module = getModule.decoupeTP(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y], niveau)
                        if (module!=""):
                            edt1[groupe1[compteurGr]][jour[CompteurJr]]["Cours"].append((module, "TP"))
                        else:
                            edt1[groupe1[compteurGr]][jour[CompteurJr]]["Cours"].append(("", ""))
                        print(heure,"- TP", groupe1[compteurGr],jour[CompteurJr])

                    if niveau == "A2":
                        if groupe2[compteurGr] == "G4A":
                            module = getModule.decoupeTP(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y], niveau)
                        if groupe2[compteurGr] == "G4B":
                            module = getModule.decoupeTP(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y],niveau)
                        if groupe2[compteurGr] == "G5A":
                            module = getModule.decoupeTP(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y], niveau)
                        if groupe2[compteurGr] == "G5B":
                            module = getModule.decoupeTP(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y], niveau)
                        if (module!=""):
                            edt2[groupe2[compteurGr]][jour[CompteurJr]]["Cours"].append((module, "TP"))
                        else:
                            edt2[groupe2[compteurGr]][jour[CompteurJr]]["Cours"].append(("", ""))
                        print(heure,"- TP", groupe2[compteurGr],jour[CompteurJr])

                    if niveau == "A3":
                        if groupe3[compteurGr] == "L1A":
                            module = getModule.decoupeTP(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y], niveau)
                        if groupe3[compteurGr] == "L1B":
                            module = getModule.decoupeTP(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y],niveau)
                        if (module!=""):
                            edt3[groupe3[compteurGr]][jour[CompteurJr]]["Cours"].append((module, "TP"))
                        else:
                            edt3[groupe3[compteurGr]][jour[CompteurJr]]["Cours"].append(("", ""))
                        print(heure,"- TP", groupe3[compteurGr],jour[CompteurJr])

#  ------- Cours de partiel ------
                elif getColor(pipette1, pipette2, pipette3, pipette4, pipette5) == "Violet":
                    if niveau == "A1":
                        if groupe1[compteurGr] == "G1A":
                            module = getModule.decoupeTD(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y], niveau)
                        if groupe1[compteurGr] == "G1B":
                            module = getModule.decoupeTD(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y-1], niveau)
                        if groupe1[compteurGr] == "G2A":
                            module = getModule.decoupeTD(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y], niveau)
                        if groupe1[compteurGr] == "G2B":
                            module = getModule.decoupeTD(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y-1], niveau)
                        if groupe1[compteurGr] == "G3A":
                            module = getModule.decoupeTD(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y], niveau)
                        if groupe1[compteurGr] == "G3B":
                            module = getModule.decoupeTD(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y-1], niveau)
                        if (module!=""):
                            edt1[groupe1[compteurGr]][jour[CompteurJr]]["Cours"].append((module, "Partiel"))
                        else:
                            edt1[groupe1[compteurGr]][jour[CompteurJr]]["Cours"].append(("", ""))
                        print(heure, "- PARTIEL", groupe1[compteurGr],jour[CompteurJr])

                    if niveau == "A2":
                        if groupe2[compteurGr] == "G4A":
                            module = getModule.decoupeTD(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y], niveau)
                        if groupe2[compteurGr] == "G4B":
                            module = getModule.decoupeTD(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y-1],niveau)
                        if groupe2[compteurGr] == "G5A":
                            module = getModule.decoupeTD(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y], niveau)
                        if groupe2[compteurGr] == "G5B":
                            module = getModule.decoupeTD(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y-1], niveau)
                        if (module!=""):
                            edt2[groupe2[compteurGr]][jour[CompteurJr]]["Cours"].append((module, "Partiel"))
                        else:
                            edt2[groupe2[compteurGr]][jour[CompteurJr]]["Cours"].append(("", ""))
                        print(heure, "- PARTIEL", groupe2[compteurGr],jour[CompteurJr])

                    if niveau == "A3":
                        if groupe3[compteurGr] == "L1A":
                            module = getModule.decoupeTD(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y], niveau)
                        if groupe3[compteurGr] == "L1B":
                            module = getModule.decoupeTD(edtImage, ecriture.pipetteCoordonnees[niveau]["X"][x], ecriture.pipetteCoordonnees[niveau]["Y"][y-1],niveau)
                        if (module!=""):
                            edt3[groupe3[compteurGr]][jour[CompteurJr]]["Cours"].append((module, "Partiel"))
                        else:
                            edt3[groupe3[compteurGr]][jour[CompteurJr]]["Cours"].append(("", ""))
                        print(heure," - PARTIEL ", groupe3[compteurGr],jour[CompteurJr])

                elif getColor(pipette1, pipette2, pipette3, pipette4, pipette5) == "None":
                    if niveau == "A1":
                        edt1[groupe1[compteurGr]][jour[CompteurJr]]["Cours"].append("[ERROR: Pipette]")
                        print(heure," - [ERROR: Pipette]", groupe1[compteurGr],jour[CompteurJr])

                    if niveau == "A2":
                        edt2[groupe2[compteurGr]][jour[CompteurJr]]["Cours"].append("[ERROR: Pipette]")
                        print(heure," - [ERROR: Pipette]", groupe2[compteurGr],jour[CompteurJr])

                    if niveau == "A3":
                        edt3[groupe3[compteurGr]][jour[CompteurJr]]["Cours"].append("[ERROR: Pipette]")
                        print(heure," - [ERROR: Pipette]", groupe3[compteurGr],jour[CompteurJr])
            h += 0.5

        if niveau == "A1":
            if compteurGr == 5:
                compteurGr = 0
                if CompteurJr == 5:
                    CompteurJr = 0
                else:
                    CompteurJr +=1
            else:
                compteurGr +=1

        if niveau == "A2":
            if compteurGr == 3:
                compteurGr = 0
                if CompteurJr == 5:
                    CompteurJr = 0
                else:
                    CompteurJr +=1
            else:
                compteurGr +=1

        if niveau == "A3":
            if compteurGr == 1:
                compteurGr = 0
                if CompteurJr == 5:
                    CompteurJr = 0
                else:
                    CompteurJr +=1
            else:
                compteurGr +=1
    if niveau == "A1":
        ecriture.ecrire(edt1)
    if niveau == "A2":
        ecriture.ecrire(edt2)
    if niveau == "A3":
        ecriture.ecrire(edt3)

def main(edtImage):
    name = edtImage.split("_")
    if name[0] == "A1":
        engine(edtImage, "A1")
    if name[0] == "A2":
        engine(edtImage, "A2")
    if name[0] == "A3":
        engine(edtImage, "A3")

main("A1_S28.jpg")