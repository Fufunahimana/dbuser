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
from ajoutExploitation import*

class Description(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("DESCRIPTION")
        self.geometry("850x550+400+200")
        self.config(bg="silver")
        self.grab_set()
        self.resizable(0,0)

        desc = ttk.Notebook(self)
        desc.place(x=0, y=0,height=550)

    
        Local_btn = Forage_desc()
        desc.add(Local_btn,text="Localisation")

        forg_btn = Forage2()
        desc.add(forg_btn,text="Forage")

        eqpmt_btn = Equipmt()
        desc.add(eqpmt_btn,text="Equipement")

        Edp_btn = PumpTest()
        desc.add(Edp_btn,text="Essai de pompages")

        Rhbl_btn = Rehabilit()
        desc.add( Rhbl_btn,text="Réhabilitation")

        Seq_btn = SequenceGeo()
        desc.add(Seq_btn,text="Séquence Géologique")

        Exp_btn = exploitation()
        desc.add(Exp_btn,text="Exoploitation Forage")

        Msr_btn = MesureEau()
        desc.add(Msr_btn,text="Mesure eaux")

        qual_btn = QualiteEau()
        desc.add(qual_btn,text="Qualité de l'eau")

        doc_btn = Document()
        desc.add(doc_btn,text="Documents")
        

if __name__ =="__main__":
    w=Description()
    w.mainloop()