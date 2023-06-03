from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import *
import mysql.connector
import os

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("CONNEXION")
        self.root.geometry("800x450+400+200")
        self.root.config(bg="white")
        self.root.focus_force()
        
         ###############les divers champs#########################

        logo1 = Frame(self.root, bd=5, relief=GROOVE, bg="white").place(x=0, y=0,width=300,height=150)
        logo2 = Frame(self.root, bd=5, relief=GROOVE, bg="gray").place(x=0, y=150,width=300,height=150)
        logo3 = Frame(self.root, bd=5, relief=GROOVE, bg="white").place(x=0, y=300,width=300,height=150)

        infoDb = Frame(self.root, bd=5, relief=GROOVE, bg="lavender").place(x=300, y=0,width=500,height=150)
        infoUser = Frame(self.root, bd=5, relief=GROOVE, bg="beige").place(x=300, y=150,width=500,height=150)
        loginBut= Frame(self.root, bd=5, relief=GROOVE, bg="silver").place(x=300, y=300,width=500,height=150)

        infoDb_title= Label(infoDb, text="GEOHYDROBASE", font=("times new roman",35,"bold"), bg="lavender").place(x=350, y=50)
         
              ##################information de l'utilisateur de la base des données ###########

        db = Label(infoUser, text= "Base des données",font=("times new roman",15),bg="beige").place(x=320, y=160)
        db_text = Entry(infoUser, font=("times new roman",15), bg="white").place(x=500, y=160, width=250)
        lbl_user = Label(infoUser, text= "Nom d'utilisateur",font=("times new roman",15),bg="beige").place(x=320, y=200)
        self.ecrit_user_text = Entry(infoUser, font=("times new roman",15), bg="white")
        self.ecrit_user_text.place(x=500, y=200, width=250)
        lbl_pwd = Label(infoUser, text= "Votre mot de passe",font=("times new roman",15),bg="beige").place(x=320, y=240)
        self.ecrit_pwd = Entry(infoUser, show="*", font=("times new roman",15), bg="white")
        self.ecrit_pwd.place(x=500, y=240, width=250)

      ####################les boutons pour la connection de la base des données##############################

        ipAdress_btn = Button(loginBut, text="CHANGER IPADRESS",cursor="hand2", font=("Latha",15, "bold"), bd=0, bg="olive", fg="blue")
        ipAdress_btn.place(x=550, y= 330)

        connect_btn = Button(loginBut, text="SE CONNECTER",cursor="hand2", font=("Latha",15, "bold"), bd=0, bg="green", fg="blue")
        connect_btn.place(x=320, y= 380)

        quit_btn = Button(loginBut, text="QUITER",cursor="hand2", font=("Latha",15, "bold"), bd=0, bg="red", fg="blue")
        quit_btn.place(x=670, y= 380)
        
        def quit(self):
            self.root.destroy()
        
root=Tk()
obj =Login(root)
root.mainloop()