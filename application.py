from tkinter import ttk
import donnees, presentation
class Application:
    def __init__(self, semaine, jour, groupe):
        self.__semaine = semaine
        self.__jour = jour
        self.__groupe = groupe
        
    
    def validationMenu(self):
        semaineValide, jourValide, groupeValide, erreurSaisi = False, False, False, ""
        print("================")
        print("L'utilisateur a selectionné la semaine " + self.__semaine())
        print("L'utilisateur a selectionné le jour " + self.__jour())
        print("L'utilisateur a selectionné le groupe " + self.__groupe())
        if ((self.__semaine() == "Numero de la Semaine") or (self.__jour() == "Jour") or (self.__groupe() == "Nom du Groupe")):
            print("Veuillez selectionner les tous les parametres")
            erreurSaisi = "incomplet"
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
                print("Une erreur de selection de parametre detecté")
                erreurSaisi = "saisi"
                return ("saisi")
        erreurSaisi = ""
        return ("")
    
    def generationEdt(self, edt):
        posY = 25
        indice = 0
        font = ("Calibri", 14)
        print(" ===========================================================")
        for i in donnees.data["heure"]:
            posY += 20
            lbheure = ttk.Label(text=donnees.data["heure"][indice]+" - "+edt[self.presentation.IHM.getGroupe()][self.presentation.IHM.getJour()]["Cours"][indice], font=font, background="#fff", foreground="#0a385a" )
            lbheure.place(x=100, y=posY)
            indice += 1