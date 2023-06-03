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

        province = ["Bubanza","Bujumura Marie","Bujumbura Rural","Bururi","Cankuzo","Cibitoke","Gitega","Karusi","Kayanza","Kirundo","Makamba","Muramvya","Muyinga","Mwaro","Ngozi","Rumonge","Rutana","Ruyigi"]
        altitude_meth = ["GPS","Carte","DGPS","Modèle Numérique de Terrain","Nivelement","Rapport"]
        type_PE = ["Forage","Puit","Source"]




if __name__ =="__main__":
    w=Forage()
    w.mainloop()
