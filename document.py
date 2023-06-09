from tkinter import *
from tkinter import ttk, messagebox
import tempfile
import random
from PIL import ImageTk, Image
from tkcalendar import *
import mysql.connector
import os

class Document(Frame):
    def __init__(self):
        super().__init__()
        self.config(bg="silver")


        scroll_x = Scrollbar(self, orient=HORIZONTAL)
        scroll_y = Scrollbar(self, orient=VERTICAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT)

        columns=("dossier","nom_de_fichier","type_de_fichier","taille_de_fichier","date_du_fichier","remarque","dernière_date_modification","dernière_modification_par","pk")
        
        self.tabl_result = ttk.Treeview(self, columns=columns,show="headings", yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

        for i in columns:
            self.tabl_result.heading(i, text=i)

        scroll_x.config(command=self.tabl_result.xview)
        scroll_y.config(command=self.tabl_result.yview)
        self.tabl_result.pack(fill=Y,side=LEFT)

        BtnFrame = Frame(self, bd=5, relief=GROOVE, bg="white")
        BtnFrame.place(x=0, y=390,width=1237, height=40)

        IPE_btn = Button(BtnFrame, text="Ajouter",cursor="hand2", font=("Times new roman",10, "bold"),width=10, bg="green", fg="black")
        IPE_btn.grid(row=0, column= 0, sticky=W, padx=50, pady=2)

        IPE_btn = Button(BtnFrame, text="Télécharger",cursor="hand2", font=("Times new roman",10, "bold"),width=10, bg="yellow", fg="black")
        IPE_btn.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        IPE_btn = Button(BtnFrame, text="Voir",cursor="hand2", font=("Times new roman",10, "bold"),width=10, bg="cyan", fg="black")
        IPE_btn.grid(row=0, column= 2, sticky=W, padx=5, pady=2)

        IPE_btn = Button(BtnFrame, text="Supprimer",cursor="hand2", font=("Times new roman",10, "bold"),width=10, bg="red", fg="black")
        IPE_btn.grid(row=0, column=3, sticky=W, padx=5, pady=2)





if __name__ =="__main__":
    w=Document()
    w.mainloop()