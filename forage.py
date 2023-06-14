from tkinter import *
from tkinter import ttk, messagebox
import tempfile
import random
from PIL import ImageTk, Image
from tkcalendar import *
import mysql.connector
import os

class Forage(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("NOUVEAU FORAGE")
        self.geometry("850x550+400+200")
        self.config(bg="silver")
        self.grab_set()
        self.resizable(0,0)
        
        ##########################LES LISTES UTILISEES##############################

        latlong_meth = ["GPS","Carte","DGPS","Rapport"]
        altitude_meth = ["GPS","Carte","DGPS","Modèle Numérique de Terrain","Nivelement","Rapport"]
        type_PE = ["Forage","Puit","Source"]

    

        CoordFrame = LabelFrame(self, text="Coordonées", font=("times new roman",15),bg="white")
        CoordFrame.place(x=15, y=10, width=350, height=180)
        
        self.lbl_longt = Label(CoordFrame, text="Longitude :", font=("times new roman",12), bg="white")
        self.lbl_longt.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.txt_coord = ttk.Entry(CoordFrame, font=("times new roman",12))
        self.txt_coord.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        self.lbl_lat = Label(CoordFrame, text="Latitude :", font=("times new roman",12), bg="white")
        self.lbl_lat.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.txt_lat = ttk.Entry(CoordFrame, font=("times new roman",12))
        self.txt_lat.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        self.lbl_lat_long_meth = Label(CoordFrame, text="Lat/Long Méthode :", font=("times new roman",12), bg="white")
        self.lbl_lat_long_meth.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.txt_lat_long_meth = ttk.Combobox(CoordFrame, font=("times new roman",10),values= latlong_meth, state="readonly")
        self.txt_lat_long_meth.grid(row=2, column=1, sticky=W, padx=5, pady=2)
        self.txt_lat_long_meth.current(0)

        Getalt_btn = Button(CoordFrame, text="Get altitude from MNT",cursor="hand2", font=("Times new roman",12, "bold"), bd=0, bg="silver", fg="black", relief=SUNKEN)
        Getalt_btn.grid(row=3,column=1, sticky=W, padx=5, pady=2)

        self.lbl_alt_meth = Label(CoordFrame, text="Lat/Long Méthode :", font=("times new roman",12), bg="white")
        self.lbl_alt_meth.grid(row=4, column=0, sticky=W, padx=5, pady=2)

        self.txt_alt_meth = ttk.Combobox(CoordFrame, font=("times new roman",10),values= altitude_meth, state="readonly")
        self.txt_alt_meth.grid(row=4, column=1, sticky=W, padx=5, pady=2)
        self.txt_alt_meth.current(0)

        ################nom de l'endroit##################

        RegFrame = LabelFrame(self, text="Region", font=("times new roman",15),bg="white")
        RegFrame.place(x=15, y=190, width=350, height=300)
        
        self.lbl_prov = Label(RegFrame, text="Province :", font=("times new roman",12), bg="white")
        self.lbl_prov.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.txt_prov = ttk.Entry(RegFrame, font=("times new roman",12))
        self.txt_prov.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        self.lbl_comm = Label(RegFrame, text="Commune :", font=("times new roman",12),bg="white")
        self.lbl_comm.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.txt_comm = ttk.Entry(RegFrame, font=("times new roman",12))
        self.txt_comm.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        self.lbl_coln = Label(RegFrame, text="Colline :", font=("times new roman",12),bg="white")
        self.lbl_coln.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.txt_coln = ttk.Entry(RegFrame, font=("times new roman",12))
        self.txt_coln.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        self.lbl_Scoln = Label(RegFrame, text="Sous Colline :", font=("times new roman",12), bg="white")
        self.lbl_Scoln.grid(row=3, column=0, sticky=W, padx=5, pady=2)

        self.txt_Scoln = ttk.Entry(RegFrame, font=("times new roman",12))
        self.txt_Scoln.grid(row=3, column=1, sticky=W, padx=5, pady=2)

        self.lbl_Methd_def_reg = Label(RegFrame, text="Autoresearch :", font=("times new roman",12),bg="white")
        self.lbl_Methd_def_reg.grid(row=4, column=0, sticky=W, padx=5, pady=2)

        Getalt_btn = Button(RegFrame, text="Rechercher la localité",cursor="hand2", font=("Times new roman",12, "bold"), bd=0, bg="silver", fg="black", relief=SUNKEN)
        Getalt_btn.grid(row=4,column=1, sticky=W, padx=5, pady=2)

        Getalt_btn = Button(RegFrame, text="Séléction manuelle de la localité",cursor="hand2", font=("Times new roman",12, "bold"), bd=0, bg="silver", fg="black", relief=SUNKEN)
        Getalt_btn.grid(row=5,column=1, sticky=W, padx=5, pady=2)

        Getalt_btn = Button(RegFrame, text="Entrée Manuelle de l'ID localité",cursor="hand2", font=("Times new roman",12, "bold"), bd=0, bg="silver", fg="black", relief=SUNKEN)
        Getalt_btn.grid(row=6,column=1, sticky=W, padx=5, pady=2)



        ################identifiant d'un forage##################

        idFrame = LabelFrame(self, text="Identifier", font=("times new roman",15),bg="white")
        idFrame.place(x=370, y=10, width=470, height=120)
        
        self.lbl_idOrg = Label(idFrame, text="ID Originale :", font=("times new roman",12), bg="white")
        self.lbl_idOrg.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.txt_idOrg = ttk.Entry(idFrame, font=("times new roman",12))
        self.txt_idOrg.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        self.lbl_typ_PE = Label(idFrame, text="Type Point d'Eau :", font=("times new roman",12),bg="white")
        self.lbl_typ_PE.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.txt_typ_PE  = ttk.Combobox(idFrame, font=("times new roman",10),values= type_PE, state="readonly")
        self.txt_typ_PE .grid(row=1, column=1, sticky=W, padx=5, pady=2)
        self.txt_typ_PE .current(0)


        self.lbl_id = Label(idFrame, text="ID :", font=("times new roman",12),bg="white")
        self.lbl_id.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.txt_id = ttk.Entry(idFrame, font=("times new roman",12))
        self.txt_id.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        ################Attribut d'un forage###################################

        AttrFrame = LabelFrame(self, text="Attributes", font=("times new roman",15),bg="white")
        AttrFrame.place(x=370, y=140, width=470, height=350)
        
        self.lbl_pp = Label(AttrFrame, text="Périmètre de Protection :", font=("times new roman",12), bg="white")
        self.lbl_pp.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        btn_pp =ttk.Checkbutton(AttrFrame,text="vraie")
        btn_pp.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        self.lbl_projet = Label(AttrFrame, text="Projet :", font=("times new roman",12),bg="white")
        self.lbl_projet.grid(row=1, column=0, sticky=W, padx=5, pady=2)
        
        self.txt_projet = ttk.Entry(AttrFrame, font=("times new roman",12))
        self.txt_projet.grid(row=1, column=1, sticky=W, padx=15, pady=2)
        
        self.lbl_sous_resp = Label(AttrFrame, text="Sous la Résponsabilité de :", font=("times new roman",12),bg="white")
        self.lbl_sous_resp.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.txt_sous_resp = ttk.Entry(AttrFrame, font=("times new roman",12))
        self.txt_sous_resp.grid(row=2, column=1, sticky=W, padx=15, pady=2)

        self.lbl_Entr_pr = Label(AttrFrame, text="Entrée Provisoire :", font=("times new roman",12,"bold"), bg="white")
        self.lbl_Entr_pr.grid(row=3, column=0, sticky=W, padx=5, pady=2)

        btn_Entr_pr =ttk.Checkbutton(AttrFrame,text="vraie")
        btn_Entr_pr.grid(row=3, column=1, sticky=W, padx=5, pady=2)
        
        self.lbl_Rmq = Label(AttrFrame, text="Remarque :", font=("times new roman",12),bg="white")
        self.lbl_Rmq.grid(row=4, column=0, sticky=W, padx=5, pady=2)

        self.txt_Rmq = Text(AttrFrame, font=("times new roman",12),width=20,height=5, relief=SOLID)
        self.txt_Rmq.grid(row=4, column=1, sticky=W, padx=15, pady=5)
        
        self.lbl_der_dat_modif = Label(AttrFrame, text="Dérnière Date de modification :", font=("times new roman",12,"bold"),bg="white")
        self.lbl_der_dat_modif.grid(row=5, column=0, sticky=W, padx=5, pady=2)
        
        self.txt_der_dat_modif = ttk.Entry(AttrFrame, font=("times new roman",12))
        self.txt_der_dat_modif.grid(row=5, column=1, sticky=W, padx=15, pady=2)
        
        self.lbl_der_modif_par = Label(AttrFrame, text="Dérnière modification par :", font=("times new roman",12,"bold"),bg="white")
        self.lbl_der_modif_par.grid(row=6, column=0, sticky=W, padx=5, pady=2)

        self.txt_der_modif_par = ttk.Entry(AttrFrame, font=("times new roman",12))
        self.txt_der_modif_par.grid(row=6, column=1, sticky=W, padx=15, pady=2)

        Part1_btn = Frame(self, bd=5, relief=GROOVE, bg="silver")
        Part1_btn.place(x=450, y=490,width=90,height=50)

        Part2_btn = Frame(self, bd=5, relief=GROOVE, bg="silver")
        Part2_btn.place(x=600, y=490,width=110,height=50)

        Creat_btn = Button(Part1_btn, text="Créer",cursor="hand2", font=("Times new roman",17, "bold"),bg="green", fg="black")
        Creat_btn.grid(row=0, column=1,sticky=W)

        Abort_btn = Button(Part2_btn, text="Annuler",cursor="hand2", font=("Times new roman",17, "bold"),bg="red", fg="black")
        Abort_btn.grid(row=0, column=1,sticky=W)

        

        

        



if __name__ =="__main__":
    w=Forage()
    w.mainloop()
