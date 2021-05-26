from tkinter import ttk
import donnees, presentation
class Application:
    def __init__(self, semaine, jour, groupe):
        self.__semaine = semaine
        self.__jour = jour
        self.__groupe = groupe
        
    
    def validationMenu(self):
        semaineValide, jourValide, groupeValide, erreurSaisi = False, False, False, ""
        if ((self.__semaine() == "Numero de la Semaine") or (self.__jour() == "Jour") or (self.__groupe() == "Nom du Groupe")):
            return ("incomplet")
        else:
            for i in donnees.data["semaine"]:
                if (self.__semaine() == i):
                    semaineValide = True
                    break

            for i in donnees.data["jour"]:
                if (self.__jour() == i):
                    jourValide = True
                    break

            for i in donnees.data["groupe"]:
                if (self.__groupe() == i):
                    groupeValide = True
                    break
            if ((not semaineValide) or (not jourValide) or (not groupeValide)):
                return ("saisi")
        return ("")
    
    