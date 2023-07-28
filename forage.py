from tkinter import *
from tkinter import ttk, messagebox
import tempfile
import random
import psycopg2 
from PIL import ImageTk, Image
from tkcalendar import *
import mysql.connector
import os

class Forage(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("NOUVEAU FORAGE")
        self.geometry("850x550+400+200")
        self.iconbitmap('igebulogo.ico')
        self.config(bg="silver")
        self.grab_set()
        self.resizable(0,0)
        
        ##########################LES LISTES UTILISEES##############################

        latlong_meth = ["GPS","Carte","DGPS","Rapport"]
        altitude_meth = ["GPS","Carte","DGPS","Modèle Numérique de Terrain","Nivelement","Rapport"]
        type_PE = ["Forage","Puit","Source"]
        
        self.id = StringVar()
        self.id_orginal = StringVar()
        self.longitude = DoubleVar()
        self.latitude = DoubleVar()
        self.altitude = DoubleVar()
        self.latlong_méthode= StringVar()
        self.altitude_z = StringVar()
        self.altitude_méthode = StringVar()
        self.type_point_d_eau = StringVar()
        self.périmètre_de_protection = StringVar()
        self.province = StringVar()
        self.commune = StringVar()
        self.colline = StringVar()
        self.sous_colline = StringVar()
        self.projet = StringVar()
        self.sous_la_responsabilité = StringVar()
        self.entrée_provisoire = StringVar()
        self.remarque = StringVar()
        self.dernière_date_modification = StringVar()
        self.dernière_modification_par = StringVar()
       
        CoordFrame = LabelFrame(self, text="Coordonées", font=("times new roman",15),bg="white")
        CoordFrame.place(x=15, y=10, width=350, height=210)
        
        self.lbl_longt = Label(CoordFrame, text="Longitude :", font=("times new roman",12), bg="white")
        self.lbl_longt.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.txt_longt = ttk.Entry(CoordFrame,textvariable=self.longitude,font=("times new roman",12))
        self.txt_longt.grid(row=0,column=1, sticky=W, padx=5, pady=2)

        self.lbl_lat = Label(CoordFrame, text="Latitude :", font=("times new roman",12), bg="white")
        self.lbl_lat.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.txt_lat = ttk.Entry(CoordFrame,textvariable=self.latitude, font=("times new roman",12))
        self.txt_lat.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        self.lbl_alt = Label(CoordFrame, text="Altitude :", font=("times new roman",12), bg="white")
        self.lbl_alt.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.txt_alt = ttk.Entry(CoordFrame,textvariable=self.altitude, font=("times new roman",12))
        self.txt_alt.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        self.lbl_lat_long_meth = Label(CoordFrame, text="Lat/Long Méthode :", font=("times new roman",12), bg="white")
        self.lbl_lat_long_meth.grid(row=3, column=0, sticky=W, padx=5, pady=2)

        self.txt_lat_long_meth = ttk.Combobox(CoordFrame,textvariable=self.latlong_méthode,font=("times new roman",10),values= latlong_meth, state="readonly")
        self.txt_lat_long_meth.grid(row=3,column=1, sticky=W, padx=5, pady=2)
        self.txt_lat_long_meth.current(0)

        Getalt_btn = Button(CoordFrame, text="Get altitude from MNT",cursor="hand2", font=("Times new roman",12, "bold"), bd=0, bg="silver", fg="black", relief=SUNKEN)
        Getalt_btn.grid(row=4,column=1, sticky=W, padx=5, pady=2)

        self.lbl_alt_meth = Label(CoordFrame, text="Lat/Long Méthode :", font=("times new roman",12), bg="white")
        self.lbl_alt_meth.grid(row=4, column=0, sticky=W, padx=5, pady=2)

        self.txt_alt_meth = ttk.Combobox(CoordFrame,textvariable=self.altitude_méthode, font=("times new roman",10),values= altitude_meth, state="readonly")
        self.txt_alt_meth.grid(row=5, column=1, sticky=W, padx=5, pady=2)
        self.txt_alt_meth.current(0)

        ################nom de l'endroit##################

        RegFrame = LabelFrame(self, text="Region", font=("times new roman",15),bg="white")
        RegFrame.place(x=15, y=220, width=350, height=300)
        
        self.lbl_prov = Label(RegFrame, text="Province :", font=("times new roman",12),bg="white")
        self.lbl_prov.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.txt_prov = ttk.Entry(RegFrame,textvariable=self.province,font=("times new roman",12))
        self.txt_prov.grid(row=0,column=1, sticky=W, padx=5, pady=2)

        self.lbl_comm = Label(RegFrame, text="Commune :", font=("times new roman",12),bg="white")
        self.lbl_comm.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.txt_comm = ttk.Entry(RegFrame,textvariable=self.commune,font=("times new roman",12))
        self.txt_comm.grid(row=1,column=1, sticky=W, padx=5, pady=2)

        self.lbl_coln = Label(RegFrame, text="Colline :", font=("times new roman",12),bg="white")
        self.lbl_coln.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.txt_coln = ttk.Entry(RegFrame,textvariable=self.colline,font=("times new roman",12))
        self.txt_coln.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        self.lbl_Scoln = Label(RegFrame, text="Sous Colline :", font=("times new roman",12), bg="white")
        self.lbl_Scoln.grid(row=3, column=0, sticky=W, padx=5, pady=2)

        self.txt_Scoln = ttk.Entry(RegFrame,textvariable=self.sous_colline,font=("times new roman",12))
        self.txt_Scoln.grid(row=3,column=1, sticky=W, padx=5, pady=2)

        self.lbl_Methd_def_reg = Label(RegFrame, text="Autoresearch :", font=("times new roman",12),bg="white")
        self.lbl_Methd_def_reg.grid(row=4, column=0, sticky=W, padx=5, pady=2)

        Getlocal_btn = Button(RegFrame, text="Rechercher la localité", command=self.getLocal,cursor="hand2", font=("Times new roman",12, "bold"), bd=0, bg="silver", fg="black", relief=SUNKEN)
        Getlocal_btn.grid(row=4,column=1, sticky=W, padx=5, pady=2)

        Getalt_btn = Button(RegFrame, text="Séléction manuelle de la localité",cursor="hand2", font=("Times new roman",12, "bold"), bd=0, bg="silver", fg="black", relief=SUNKEN)
        Getalt_btn.grid(row=5,column=1, sticky=W, padx=5, pady=2)

        Getalt_btn = Button(RegFrame, text="Entrée Manuelle de l'ID localité",cursor="hand2", font=("Times new roman",12, "bold"), bd=0, bg="silver", fg="black", relief=SUNKEN)
        Getalt_btn.grid(row=6,column=1, sticky=W, padx=5, pady=2)



        ################identifiant d'un forage##################

        idFrame = LabelFrame(self, text="Identifier", font=("times new roman",15),bg="white")
        idFrame.place(x=370, y=10, width=470, height=120)
        
        self.lbl_idOrg = Label(idFrame, text="ID Originale :", font=("times new roman",12), bg="white")
        self.lbl_idOrg.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.txt_idOrg = ttk.Entry(idFrame,textvariable=self.id_orginal,font=("times new roman",12))
        self.txt_idOrg.grid(row=0,column=1, sticky=W, padx=5, pady=2)

        self.lbl_typ_PE = Label(idFrame, text="Type Point d'Eau :", font=("times new roman",12),bg="white")
        self.lbl_typ_PE.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.txt_typ_PE  = ttk.Combobox(idFrame,textvariable=self.type_point_d_eau,font=("times new roman",10),values= type_PE, state="readonly")
        self.txt_typ_PE.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        self.txt_typ_PE.current(0)
        self.txt_typ_PE.bind("<<ComboboxSelected>>", self.setId)
        
        self.lbl_id = Label(idFrame, text="ID :", font=("times new roman",12),bg="white")
        self.lbl_id.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.txt_id = ttk.Entry(idFrame,textvariable=self.id, font=("times new roman",12))
        self.txt_id.grid(row=2,column=1, sticky=W, padx=5, pady=2)

        ################Attribut d'un forage###################################

        AttrFrame = LabelFrame(self, text="Attributes", font=("times new roman",15),bg="white")
        AttrFrame.place(x=370, y=140, width=470, height=350)
        
        self.lbl_pp = Label(AttrFrame, text="Périmètre de Protection :", font=("times new roman",12), bg="white")
        self.lbl_pp.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        btn_pp =ttk.Checkbutton(AttrFrame,text="vraie")
        btn_pp.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        self.lbl_projet = Label(AttrFrame, text="Projet :", font=("times new roman",12),bg="white")
        self.lbl_projet.grid(row=1, column=0, sticky=W, padx=5, pady=2)
        
        self.txt_projet = ttk.Entry(AttrFrame,textvariable=self.projet,font=("times new roman",12))
        self.txt_projet.grid(row=1,column=1, sticky=W, padx=15, pady=2)
        
        self.lbl_sous_resp = Label(AttrFrame, text="Sous la Résponsabilité de :", font=("times new roman",12),bg="white")
        self.lbl_sous_resp.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.txt_sous_resp = ttk.Entry(AttrFrame,textvariable=self.sous_la_responsabilité,font=("times new roman",12))
        self.txt_sous_resp.grid(row=2,column=1, sticky=W, padx=15, pady=2)

        self.lbl_Entr_pr = Label(AttrFrame, text="Entrée Provisoire :", font=("times new roman",12,"bold"), bg="white")
        self.lbl_Entr_pr.grid(row=3, column=0, sticky=W, padx=5, pady=2)

        btn_Entr_pr =ttk.Checkbutton(AttrFrame,text="vraie")
        btn_Entr_pr.grid(row=3, column=1, sticky=W, padx=5, pady=2)
        
        self.lbl_Rmq = Label(AttrFrame, text="Remarque :", font=("times new roman",12),bg="white")
        self.lbl_Rmq.grid(row=4, column=0, sticky=W, padx=5, pady=2)

        self.txt_Rmq = Text(AttrFrame,font=("times new roman",12),width=20,height=5, relief=SOLID)
        self.txt_Rmq.grid(row=4, column=1,sticky=W, padx=15, pady=5)
        
        self.lbl_der_dat_modif = Label(AttrFrame, text="Dérnière Date de modification :", font=("times new roman",12,"bold"),bg="white")
        self.lbl_der_dat_modif.grid(row=5, column=0, sticky=W, padx=5, pady=2)
        
        self.ecri_date_heure = DateEntry(AttrFrame, font=("times new roman", 12),width=17, bg="lightyellow", state="readonly", locale='fr_FR',date_pattern = 'dd/mm/yyyy')
        self.ecri_date_heure.grid(row=5, column=1, sticky=W, padx=15, pady=2)

        self.lbl_der_modif_par = Label(AttrFrame, text="Dérnière modification par :", font=("times new roman",12,"bold"),bg="white")
        self.lbl_der_modif_par.grid(row=6, column=0, sticky=W, padx=5, pady=2)

        self.txt_der_modif_par = ttk.Entry(AttrFrame,textvariable=self.dernière_modification_par,font=("times new roman",12))
        self.txt_der_modif_par.grid(row=6, column=1, sticky=W, padx=15, pady=2)

        Part1_btn = Frame(self, bd=5, relief=GROOVE, bg="silver")
        Part1_btn.place(x=450, y=490,width=90,height=50)

        Part2_btn = Frame(self, bd=5, relief=GROOVE, bg="silver")
        Part2_btn.place(x=600, y=490,width=110,height=50)

        Creat_btn = Button(Part1_btn, text="Créer",cursor="hand2",command=self.ajoutPE, font=("Times new roman",17, "bold"),bg="green", fg="black")
        Creat_btn.grid(row=0, column=1,sticky=W)

        Abort_btn = Button(Part2_btn, text="Annuler",cursor="hand2",command=self.quit, font=("Times new roman",17, "bold"),bg="red", fg="black")
        Abort_btn.grid(row=0, column=1,sticky=W)

    def quit(self):
         self.destroy()

    
    def ajoutPE(self):
        if self.id_orginal.get()=="" or self.longitude.get()=="" or self.latitude.get()=="":
            messagebox.showerror("Erreur", "Veiller Remplir tous les champs")
        else:
            mydb = psycopg2.connect(host="192.168.88.201",database="hydrogeology", user="postgres", password="igebu99")
            mycursor = mydb.cursor()
            mycursor.execute("insert into tbl_localisation values(%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                     (self.txt_id.get(),
                                      self.txt_idOrg .get(),
                                      self.txt_longt.get(),
                                      self.txt_lat.get(),
                                      self.txt_alt.get(),
                                      self.txt_lat_long_meth.get(),
                                      self.txt_alt_meth.get(),
                                      self.txt_lat_long_meth.get(),
                                      self.txt_typ_PE.get(),
                                      self.province.get(),
                                      self.commune.get(),
                                      self.colline.get(),
                                      self.sous_colline.get(),
                                      self.txt_projet.get("1.0", END),
                                      self.txt_sous_resp.get("1.0", END),
                                      self.txt_Rmq.get("1.0", END),
                                      self.ecri_date_heure.get(),
                                      self.txt_der_modif_par.get(),
                                      ))
            mydb.commit()
            self.affich_result()
            self.reinitia()
            mydb.close()
            messagebox.showinfo("Réussite","Enregistré")    

    def getLocal(self):
        query=f"SELECT *, st_contains(geometry(geom),geometry(ST_GeomFromText('POINT ({self.txt_longt.get()} {self.txt_lat.get()})', 4326))) FROM geo_communes WHERE st_contains(geometry(geom),geometry(ST_GeomFromText('POINT ({self.txt_longt.get()} {self.txt_lat.get()})', 4326)));"
        query2= f"SELECT *, st_contains(geometry(geom),geometry(ST_GeomFromText('POINT ({self.txt_longt.get()} {self.txt_lat.get()})', 4326))) FROM geo_collines WHERE st_contains(geometry(geom),geometry(ST_GeomFromText('POINT ({self.txt_longt.get()} {self.txt_lat.get()})', 4326)));"
        mydb = psycopg2.connect(host="192.168.88.201",database="hydrogeology", user="postgres", password="igebu99")
        global mycursor
        if mydb:
            print("connection etablie")
            mycursor = mydb.cursor()
            mycursor.execute(query)
            rows = mycursor.fetchall()
            mycursor.execute(query2)
            rows2 = mycursor.fetchall()
 
            for k in rows:
                    print(k[2])
                    self.txt_prov.delete(0,END)
                    self.txt_comm.delete(0,END)
                    self.txt_prov.insert(0,k[3])
                    self.txt_comm.insert(0,k[2])
            
            for i in rows2:
                    print(i[2])
                    self.txt_coln.delete(0,END)
                    self.txt_coln.insert(0,i[6])
                    
            #type_PE = ["Forage","Puit","Source"]
    def setId(self,event):
            if self.txt_typ_PE.get()=="Forage":
                query3= f"select * from tbl_localisation where colline like '{self.txt_coln.get()}' and id like 'FO-%' ORDER BY id ASC"
                mycursor.execute(query3)
                rows3 = mycursor.fetchall()
                id_holder=[]
                
               

                for j in rows3:
                       if j =="":
                           print ("premier point d'eau")
                       id_holder.append((j[0]))
                
                print(len(id_holder))
                if len(rows3)<10:
                      new_id=f'00{len(rows3)}'
                if len(rows3)>=10 and len(rows3)<100 :
                      new_id=f'0{len(rows3)}'
                if len(rows3)>=100:
                      new_id=f'{len(rows3)}'            
                
                print(id_holder)
                last_id=id_holder[len(rows3)-1]
                new_id=f'{last_id[0:10]}{new_id}'
                self.txt_id.delete(0,END)
                self.txt_id.insert(0,new_id)

            if self.txt_typ_PE.get()=="Puit":
                query3= f"select * from tbl_localisation where colline like '{self.txt_coln.get()}' and id like 'PU-%' ORDER BY id ASC"
                mycursor.execute(query3)
                rows3 = mycursor.fetchall()
                id_holder=[]
                for j in rows3:
                       id_holder.append((j[0]))
                if len(rows3)<10:
                      new_id=f'00{len(rows3)}'
                if len(rows3)>=10 and len(rows3)<100 :
                      new_id=f'0{len(rows3)}'
                if len(rows3)>=100:
                      new_id=f'{len(rows3)}'       
                               
                last_id=id_holder[len(rows3)-1]
                new_id=f'{last_id[0:10]}{new_id}'
                self.txt_id.delete(0,END)
                self.txt_id.insert(0,new_id)
               
            
            if self.txt_typ_PE.get()=="Source":
                query3= f"select * from tbl_localisation where colline like '{self.txt_coln.get()}' and id like 'SR-%' ORDER BY id ASC"
                mycursor.execute(query3)
                rows3 = mycursor.fetchall()
                id_holder=[]
                print(len( self.txt_coln.get()))

                for j in rows3:
                       id_holder.append((j[0]))
                
                print(len(id_holder))
                #if len(rows3)=="":
                #     new_id=f'SR-{}'
                if len(rows3)<10:
                      new_id=f'00{len(rows3)}'
                if len(rows3)>=10 and len(rows3)<100 :
                      new_id=f'0{len(rows3)}'
                if len(rows3)>=100:
                      new_id=f'{len(rows3)}'            
                
                print(id_holder)
                last_id=id_holder[len(rows3)-1]
                new_id=f'{last_id[0:10]}{new_id}'
                self.txt_id.delete(0,END)
                self.txt_id.insert(0,new_id)
            
            else:
                print("veiller selectionner un point d'eau")
           


if __name__ =="__main__":
    w=Forage()
    w.mainloop()
