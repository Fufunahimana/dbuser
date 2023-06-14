from tkinter import *
from tkinter import ttk, messagebox
import tempfile
import random
from PIL import ImageTk, Image
from tkcalendar import *
import mysql.connector
import os
from ajoutQualit import*

class MesureEau(Frame):
    def __init__(self):
        super().__init__()
        self.config(bg="silver")


        scroll_x = Scrollbar(self, orient=HORIZONTAL)
        scroll_y = Scrollbar(self, orient=VERTICAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT)

        columns=("No","id","id_orginal","date_heure","niveau_d_eau","hauteur_tête_forage","conductivité","temperature","ph","o2","mesuré_par","methode_mesure_pt","remarque","dernière_date_modification","dernière_modification_par","pk")
        
        self.tabl_result = ttk.Treeview(self, columns=columns,show="headings", yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

        for i in columns:
            self.tabl_result.heading(i, text=i)

        scroll_x.config(command=self.tabl_result.xview)
        scroll_y.config(command=self.tabl_result.yview)
        self.tabl_result.pack(fill=Y,side=LEFT)

        def ajouter():
            AddQualt()
            

        BtnFrame = Frame(self, bd=5, relief=GROOVE, bg="white")
        BtnFrame.place(x=0, y=390,width=1237, height=40)

        IPE_btn = Button(BtnFrame, text="search",cursor="hand2", font=("Times new roman",10, "bold"),width=10, bg="silver", fg="black")
        IPE_btn.grid(row=0, column= 0, sticky=W, padx=50, pady=2)

        IPE_btn = Button(BtnFrame, text="Showall",cursor="hand2", font=("Times new roman",10, "bold"),width=10, bg="silver", fg="black")
        IPE_btn.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        IPE_btn = Button(BtnFrame, text="Importer",cursor="hand2", font=("Times new roman",10, "bold"),width=10, bg="cyan", fg="black")
        IPE_btn.grid(row=0, column= 2, sticky=W, padx=5, pady=2)

        IPE_btn = Button(BtnFrame, text="Ajouter",cursor="hand2",command=ajouter, font=("Times new roman",10, "bold"),width=10, bg="green", fg="black")
        IPE_btn.grid(row=0, column=3, sticky=W, padx=5, pady=2)
        
        IPE_btn = Button(BtnFrame, text="Modifier",cursor="hand2", font=("Times new roman",10, "bold"),width=10, bg="yellow", fg="black")
        IPE_btn.grid(row=0, column= 4, sticky=W, padx=5, pady=2)

        IPE_btn = Button(BtnFrame, text="Supprimer",cursor="hand2", font=("Times new roman",10, "bold"),width=10, bg="red", fg="black")
        IPE_btn.grid(row=0, column=5, sticky=W, padx=5, pady=2)







if __name__ =="__main__":
    w=MesureEau()
    w.mainloop()