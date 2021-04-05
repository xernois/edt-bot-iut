import datetime, json, requests, pdf2image, os, main
from selenium import webdriver                                                                          # import des webdrivers depuis la librairy selenium
from selenium.webdriver.common import keys                                                              


def download_edt(file_name):
    pdf = requests.get('http://edt-iut-info.unilim.fr/edt/' + file_name, stream=True)
    pages = pdf2image.convert_from_bytes(pdf.raw.read())
    for page in pages:
        page.save('edt/'+file_name.split('/')[1].split('.')[0]+".jpg", 'JPEG')
        main.main('edt/'+file_name.split('/')[1].split('.')[0]+".jpg")
        if os.path.exists('edt/'+file_name.split('/')[1].split('.')[0]+".jpg"):
            os.remove('edt/'+file_name.split('/')[1].split('.')[0]+".jpg")


def fetch_edt():                                                                                        # fonction pour recuperer tout les edts 
    driver = webdriver.Firefox(executable_path="C:\\browser_driver\\geckodriver.exe")                   # creation d'un nouveau driver pour naviguer sur internet
    driver.minimize_window()                                                                            # reduction du navigateuur pour pas le voir sur l'ecrans
    driver.get("http://edt-iut-info.unilim.fr/edt/")                                                    # recupere le contenu de la page internet
    folders = driver.find_elements_by_xpath("/html/body/table/tbody/tr")                                # recuperer la liste des dossier contenant des edts sur le site
    for i in range(0, len(folders)):                                                                    # boucle sur le nombre de dossier pour recuperer les edts present dans chaque dossier 
        info = folders[i].text.split(" ")                                                               # recuperation du nom du dossier pour rentrer dedans 
        if(info[0].startswith('A')):                                                                    # 
            driver.get("http://edt-iut-info.unilim.fr/edt/"+info[0])                                    # le driver charge un des dossier contenant les edts 
            edts = driver.find_elements_by_xpath("/html/body/table/tbody/tr")                           # le driver recupere la liste des edts                                                                            #
            for j in range(3, len(edts) - 1):
                info_edt = edts[j].text.split(" ")                                                      # le texte est couper pour en recuperer des données
                date_edt = [int(data) for data in info_edt[1].split("-")]                               # recuperation des données correspondant a la date de publication
                heure_edt = [int(data) for data in info_edt[2].split(":")]                              # recuperation des données correspondant a l'heure de publication
                date = datetime.datetime(date_edt[0],date_edt[1],date_edt[2],heure_edt[0],heure_edt[1]) # creation d'une date pour l'obj Edt
                try:
                    with open('edt/' + info_edt[0].split('.')[0] + '.json') as f:
                        pass
                except IOError:
                    download_edt(info[0]+info_edt[0])
            driver.back()                                                                               # le driver fais un retour en arriere pour revenir a la page avec la liste des dossier contenant les edts                                                                       # affichage du nom du repertoire contenant les edts                                                                             #
    driver.quit()                                                                                       # fermeture du driver


fetch_edt()                                                                                             # appel de la fonction fetch_edt pour   