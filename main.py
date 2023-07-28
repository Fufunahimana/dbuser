from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import *
from datetime import datetime 
from time import strftime
from PIL import ImageTk, Image
import mysql.connector
import psycopg2 
import os
from Forage2 import*
from forage import*
from Requete import*
from equipement import*
from EssaiPompage import*
from Rehabilitation import*
from sequenceGeo import*
from exploitationFor import*
from MesureEau import*
from QualiteEau import*
from document import*
from DescriptionFor import*
from selectionnerPE import*

#from databaseAdm import*

#############################fonctionalité de l'application#######################
def quit():
    root.destroy()
    
def forage():
    Forage()

def requete():
     Requete()
def PE_select():
     Selectione()
     

def quit():
  root.destroy()

global nom_u
global nom_gr

def connexion():
    global user
    global host
    N_user= user_text.get()
    N_pwd = ecrit_pwd.get()
    
    if user_text.get()=="" or ecrit_pwd.get() =="":
        messagebox.showerror("Erreur", "Veiller Saisir Email et le mot de passe")
        
    else:
        try:
            global db
            host="192.168.88.201"
            Database= "hydrogeology"
            userM="postgres"
            password= "igebu99"  
            mydb = psycopg2.connect(host=host,database=Database, user=userM, password=password)
            mycursor = mydb.cursor()
            mycursor.execute("select * from pg_user where usename=%s and passwd=%s", (N_user, (N_pwd),))
            row = mycursor.fetchall()
            
            print(row)
            
            if row == None:
                messagebox.showerror("Erreur","le nom d'utisisateur et le mot de passe invalides",parent=root)
              
            else:
                #messagebox.showinfo("Réussite", "Bienvenu")
                quit()
                root1 = Tk()
                root1.title("CONNEXION")
                root1.geometry("1500x900+0+0")
                root1.config(bg="white")
                root1.update_idletasks()
                #time.sleep(2)
                root1.focus_force()
                root1.iconbitmap('igebulogo.ico')
                
                #mainframe = Frame(root, bd=5, relief=GROOVE, bg="white")
                #mainframe.place(x=0, y=0,width=1480,height=880)
                
                def heure():
                        heur=strftime("%H:%M:%S")
                        lblheure.config(text=heur)
                        lblheure.after(1000,heure)
                    
                    
                lblheure = Label(root1, text="HH:MM:SS", font=("times new roman", 15, "bold"),bg="white", fg="black")
                lblheure.grid(row=0, column=0, sticky=W, padx=5, pady=5)
                
                heure()
                
                Part1 = Frame(root1, bd=5, relief=GROOVE, bg="white")
                Part1.place(x=0, y=50,width=300,height=770)
                Part2 = Frame(root1, bd=5, relief=GROOVE, bg="yellow")
                Part2.place(x=300, y=50,width=1255,height=300)
                
                scroll_x = Scrollbar(Part2, orient=HORIZONTAL)
                scroll_x.pack(side=BOTTOM, fill=X)
                
                scroll_y = Scrollbar(Part2, orient=VERTICAL)
                scroll_y.pack(fill=Y,side=LEFT)
                
                def affich_result(): 
                    host="192.168.88.201"
                    db= "hydrogeology"
                    userM="postgres"
                    password= "igebu99"  
                    mydb = psycopg2.connect(host=host,database=db, user=userM, password=password)
                    mycursor = mydb.cursor()
                    mycursor.execute("select * from tbl_localisation")
                    rows = mycursor.fetchall()
                    if len(rows)!=0:
                        tabl_result.delete(*tabl_result.get_children())
                        for row in rows:
                            tabl_result.insert("",END, values=row)
                         
                    mydb.commit()
                    mydb.close()
                    
                def quiter():
                    root1.destroy()
                    
                
                columns=("id","id_orginal","longitude","latitude","latlong_méthode","altitude_z","altitude_méthode","type_point_d_eau","périmètres_de_protection","province","commune","colline","sous_colline","projet","sous_la_responsabilité","entrée_provisoire","remarque","dernière_date_modification","dernière_modification_par")
                
                tabl_result = ttk.Treeview(Part2, columns=columns,show="headings", yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
                     
                scroll_x.config(command=tabl_result.xview)
                scroll_y.config(command=tabl_result.yview)
                
                tabl_result.heading("id", text="id")
                tabl_result.heading("id_orginal", text="id_orginal")
                tabl_result.heading("longitude", text="longitude")
                tabl_result.heading("latitude", text="latitude")
                tabl_result.heading("latlong_méthode", text="latlong_méthode")
                tabl_result.heading("altitude_z", text="altitude_z")
                tabl_result.heading("altitude_méthode", text="altitude_méthode")
                tabl_result.heading("type_point_d_eau", text="type_point_d_eau") 
                tabl_result.heading("périmètres_de_protection", text="périmètres_de_protection")
                tabl_result.heading("province", text="province")
                tabl_result.heading("commune", text="commune")
                tabl_result.heading("colline", text="colline")
                tabl_result.heading("sous_colline", text="sous_colline")
                tabl_result.heading("projet", text="projet")
                tabl_result.heading("sous_la_responsabilité", text="sous_la_responsabilité")
                tabl_result.heading("entrée_provisoire", text="entrée_provisoire")
                tabl_result.heading("remarque", text="remarque")
                tabl_result.heading("dernière_date_modification", text="dernière_date_modification") 
                tabl_result.heading("dernière_modification_par", text="dernière_modification_par")
                
                
                tabl_result.pack(fill=Y,side=LEFT)
                
                affich_result()
                
   
                ##############entête #######################
                
                global nom_u
                global nom_db
                global nom_gr 
                user = Label(root1,text='Utilisateur', font=("times new roman",12), bg="gray",width=17)
                user.grid(row=0, column=2, sticky=W, padx=2, pady=5)
                
                nom_u = Entry(root1, font=("times new roman",12), bg="olive",width=17)
                nom_u.grid(row=0, column=3, sticky=W, padx=2, pady=5)
                nom_u.insert(END, N_user)
                
                Group = Label(root1,text='Groupe', font=("times new roman",12), bg="cyan",width=17)
                Group.grid(row=0, column= 4, sticky=W, padx=2, pady=5)
                
                nom_gr = Entry(root1, font=("times new roman",12), bg="beige",width=17)
                nom_gr.grid(row=0, column= 5, sticky=W, padx=2, pady=5)
                
                serveur = Label(root1,text='Serveur', font=("times new roman",12), bg="lavender",width=17)
                serveur.grid(row=0, column= 6, sticky=W, padx=2, pady=5)
                
                id_serv = Entry(root1, font=("times new roman",12), bg="khaki",width=17)
                id_serv.grid(row=0, column= 7, sticky=W, padx=2, pady=5)
                id_serv.insert(END,host)
                
                db = Label(root1,text='Database', font=("times new roman",12), bg="silver",width=17)
                db.grid(row=0, column= 8, sticky=W, padx=2, pady=5)
                
                
                nom_db = Entry(root1, font=("times new roman",12), bg="brown",width=17)
                nom_db.grid(row=0, column= 9, sticky=W, padx=2, pady=5)
                nom_db.insert(END, Database)
                
                #############boutons divers###########################
              
                NPE_btn = Button(Part1, text="Nouveau point d'eau",cursor="hand2",command=forage,font=("Times new roman",14, "bold"),width=22, bg="cyan", fg="black",relief=GROOVE)
                NPE_btn.grid(row=0, sticky=W, padx=5, pady=2)
                
                MPE_btn = Button(Part1, text="Modifier un Point d'eau",cursor="hand2", font=("Times new roman",14, "bold"),width=22,bg="silver", fg="black",relief=GROOVE)
                MPE_btn.grid(row=1, sticky=W, padx=5, pady=2)
                
                SPE_btn = Button(Part1, text="Supprimer un Point d'eau",cursor="hand2", font=("Times new roman",14, "bold"),width=22, bg="silver", fg="black",relief=GROOVE)
                SPE_btn.grid(row=2, sticky=W, padx=5, pady=2)
                
                RQT_btn = Button(Part1, text="Requêtes",cursor="hand2",command=requete, font=("Times new roman",14, "bold"),width=22, bg="silver", fg="black",relief=GROOVE)
                RQT_btn.grid(row=3, sticky=W, padx=5, pady=2)
                
                SelPE_btn = Button(Part1, text="Selectionner un Point d'eau",cursor="hand2",command=PE_select, font=("Times new roman",14, "bold"),width=22, bg="silver", fg="black",relief=GROOVE)
                SelPE_btn.grid(row=4, sticky=W, padx=5, pady=2)
                
                
                IPE_btn = Button(Part1, text="Importer un Point d'eau",cursor="hand2",font=("Times new roman",14, "bold"),width=22, bg="silver", fg="black",relief=GROOVE)
                IPE_btn.grid(row=5, sticky=W, padx=5, pady=2)
                
                SRT_btn = Button(Part1, text="Quiter",cursor="hand2",command=quiter, font=("Times new roman",14, "bold"),width=22, bg="red", fg="black",relief=GROOVE)
                SRT_btn.grid(row=6, sticky=W, padx=5, pady=2)
                
                ####################partie numero 3######################################
                Part3 = ttk.Notebook(root1)
                Part3.place(x=300, y=350,width=1255,height=470)
                
                forg_btn = Forage2()
                Part3.add(forg_btn,text="Forage")
                
                eqpmt_btn = Equipmt()
                Part3.add(eqpmt_btn,text="Equipement")
                
                Edp_btn = PumpTest()
                Part3.add(Edp_btn,text="Essai de pompages")
                
                Rhbl_btn = Rehabilit()
                Part3.add( Rhbl_btn,text="Réhabilitation")
                
                Seq_btn = SequenceGeo()
                Part3.add(Seq_btn,text="Séquence Géologique")
                
                Exp_btn = exploitation()
                Part3.add(Exp_btn,text="Exoploitation Forage")
                
                Msr_btn = MesureEau()
                Part3.add(Msr_btn,text="Mesure eaux")
                
                qual_btn = QualiteEau()
                Part3.add(qual_btn,text="Qualité de l'eau")
                
                doc_btn = Document()
                Part3.add(doc_btn,text="Documents")
                
        except psycopg2.OperationalError:
            messagebox.showerror("Erreur","Impossible d'acceder au serveur!!")
            messagebox.askretrycancel("askretrycancel", "Try again?")
            connexion()
root = Tk()
root.title("CONNEXION")
root.geometry("800x450+400+200")
root.config(bg="white")
root.iconbitmap('igebulogo.ico')
root.focus_force()
        
         ###############les divers champs#########################

logo1 = Frame(root, bd=5, relief=GROOVE, bg="white").place(x=0, y=0,width=300,height=150)
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    day_string = strftime("%A")
    day_label.config(text=day_string)
    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)
    label.after(1000,time)
    

label = Label(logo1,font=("ds-digital",35),background="black",foreground="cyan")
label.place(x=5,y=5,width=290,height=80)
day_label = Label(logo1,font=("Monotype Corsiva",20,"bold"),background="black",foreground="green")
day_label.place(x=5,y=87,width=290,height=30)

date_label = Label(logo1,font=("Elephant",15),background="black",foreground="yellow")
date_label.place(x=5,y=120,width=290,height=25)

time()

canvas_for_image = Canvas(root, bg='green', height=150, width=300, borderwidth=0, highlightthickness=0)
canvas_for_image.place(x=0, y=150,width=300,height=150)

# create image from image location resize it to 300X150 and put in on canvas

image = Image.open('logoIgebu.jpg')
canvas_for_imaget = ImageTk.PhotoImage(image.resize((300, 150), Image.LANCZOS))
canvas_for_image.create_image(0, 0, image=canvas_for_imaget, anchor='nw')



canvas_for_image2 = Canvas(root, bg='green', height=150, width=300, borderwidth=0, highlightthickness=0)
canvas_for_image2.place(x=0, y=300, width=300,height=150)

# create image from image location resize it to 300X150 and put in on canvas

image = Image.open('blassonUnite.jpg')
canvas_for_imaget2 = ImageTk.PhotoImage(image.resize((300, 150), Image.LANCZOS))
canvas_for_image2.create_image(0, 0, image=canvas_for_imaget2, anchor='nw')

infoDb = Frame(root, bd=5, relief=GROOVE, bg="lavender").place(x=300, y=0,width=500,height=150)
infoUser = Frame(root, bd=5, relief=GROOVE, bg="beige").place(x=300, y=150,width=500,height=150)
loginBut= Frame(root, bd=5, relief=GROOVE, bg="silver").place(x=300, y=300,width=500,height=150)

infoDb_title= Label(infoDb, text="GEOHYDROBASE", font=("times new roman",35,"bold"), bg="lavender").place(x=350, y=50)
         
##################information de l'utilisateur de la base des données ###########


db = Label(infoUser, text= "Base des données",font=("times new roman",15),bg="beige").place(x=320, y=160)
db_name = ttk.Combobox(infoUser, font=("times new roman",15),width=25,values= ("Hydrogeology", "hydrology","meteology"),state="readonly")
db_name.place(x=500,y=160, width=250)
db_name.current(0)
lbl_user = Label(infoUser, text= "Nom d'utilisateur",font=("times new roman",15),bg="beige").place(x=320, y=200)
user_text = Entry(infoUser, font=("times new roman",15), bg="white")
user_text.place(x=500, y=200, width=250)

#user_text.insert(END,)
lbl_pwd = Label(infoUser, text= "Votre mot de passe",font=("times new roman",15),bg="beige").place(x=320, y=240)
ecrit_pwd = Entry(infoUser, show="*", font=("times new roman",15), bg="white")
ecrit_pwd.place(x=500, y=240, width=250)
ecrit_pwd.insert(END,79166956)

####################les boutons pour la connection de la base des données##############################

ipAdress_btn = Button(loginBut, text="CHANGER IPADRESS",cursor="hand2", font=("Latha",15, "bold"), bd=0, bg="olive", fg="blue")
ipAdress_btn.place(x=550, y= 330)

connect_btn = Button(loginBut, text="SE CONNECTER",cursor="hand2",command=connexion, font=("Latha",15, "bold"), bd=0, bg="green", fg="blue")
connect_btn.place(x=320, y= 380)

quit_btn = Button(loginBut, text="QUITER",cursor="hand2",command=quit, font=("Latha",15, "bold"), bd=0, bg="red", fg="blue")
quit_btn.place(x=670, y= 380)
     

root.mainloop()