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






if __name__ =="__main__":
    w=Document()
    w.mainloop()