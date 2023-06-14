from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import *
from datetime import datetime 
from time import strftime
import mysql.connector
import os
from Forage2 import*
from forage import*
from Requete import*
from equipement import*
from EssaiPompage import*
from Rehabilitation import*
from sequenceGeo import*
from exploitationFor import*
from MesureEau import*
from QualiteEau import*
from document import*
from DescriptionFor import*
from selectionnerPE import*

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("CONNEXION")
        self.root.geometry("1500x900+0+0")
        self.root.config(bg="white")
        self.root.focus_force()

        def heure():
                heur=strftime("%H:%M:%S")
                lblheure.config(text=heur)
                lblheure.after(1000,heure)
            
            
        lblheure = Label(self.root, text="HH:MM:SS", font=("times new roman", 15, "bold"),bg="white", fg="black")
        lblheure.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        
        heure()
        

        Part1 = Frame(self.root, bd=5, relief=GROOVE, bg="white")
        Part1.place(x=0, y=50,width=300,height=770)
        Part2 = Frame(self.root, bd=5, relief=GROOVE, bg="yellow")
        Part2.place(x=300, y=50,width=1255,height=300)

        scroll_x = Scrollbar(Part2, orient=HORIZONTAL)
        scroll_y = Scrollbar(Part2, orient=VERTICAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT)

        columns=("No","id","id_orginal","longitude","latitude","latlong_méthode","altitude_z","altitude_méthode","type_point_d_eau","périmètres_de_protection","province","commune","colline","sous_colline","projet","sous_la_responsabilité","entrée_provisoire","remarque","dernière_date_modification","dernière_modification_par")
        
        self.tabl_result = ttk.Treeview(Part2, columns=columns,show="headings", yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
             
        scroll_x.config(command=self.tabl_result.xview)
        scroll_y.config(command=self.tabl_result.yview)
        
        self.tabl_result.heading("No", text="No.")
        self.tabl_result.heading("id", text="id")
        self.tabl_result.heading("id_orginal", text="id_orginal")
        self.tabl_result.heading("longitude", text="longitude")
        self.tabl_result.heading("latitude", text="latitude")
        self.tabl_result.heading("latlong_méthode", text="latlong_méthode")
        self.tabl_result.heading("altitude_z", text="altitude_z")
        self.tabl_result.heading("altitude_méthode", text="altitude_méthode")
        self.tabl_result.heading("type_point_d_eau", text="type_point_d_eau") 
        self.tabl_result.heading("périmètres_de_protection", text="périmètres_de_protection")
        self.tabl_result.heading("province", text="province")
        self.tabl_result.heading("commune", text="commune")
        self.tabl_result.heading("colline", text="colline")
        self.tabl_result.heading("sous_colline", text="sous_colline")
        self.tabl_result.heading("projet", text="projet")
        self.tabl_result.heading("sous_la_responsabilité", text="sous_la_responsabilité")
        self.tabl_result.heading("entrée_provisoire", text="entrée_provisoire")
        self.tabl_result.heading("remarque", text="remarque")
        self.tabl_result.heading("dernière_date_modification", text="dernière_date_modification") 
        self.tabl_result.heading("dernière_modification_par", text="dernière_modification_par")
        
        
        self.tabl_result.pack(fill=Y,side=LEFT)
        
        
        for i in range (1,100):
            self.tabl_result.insert("", END,values=columns)
        
        #self.tabl_result.bind("<ButtonRelease-1>",self.information)


        ##############entête #######################
        user = Entry(root, font=("times new roman",12), bg="gray")
        user.grid(row=0, column=2, sticky=W, padx=2, pady=5)
        nom_u = Entry(root, font=("times new roman",12), bg="olive")
        nom_u.grid(row=0, column=3, sticky=W, padx=2, pady=5)
        Group = Entry(root, font=("times new roman",12), bg="cyan")
        Group.grid(row=0, column= 4, sticky=W, padx=2, pady=5)
        nom_gr = Entry(root, font=("times new roman",12), bg="beige")
        nom_gr.grid(row=0, column= 5, sticky=W, padx=2, pady=5)
        serveur = Entry(root, font=("times new roman",12), bg="lavender")
        serveur.grid(row=0, column= 6, sticky=W, padx=2, pady=5)
        id_serv = Entry(root, font=("times new roman",12), bg="khaki")
        id_serv.grid(row=0, column= 7, sticky=W, padx=2, pady=5)
        db = Entry(root, font=("times new roman",12), bg="silver")
        db.grid(row=0, column= 8, sticky=W, padx=2, pady=5)
        nom_db = Entry(root, font=("times new roman",12), bg="brown")
        nom_db.grid(row=0, column= 9, sticky=W, padx=2, pady=5)
        
        #############boutons divers###########################
        def forage():
             Forage()

        def requete():
             Requete()

        def importer():
             wx=Description(self)
             wx.mainloop()

        def PE_select():
             Selectione()
             
        

        def quit():
          self.root.destroy()

             
        NPE_btn = Button(Part1, text="Nouveau point d'eau",cursor="hand2",command=forage,font=("Times new roman",14, "bold"),width=22, bg="cyan", fg="black",relief=GROOVE)
        NPE_btn.grid(row=0, sticky=W, padx=5, pady=2)

        MPE_btn = Button(Part1, text="Modifier un Point d'eau",cursor="hand2", font=("Times new roman",14, "bold"),width=22,bg="silver", fg="black",relief=GROOVE)
        MPE_btn.grid(row=1, sticky=W, padx=5, pady=2)

        SPE_btn = Button(Part1, text="Supprimer un Point d'eau",cursor="hand2", font=("Times new roman",14, "bold"),width=22, bg="silver", fg="black",relief=GROOVE)
        SPE_btn.grid(row=2, sticky=W, padx=5, pady=2)

        RQT_btn = Button(Part1, text="Requêtes",cursor="hand2",command=requete, font=("Times new roman",14, "bold"),width=22, bg="silver", fg="black",relief=GROOVE)
        RQT_btn.grid(row=3, sticky=W, padx=5, pady=2)

        SelPE_btn = Button(Part1, text="Selectionner un Point d'eau",cursor="hand2",command=PE_select, font=("Times new roman",14, "bold"),width=22, bg="silver", fg="black",relief=GROOVE)
        SelPE_btn.grid(row=4, sticky=W, padx=5, pady=2)


        IPE_btn = Button(Part1, text="Importer un Point d'eau",cursor="hand2",command=importer, font=("Times new roman",14, "bold"),width=22, bg="silver", fg="black",relief=GROOVE)
        IPE_btn.grid(row=5, sticky=W, padx=5, pady=2)

        SRT_btn = Button(Part1, text="Quiter",cursor="hand2",command=quit, font=("Times new roman",14, "bold"),width=22, bg="red", fg="black",relief=GROOVE)
        SRT_btn.grid(row=6, sticky=W, padx=5, pady=2)

        ####################partie numero 3######################################
        Part3 = ttk.Notebook(self.root)
        Part3.place(x=300, y=350,width=1255,height=470)

    
        forg_btn = Forage2()
        Part3.add(forg_btn,text="Forage")

        eqpmt_btn = Equipmt()
        Part3.add(eqpmt_btn,text="Equipement")

        Edp_btn = PumpTest()
        Part3.add(Edp_btn,text="Essai de pompages")

        Rhbl_btn = Rehabilit()
        Part3.add( Rhbl_btn,text="Réhabilitation")

        Seq_btn = SequenceGeo()
        Part3.add(Seq_btn,text="Séquence Géologique")

        Exp_btn = exploitation()
        Part3.add(Exp_btn,text="Exoploitation Forage")

        Msr_btn = MesureEau()
        Part3.add(Msr_btn,text="Mesure eaux")

        qual_btn = QualiteEau()
        Part3.add(qual_btn,text="Qualité de l'eau")

        doc_btn = Document()
        Part3.add(doc_btn,text="Documents")












root=Tk()
obj =Login(root)
root.mainloop()