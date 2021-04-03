import datetime, json                                                                                   # import de json pour manipuler des json et de datetime pour manipuler des dates
from selenium import webdriver                                                                          # import des webdrivers depuis la librairy selenium
from selenium.webdriver.common import keys                                                              # 



class Edt():                                                                                            # Definition de l'objet Edt qui a pour attribut un nom une date et une taille
    def __init__(self, nom, date, taille):                                                              # constructeur 3 parametre
        self.nom = nom                                                                                  #
        self.date = date                                                                                #
        self.taille = taille                                                                            #
    def info_json(self):                                                                                # Methode pour retourner les infos de l'Edt sous forme de JSON
        return {'nom': self.nom,'date':self.date.strftime("%Y-%m-%d %H:%M"),'taille':self.taille}       # info sous forme de js avec la date au format (Annee-Mois-Jour Heure:Minutes)



def download_edt():
    print('existe po')



def fetch_edt():                                                                                        # fonction pour recuperer tout les edts 
    driver = webdriver.Firefox(executable_path="C:\\Program Files\\browser_Driver\\geckodriver.exe")    # creation d'un nouveau driver pour naviguer sur internet
    driver.minimize_window()                                                                            # reduction du navigateuur pour pas le voir sur l'ecrans
    driver.get("http://edt-iut-info.unilim.fr/edt/")                                                    # recupere le contenu de la page internet
    folders = driver.find_elements_by_xpath("/html/body/table/tbody/tr")                                # recuperer la liste des dossier contenant des edts sur le site
    for i in range(0, len(folders)):                                                                    # boucle sur le nombre de dossier pour recuperer les edts present dans chaque dossier 
        info = folders[i].text.split(" ")                                                               # recuperation du nom du dossier pour rentrer dedans 
        if(info[0].startswith('A')):                                                                    # 
            driver.get("http://edt-iut-info.unilim.fr/edt/"+info[0])                                    # le driver charge un des dossier contenant les edts 
            edts = driver.find_elements_by_xpath("/html/body/table/tbody/tr")                           # le driver recupere la liste des edts
            list_edt = []                                                                               #
            for j in range(3, len(edts)-1):                                                             # boucle sur la liste des edts dans le dossier courrant
                info_edt = edts[j].text.split(" ")                                                      # le texte est couper pour en recuperer des données
                date_edt = [int(data) for data in info_edt[1].split("-")]                               # recuperation des données correspondant a la date de publication
                heure_edt = [int(data) for data in info_edt[2].split(":")]                              # recuperation des données correspondant a l'heure de publication
                date = datetime.datetime(date_edt[0],date_edt[1],date_edt[2],heure_edt[0],heure_edt[1]) # creation d'une date pour l'obj Edt
                list_edt.append(Edt(info_edt[0],date,info_edt[3]))                                      # creation d'un obj Edt pour chaques edts, cet obj est stocker dans la liste list_edt 
            driver.back()                                                                               # le driver fais un retour en arriere pour revenir a la page avec la liste des dossier contenant les edts
            print(info[0]+":")                                                                          # affichage du nom du repertoire contenant les edts
            for edt in list_edt:                                                                        # boucle sur le nombre d'obj Edt
                try:
                    with open(edt.nom.split('.')[0]+'.json') as f:
                        print(f.readlines())
                except IOError:
                    download_edt()
                print(edt.info_json())                                                                  # print le text retourner par la methode info_json() de l'obj Edt
            print("\n\n")                                                                               #
    driver.quit()                                                                                       # fermeture du driver


fetch_edt()                                                                                            # appel de la fonction fetch_edt pour   