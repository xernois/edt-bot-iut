from PIL import Image
import ecriture, decoupe

# =====================
# Fonction qui detect si une couleur est dans un intervalle
# 
# Entree: 3 tuples de couleurs au format (RVB)
# Sortie: Booleen
# =====================
def intervalleCouleur(cdColor,borneInf, borneSup):
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
def engine(edtImage):
    im = Image.open(edtImage)
    # imgScinde = ["fond1.jpg","fond2.jpg","fond3.jpg","fond4.jpg","fond5.jpg","fond6.jpg","fond7.jpg","fond8.jpg","fond9.jpg","fond10.jpg","fond11.jpg",
    # "fond12.jpg","fond13.jpg","fond14.jpg","fond15.jpg","fond16.jpg","fond17.jpg","fond18.jpg","fond19.jpg","fond20.jpg","fond21.jpg","fond22.jpg","fond23.jpg","fond24.jpg"]
    compteur = 1
    height = 5
    width = 79

    # Dictionnaire de données
    edt = {"G1A" : {"Lundi" : {"Cours" :  []},"Mardi" : {"Cours" :  []},"Mercredi" : {"Cours" :  []},"Jeudi" : {"Cours" :  []},"Vendredi" : {"Cours" :  []},"Samedi" : {"Cours" :  []}},
        "G1B" : {"Lundi" : {"Cours" :  [] }, "Mardi" : { "Cours" :  []},"Mercredi" : {"Cours" :  []},"Jeudi" : {"Cours" :  []},"Vendredi" : {"Cours" :  []},"Samedi" : {"Cours" :  []}},
        "G2A" : {"Lundi" : {"Cours" :  [] }, "Mardi" : { "Cours" :  []},"Mercredi" : {"Cours" :  []},"Jeudi" : {"Cours" :  []},"Vendredi" : {"Cours" :  []},"Samedi" : {"Cours" :  []}},
        "G2B" : {"Lundi" : {"Cours" :  [] }, "Mardi" : { "Cours" :  []},"Mercredi" : {"Cours" :  []},"Jeudi" : {"Cours" :  []},"Vendredi" : {"Cours" :  []},"Samedi" : {"Cours" :  []}},
        "G3A" : {"Lundi" : {"Cours" :  [] }, "Mardi" : {"Cours" :  []}, "Mercredi" : {"Cours" :  []},"Jeudi" : {"Cours" :  []},"Vendredi" : {"Cours" :  []},"Samedi" : {"Cours" :  []}},
        "G3B" : {"Lundi" : {"Cours" :  [] }, "Mardi" : {"Cours" :  []}, "Mercredi" : {"Cours" :  []},"Jeudi" : {"Cours" :  []},"Vendredi" : {"Cours" :  []},"Samedi" : {"Cours" :  []}}}


    groupe = ["G1A","G1B","G2A","G2B","G3A","G3B"]
    jour = ["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi"]
    compteurGr = 0
    CompteurJr = 0
    compteurY = 1
    for y in range (0,len(ecriture.Y1),1): 
        h = 8
        for x in range (0,len(ecriture.X1)-1,1):

            compteur += 1
            pipette1 = im.getpixel((ecriture.X1[x],ecriture.Y1[y]))
            pipette2 = im.getpixel((ecriture.X2[x],ecriture.Y1[y]))
            pipette3 = im.getpixel((ecriture.X1[x],ecriture.Y2[y]))
            pipette4 = im.getpixel((ecriture.X2[x],ecriture.Y2[y]))
            pipette5 = im.getpixel((ecriture.speX[x],ecriture.speY[y]))
            if (int(h)==h):
                heure = str(int(h)) +"h00"
            else:
                heure = str(int(h)) +"h30"

            if getColor(pipette1, pipette2, pipette3, pipette4, pipette5) == "Rose":
                edt[groupe[compteurGr]][jour[CompteurJr]]["Cours"].append("")
                print(heure," - ", groupe[compteurGr],jour[CompteurJr])
            else:
                if getColor(pipette1, pipette2, pipette3, pipette4, pipette5) == "Jaune":
                    edt[groupe[compteurGr]][jour[CompteurJr]]["Cours"].append("[Cours Magistral]")
                    print(heure," - [Cours Magistral] ", groupe[compteurGr],jour[CompteurJr])

                elif getColor(pipette1, pipette2, pipette3, pipette4, pipette5) == "Beige":
                    edt[groupe[compteurGr]][jour[CompteurJr]]["Cours"].append("[Travaux Diriges]")
                    print(heure," - [Travaux Diriges]", groupe[compteurGr],jour[CompteurJr])

                elif getColor(pipette1, pipette2, pipette3, pipette4, pipette5) == "Bleu":
                    edt[groupe[compteurGr]][jour[CompteurJr]]["Cours"].append("[Travaux Pratique]")
                    print(heure," - [Travaux Pratique]", groupe[compteurGr],jour[CompteurJr])

                elif getColor(pipette1, pipette2, pipette3, pipette4, pipette5) == "Violet":
                    edt[groupe[compteurGr]][jour[CompteurJr]]["Cours"].append("[Partiel]")
                    print(heure," - [Partiel]", groupe[compteurGr],jour[CompteurJr])

                elif getColor(pipette1, pipette2, pipette3, pipette4, pipette5) == "None":
                    edt[groupe[compteurGr]][jour[CompteurJr]]["Cours"].append("[ERROR: Pipette]")
                    print(heure," - [ERROR: Pipette]", groupe[compteurGr],jour[CompteurJr])
            h += 0.5

        if compteurGr == 5:
            compteurGr = 0
            if CompteurJr == 5:
                CompteurJr = 0
            else:
                CompteurJr +=1
        else:
            compteurGr +=1
        
    ecriture.ecrire(edt, edtImage)

def main(edtImage):
    engine(edtImage)
    #decoupe.decouper(edtImage)

# main("A1_S28.jpg")