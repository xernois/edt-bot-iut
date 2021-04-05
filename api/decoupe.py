from PIL import Image

# =====================
# Fonction qui decoupe une image
# 
# Entree: Nom de l'image 
# Sortie: RIEN
# =====================
def decouper(image):
    im = Image.open(image)
    im_size = im.size
    origine = (208,216)
    fin = (2100, 216)
    width = 81
    height = 219
    i = 0
    for x in range (origine[0],fin[0],width):
        i += 1
        # Create Box
        box = (x, origine[1], x+width, origine[1]+height)
        # Crop Image
        area = im.crop(box)
        
        # Save Image
        nameImg = str("fond%s.jpg") % str(i)
        area.save(nameImg, "JPEG")