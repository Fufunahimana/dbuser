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
        self.config(bg="cyan")
        self.grab_set()
        self.resizable(0,0)

        recherch_par = Label(self, text="Rechercher par",font=("times new roman",15, "bold"),bg="cyan",fg="black")
        recherch_par.grid(row=0, column=0,sticky=W, padx=5, pady=5)

        recherch_text = Entry(self, font=("times new roman",15), bg="white")
        recherch_text.grid(row=0, column=1,sticky=W, padx=5, pady=5)

        recherch_txt = ttk.Combobox(self, font=("times new roman",12), state="readonly")                               
        recherch_txt["values"]=("ID","orginal_ID","Province","Commune","Colline","Autre")
        recherch_txt.grid(row=0, column=2,sticky=W, padx=5, pady=5)
        recherch_txt.current(2)
        
        self.btn_rechercher = Button(self, text="Rechercher", font=("times new roman", 15, "bold"), bg='gray')
        self.btn_rechercher.grid(row=0, column=3,sticky=W, padx=5, pady=5)

        self.btn_affich = Button(self, text="Tous Afficher", font=("times new roman", 13, "bold"), bg='gray')
        self.btn_affich.grid(row=0, column=4,sticky=W, padx=5, pady=5)




if __name__ =="__main__":
    w=Selectione()
    w.mainloop()