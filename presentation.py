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
        self.fenetre.iconphoto(False, PhotoImage(file='./favicon.png'))
    
    def creationWidget(self):
        txtFont = ("Calibri", 18, "bold")
        self.containerMenu(txtFont)
        self.containerEdt()
        self.fenetre.mainloop()

    def containerEdt(self):
        txtFont = ("Calibri", 14, "bold")
        self.edt = Frame(self.fenetre, background="#fff",width=LARGEUR-LARGEUR_MENU, height=HAUTEUR)
        self.lbheure1 = ttk.Label(background="#fff")
        self.lbheure1.place(x=100, y=50)
        self.lbheure2 = ttk.Label(background="#fff")
        self.lbheure2.place(x=100, y=70)
        self.lbheure3 = ttk.Label(background="#fff")
        self.lbheure3.place(x=100, y=90)
        self.lbheure4 = ttk.Label(background="#fff")
        self.lbheure4.place(x=100, y=110)
        self.lbheure5 = ttk.Label(background="#fff")
        self.lbheure5.place(x=100, y=130)
        self.lbheure6 = ttk.Label(background="#fff")
        self.lbheure6.place(x=100, y=150)
        self.lbheure7 = ttk.Label(background="#fff")
        self.lbheure7.place(x=100, y=170)
        self.lbheure8 = ttk.Label(background="#fff")
        self.lbheure8.place(x=100, y=190)
        self.lbheure9 = ttk.Label(background="#fff")
        self.lbheure9.place(x=100, y=210)
        self.lbheure10 = ttk.Label(background="#fff")
        self.lbheure10.place(x=100, y=230)
        self.lbheure11 = ttk.Label(background="#fff")
        self.lbheure11.place(x=100, y=250)
        self.lbheure12 = ttk.Label(background="#fff")
        self.lbheure12.place(x=100, y=270)
        self.lbheure13 = ttk.Label(background="#fff")
        self.lbheure13.place(x=100, y=290)
        self.lbheure14 = ttk.Label(background="#fff")
        self.lbheure14.place(x=100, y=310)
        self.lbheure15 = ttk.Label(background="#fff")
        self.lbheure15.place(x=100, y=330)
        self.lbheure16 = ttk.Label(background="#fff")
        self.lbheure16.place(x=100, y=350)
        self.lbheure17 = ttk.Label(background="#fff")
        self.lbheure17.place(x=100, y=370)
        self.lbheure18 = ttk.Label(background="#fff")
        self.lbheure18.place(x=100, y=390)
        self.lbheure19 = ttk.Label(background="#fff")
        self.lbheure19.place(x=100, y=410)
        self.lbheure20 = ttk.Label(background="#fff")
        self.lbheure20.place(x=100, y=430)
        self.labelEdt = ttk.Label(self.edt, text="EDT",background="#fff", font=txtFont, foreground="#b10117")
        self.labelEdt.place(x=250,y=10)
        self.edt.place(x=0,y=0)

    def erreurParametre(self, typeError):
        erreurTrouve = False
        if typeError == "saisi":
            self.labelErreurParametre.config(text="Parametres invalides")
            self.labelErreurParametre.place(x=25,y=107)
            erreurTrouve = True
        if typeError == "incomplet":
            self.labelErreurParametre.config(text="Parametres incompletes")
            self.labelErreurParametre.place(x=25,y=107)
            erreurTrouve = True
        if typeError == "":
            self.labelErreurParametre.config(text="")
            self.majTitre()
            edt15214 = donnees.lecteurEDT(donnees.data["groupe"].index(self.getGroupe()), donnees.data["semaine"].index(self.getSemaine()))

        try:
            edt15214[self.getGroupe()]
            erreur = False
        except:
            if not (erreurTrouve):
                self.labelErreurParametre.config(text="EDT introuvable")
                self.labelErreurParametre.place(x=25,y=107)
                erreurTrouve = True
            erreur = True

        font = ("Calibri", 14)
        if not erreur:
            if (edt15214!=False):
                self.lbheure1.config(text=self.afficheModule(0,edt15214), font=font, background="#fff", foreground="#0a385a" )
                self.lbheure2.config(text=self.afficheModule(1,edt15214), font=font, background="#fff", foreground="#0a385a" )
                self.lbheure3.config(text=self.afficheModule(2,edt15214), font=font, background="#fff", foreground="#0a385a" )
                self.lbheure4.config(text=self.afficheModule(3,edt15214), font=font, background="#fff", foreground="#0a385a" )
                self.lbheure5.config(text=self.afficheModule(4,edt15214), font=font, background="#fff", foreground="#0a385a" )
                self.lbheure6.config(text=self.afficheModule(5,edt15214), font=font, background="#fff", foreground="#0a385a" )
                self.lbheure7.config(text=self.afficheModule(6,edt15214), font=font, background="#fff", foreground="#0a385a" )
                self.lbheure8.config(text=self.afficheModule(7,edt15214), font=font, background="#fff", foreground="#0a385a" )
                self.lbheure9.config(text=self.afficheModule(8,edt15214), font=font, background="#fff", foreground="#0a385a" )
                self.lbheure10.config(text=self.afficheModule(9,edt15214), font=font, background="#fff", foreground="#0a385a" )
                self.lbheure11.config(text=self.afficheModule(10,edt15214), font=font, background="#fff", foreground="#0a385a" )
                self.lbheure12.config(text=self.afficheModule(11,edt15214), font=font, background="#fff", foreground="#0a385a" )
                self.lbheure13.config(text=self.afficheModule(12,edt15214), font=font, background="#fff", foreground="#0a385a" )
                self.lbheure14.config(text=self.afficheModule(13,edt15214), font=font, background="#fff", foreground="#0a385a" )
                self.lbheure15.config(text=self.afficheModule(14,edt15214), font=font, background="#fff", foreground="#0a385a" )
                self.lbheure16.config(text=self.afficheModule(15,edt15214), font=font, background="#fff", foreground="#0a385a" )
                self.lbheure17.config(text=self.afficheModule(16,edt15214), font=font, background="#fff", foreground="#0a385a" )
                self.lbheure18.config(text=self.afficheModule(17,edt15214), font=font, background="#fff", foreground="#0a385a" )
                self.lbheure19.config(text=self.afficheModule(18,edt15214), font=font, background="#fff", foreground="#0a385a" )
                self.lbheure20.config(text=self.afficheModule(19,edt15214), font=font, background="#fff", foreground="#0a385a" )
            else:
                self.labelErreurParametre.config(text="Parametre(s) un correct")
                self.labelErreurParametre.place(x=25,y=107)
        else:
            self.lbheure1.config(text="", background="#fff")
            self.lbheure2.config(text="", background="#fff")
            self.lbheure3.config(text="", background="#fff")
            self.lbheure4.config(text="", background="#fff")
            self.lbheure5.config(text="", background="#fff")
            self.lbheure6.config(text="", background="#fff")
            self.lbheure7.config(text="", background="#fff")
            self.lbheure8.config(text="", background="#fff")
            self.lbheure9.config(text="", background="#fff")
            self.lbheure10.config(text="", background="#fff")
            self.lbheure11.config(text="", background="#fff")
            self.lbheure12.config(text="", background="#fff")
            self.lbheure13.config(text="", background="#fff")
            self.lbheure14.config(text="", background="#fff")
            self.lbheure15.config(text="", background="#fff")
            self.lbheure16.config(text="", background="#fff")
            self.lbheure17.config(text="", background="#fff")
            self.lbheure18.config(text="", background="#fff")
            self.lbheure19.config(text="", background="#fff")
            self.lbheure20.config(text="", background="#fff")
            if (not erreurTrouve):
                self.labelErreurParametre.config(text="Parametre(s) un correct")
                self.labelErreurParametre.place(x=25,y=107)
            
    def afficheModule(self, index, edt15214):
        
        if str(edt15214[self.getGroupe()][self.getJour()]["Cours"][index][0]) != "":
            return donnees.data["heure"][index]+" - "+str(edt15214[self.getGroupe()][self.getJour()]["Cours"][index][1])+" | "+str(edt15214[self.getGroupe()][self.getJour()]["Cours"][index][0])
        else:
            return donnees.data["heure"][index]+" - "

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