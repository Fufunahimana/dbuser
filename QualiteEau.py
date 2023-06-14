from tkinter import *
from tkinter import ttk, messagebox
import tempfile
import random
from PIL import ImageTk, Image
from tkcalendar import *
import mysql.connector
import os

class QualiteEau(Frame):
    def __init__(self):
        super().__init__()
        self.config(bg="silver")


        scroll_x = Scrollbar(self, orient=HORIZONTAL)
        scroll_y = Scrollbar(self, orient=VERTICAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT)

        columns=("No.","id","id_original","sample_ID","date_heure","nom_du_laboratoire","lab_certification","lab_reference,remarque",
                "na_mgl","k_mgl","ca2_mgl","mg2_mgl","nh4_mgl","li_mgl","hco3_mgl","co32_mgl","so42_mgl","no3_mgl",
                 "no2_mgl","cl_mgl","cn_mgl","po43_mgl","br_mgl","mn_mgl","fe2_mgl","fe3_mgl","cr_total_mgl","ni_mgl","pb_mgl","cu_mgl",
                 "zn_mgl","cd_mgl","ba_mgl","be_mgl","co_mgl","sc_mgl","sr_mgl","th_μgl","ti_mgl","u_mgl","v_mgl,","fe_mgl","sio2_mgl",
                 "al_mgl","b_mgl","bo2_mgl","as_total_mgl","od_mgl","tds_mgl","ph","bod5_mgl","hydrocarbure_c6_c25_mgl","pah_mgl",
                 "organochlorés_mgl","btex_mgl","cod_mgl","turbidité","coliformes_totaux","coliformes_thermo_tolerant","escherichia_coli",
                 "entérocoques","d18o","d18o_sd","d2h","d2h_sd","d13c","d13c_sd","d15n"	"d15n_sd","d3h","d3h_sd","d14c","d14c_sd","u234","u235",
                 "u238","ra226","ra228","pb210","po210","dti","ec","ph1","o2_mgl","redox_p","deuterium_excess","ag_μgl","al_μgl,as_μgl","b_μgl",
                 "ba_μgl","be_μgl","bi_μgl","br_μgl","ca_μgl","cd_μgl","ce_μgl","co_μgl","cr_μgl","cs_μgl","cu_μgl","dy_μgl,er_μgl","eu_μgl",
                 "fe_μgl","ga_μgl","gd_μgl","ge_μgl","hf_μgl","hg_μgl","ho_μgl","i_μgl","k_μgl","la_μgl","li_μgl","lu_μgl","mg_μgl","mn_μgl","mo_μgl",
                 "na_μgl","nb_μgl","nd_μgl","ni_μgl","pb_μgl","pr_μgl","sb_μgl","sc_μgl","se_μgl","sm_μgl","sn_μgl","sr_μgl","ta_μgl","tb_μgl","te_μgl",
                 "tl_μgl","tm_μgl","u_μgl","v_μgl","w_μgl","y_μgl","yb_μgl","zn_μgl","zr_μgl","rb_μgl","pk")
        
        self.tabl_result = ttk.Treeview(self, columns=columns,show="headings", yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        
        for i in columns:
            self.tabl_result.heading(i, text=i)

        scroll_x.config(command=self.tabl_result.xview)
        scroll_y.config(command=self.tabl_result.yview)
        self.tabl_result.pack(fill=Y,side=LEFT)


        BtnFrame = Frame(self, bd=5, relief=GROOVE, bg="white")
        BtnFrame.place(x=0, y=390,width=1237, height=40)

        IPE_btn = Button(BtnFrame, text="search",cursor="hand2", font=("Times new roman",10, "bold"),width=10, bg="silver", fg="black")
        IPE_btn.grid(row=0, column= 0, sticky=W, padx=50, pady=2)

        IPE_btn = Button(BtnFrame, text="Showall",cursor="hand2", font=("Times new roman",10, "bold"),width=10, bg="silver", fg="black")
        IPE_btn.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        IPE_btn = Button(BtnFrame, text="Importer",cursor="hand2", font=("Times new roman",10, "bold"),width=10, bg="cyan", fg="black")
        IPE_btn.grid(row=0, column= 2, sticky=W, padx=5, pady=2)

        IPE_btn = Button(BtnFrame, text="Ajouter",cursor="hand2", font=("Times new roman",10, "bold"),width=10, bg="green", fg="black")
        IPE_btn.grid(row=0, column=3, sticky=W, padx=5, pady=2)
        
        IPE_btn = Button(BtnFrame, text="Modifier",cursor="hand2", font=("Times new roman",10, "bold"),width=10, bg="yellow", fg="black")
        IPE_btn.grid(row=0, column= 4, sticky=W, padx=5, pady=2)

        IPE_btn = Button(BtnFrame, text="Supprimer",cursor="hand2", font=("Times new roman",10, "bold"),width=10, bg="red", fg="black")
        IPE_btn.grid(row=0, column=5, sticky=W, padx=5, pady=2)







if __name__ =="__main__":
    w=QualiteEau()
    w.mainloop()