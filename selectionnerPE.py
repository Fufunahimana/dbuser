from tkinter import *
from tkinter import ttk, messagebox
import tempfile
import random
from PIL import ImageTk, Image
from tkcalendar import *
import mysql.connector
import os


class Selectione(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("NOUVEAU FORAGE")
        self.geometry("850x550+400+200")
        self.iconbitmap('logodrapeau.ico')
        self.config(bg="cyan")
        self.grab_set()
        self.resizable(0,0)

        recherch_par = Label(self, text="Rechercher par",font=("times new roman",15, "bold"),bg="cyan",fg="black")
        recherch_par.place(x=5,y=5,width=180,height=30)

        recherch_text = Entry(self, font=("times new roman",15), bg="white")
        recherch_text.place(x=190,y=5,width=180,height=30)

        recherch_txt = ttk.Combobox(self, font=("times new roman",14), state="readonly")                               
        recherch_txt["values"]=("id","id_orginal","longitude","latitude","latlong_méthod","altitude_z","altitude_méthode","type_point_d_eau","périmètre_de_protection","Province","Commune","Colline","sous_colline","projet","sous_la_responsabilité_de","entrée_provisoire","remarque","dernière_modification_par")
        recherch_txt.place(x=380,y=5,width=180,height=30)
        recherch_txt.current(2)
        
        self.btn_rechercher = Button(self, text="Rechercher", font=("times new roman", 13, "bold"), bg='gray')
        self.btn_rechercher.place(x=570,y=5,width=150,height=30)

        self.btn_affich = Button(self, text="Tous Afficher", font=("times new roman", 13, "bold"), bg='yellow')
        self.btn_affich.place(x=725,y=5,width=120,height=30)

        searchF = Frame(self, bd=5, relief=GROOVE, bg="white",width=300, height=400)
        searchF.place(x=5,y=50,width=840,height=450)

        result = Text(searchF, font=("times new roman",15), bg="white")
        result.place(x=5,y=5,width=820,height=430)

        Abrt = Button(self,text="Quiter",cursor="hand2",command=quit, font=("Times new roman",13, "bold"),width=15, bg="red", fg="black")
        Abrt.place(x=735,y=510,width=110)




if __name__ =="__main__":
    w=Selectione()
    w.mainloop()