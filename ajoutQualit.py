from tkinter import *
from tkinter import ttk, messagebox
import tempfile
import random
from PIL import ImageTk, Image
from tkcalendar import *
import mysql.connector
import os

class AddQualt(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("EXPLOITATION FORAGE")
        self.geometry("770x650+400+100")
        self.iconbitmap('igebulogo.ico')
        self.config(bg="white")
        self.grab_set()
        self.resizable(0,0)


        title = Label(self, text="FORAGE",bd=20,font=('Times new roman', 15, "bold"),bg='beige', fg='black')
        title.place(x=5,y=5,width=760, height=25)

        Part1 = Frame(self, bd=5, bg="silver")
        Part1.place(x=5, y=35, width=760,height=100)

        id = Label(Part1, text="id",borderwidth=1, font=("times new roman",12,"bold"),width=20, bg="khaki", relief=SOLID)
        id.grid(row=0, column=0, sticky=W, padx=0, pady=0)

        id = Entry(Part1, font=("times new roman",12),width=23,borderwidth=1,relief=SOLID, bg="silver", state="readonly")
        id.grid(row=0, column=1, sticky=W, padx=0, pady=0)

        permetr = Label(Part1, text="périmètre_de_protection",borderwidth=1,font=("times new roman",12,"bold"),width=20, bg="khaki", relief=SOLID)
        permetr.grid(row=0, column=2, sticky=W, padx=0, pady=0)

        id = Entry(Part1, font=("times new roman",12),width=24,borderwidth=1,relief=SOLID, bg="silver", state="readonly")
        id.grid(row=0, column=3, sticky=W, padx=0, pady=0)

        id_org = Label(Part1, text="id_orginal",borderwidth=1, font=("times new roman",12,"bold"),width=20, bg="khaki", relief=SOLID)
        id_org.grid(row=1, column=0, sticky=W, padx=0, pady=0)

        id_org = Entry(Part1, font=("times new roman",12),width=23,borderwidth=1,relief=SOLID, bg="silver", state="readonly")
        id_org.grid(row=1, column=1, sticky=W, padx=0, pady=0)

        province = Label(Part1, text="province",borderwidth=1, font=("times new roman",12,"bold"),width=20, bg="khaki", relief=SOLID)
        province.grid(row=1, column=2, sticky=W, padx=0, pady=0)

        id_org = Entry(Part1, font=("times new roman",12),width=24,borderwidth=1,relief=SOLID,bg="silver", state="readonly")
        id_org.grid(row=1, column=3, sticky=W, padx=0, pady=0)

        longt = Label(Part1, text="longitude",borderwidth=1, font=("times new roman",12,"bold"),width=20, bg="khaki", relief=SOLID)
        longt.grid(row=2, column=0, sticky=W, padx=0, pady=0)

        longt = Entry(Part1, font=("times new roman",12),width=23,borderwidth=1,relief=SOLID,bg="silver", state="readonly")
        longt.grid(row=2, column=1, sticky=W, padx=0, pady=0)

        commune = Label(Part1, text="commune",borderwidth=1, font=("times new roman",12,"bold"),width=20, bg="khaki", relief=SOLID)
        commune.grid(row=2, column=2, sticky=W, padx=0, pady=0)

        longt = Entry(Part1, font=("times new roman",12),width=24,borderwidth=1,relief=SOLID,bg="silver", state="readonly")
        longt.grid(row=2, column=3, sticky=W, padx=0, pady=0)

        latit = Label(Part1, text="latitude",borderwidth=1, font=("times new roman",12,"bold"),width=20, bg="khaki", relief=SOLID)
        latit.grid(row=3, column=0, sticky=W, padx=0, pady=0)

        latit = Entry(Part1, font=("times new roman",12),width=23,borderwidth=1,relief=SOLID,bg="silver", state="readonly")
        latit.grid(row=3, column=1, sticky=W, padx=0, pady=0)

        colline= Label(Part1, text="colline",borderwidth=1, font=("times new roman",12,"bold"),width=20, bg="khaki", relief=SOLID)
        colline.grid(row=3, column=2, sticky=W, padx=0, pady=0)

        latit = Entry(Part1, font=("times new roman",12),width=24,borderwidth=1,relief=SOLID,bg="silver", state="readonly")
        latit.grid(row=3, column=3, sticky=W, padx=0, pady=0)

        Part2 = Frame(self, bd=5, bg="silver")
        Part2.place(x=5, y=140, width=760,height=35)

        fieldN = Label(Part2, text="Fieldname",borderwidth=1, font=("times new roman",12,"bold"),width=20, bg="silver",fg="white", relief=RAISED)
        fieldN.grid(row=0, column=0, sticky=W, padx=0, pady=0)

        fieldN = Label(Part2, text="Value",borderwidth=1, font=("times new roman",12,"bold"),width=20, bg="silver",fg="white", relief=RAISED)
        fieldN.grid(row=0, column=1, sticky=W, padx=0, pady=0)

        fieldN = Label(Part2, text="Description",borderwidth=1, font=("times new roman",12,"bold"),width=42, bg="silver",fg="white", relief=RAISED)
        fieldN.grid(row=0, column=2, sticky=W, padx=0, pady=0)

#######################################Entry###########################################################################################
        
        Part3 = Frame(self, bd=5, bg="silver")
        Part3.place(x=5, y=180, width=760,height=400)

        simple_id = Label(Part3, text="simple_ID",borderwidth=1, font=("times new roman",12,"bold"),width=21, bg="khaki", relief=SOLID)
        simple_id.grid(row=0, column=0, sticky=W, padx=0, pady=0)

        simple_id= Entry(Part3, font=("times new roman",12),width=22,borderwidth=1,relief=SOLID,bg="white")
        simple_id.grid(row=0, column=1, sticky=W, padx=0, pady=0)

        date_heure = Label(Part3, text="date_heure",borderwidth=1, font=("times new roman",12,"bold"),width=21, bg="khaki", relief=SOLID)
        date_heure.grid(row=1, column=0, sticky=W, padx=0, pady=0)

        ecri_date_heure = DateEntry(Part3, font=("times new roman", 14),width=17, bg="lightyellow", state="readonly", locale='fr_FR',date_pattern = 'dd/mm/yyyy')
        ecri_date_heure.grid(row=1, column=1, sticky=W, padx=0, pady=0)

        niv_eau = Label(Part3, text="niveau_d_eau",borderwidth=1, font=("times new roman",12,"bold"),width=21, bg="khaki", relief=SOLID)
        niv_eau.grid(row=2, column=0, sticky=W, padx=0, pady=0)

        niv_eau= Entry(Part3, font=("times new roman",12),width=22,borderwidth=1,relief=SOLID,bg="white")
        niv_eau.grid(row=2, column=1, sticky=W, padx=0, pady=0)

        niv_eau = Label(Part3, text="Niveau d'eau mesuré par rapport au repère du point d'eau (en mètre)",borderwidth=1, font=("times new roman",10,"bold"),width=53, bg="silver", relief=SOLID)
        niv_eau.grid(row=2, column=2, sticky=W, padx=0, pady=0)

        hauteut_tt_frg = Label(Part3, text="hauteur_tête_forage",borderwidth=1, font=("times new roman",12,"bold"),width=21, bg="khaki", relief=SOLID)
        hauteut_tt_frg.grid(row=3, column=0, sticky=W, padx=0, pady=0)

        hauteut_tt_frg= Entry(Part3, font=("times new roman",12),width=22,borderwidth=1,relief=SOLID,bg="white")
        hauteut_tt_frg.grid(row=3, column=1, sticky=W, padx=0, pady=0)

        hauteut_tt_frg = Label(Part3, text="Distance entre le sol et le point haut du repère\ndu point d'eau(utilisé pour mésure du niveau de l'eau)",borderwidth=1, font=("times new roman",10,"bold"),width=53, bg="silver", relief=SOLID)
        hauteut_tt_frg.grid(row=3, column=2, sticky=W, padx=0, pady=0)

        
        methd_mes_niv_eau = Label(Part3, text="méthode_mesure_niv_d_eau",borderwidth=1, font=("times new roman",12,"bold"),width=21, bg="khaki", relief=SOLID)
        methd_mes_niv_eau.grid(row=4, column=0, sticky=W, padx=0, pady=0)

        methd_mes_niv_eau = ttk.Combobox(Part3, font=("times new roman",10),width=25,values= ("IGEBU Gitega", "BGR Hanovre","Labo privé du Burundi","Labo sur terrain(SKAT)"), state="readonly")
        methd_mes_niv_eau.grid(row=4, column=1, sticky=W, padx=5, pady=2)
        methd_mes_niv_eau.current(0)

        methd_mes_niv_eau = Label(Part3, text="Méthode utilisée pour mesurer le niveau d'eau",borderwidth=1, font=("times new roman",10),width=53, bg="silver", relief=SOLID)
        methd_mes_niv_eau.grid(row=4, column=2, sticky=W, padx=0, pady=0)

        conctvt = Label(Part3, text="condictivité",borderwidth=1, font=("times new roman",12,"bold"),width=21, bg="khaki", relief=SOLID)
        conctvt.grid(row=5, column=0, sticky=W, padx=0, pady=0)

        conctvt= Entry(Part3, font=("times new roman",12),width=22,borderwidth=1,relief=SOLID,bg="white")
        conctvt.grid(row=5, column=1, sticky=W, padx=0, pady=0)

        conctvt = Label(Part3, text="Condictivité electrique de l'eau en µS//cm",borderwidth=1, font=("times new roman",10,"bold"),width=53, bg="silver", relief=SOLID)
        conctvt.grid(row=5, column=2, sticky=W, padx=0, pady=0)

        tempratr = Label(Part3, text="température",borderwidth=1, font=("times new roman",12,"bold"),width=21, bg="khaki", relief=SOLID)
        tempratr.grid(row=6, column=0, sticky=W, padx=0, pady=0)

        tempratr= Entry(Part3, font=("times new roman",12),width=22,borderwidth=1,relief=SOLID,bg="white")
        tempratr.grid(row=6, column=1, sticky=W, padx=0, pady=0)

        tempratr = Label(Part3, text="Temperature en °C",borderwidth=1, font=("times new roman",10,"bold"),width=53, bg="silver", relief=SOLID)
        tempratr.grid(row=6, column=2, sticky=W, padx=0, pady=0)

        ph = Label(Part3, text="ph",borderwidth=1, font=("times new roman",12,"bold"),width=21, bg="khaki", relief=SOLID)
        ph.grid(row=7, column=0, sticky=W, padx=0, pady=0)

        ph= Entry(Part3, font=("times new roman",12),width=22,borderwidth=1,relief=SOLID,bg="white")
        ph.grid(row=7, column=1, sticky=W, padx=0, pady=0)

        ph = Label(Part3, text="pH de l'eau",borderwidth=1, font=("times new roman",10,"bold"),width=53, bg="silver", relief=SOLID)
        ph.grid(row=7, column=2, sticky=W, padx=0, pady=0)

        o2 = Label(Part3, text="o2",borderwidth=1, font=("times new roman",12,"bold"),width=21, bg="khaki", relief=SOLID)
        o2.grid(row=8, column=0, sticky=W, padx=0, pady=0)

        o2= Entry(Part3, font=("times new roman",12),width=22,borderwidth=1,relief=SOLID,bg="white")
        o2.grid(row=8, column=1, sticky=W, padx=0, pady=0)

        o2 = Label(Part3, text="Oxygène dissous de l'eau %",borderwidth=1, font=("times new roman",10,"bold"),width=53, bg="silver", relief=SOLID)
        o2.grid(row=8, column=2, sticky=W, padx=0, pady=0)


        turbidit = Label(Part3, text="turbidité",borderwidth=1, font=("times new roman",12,"bold"),width=21, bg="khaki", relief=SOLID)
        turbidit.grid(row=9, column=0, sticky=W, padx=0, pady=0)
        
        turbidit = ttk.Combobox(Part3, font=("times new roman",10),width=25,values= ("légerement transparente(1-10NTU)", "non transparente(>10NTU)","transparente(<10NTU)"), state="readonly")
        turbidit.grid(row=9, column=1, sticky=W, padx=5, pady=2)
        turbidit.current(0)

        turbidit = Label(Part3, text="Turbidité de l'eau",borderwidth=1, font=("times new roman",10),width=53, bg="silver", relief=SOLID)
        turbidit.grid(row=9, column=2, sticky=W, padx=0, pady=0)

        couleur = Label(Part3, text="couleur",borderwidth=1, font=("times new roman",12,"bold"),width=21, bg="khaki", relief=SOLID)
        couleur.grid(row=10, column=0, sticky=W, padx=0, pady=0)
        
        couleur = ttk.Combobox(Part3, font=("times new roman",10),width=25,values= ("jaunâtre", "limpide","noirâtre","rougeâtre","verdâtre"), state="readonly")
        couleur.grid(row=10, column=1, sticky=W, padx=5, pady=2)
        couleur.current(0)

        couleur = Label(Part3, text="couleur de l'eau",borderwidth=1, font=("times new roman",10),width=53, bg="silver", relief=SOLID)
        couleur.grid(row=10, column=2, sticky=W, padx=0, pady=0)

        odeur = Label(Part3, text="odeur",borderwidth=1, font=("times new roman",12,"bold"),width=21, bg="khaki", relief=SOLID)
        odeur.grid(row=11, column=0, sticky=W, padx=0, pady=0)
        
        odeur = ttk.Combobox(Part3, font=("times new roman",10),width=25,values= ("Oeuf poulis", "pouli,moisie(marais)","autre"), state="readonly")
        odeur.grid(row=11, column=1, sticky=W, padx=5, pady=2)
        odeur.current(0)

        odeur = Label(Part3, text="Type de certification",borderwidth=1, font=("times new roman",10),width=53, bg="silver", relief=SOLID)
        odeur.grid(row=11, column=2, sticky=W, padx=0, pady=0)

        mesur_par = Label(Part3, text="mesuré_par",borderwidth=1, font=("times new roman",12,"bold"),width=21, bg="khaki", relief=SOLID)
        mesur_par.grid(row=12, column=0, sticky=W, padx=0, pady=0)
        
        mesur_par = ttk.Combobox(Part3, font=("times new roman",10),width=25,values= ("certifié mais numero inconnu", "ISO 9000","ISO 9001","sans certification"), state="readonly")
        mesur_par.grid(row=12, column=1, sticky=W, padx=5, pady=2)
        mesur_par.current(0)

        mesur_par = Label(Part3, text="nom de la personne ayant fai les mesure sur terrain",borderwidth=1, font=("times new roman",10),width=53, bg="silver", relief=SOLID)
        mesur_par.grid(row=12, column=2, sticky=W, padx=0, pady=0)

        meth_mes_pt = Label(Part3, text="mathode_mesure_pt",borderwidth=1, font=("times new roman",12,"bold"),width=21, bg="khaki", relief=SOLID)
        meth_mes_pt.grid(row=13, column=0, sticky=W, padx=0, pady=0)
        
        meth_mes_pt = ttk.Combobox(Part3, font=("times new roman",10),width=25,values= ("certifié mais numero inconnu", "ISO 9000","ISO 9001","sans certification"),state="readonly")
        meth_mes_pt.grid(row=13, column=1, sticky=W, padx=5, pady=2)
        meth_mes_pt.current(0)

        meth_mes_pt = Label(Part3, text="Appareillage utilisé pour mesurer les paramètres sur terrain",borderwidth=1, font=("times new roman",10),width=53, bg="silver", relief=SOLID)
        meth_mes_pt.grid(row=13, column=2, sticky=W, padx=0, pady=0)

        remarq = Label(Part3, text="remarque",borderwidth=1, font=("times new roman",12,"bold"),width=21, bg="khaki", relief=SOLID)
        remarq.grid(row=14, column=0, sticky=W, padx=0, pady=0)

        remarq = Text(Part3, font=("times new roman",12),width=22,height=2,borderwidth=1,relief=SOLID,bg="white",)
        remarq.grid(row=14, column=1, sticky=W, padx=0, pady=0)

        remarq = Label(Part3, text="Commentaire sur la localisation",borderwidth=1, font=("times new roman",10),width=53,bg="silver", relief=SOLID)
        remarq.grid(row=14, column=2, sticky=W, padx=0, pady=0)
         
#########################################################Button#################################################################################

        Part4 = Frame(self, bd=5, bg="white")
        Part4.place(x=500, y=580, width=260,height=55)

        def quit(self):
             self.destroy()

        Creat_btn = Button(Part4 , text="Ajouter",cursor="hand2", font=("Times new roman",17, "bold"),bg="green",width=8, fg="black")
        Creat_btn.grid(row=0, column=0,sticky=W, padx=0, pady=0)

        Abort_btn = Button(Part4 , text="quiter",cursor="hand2",command=quit, font=("Times new roman",17, "bold"),bg="red",width=8, fg="black")
        Abort_btn.grid(row=0, column=1,sticky=W, padx=0, pady=0)

def quit(self):
     self.destroy()






if __name__ =="__main__":
    w=AddQualt()
    w.mainloop()
