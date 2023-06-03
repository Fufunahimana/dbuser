from tkinter import *
from tkinter import ttk, messagebox
import tempfile
import random
from PIL import ImageTk, Image
from tkcalendar import *
import mysql.connector
import os

class Requete(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Request")
        self.geometry("650x450+400+200")
        self.config(bg="silver")
        self.grab_set()
        self.resizable(0,0)

        title = Label(self, text="CHOISIR UNE REQUETE",bd=20, relief= RAISED, font=('Antiqua', 20, "bold"),bg='cyan', fg='black')
        title.place(x=0,y=0, width=650)

        btn_Req_is = Button(self, text="Requête sur les isolignes...",cursor="hand2",font=("Times new roman",18, "bold"), bd=0, bg="yellow", fg="black")
        btn_Req_is.place(x=170,y=170)
        
        btn_Req_ser_chron = Button(self, text="Requêtes sur les séries chroniques...",cursor="hand2", font=("Times new roman",18, "bold"), bd=0, bg="yellow", fg="black")
        btn_Req_ser_chron.place(x=170, y=230)

        btn_Req_donn_gen = Button(self, text="Requêtes sur les données générales...",cursor="hand2", font=("Times new roman",18, "bold"), bd=0, bg="yellow", fg="black")
        btn_Req_donn_gen.place(x=170, y=300)

        btn_quit_req = Button(self, text="Quiter",cursor="hand2", font=("Times new roman",18, "bold"), bd=0, bg="red", fg="black",)
        btn_quit_req.place(x=550, y=400)












if __name__ =="__main__":
    w=Requete()
    w.mainloop()
