from tkinter import *
from tkinter import ttk, messagebox
import tempfile
import random
from PIL import ImageTk, Image
from tkcalendar import *
import mysql.connector
import os

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






if __name__ =="__main__":
    w=MesureEau()
    w.mainloop()