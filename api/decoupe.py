from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract' #IMPORTANT Appel le chemin pour la librairie pytesseract
# =====================
# Fonction qui decoupe une image
# 
# Entree: Nom de l'image 
# Sortie: RIEN
# =====================
# def decouperCM(image):
#     im = Image.open(image)
#     im_size = im.size
#     origine = (208,216)
#     fin = (2100, 216)
#     width = 81
#     height = 219
#     i = 0
#     for x in range (origine[0],fin[0],width):
#         i += 1
#         # Create Box
#         box = (x, origine[1], x+width, origine[1]+height)
#         # Crop Image
#         area = im.crop(box)
        
#         # Save Image
#         nameImg = str("fond%s.jpg") % str(i)
#         area.save(nameImg, "JPEG")

def decoupeCM(image, pointeurX, pointeurY, niveau):
    image = Image.open(image)
    imageGris = image.convert('L')
    rogner = imageGris.crop((pointeurX,pointeurY,pointeurX+85,pointeurY+220)) #Faire un capture d'ecran par region
    return pytesseract.image_to_string(rogner) #OCR image en nuance de gris

def decoupeTD(image, pointeurX, pointeurY, niveau):
    if niveau == 'A1':
        image = Image.open(image)
        imageGris = image.convert('L')
        rogner = imageGris.crop((pointeurX,pointeurY,pointeurX+85,pointeurY+74)) #Faire un capture d'ecran par region
        return pytesseract.image_to_string(rogner) #OCR image en nuance de gris
    if niveau == 'A2':
        image = Image.open(image)
        imageGris = image.convert('L')
        rogner = imageGris.crop((pointeurX,pointeurY,pointeurX+85,pointeurY+108)) #Faire un capture d'ecran par region
        return pytesseract.image_to_string(rogner) #OCR image en nuance de gris
    if niveau == 'A3':
        image = Image.open(image)
        imageGris = image.convert('L')
        rogner = imageGris.crop((pointeurX,pointeurY,pointeurX+85,pointeurY+220)) #Faire un capture d'ecran par region
        return pytesseract.image_to_string(rogner) #OCR image en nuance de gris

def decoupeTP(image, pointeurX, pointeurY, niveau):
    if niveau == 'A1':
        image = Image.open(image)
        imageGris = image.convert('L')
        rogner = imageGris.crop((pointeurX,pointeurY,pointeurX+85,pointeurY+37)) #Faire un capture d'ecran par region
        return pytesseract.image_to_string(rogner) #OCR image en nuance de gris

    if niveau == 'A2':
        image = Image.open(image)
        imageGris = image.convert('L')
        rogner = imageGris.crop((pointeurX,pointeurY,pointeurX+85,pointeurY+54)) #Faire un capture d'ecran par region
        return pytesseract.image_to_string(rogner) #OCR image en nuance de gris

    if niveau == 'A3':
        image = Image.open(image)
        imageGris = image.convert('L')
        rogner = imageGris.crop((pointeurX,pointeurY,pointeurX+85,pointeurY+110)) #Faire un capture d'ecran par region
        return pytesseract.image_to_string(rogner) #OCR image en nuance de gris