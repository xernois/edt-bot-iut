from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract' #IMPORTANT Appel le chemin pour la librairie pytesseract

numeroModule = ["M1102","M1103","M3103","M1101","M2101","M2102","M3101","M3102","M4101C","M4102C","M1105","M3104","M4103C","M4104C","M1104","2106","M3106","M2103","M2104","M2105","M2204","M3105","M3301","M4102C","M4105C","M1201","M1202","M2201","M2202","M3201","M3202C","M4202C","M1203","M1204","M2203","M2204","M3203","M3301","M4201C","M1105","M1205","M2205","M3205","M4203","M1206","M2206","M3206","M4204"]

def reconnaissanceModule(nom):
    listeCara = []
    strCara = ""
    for i in nom:
        different = True
        if i == '-':
            different = False
        if i == '‘':
            different = False
        if i == '\x0c':
            different = False
        if i == '.':
            different = False
        if i == 'P':
            different = False
        if i == 'n':
            different = False
        if i == '\n':
            different = False
        if  i == '\f':
            different = False
        if i =='—':
            different = False

        if different:
            listeCara.append(i)
    for j in listeCara:
        strCara += j

    return strCara

# =====================
# Fonction qui recupere le numero du module
# 
# Entree: chaine saisi par l'OCR
# Sortie: chaine numéro du module
# ===================== 
def analyse(chaineOcr, annee):
    chaines = chaineOcr.split(" ")
    for mot in chaines:
        for lettre in mot:
            if annee == "A3":
                if lettre == "L":
                    return mot[:4]
            else:
                if lettre == "M":
                    return reconnaissanceModule(mot)
                if annee == "A2":
                    if lettre == "O":
                        return reconnaissanceModule(mot)
                    if lettre=="A":
                        return reconnaissanceModule(mot)

    return ""
    


# =====================
# Fonction qui scinde l'edt en cm
# 
# Entree: image entier et coordonnée ancrage
# Sortie: chaine de caractere
# =====================
def decoupeCM(image, pointeurX, pointeurY, niveau):
    image = Image.open(image)
    imageGris = image.convert('L')
    rogner = imageGris.crop((pointeurX,pointeurY,pointeurX+85,pointeurY+220)) #Faire un capture d'ecran par region
    module = analyse(pytesseract.image_to_string(rogner), niveau)
    return module #OCR image en nuance de gris

def decoupeTD(image, pointeurX, pointeurY, niveau):
    if niveau == 'A1':
        image = Image.open(image)
        imageGris = image.convert('L')
        rogner = imageGris.crop((pointeurX,pointeurY,pointeurX+85,pointeurY+74)) #Faire un capture d'ecran par region
        module = analyse(pytesseract.image_to_string(rogner), niveau)
        return module #OCR image en nuance de gris
    if niveau == 'A2':
        image = Image.open(image)
        imageGris = image.convert('L')
        rogner = imageGris.crop((pointeurX,pointeurY,pointeurX+85,pointeurY+108)) #Faire un capture d'ecran par region
        module = analyse(pytesseract.image_to_string(rogner), niveau)
        return module #OCR image en nuance de gris
    if niveau == 'A3':
        image = Image.open(image)
        imageGris = image.convert('L')
        rogner = imageGris.crop((pointeurX,pointeurY,pointeurX+85,pointeurY+220)) #Faire un capture d'ecran par region
        module = analyse(pytesseract.image_to_string(rogner), niveau)
        return module #OCR image en nuance de gris

def decoupeTP(image, pointeurX, pointeurY, niveau):
    if niveau == 'A1':
        image = Image.open(image)
        imageGris = image.convert('L')
        rogner = imageGris.crop((pointeurX,pointeurY,pointeurX+85,pointeurY+37)) #Faire un capture d'ecran par region
        module = analyse(pytesseract.image_to_string(rogner), niveau)
        return module #OCR image en nuance de gris

    if niveau == 'A2':
        image = Image.open(image)
        imageGris = image.convert('L')
        rogner = imageGris.crop((pointeurX,pointeurY,pointeurX+85,pointeurY+54)) #Faire un capture d'ecran par region
        module = analyse(pytesseract.image_to_string(rogner), niveau)
        return module #OCR image en nuance de gris

    if niveau == 'A3':
        image = Image.open(image)
        imageGris = image.convert('L')
        rogner = imageGris.crop((pointeurX,pointeurY,pointeurX+85,pointeurY+110)) #Faire un capture d'ecran par region
        module = analyse(pytesseract.image_to_string(rogner), niveau)
        return module #OCR image en nuance de gris
