import datetime
from selenium import webdriver
from selenium.webdriver.common import keys

class Edt():
    def __init__(self, nom, date, taille):
        self.nom = nom
        self.date = date
        self.taille = taille
    def info_json(self):
        return {'nom': self.nom,'date':self.date.strftime("%Y-%m-%d %H:%M"),'taille':self.taille}

driver = webdriver.Firefox(executable_path="C:\\Program Files\\browser_Driver\\geckodriver.exe")
driver.minimize_window()
driver.get("http://edt-iut-info.unilim.fr/edt/")
folders = driver.find_elements_by_xpath("/html/body/table/tbody/tr")
for i in range(0, len(folders)):
    info = folders[i].text.split(" ")
    if(info[0].startswith('A')):
        driver.get("http://edt-iut-info.unilim.fr/edt/"+info[0])
        edts = driver.find_elements_by_xpath("/html/body/table/tbody/tr")
        list_edt = []
        for j in range(3, len(edts)-1):
            infoEdt = edts[j].text.split(" ")
            dateEdt = [int(data) for data in infoEdt[1].split("-")]
            heureEdt = [int(data) for data in infoEdt[2].split(":")]
            date = datetime.datetime(dateEdt[0],dateEdt[1],dateEdt[2],heureEdt[0],heureEdt[1])
            list_edt.append(Edt(infoEdt[0],date,infoEdt[3]))
        driver.back()
        print(info[0]+":")
        for edt in list_edt:
            print(edt.info_json())
        print("\n\n")
driver.quit()