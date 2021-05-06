import os
from tkinter import *
from tkinter import ttk
import donnees, application

LARGEUR = 800
HAUTEUR = 600
LARGEUR_MENU = 200
POSITION_X = 400
POSITION_Y = 150

class IHM:
    def __init__(self):
        self.fenetre = Tk()
        self.fenetre.title("Application EDT")
        taille = (str(LARGEUR)+"x"+str(HAUTEUR)+"+"+str(POSITION_X)+"+"+str(POSITION_Y))
        self.fenetre.geometry(taille)
        self.fenetre.resizable(False, False)
    
    def creationWidget(self):
        txtFont = ("Calibri", 18, "bold")
        self.containerMenu(txtFont)
        self.containerEdt()
        self.fenetre.mainloop()

    def containerEdt(self):
        txtFont = ("Calibri", 14, "bold")
        self.edt = Frame(self.fenetre, background="#fff",width=LARGEUR-LARGEUR_MENU, height=HAUTEUR)
        self.labelEdt = ttk.Label(self.edt, text="EDT",background="#fff", font=txtFont, foreground="#b10117")
        self.labelEdt.place(x=250,y=10)
        self.edt.place(x=0,y=0)

    def erreurParametre(self, typeError):
        if typeError == "saisi":
            self.labelErreurParametre.config(text="Saisi des parametres invalides")
        if typeError == "incomplet":
            self.labelErreurParametre.config(text="Saisi des parametres incompletes")
        if typeError == "":
            self.labelErreurParametre.config(text="")
            self.majTitre()
            edt15214 = donnees.lecteurEDT(donnees.data["codeSemaine"], self.getIndice())
            print(edt15214)
            posY = 25
            indice = 0
            font = ("Calibri", 14)
            print(" ===========================================================")
            if (edt15214!=False):
                for i in donnees.data["heure"]:
                    posY += 20
                    lbheure = ttk.Label(text=donnees.data["heure"][indice]+" - "+str(edt15214[self.getGroupe()][self.getJour()]["Cours"][indice]), font=font, background="#fff", foreground="#0a385a" )
                    lbheure.place(x=100, y=posY)
                    indice += 1
            

    def majTitre(self):
        titre = ("EDT - "+ self.getSemaine() +" , "+ self.getJour() +" , "+self.getGroupe())
        self.labelEdt.config(text=titre)
        self.labelEdt.place(x=175,y=10)
    
    def getIndice(self):
        indice = donnees.data["semaine"].index(self.getSemaine())
        return indice

    def getSemaine(self):
        return self.listeSemaine.get()

    def getJour(self):
        return self.listeJour.get()

    def getGroupe(self):
        return self.listeGroupe.get()

    def getValidation(self):
        validation = application.Application(self.getSemaine, self.getJour,self.getGroupe)
        self.erreurParametre(validation.validationMenu())

    def containerMenu(self, txtFont):
        menu = Frame(self.fenetre, background="#b10117", width=LARGEUR_MENU, height=HAUTEUR)
        self.labelMenu = ttk.Label(menu, text="Menu",background="#b10117", font=txtFont, foreground="#ffffff")
        self.labelMenu.place(x=65,y=80)

        self.labelErreurParametre = ttk.Label(menu, text="",background="#b10117", foreground="#fff")
        self.labelErreurParametre.place(x=10,y=107)

        self.listeSemaine = ttk.Combobox(menu, values=donnees.data["semaine"])
        self.listeSemaine.set("Numero de la Semaine")
        self.listeSemaine.place(x=25,y=125)

        self.listeGroupe = ttk.Combobox(menu, values=donnees.data["groupe"])
        self.listeGroupe.set("Nom du Groupe")
        self.listeGroupe.place(x=25,y=175)

        self.listeJour = ttk.Combobox(menu, values=donnees.data["jour"])
        self.listeJour.set("Jour")
        self.listeJour.place(x=25,y=225)

        self.style = ttk.Style()
        self.style.configure('W.TButton', foreground='#0a385a')
        self.btnValide = ttk.Button(menu, style='W.TButton', text="Valider", command=self.getValidation)
        self.btnValide.place(x=60,y=275)
        menu.place(x=LARGEUR-LARGEUR_MENU,y=0)

if __name__ == '__main__':
    app = IHM()
    app.creationWidget()