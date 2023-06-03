from tkinter import *
from tkinter import ttk, messagebox
import tempfile
import random
from PIL import ImageTk, Image
from tkcalendar import *
import mysql.connector
import os
from forage_desc import*
from Forage2 import*
from equipement import*
from EssaiPompage import*
from Rehabilitation import*
from sequenceGeo import*
from exploitationFor import*
from MesureEau import*
from QualiteEau import*
from document import*

class Description(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("NOUVEAU FORAGE")
        self.geometry("850x550+400+200")
        self.config(bg="silver")
        self.grab_set()
        self.resizable(0,0)
        self = ttk.Notebook()
        self.place(x=0, y=0)

        Local_btn = Forage_desc()
        self.add(Local_btn,text="Localisation")

        forg_btn = Forage2()
        self.add(forg_btn,text="Forage")

        eqpmt_btn = Equipmt()
        self.add(eqpmt_btn,text="Equipement")

        Edp_btn = PumpTest()
        self.add(Edp_btn,text="Essai de pompages")

        Rhbl_btn = Rehabilit()
        self.add( Rhbl_btn,text="Réhabilitation")

        Seq_btn = SequenceGeo()
        self.add(Seq_btn,text="Séquence Géologique")

        Exp_btn = exploitation()
        self.add(Exp_btn,text="Exoploitation Forage")

        Msr_btn = MesureEau()
        self.add(Msr_btn,text="Mesure eaux")

        qual_btn = QualiteEau()
        self.add(qual_btn,text="Qualité de l'eau")

        doc_btn = Document()
        self.add(doc_btn,text="Documents")
        











if __name__ =="__main__":
    w=Description()
    w.mainloop()