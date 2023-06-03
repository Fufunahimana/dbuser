from tkinter import *
from tkinter import ttk, messagebox
import tempfile
import random
from PIL import ImageTk, Image
from tkcalendar import *
import mysql.connector
import os

class Forage2(Frame):
    def __init__(self):
        super().__init__()
        self.config(bg="silver")
     
        ##########################LES LISTES UTILISEES##############################

        latlong_meth = ["GPS","Carte","DGPS","Rapport"]
        altitude_meth = ["GPS","Carte","DGPS","Modèle Numérique de Terrain","Nivelement","Rapport"]
        type_PE = ["Forage","Puit","Source"]

        Meth_Foration= ["Manuel","MFT","Mixte (Rotatio&MFT)","Odex","Rotation"]
        Meth_dev = ["Airlift","Injection d'eau","Soufflage"]
        Utilisation_eau = ["Boisson","Indistrielle","Irrigation","Pas Utilisée","Piezomètre"]
        QUalit_Apparent = ["Autre","Blanchâtre","Jaunâtre","Noir","Pas de couleur","Rouge orangé ou Marron"]
        Etat_PE= ["Fonctionnel","Non Fonctionnel"]
        Utilisation_Forg = ["Exploitation","Piézomètre","Reconnaissance"]
        Typ_equ = ["Aucun","Pompe Eléctrique ","Pompe Manuelle","Logger"]
        Type_aqui = ["Fracturé","Poreux","Poreux et Fracturé"]



        #scroll_x = Scrollbar(self, orient=HORIZONTAL)
        scroll_y = Scrollbar(self, orient=VERTICAL)
        scroll_y.place(x=0, y=0, height=1000)
        #scroll_y.place(side=RIGHT)

        #scroll_x.config(command=self.tabl_result.xview)
        #scroll_y.config(command=self.yview)
        #self.config(yscrollcommand=scroll_y.set)



        ForationFrame = LabelFrame(self, text="Foration", font=("times new roman",15),bg="white")
        ForationFrame.place(x=15, y=10, width=450, height=180)
        
        self.lbl_Entr_forg = Label(ForationFrame, text="Entreprise Forage :", font=("times new roman",10), bg="white")
        self.lbl_Entr_forg.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.txt_coord = ttk.Entry(ForationFrame, font=("times new roman",10))
        self.txt_coord.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        self.lbl_DatFor = Label(ForationFrame, text="Date Fin Foration :", font=("times new roman",10), bg="white")
        self.lbl_DatFor.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.ecri_DatFor = DateEntry(ForationFrame, font=("times new roman", 10), bg="lightyellow", state="readonly", locale='fr_FR',date_pattern = 'dd/mm/yyyy')
        self.ecri_DatFor.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        self.lbl_MethFor = Label(ForationFrame, text="Méthode  Foration:", font=("times new roman",10), bg="white")
        self.lbl_MethFor.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.txt_MethFor= ttk.Combobox(ForationFrame, font=("times new roman",10),values= Meth_Foration, state="readonly")
        self.txt_MethFor.grid(row=2, column=1, sticky=W, padx=5, pady=2)
        self.txt_MethFor.current(0)

        self.lbl_MethDev = Label(ForationFrame, text="Méthode de Développement :", font=("times new roman",10), bg="white")
        self.lbl_MethDev.grid(row=3, column=0, sticky=W, padx=5, pady=2)

        self.txt_MethDev = ttk.Combobox(ForationFrame, font=("times new roman",10),values= Meth_dev, state="readonly")
        self.txt_MethDev.grid(row=3, column=1, sticky=W, padx=5, pady=2)
        self.txt_MethDev.current(0)

        self.lbl_DirDev = Label(ForationFrame, text="Durée de Développement :", font=("times new roman",10), bg="white")
        self.lbl_DirDev.grid(row=4, column=0, sticky=W, padx=5, pady=2)

        self.txt_DirDev = ttk.Entry(ForationFrame, font=("times new roman",10))
        self.txt_DirDev.grid(row=4, column=1, sticky=W, padx=5, pady=2)

        self.lbl_ProfFor = Label(ForationFrame, text="Profondeur Forage :", font=("times new roman",10), bg="white")
        self.lbl_ProfFor.grid(row=5, column=0, sticky=W, padx=5, pady=2)

        self.txt_ProfFor = ttk.Entry(ForationFrame, font=("times new roman",10))
        self.txt_ProfFor.grid(row=5, column=1, sticky=W, padx=5, pady=2)

        ###############Condition d'un forage##########################

        CondtionFrame = LabelFrame(self, text="Condition", font=("times new roman",15),bg="white")
        CondtionFrame.place(x=15, y=190, width=450, height=130)
        
        self.lbl_Haut_tt_Forag = Label(CondtionFrame, text="Hauteur Tête Forage :", font=("times new roman",10), bg="white")
        self.lbl_Haut_tt_Forag.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.txt_Haut_tt_Forag = ttk.Entry(CondtionFrame, font=("times new roman",10))
        self.txt_Haut_tt_Forag.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        self.lbl_EtatPE = Label(CondtionFrame, text="Etat Point d'Eau :", font=("times new roman",10), bg="white")
        self.lbl_EtatPE.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.txt_EtatPE = ttk.Combobox(CondtionFrame, font=("times new roman",10),values= Etat_PE, state="readonly")
        self.txt_EtatPE.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        self.txt_EtatPE.current(0)

        self.lbl_UtilisFor = Label(CondtionFrame, text="Utilisation Forage :", font=("times new roman",10), bg="white")
        self.lbl_UtilisFor.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.txt_UtilisFor = ttk.Combobox(CondtionFrame, font=("times new roman",10),values= Utilisation_Forg, state="readonly")
        self.txt_UtilisFor.grid(row=2, column=1, sticky=W, padx=5, pady=2)
        self.txt_UtilisFor.current(0)

        self.lbl_Typ_Equi = Label(CondtionFrame, text="Type Equipement :", font=("times new roman",10), bg="white")
        self.lbl_Typ_Equi.grid(row=3, column=0, sticky=W, padx=5, pady=2)

        self.txt_Typ_Equi = ttk.Combobox(CondtionFrame, font=("times new roman",10),values= Typ_equ,state="readonly")
        self.txt_Typ_Equi.grid(row=3, column=1, sticky=W, padx=5, pady=2)
        self.txt_Typ_Equi.current(0)

        ################Administration##################
        
        AdmFrame = LabelFrame(self, text="Administration", font=("times new roman",15),bg="white")
        AdmFrame.place(x=15, y=320, width=450, height=125)
        
        self.lbl_Superv_W = Label(AdmFrame, text="Superviseur Travaux :", font=("times new roman",12), bg="white")
        self.lbl_Superv_W.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.txt_Superv_W = ttk.Entry(AdmFrame, font=("times new roman",12))
        self.txt_Superv_W.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        self.lbl_Propriet = Label(AdmFrame, text="Proprietaire :", font=("times new roman",12),bg="white")
        self.lbl_Propriet.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.txt_Propriet = ttk.Entry(AdmFrame, font=("times new roman",12))
        self.txt_Propriet.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        self.lbl_SupervInd = Label(AdmFrame, text="Supervision indépendante :", font=("times new roman",12),bg="white")
        self.lbl_SupervInd.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        btn_Superv =ttk.Checkbutton(AdmFrame,text="vraie")
        btn_Superv.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        ##################Hydrologie###################

        HydrFrame = LabelFrame(self, text="Hydrologie", font=("times new roman",15),bg="white")
        HydrFrame.place(x=465, y=10, width=470, height=225)

        self.lbl_UtilisEau = Label(HydrFrame, text="Utilisation Eau :", font=("times new roman",10), bg="white")
        self.lbl_UtilisEau.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.txt_UtilisEau = ttk.Combobox(HydrFrame, font=("times new roman",10),values= Utilisation_eau, state="readonly")
        self.txt_UtilisEau.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.txt_UtilisEau.current(0)

        self.lbl_Qual_app_eau = Label(HydrFrame, text="Qualité Apparente eau :", font=("times new roman",10), bg="white")
        self.lbl_Qual_app_eau.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.txt_Qual_app_eau = ttk.Combobox(HydrFrame, font=("times new roman",10),values= QUalit_Apparent, state="readonly")
        self.txt_Qual_app_eau.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        self.txt_Qual_app_eau.current(0)

        self.lbl_Niv_stat = Label(HydrFrame, text="Niveau Statique :", font=("times new roman",12),bg="white")
        self.lbl_Niv_stat.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.txt_Niv_stat = ttk.Entry(HydrFrame, font=("times new roman",12))
        self.txt_Niv_stat.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        self.lbl_Débit_Unit = Label(HydrFrame, text="Débit Unitiale :", font=("times new roman",12),bg="white")
        self.lbl_Débit_Unit.grid(row=3, column=0, sticky=W, padx=5, pady=2)

        self.txt_Débit_Unit = ttk.Entry(HydrFrame, font=("times new roman",12))
        self.txt_Débit_Unit.grid(row=3, column=1, sticky=W, padx=5, pady=2)
        
        self.lbl_NIv_dyn = Label(HydrFrame, text="Niveau Dynamique :", font=("times new roman",12),bg="white")
        self.lbl_NIv_dyn.grid(row=4, column=0, sticky=W, padx=5, pady=2)

        self.txt_NIv_dyn = ttk.Entry(HydrFrame, font=("times new roman",12))
        self.txt_NIv_dyn.grid(row=4, column=1, sticky=W, padx=5, pady=2)

        self.lbl_Cond_init = Label(HydrFrame, text="Condictivité Unitiale :", font=("times new roman",12),bg="white")
        self.lbl_Cond_init.grid(row=5, column=0, sticky=W, padx=5, pady=2)

        self.txt_Cond_init = ttk.Entry(HydrFrame, font=("times new roman",12))
        self.txt_Cond_init.grid(row=5, column=1, sticky=W, padx=5, pady=2)
        
        self.lbl_Typ_Aquif = Label(HydrFrame, text="Type d'Aquifère :", font=("times new roman",10), bg="white")
        self.lbl_Typ_Aquif.grid(row=6, column=0, sticky=W, padx=5, pady=2)

        self.txt_Typ_Aquif = ttk.Combobox(HydrFrame, font=("times new roman",10),values= Type_aqui, state="readonly")
        self.txt_Typ_Aquif.grid(row=6, column=1, sticky=W, padx=5, pady=2)
        self.txt_Typ_Aquif.current(0)
        
        ######################Attribites##################################
        
        AttrFrame = LabelFrame(self, text="Attributes", font=("times new roman",15),bg="white")
        AttrFrame.place(x=465, y=235, width=470, height=210)
        
        self.lbl_Rmq = Label(AttrFrame, text="Remarque :", font=("times new roman",12),bg="white")
        self.lbl_Rmq.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.txt_Rmq = Text(AttrFrame, font=("times new roman",12),width=20,height=5, relief=RAISED)
        self.txt_Rmq.grid(row=0, column=1, sticky=W, padx=5, pady=5)
        
        self.lbl_der_dat_modif = Label(AttrFrame, text="Dérnière Date de modification :", font=("times new roman",12,"bold"),bg="white")
        self.lbl_der_dat_modif.grid(row=1, column=0, sticky=W, padx=5, pady=2)
        
        self.txt_der_dat_modif = ttk.Entry(AttrFrame, font=("times new roman",12))
        self.txt_der_dat_modif.grid(row=1, column=1, sticky=W, padx=15, pady=2)
        
        self.lbl_der_modif_par = Label(AttrFrame, text="Dérnière modification par :", font=("times new roman",12,"bold"),bg="white")
        self.lbl_der_modif_par.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.txt_der_modif_par = ttk.Entry(AttrFrame, font=("times new roman",12))
        self.txt_der_modif_par.grid(row=2, column=1, sticky=W, padx=15, pady=2)

        #Update_btn = Button( self, text="Update",cursor="hand2", font=("Times new roman",12, "bold"), bd=0, bg="silver", fg="black", relief=SUNKEN)
        #Update_btn.grid(sticky=W, padx=15, pady=2)

        #Abort_btn = Button(self, text="Annuler",cursor="hand2", font=("Times new roman",12, "bold"), bd=0, bg="silver", fg="black", relief=SUNKEN)
        #Abort_btn.grid(sticky=W, padx=15, pady=2)
    

        



if __name__ =="__main__":
    w=Forage2()
    w.mainloop()
