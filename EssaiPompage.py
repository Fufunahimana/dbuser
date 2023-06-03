from tkinter import *
from tkinter import ttk, messagebox
import tempfile
import random
from PIL import ImageTk, Image
from tkcalendar import *
import mysql.connector
import os

class PumpTest(Frame):
    def __init__(self):
        super().__init__()
        self.config(bg="silver")


        AttrFrame = LabelFrame(self, text="Attributes", font=("times new roman",15),bg="white")
        AttrFrame.place(x=0, y=0, width=470, height=445)
        
        self.lbl_Debit_rcmnd = Label(AttrFrame, text="Débit Recommandé :", font=("times new roman",12), bg="white")
        self.lbl_Debit_rcmnd.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.txt_Debit_rcmnd = ttk.Entry(AttrFrame, font=("times new roman",12))
        self.txt_Debit_rcmnd.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        self.lbl_Rmq = Label(AttrFrame, text="Remarque :", font=("times new roman",12),bg="white")
        self.lbl_Rmq.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        
        self.txt_Rmq = Text(AttrFrame, font=("times new roman",12),width=21,height=5, relief=RAISED)
        self.txt_Rmq.grid(row=1, column=1, sticky=W, padx=5, pady=5)
        
        self.lbl_der_dat_modif = Label(AttrFrame, text="Dérnière Date de modification :", font=("times new roman",12,"bold"),bg="white")
        self.lbl_der_dat_modif.grid(row=2, column=0, sticky=W, padx=5, pady=2)
        
        self.txt_der_dat_modif = ttk.Entry(AttrFrame, font=("times new roman",12))
        self.txt_der_dat_modif.grid(row=2, column=1, sticky=W, padx=5, pady=2)
        
        self.lbl_der_modif_par = Label(AttrFrame, text="Dérnière modification par :", font=("times new roman",12,"bold"),bg="white")
        self.lbl_der_modif_par.grid(row=3, column=0, sticky=W, padx=5, pady=2)

        self.txt_der_modif_par = ttk.Entry(AttrFrame, font=("times new roman",12))
        self.txt_der_modif_par.grid(row=3, column=1, sticky=W, padx=5, pady=2)







if __name__ =="__main__":
    w=PumpTest()
    w.mainloop()
