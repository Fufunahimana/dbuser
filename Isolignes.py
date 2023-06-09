from tkinter import *
from tkinter import ttk, messagebox
import tempfile
import random
from PIL import ImageTk, Image
from tkcalendar import *
import mysql.connector
import os


class RequeteIso(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("NOUVEAU FORAGE")
        self.geometry("810x700+450+50")
        self.config(bg="white")
        self.grab_set()
        self.resizable(0,0)
        global comm
        
        ##########################LES LISTES UTILISEES##############################

        
        province = ["Bubanza","Bujumbura Marie","Bujumbura Rural","Bururi","Cankuzo","Cibitoke","Gitega","Karuzi","Kayanza","Kirundo","Makamba","Muramvya","Muyinga","Mwaro","Ngozi","Rumonge","Rutana","Ruyigi"]
        
        Prov_Bubanza = ["Bubanza","Gihanga","Musigati","Mpanda","Rugazi"]
        
        Col_Bubanza=["Cimbizi","Rugunga","Zina","Rurabo","Muhanza","Centre Ville","Gitanga","Karinzi","Ciya","Mugimbu","Mwanda","Gahongore","Kivyiru","Muramba","Buhororo I","Buhororo II","Shari I","Shari II","Gatura","Mitakataka","Ngara","Nyabitaka","Muhenga"]
        Col_Gihanga=["Buringa","Ninga V4","Bwiza Bwa Ninga V6","NYESHANGA","MURIRA V2","Rugungu","Kagwema","Gihungwe","Rumotomoto","Gihanga","Kizina","Mpanda V5","Buramata","Ndava Busongo"]
        Col_Musigati=["Mugoma","Dondi","Nyarusange","Rushiha","Ntamba","Munanira","Kiziba","Gashinge","Rusekabuye","Rugeyo","Butaha","Bubenga","Muyebe","Masare","Ruvyimvya","Mpishi","Kanazi","Busiga","Gatara","Kayange","Bukinga","Musigati","Mugombarima","Buhurika"]
        Col_Mpanda=["Murengeza","Gatagura","Butanuka","Ruziba","Butembe","Kanenga","Masha","Nyomvyi","Rubira","Nyamabere","Gahwazi I","Gahwazi II","Rugenge","Gifurwe","Musenyi"]
        Col_Rugazi=["Kibenga","Muzinda","Kayange","Bugume","Butavuka","Kirengane","Rugazi","Karambira","Kibuye","Rutake","Nyenkarange","Ruce","Kabanga","Rwamvurwe"]
        
        Prov_Bujumbura_Mairie=["Muha","Mukaza","Ntahangwa"]
        
        Col_Muha=["Gitaramuka","Kibenga","Kamesa","OUA ZEIMET","Kinindo","Gasekebuye","Kinanira II","Kinanira I","Kinanira I et II","Kinanira III","Musama","Kajiji","Nkenga Busoro","Nyabugete","Gisyo Nyabaranda","Ruziba","Kizingwe Bihara"]
        Col_Mukaza=["Q IV","Q III","Q I","Q IV","Q VII","Q II","Q V","Q VI","Q III","Nyakabiga III","Kigwati","Nyakabiga II","Nyakabiga I","Q VII","Q I","Q II","Q V","Q VI","Asiatique","Kabondo","Mutanga sud Sororezo Mugoboka","Kiriri Vugizo","Rohero II","Rohero I Gatoke","INSS","Centre Ville"]
        Col_Ntahangwa=["Q VIII","Q I","Q II","Q VI","Kanga","Buterere II B","Mubone","Gasenyi","Mugaruro","Kabusa","Kiyange II","Kiyange I","Buterere I","Buterere II A","Kavumu","Heha","Gituro","Mirango I","Mirango II","Songa","Twinyoni","Gikizi","Teza","Q II","Q I","Q IV","Q V","Q VII","Q VI","Nyabagere","Winterekwa","Taba","Muyaga","Gikungu Gihosha Rural","Q IX","Gihosha","Gikungu II","Gikungu I","Q IV","Q VII","Q V","Q III","Buhinyuza","Gatunguru","Bukirasazi I","Bururi","Gitega","Ngozi","Muramvya","Ruyigi","Bukirasazi II","Bubanza","Carama","Q Industriel","Muyinga","Socarti","Q III"]
        
        Prov_Bujumbura_rural=["Isale","Kabezi","Kanyosha","Mubimbi","Mugongomanga","Mukike","Mutambu","Mutimbuzi","Nyabiraba"]
        
        Col_Isare=[""]
        Col_Kabezi=["Masama","Mwaza","Kimina","Migera","Gitenga","Kabezi","Kiremba","Mena","Rugembe","Mubone","Gakungwe","Ramba"]
        Col_Kanyosha=[""]
        Col_Mubimbi=["Burenza","Karugamba","Mageyo","Muhororo","Muyabara","Magarure","Muzazi","Kigunga","Butega","Kanyinya","Mubimbi","Kiziba","Nyankunda","Gisagara","Buhanda","Gitwe"]
        Col_Mugongomanga=["Nyarushanga","Mugoyi","Jenda","Nyamugari","Rutambiro","Gisarwe","Mwura","Murunga","Mugongo","Butaganzwa","Kibira","Buhoro","Centre Urbain","Rwibaga","Kayoyo"]
        Col_Mukike=["Ruzibazi","Nyarumanga","Rurambira","Mayuyu","Mutobo","Ruhororo","Bikanka","Kigozi","Ndayi","Rukina","Kanyunya"]
        Col_Mutambu=["Gomvyi","Rutovu","Gakara","Nyankere","Ntobo","Ruvyagira","Masenga","Buhanda","Nyarwedeka","Bubanza","Murambi","Rubanda","Burima II","Burima I","Rukingiro","Bugongo"]
        Col_Mutimbuzi=["Muyange Rubirizi","Mushasha I","Mushasha II","Kinyinya II Gatumba","Muyange I Gatumba","Vugiwo","Warubondo","Gaharawe","Kinyinya I Gatumba","Muyange II Gatumba","Kirwati II","Gahwama","Kinyinya III Rukaramu","Kinyinya I Rukaramu","Kinyinya II Rukaramu","Kirwati I","Kirekura T12","Maramvya IV, T12","Maramvya III, T13","Kirekura T13","Budahirwa","Mutara","Maramvya II, T14","Kirekura T14","Rubirizi","Nyabunyegeri","Tenga","Kirekura T15","Maramvya I, T15","Gahahe","Maramvya"]
        Col_Nyabiraba=["Musenyi","Kinyami","Mayemba","Gasarara","Mbare","Bubaji","Nyabibondo","Nyabiraba","Mwumba","Kizunga","Mukonko","Karama","Matara","Mwumba","Raro","Kinama","Kigina","Mugendo"]
        
        Prov_Bururi=["Bururi","Matana","Mugamba","Rutovu","Songa","Vyanda"]
        
        Col_Bururi=["Rukanda","Burunga","Mubuga","Gisanze","Mahonda","Nyavyamo","Nyarugera","Muzima","Rushemeza","Buhinga","Burenza","Nyagwaga","Karwa","Ruvumu","Nyamiyaga","Kiremba-Ville","Kiremba-rural","Gatanga","Muyange","Jugwe","Burarana","Gaharo","Gasenyi","Mudahandwa","Tongwe","Kiganda","Bururi Centre-Urbain","Mugozi","Murago","Munini"]
        Col_Matana=["Bihanga","Bitezi","Butwe","Mahango","Ntega","Gitanga","Sakinyonga","Kinyinya","Gisisye","Gisarenda","Ruzira","Matana","Matana","Mugano"]
        Col_Mugamba=["Kibezi","Donge-Ruzi","Musho","Mpota","Mutobo","Kivumu","Donge-Burasira","Munini","Mwumba","Gozi","Taba","Nyatubuye","Coma","Muyange-Kavumu","Gitaramuka","Kirinzi","Rukere","Nyakimonyi","Mukike","Gakaranka","Mubira","Ruhinga","Mugendo-Ruko","Nyamugari","Nyakigano","Mugendo-Ndengo","Gitaka","Kigina-Mugomera","Gataka","Vyuya"]
        Col_Rutovu=["Rutoke","Muhweza","Kajondi","Ruringanizo","Gihanga","Muzenga","Musongati","Mutangaro","Gikwa","Sanzu","Nyabucokwe","Kagimbu","Kivubo","Gitobo","Kinyonzo","Rwamabuye-Gikana","Mwarusi","Gikizi","Musenyi","Ruhando","Kijima","Munyinya"]
        Col_Songa=["Ndago","Muheka","Musenyi","Kigabiro","Taba","Muzamba","Songa","Mutsinda","Jenda","Rusama","Tara","Yengero","Rutundwe","Kiryama","Kinwa","Rwego","Gahanda"]
        Col_Vyanda=["Karirimvya","Karehe","Kabwayi","Rweza","Nyakabenga","Kagoma","Migera","Mushishi","Gitwaro","Gihinga","Bwatemba","Bugeni","Mubuga","Ntunda","Mirango","Kirungu","Kigutu"]
        
        Prov_Cankuzo=["Cankuzo","Cendajuru","Gisagara","Kigamba","Mishiha"]
        
        Col_Cankuzo=["Karago","Kigusu","Gatungurwe","Mugozi","Kavumu","Musenyi","Murehe","Rutoke","Nyakerera","Nyabisindu","Nyamusenga","Mugenda","Muyaga","Gahoko","Nyarutiti","Muterero","Kabeza","Kabuga","Muhweza","Cankuzo","Nyakivumu"]
        Col_Cendajuru=["Nyamugari","Gashingwe","Busyana","Gitaramuka","Rukoyoyo","Cendajuru","Kiyange","Kabageni","Nyagisovu","Misugi","Gisoro","Kigarika","Twinkwavu","Nyakuguma","Mugongo","Kibande","Kiruhura"]
        Col_Gisagara=["Muganza","Bunyerere","Kibogoye","Nyuro","Gisagara","Gitanga","Ruramba","Gerero","Rabiro","Muzire","Bumba","Nkoro","Mburi","Kagoma","Gitwenge","Rubabara","Kirambi","Ramba","Murago","Gisoko","Camazi","Kigati","Muhingamo"]
        Col_Kigamba=["Nyarurambi","Kigamba","Kivumu","Rusagara","Rwanvura","Saswe","Gitanga","Kibungo","Shinge","Buyongwe","Mashinga","Rujungu","Humure I","Humure II"]
        Col_Mishiha=["Rugerero","Mwiruzi","Musemo","Busumanyi","Rutsindu","Mishiha","Buyongwe","Munzenze","Kaniha","Mugera","Rukrwega","Kibimba"]
        
        
        Prov_Cibitoke=["Buganda","Bukinanyana","Mabayi","Mugina","Murwi","Rugombo"]
        
        Col_Buganda=["Ndava village","Kaburantwa","Mwunguzi","Murambi","Cunyu","Gasenyi Rural","Ruhagarika","Gasenyi Centre","Kansenga","Muremera","Nimba","Nyamitanga"]
        Col_Bukinanyana=["Nyamyeha","Burimbi I","Giserama","Kibaya I Ndora","Kibati","Myave","Nyarwumba","Sehe","Nyarubugu","Nyangwe","Nyampinga","Nderama","Rusenda","Rangira","Shimwe","Gahabura","Murengera","Butara","Runege","Mikoni","Kibaya II Gah","Tyazo","Bihembe","Bitare","Burimbi II","Masango","Ruhembe","Bumba","Munyinya"]
        Col_Mabayi=["Buhoro","Nyarusebeyi","Kabere","Mukaka","Miremera","Gasebeyi","Ruhororo","Gahoma","Nyabungere","Muhungu","Gakerekwa","Mageyo","Rutorero","Gafumbegeti","Rushiha","Nyagaseke","Kibande","Gitukura","Rungogo","Mukoma","Mayuki","Busesa","Rumvya"]
        Col_Mugina=["Mugina","Rubirizi","Camakombe","Gitebe","Rugajo","Rugendo","Gitumba","Rushimabarimyi","Nyamakarabo","Nyempundu","Ruziba","Marumpu","Ngoma","Nyamihana","Rubona","Kagurutsi","Mwarangabo","Rusagara","Kirinzi","Butaramuka","Bwayi","Muyange"]
        Col_Murwi=["Kabuye","Kagimbu","Mushanga","Mugimbu","Mirombero","Kivunvu","Bubogora","Mahande","Nyarurinzi","Nyabubuye","Rugano","Ngoma","Remera","Kajerama","Buhindo","Butega","Kahirwa","Gitohera","Manege","Masha","Murwi","Muzenga","Buhayira","Gasheke","Jerama","Maranga","Gitera"]
        Col_Rugombo=["Rusororo","Musenyi","Gicaca","Munyika I","Rukana I","Rukana II","Kagazi","Mparambo II","Mparambo I","Munyika II","Gabiro-Rvyag","Samwe","Rugeregere","Kiramira","Ruvumera","Rusiga","Cibitoke"]
        
        Prov_Gitega=["Bugendana","Bukirasazi","Buraza","Giheta","Gishubi","Gitega","Itaba","Makebuko","Mutaho","Nyarusange","Ryansoro"]
        
        Col_Bugendana=["Gitongo","Carire","Kibasi","Jenda","Mirama","Runyeri","Bitare","Rwingiri","Mwurire","Gitora","Rushanga","Nyamagana","Cishwa","Nkanda","Nyakeru","Mutoyi","Kivuvu","Nyagisenyi","Mugitega","Mukoro","Gaterama","Kibungo"]
        Col_Bukirasazi=["Nyamisure","Bunyuka","Kibere","Migano","Rugoma","Ruvumu","Buhanda","Mpingwe","Ruhinga","Gasongati","Tema","Shaya","Nyambuye","Kibuye","Rwinyana","Bukirasazi","Rugabano","Rukoki"]
        Col_Buraza=["Buriza","Maza","Mahonda","Mugano","Bibate","Bugega","Musebeyi","Buraza","Ndago","Ndava","Kabumbe","Butezi","Rweza","Gisura","Gitaramuka","Bubaji","Gicumbi","Muyange","Butemba"]
        Col_Giheta=["Bihororo","Nyamugari","Korane","Gihehe","Gisuru","Muyange","Kiremera","Muremera","Rutegama","Nyarunazi","Masasu","Rwingiri","Gishuha","Bukinga","Mitimire","Rubarasi","Kamonyi","Kibande","Kiriba","Gisarara","Gasunu","Gihuga","Murayi","Rweru","Kanyinya","Mubuga","Kibimba","Kaguhu","Musama","Kibogoye","Ruhanza"]
        Col_Gishubi=["Rukiga","Muhuzu","Ruhande","Gishubi","Nyakigina","Murangara","Yanza","Mikore","Kigomera","Nyamugari","Kigufi","Gatoza","Musenga","Nyamirama","Rurimbi","Bukzavu","Muhagaze","Kejari","Nyamutobo","Mujejuru","Rwintamba","Gatare","Mugaruro","Cimba","Bucana","Mtunda","Kayogoro","Murehe","Nyakanazi","Ndago","Gikuka","Munyinya","Remera","Mugozi"]
        Col_Gitega=["Kibiri","Rutoke","Rweza","Jimbi","Bihanga","Nyabututsi rural","Mugoboka","Birohe","Nyakibingo","Rubamvyi","Mahonda","Mugutu","Higiro","Mirama","Karenda","Mukanda","Bukwazo","Murirwe","Ngobeke","Ntobwe","Mungwa","Butamuheba","Bwoga","Rukoba","Rutegama","Kimanama","Mubuga","Centre-Urbain","Rugari Gitamo","Songa"]
        Col_Itaba=["Buhanga","Karemba","Mutanga","Itaba","Nkima","Butare","Kanyinya","Gisikara","Macu","Mugomera","Kirambi","Ruhanza","Kagoma","Buhinda","Kanyonga","Rukobe I","Rukobe II","Kugitega","Gihamagara","Kibogoye"]
        Col_Makebuko=["Nyamagandika","Gasasa","Mwumba","Murenda","Gasagara","Kinyonza","Rutanganika","Buga","Ntita","Makebuko","Rwezamenyo","Musqve","Rwanda","Murago","Simba","Muyange","Rwesero","Mwaro Mavuvu","Mwaro Ngundu","Kagege","Bugumbasha","Karoba","Kiyange","Janja","Rusagara","Butobwe","Gasenyi","Muhororo","Mwanzari"]
        Col_Mutaho=["Nkongwe","Muzenga","Muyange","Mwumba","Muririmbo","Mutaho Rural","Mutaho Urbain","Ngoma","Kidasha","Bigera","Nzove","Kivoga","Gerangabo","Kinyinya","Nyabisaka","Nyangungu","Rurengera","Gitongo","Masango"]
        Col_Nyarusange=[""]
        Col_Ryansoro=["Ndava","Nyabikenke","Mirango","Ntunda","Nyentambwe","Rusaga","Ngaruzwa","Nyamugari","Murama","Kibagara","Nyakarambo","Mahonda","Kibaya","Kampezi","Mahwa","Kinyonzo","Murenge"]
        
         
        Prov_Karuzi=["Bugenyuzi","Buhiga","Gihogazi","Gitaramuka","Mutumba","Nyabikere","Shombo"]
        
        Col_Bugenyuzi=["Kabwira","Rusasa","Gishikanwa","Teme","Buhindye","Kidahwe","Kanazi","Ruharo","Kigufi","Rzandagaro","Bonero","Canzikiro","Kiranda","Nyagoba","Rugazi","Munyinya","Gashanga","Cuba","Muyange","Tambi Kabande","Burenza Kibande","Rusengo","Mubaya","Rwimbogo","Mugoboka","Bugenyuzi","Muramba"]
        Col_Buhiga=["Rukamba","Kajeri","Nyamabega","Muhweza","Buhinyuza","Nkoronko","Karuri","Karunyinya","Ramvya","Burenza","Gisenyi","Bushirambeho","Gitanga","Karamba","Rudaraza","Shanga","Kanyange","Mwoya","Magamba","Rweya","Nzibariba","Cigati","Rutonganirwa","Ruyaga","Mayenzi","Gasenyi","Rwingoma","C U Buhiga","C U Karuzi"]
        Col_Gihogazi=["Mugero","Munanira","Rutegama","Ruyaga","Murago","Muwenga","Bihembe","Gasivya","Rusamaza","Ramba","Gasenyi","Mushikanwa","Mugogo","Taba","Gihogazi","Kibezi","Kizingoma","Kivoga","Ruganira","Bikinga","Nyamiyaga"]
        Col_Gitaramuka=["Bikinga","Karwa","Kigozi","Kibenga","Rubuga","Nyarutovu","Gitaramuka","Ruhata","Nyaruhinda","Gahashi","Rwizingwe","Gasasa","Maramvya","Kinyota","Kiyange","Gahahe","Gitandu","Rusagara","Cirambo","Nyakabugu","Kibumbwe","Mugende","Ntunda","Bugwana","Ngayane","Gasekanya"]
        Col_Mutumba=["Yagizo","Mubaragaza","Rabiro","Kigoma","Gisimbawaga","Sagara","Nkuba","Bibara","Kibuye","Mutara","Gasera"]
        Col_Nyabikere=["Ngugo","Nyarunazi","Butamenwa","Rwandagaro","Ruhuma","Rugwiza","Masama","Mazita","Ruvumu","Gatonde","Nyenzi","Taba","Mbabazi","Maramvya"]
        Col_Shombo=["Gisenyi","Muhigo","Muhororo","Kigo","Kiyange","Butwe","Gaharo","Gikombe","Rusi","Mujenjwa","Gitaramuka","Shombo","Gatabo","Nyabibuye","Bukirasazi","Kiryama"]
        
        
        Prov_Kayanza=["Butaganzwa","Gahombo","Gatara","Kabarore","Kayanza","Matongo","Muhanga","Muruta","Rango"]
        
        Col_Butaganzwa=["Gakonko","Mihana","Kizigama","Mpame","Mugege","Nyarurambi","Gishubi","Nyamiyaga","Gikwiye","Rubambari","Muriza","Nyamugari","Gasasa","Kiyabu","Nyaburondwe","Burenza","Biyorwa","Nyarubabi","Rugata","Masazi","Nyagashubi","Itaba","Kanyinya","Kirambi","Kirangara","Rugongo","Kivumu","Musenga","Muhene","Mpungwe","Bartye","Maramvya","Nyangurube","Kivoga","Nyange","Bigera","Titi","Caragata","Nyankende"]
        Col_Gahombo=["Nzewe","Mwenene","Rukanu","Nyagatobo Businde","Butwe","Bigugo","Kivuvuma","Gasave","Gakuro","Rukago","Butezi","Nyagatobo Kiyange","Mikoni","Kivoga","Gishunzi","Kavuvuma","Shurungumya","Kinyonga","Gahombo","Ruzingati","Karinzi"]
        Col_Gatara=["Bubogoro","Karambi","Kigume","Gisyo","Ngoro","Nteko","Gitwenge","Kabungo","Migende","Gakenke","Ngendo","Muhinga","Gihororo","Nyarubabi","Rwankuba","Shinya","Ruhengeri","Murago","Kibaribari","Kivuruga","Mudusi","Rubagabaga","Mbirizi","Kibayi","Karurusi","Munini","Kibenga","Kanyankuru"]
        Col_Kabarore=["Yanza","Nyamisagara","Gisagara","Mugere","Gashiru","Dusasa","Kibati","Kidunduri","Buyumpu","Buvumo","Mugongo","Mugoyi","Kirehe","Gikingo","Yandaro","Rusambi","Mutana","Randa","Munege","Kivuvu","Kibuba","Ryamukona","Kigeri","Ngoma","Rorero","Runyinya","Manga","Rukere","Caratsi","Ruhinga","Karama","Ruhororo","Rutega","Jene","Songore","Caguka","Tondero"]
        Col_Kayanza=["Gitwa","Ruhande","Nyabihogo","Nemba","Muhweza","Mihigo","Kinga","Kayanza Ville","Gahahe","Cukiro","Nyabihanga","Mwendo","Bubezi","Murago","Kibingo","Ruvomo","Canzara","Gacu","Murima","Shikankoni","Ryirengeye","Mpanga","Benga","Nyangwe","Karinzi","Kinzobe","Migege","Nkuba","Kavumu","Gihororo","Rwintare","Magamba","Kinyamukizi","Nyabikaranka","Ntarambo","Maruri"]
        Col_Matongo=["Rudehe","Muganza","Bihunge","Murambi","Banga","Matongo","Mpemba","Bwisange","Butuhurana","Nyarumanga","Bandaga","Kivumu","Ngoro","Gasare","Mvumvu","Burengo","Ruvumu","Nyarurambi","Bwayi","Ruganza","Musonge","Kibavu","Burarana","Kijuri","Mikamba","Gitwe","Kabuye","Camizi","Munyinya","Mutarure","Nteko","Kinyovu","Rukoma","Munini","Nyakibingo"]
        Col_Muhanga=["Gatura","Nyarurambi","Jimbi","Nyamwera","Nyamitanga","Bushoka","Gitamo","Rubanga","Gisara","Masama Mugobora","Kivuzo","Rushubi","Masama Muhanga","Gaharo","Ceyerezi","Sakinyinya","Mibazi","Mborwe","Gasenyi","Masanze","Muhanga","Mwendo","Kibimba","Gashibuka","Rugamba","Rushenza","Ngoma","Ndava","Kanyundo","Gatozo"]
        Col_Muruta=["Mutana","Gishubi","Remera","Ruvumu","Nyakibari","Mpfunda","Ruharo","Rwegura","Muciro","Nkonge","Yanza","Mikuba","Busambo","Buziraguhindwa","Campazi","Karunyinya","Muruta","Manini","Nyamiyogoro","Myugariro","Rwagongwe","Kibakwe","Kavoga","Kaserege","Muganza"]
        Col_Rango=["Rubirizi","Tara","Gatare","Nyabitwe","Bishuri","Karehe","Gihororo","Musagara","Kiguruka","Bisha","Kabuye","Nyamonde","Butanyerera","Gitibu","Rama","Gacokwe","Muzumure","Nyabigoyi","Gipfuvya","Nyabibuye","Rango","Karama","Nyarusange","Kaguruka","Rusave","Gikomero","Ruhinga","Kiramahira","Rubungu"]
        
        
        Prov_Kirundo=["Bugabira","Busoni","Bwambarangwe","Gitobe","Kirundo","Ntega","Vumbi"]
        
        Col_Bugabira=["Rugasa","Kigoma","Gitwe","Nyamabuye","Nyabikenke","Kiri","Kiyonza","Gaturanda","Nyakarama","Rubuga","Kigina","Ruhehe"]
        Col_Busoni=["Murambi","Marembo","Higiro","Rwibikara","Runyinya","Mukerwa","Kagege","Munyinya","Kiravumba","Nyabisindu","Kigoma","Buhimba","Buringa","Karambo","Muvyuko","Gitete","Gatete","Gatare","Kivo","Nyakizu","Munazi","Sigu","Kumana","Nyagisozi","Muyange","Ruheha","Nyabugeni","Rutabo","Kabanga","Kididiri","Rurende","Gatemere","Rurira","Murore","Ruyaga","Gisenyi","Kibonde","Renga","Rugarama","Mugobe","Burara"]
        Col_Bwambarangwe=["Bugorora","Bunywera","Rusara","Karambo","Buhoro","Minyago","Kibazi","Ruyenzi","Butegana","Mukenke I Urbain","Budahunga","Mukenke II Rural","Buhevyi","Gasave","Mugongo","Kimeza","Mutarishwa","Kibonobono"]
        Col_Gitobe=["Ngoma","Cumba","Bucana","Burwana","Butihinda","Gasuga","Kivumu","Mirwa","Butahana","Baziro","Gihinga","Rungazi","Shore","Ruhongore","Marembo","Tonga","Nyenzi","Santunda","Bigombo","Gahosha"]
        Col_Kirundo=["Cumba","Busenyi","Bugera","Gikuyo","Karamagi","Cewe","Mataka","Kavomo","Mutara","Kinyangurube","Yaranda","Ceru","Kiyanza","Muramba","Mwenya","Gihosha","Gakana","Murama II","Rugero II","Rugero I","Centre-Urbain","Rambo","Kanyinya","Murama I","Runyonza"]
        Col_Ntega=["Rukore","Runyankezi","Gisitwe","Bugorora","Mwendo","Gatanga","Rushubije","Kanabugiri","Nyemera","Gitwenzi","Kigaga","Buringanire","Sasa","Monge","Gasave","Carubambo","Makombe","Mariza","Gihome","Rugese","Nkorwe","Nyakibingo","Muyinza","Murarambwe","Gatwe","Rwimbogo","Susa","Kinyovu","Ntago","Mugendo","Rutagara","Mihigo","Ntega","Kigina","Murungurira","Kamenya","Kanyagu"]
        Col_Vumbi=["Rwisuri","Nyagatovu","Bwinyana","Muyebe","Muramba","Kiraro","Nyakibande","Nyamyumba","Gikomero","Kavumu","Mbasi","Mutoyi","Gashingwa","Ruhengeri","Vumbi","Rwamikore","Gahe","Nyamivuma","Nyabihanga","Nyamirembe","Gatare","Burarana","Martyazo","Kirima","Gasura","Kabuye Shororo","Butsimba","Nyabikenke","Rwimanzovu","Kabuye Gitanga","Kigobe","Kiziba","Cendajuru","Nyamisagara","Kabirizi","Canika"]
        
        Prov_Makamba=["Kayogoro","Kibago","Mabanda","Makamba","Nyanza-Lac","Vugizo"]
        
        Col_Kayogoro=["Rusovu","Shaka","Kigaza","Bujondi","Mukingo","Sampeke","Rutenderi","Gatabo","Buga","Kibimba","Butare","Borera","Kabizi","Muyange","Kiyange","Buhema","Kigomagoma","Mudaturwa","Mayange","Mugeni","Gasenga","Kibara","Gitaba","Mugeregere","Muguruka","Nyantakara","Musasa","Bigina","Nkara Manyenye"]
        Col_Kibago=["Mbizi","Rubimba","Kibago","Nyarubanga","Nyakazi","Kabanga","Migongo","Nyarutuntu","Kiyange","Nyabigina","Jimbi","Murambi","Bukeye"]
        Col_Mabanda=["Mubondo","Ruvuga","Gikombe","Kigambwe","Burima","Mabanda Rural et Urbain","Karinzi","Sanvura","Mivo","Bikobe","Musenyi","Budaketwa","Nyamugari","Mutwazi","Bukunda","Nyabitabo","Kibimba","Gikurazo","Mara"]
        Col_Makamba=["Musanga","Rabiro","Mpinga","Gasaka","Gisenyi","Siza","Kayoba","Munonotsi","Murago","Muresi","Muvumu","Mugutu","Murambi","Nyankara","Canda","Kirama","Kizingoma","Cunamwe","Kinoso","Ruremba","Mihongo","Nyabangwe","Kanzege","Makamba I","Ndago","Giheru","Nyabigina","Kirare","Karonge","Mahembe","Gitaba","Makamba II"]
        Col_Nyanza_Lac=["Rimbo","Rubindi","Buheka","Mvugo","Mukumgu","Mugerama","Mukimba","Kabondo","Biniganyi","Kazirabageni","Gasaraba","Mukerezi","Rangi","Nyabutare","Gisenga","Kabonga","Bukeye","Mwimbiro","Ruvyagira","Ruvumera","Kabo","Mugumure","Kiderege","Nyabigina","Mukubano","Muyange"]
        Col_Vugizo=["Kagege","Nyamirinzi","Murinda","Karonge","Gitaba","Mazuru","Mutobo","Nyarubano","Gahandu","Mugu","Rabiro","Ndoba","Jongwe","Mbizi","Gikuzi","Martyazo","Rutegama","Rurambira","Kiyazi","Kigombe"]
        
        Prov_Muramvya=["Bukeye","Kiganda","Mbuye","Muramvya","Rutegama"]

        Col_Bukeye=["Busekera","Kigereka","Shumbo","Rusha","Busangana","Nyambo","Rweteto","Kivogero","Gahaga","Gikonge","Kiziguro","Gaharo","Buhorwa","Nyarucamo","Musumba","Rwatsinda","Gashishima","Burarana"]
        Col_Kiganda=["Musongati","Kanyami","Rubumba","Gahweza","Ngara","Burenza","Nkomwe","Ruvumu","Kiganda","Kanengwa","Kayange","Kivyeyi","Martyazo","Renga","Murambi","Nyagisozi"]
        Col_Mbuye=["Rwuya","Mugerera","Murama","Mbuye","Kirembera","Kiziba","Mwegera","Migezi","Nyakijwira","Kigina","Kibumbu","Janga","Mubuga","Masama","Nete","Rugari","Kigabiro","Gasenyi","Teka","Buhangura","Buyaga","Bigwana","Kirika","Taba","Murehe","Kabuye"]
        Col_Muramvya=["Kavya","Mpehe","Shombo","Ruhinga","Murambi","Remera","Gatwaro","Mubira""Gatebe","Kirama","Burambana","Kibogoye","Busimba","Musagara","Mirinzi","Muramvya","Muramvya","Muramvya","Biganda","Masango","Mugomere","Muhweza","Gishubi","Gakenke"]
        Col_Rutegama=["Mushikamo","Murinzi","Musave","Gashingwa","Nyarukere","Camumandu","Rutegama","Nkonyovu","Bubanda","Cumba","Nyarunazi","Nyakararo","Nyamitwenzi","Munyinya","Bupfunda","Munanira II","Munanira I"]
        
        Prov_Muyinga=["Buhinyuza","Butihinda","Gashoho","Gasorwe","Giteranyi","Muyinga","Mwakiro"]
        
        Col_Buhinyuza=["Jarama","Kara","Mabago","Ruvumu","Rugongo","Burasira","Gihongo","Nyaruhengeri","Nyabucugu","Rugazi","Buhinyuza","Kibimba","Nyagishiru","Muramba","Karehe","Nyarunazi","Nyankurazo","Butihinda","Bugungu","Karongwe","Ntobwe","Gitaramuka","Bunywana","Kiyange","Gasave"]
        Col_Butihinda=["Nyamihondi","Munyinya","Bucamihigo","Zaga","Masaka","Buvumbi","Gahahe","Gitega","Maramvya","Butihinda","Ngara","Kamaramagambo","Kinonora","Gatwenzi","Cagizo","Maruri","Mugongo","Kibande","Tangara","Murehe","Kinyuku","Rwamfu","Wingoma","Ntaruka","Rabiro","Kobero","Buhorana","Kavumu","Rukira","Rushombo"]
        Col_Gashoho=["Muyange","Gitwa","Muruta","Bwisha","Kinyami","Nkohwa","Gisabazuba","Burambi","Kobero","Nyarushanga","Gisebeyi","Gisanze Muzingi","Gikingo","Bunyarukiga","Burenza","Mirwa","Nyagatovu","Buvumbi","Bonero","Murama","Musama II","Musama I","Busasa","Gisanze Rugerero","Cihonda","Gishambusha","Gashoho","Kagari"]
        Col_Gasorwe=["Kaguhu","Kinama","Kagurwe","Rusimbuko","Buringa","Bihogo","Kizi","Karambo","Butirabura","Rukinzo","Bwasare","Jani","Karama","Migunga","Gikwiye","Karira","Masasu","Gishuha","Nyungu","Kimanga","Kivubo","Kiremba","Martyazo","Kiryama","Ngogomo","Gasuru","Kigoganya","Higiro","Karambi"]
        Col_Giteranyi=["Bugoma","Mugano","Mukoni","Mangoma","Ndava","Rubenga","Kabogo","Shoza","Nonwe","Kagugo","Nzove","Cagakori","Kayove","Mika","Rugese","Karugunda","Giteranyi","Rukungere","Bisiga","Kabira","Mihigo","Gasenyi","Rumandari","Kinyami","Rusenyi","Buhangara","Gakoni","Tura","Kijumbura","Kinanira","Murama","Ngomo","Masaka","Kidasha","Vumasi","Ruzo","Rukusha"]
        Col_Muyinga=["Mizuga","Kiringaniro","Nyamirambo","Bwica","Cumba","Burenza","Butihinda","Ruganirwa","Musenga","Nyarusange","Rusengo","Bugomora","Rwimbogo","Kwibuye","Kayenzi","Kibogoye","Kinyota","Gitongwe","Kivoga","Kibongera","Karemera","Cibari","Gahororo","Nyamarumba","Buhurana","Gatovu","Nkoyoyo","Mageni","Munagano","Mahonda","Bunywana","Musenyi","Kinazi","Gasasa","Kavumu","Mwurire","Murama","Rutoke","Rusumo","Ryabihira","Rugari","Sanzwe","Ntamba","Kiryama","Burima","Mukoni","Gatongati I","Gatongati II","Ruyivyi","Kiryama"]
        Col_Mwakiro=["Kagombe","Kabingo","Gihoza","Mwakiro","Rukanya","Butobwe","Kadende","Kavugangoma","Bugonza","Karehe","Kigajo","Kibande","Kiyanza","Gasenyi","Bukwanzi","Mukungu","Bonero","Kibongera","Ciyando","Gitaba","Gisuma","Rusheri","Gahemba","Kibwira","Muyange","Rurtyazo","Musenga","Bubaji","Gahekenya","Rugabano","Mukunguza"]
        
        
        Prov_Mwaro=["Bisoro","Gisozi","Kayokwe","Ndava","Nyabihanga","Rusaka"]
        
        Col_Bisoro=["Munarira","Kiganda","Buburu","Mabaya","Gitaramuka","Musumba","Kariba","Kanka","Kiriba","Buhabwa","Rubamvye","Masango","Nyabisiga","Kivoga","Mashunzi"]
        Col_Gisozi=["Musimbwe","Kibimba","Nyakigwa","Musivya","Nyamiyaga","Rweza","Ndava","Gatare","Kiyange","Nyagahwabare","Butegana","Mugero","Gisozi","Buburu"]
        Col_Kayokwe=["Maramvya","Ngara","Rwuya","Nyamugari","Mago","Nyagitongati","Ruramba","Saswe","Rusivya","Masama","Rurtyazo","Kibenga Murehe","Rwankangoma","Kibenga Migende","Nyakibari","Muyebe","Gitunga","Benja","Bisoro","Bwakira","Kanyami","Kibogoye","Ruvumu","Gihinga"]
        Col_Ndava=["Ngorore","Gahondo","Gatsinda","Fota","Kigarama","Rango","Bugera","Kabogi","Murago","Ndava","Higiro","Butazi","Muyogoro","Matongo","Gitaba","Nyamurenge","Ngoro","Nyabisaka","Mpanuka","Kamushiha"]
        Col_Nyabihanga=["Migera","Nyarubayi","Muhaganya","Muyange","Gihoma","Magamba","Nyamitobo","Munago","Mubuga","Murama","Mbogora","Kavumu","Kivomwa","Gatwe","Miterama","Butegeye","Martyazo","Kibungere","Kivuzo","Kibungo","Gitaramuka","Taba","Buhogo","Kirambi","Kibogoye","Iteka","Musongati","Muyebe","Gisirtye"]
        Col_Rusaka=["Mpumbu","Martyazo","Mureba","Nkurunzi","Nyamugari","Kibimba","Shana","Rusaka","Mahonda","Kinyovu","Murambi","Rucunda","Namande","Kirambi","Rwintare","Nyamiyaga","Makamba","Gasenyi","Kizi","Nyamurenge","Bisha","Nyamigogo","Bunyange","Kiyege","Gikebuka","Nyagashanga","Kiga","Bugorora","Nkundusi"]
        
        Prov_Ngozi=["Busiga","Gashikanwa","Kiremba","Marangara","Mwumba","Ngozi","Nyamurenza","Ruhororo","Tangara"]
        
        Col_Busiga=["Mihama","Bigera","Magana","Nyanza Tubiri","Kirimba","Munyange","Gahini","Cendajuru","Mutsinda","Kimagara","Kavumu","Gatika","Rugori","Mpondogoto","Nyabizinu","Murambi","Rumbaga","Bitambwe","Nyange","Kididiri","Rubari","Rwanyege","Gatemezi","Mparamirundi","Kinyami","Mihigo","Muremera","Mutumba","Muyogoro","Caga","Kigufi","Makombe","Nyamisebo"]
        Col_Gashikanwa=["Rwizingwe","Nyarugunda","Kabamba","Sigi","Rutanga","Ngoma","Remera","Rutambwe","Gitanga","Gashikanwa","Maruri","Cihonda","Gatukuza","Butaha","Ruhengeri","Nini","Sabunda","Rusengo","Gatare","Butaganda","Mafuro","Kivumu","Musumba","Buhoro"]
        Col_Kiremba=["Ruyumbu","Kibande","Kiremera","Ruhama","Masasu","Ruvumu","Ciri","Gatwaro","Kiremba","Ngeramigongo","Kibezi","Gitaro","Mugerera","Rwimbogo","Cayi","Gakere","Magembe","Masoro","Kiyange","Rutobo","Ruhata","Canamo","Bitaganzwa","Cagwa","Nyamarobe","Kagarama","Musasa","Kivoga","Kidasha","Buhama","Kabari","Ragwe","Kibuye","Munagano","Musanga","Gisuka","Gahororo","Bunywana","Bunogera","Nkomero","Migongo","Nyabikenke","Mufigi","Kabanga","Butare"]
        col_Marangara=["Burenza","Rugomba","Nyunzwe","Congori","Kidobori","Nyamurenge","Runda","Kagina","Muhuzo","Bihangare","Masama","Kagoti","Kigufi","Bitambwe","Gisekuro","Makaba","Kigoma","Burenge","Nyambo","Kidasha","Rubaya","Nyanza","Nyakibari","Ruramba","Ndihwe","Kirungu","Bisiga","Kizenga","Mutara","Gikomero","Gicumbi","Nyamugari","Higiro","Renga"]
        Col_Mwumba=["Gakenke","Bugorora","Karungura","Kabasazi","Gihama","Murama","Kagozi","Saramasaka","Buziragahama","Rukurazo","Kibindi","Gitasi","Ntembe","Mushitsi","Buye","Nzove","Hayiro","Kayanza","Kabazana","Rwarangabo","Buhanda","Muremera","Gatsinda","Kabataha","Gitwa","Burenza","Rwabiriro","Butaganda","Cahi"]
        Col_Ngozi=["Makombe","Busoro","Mwungere","Mirango","Kambati","Hima","Kiruri","Cigumije","Nyanza","Ntaho","Mivo","Sare","Gasebeyi","Gahengeri","Kavumu","Mubuga","Masama Buhiga","Gakeceri","Gahwazi","Kinyana","Masama Burima","Mugomera","Bwiza Bweranka","Nyabihanga","Ruhongore","Kimenyi","Mbaba","Kayogoro","Nkero","Shango","Gisagara","Camugani","Gisagara","Nyaruntana","Gihoma","Gitwenzi","Kivuzo","Rwahirwa","Makaba"]
        Col_Nyamurenza=["Gikingo","Kagoma","Mugende","Kajaga","Nyabukenke","Buhigiranka","Nyarusange","Gitare","Gatwe","Mushonge","Rurama","Masama","Kinyovu","Shoza","Kigina","Matyazo","Gicu","Kaganda","Shinge","Gasererwa"]
        Col_Ruhororo=["Buniha","Rwamiko","Gitamo","Kagoma","Gitanga","Kabuye","Nyamugari","Mutobo","Mubira","Mukoni","Ruyaga","Rimiro","Nyakibingo","Buganuka","Gitwenzi","Kimerejana","Mihigo","Nyiba","Nyinya","Giturwe","Ryarunyinya","Banda","Kobero","Cagura","Gitaramuka","Kinyami","Bucamihigo","Mubanga","Muhama","Taba I","Taba II"]
        Col_Tangara=["Kiruhura","Gisura","Myando","Nyakabanda","Gasekanya","Mbasi","Ngendo","Gitwa","Mugirampeke","Rushoka","Bomba","Gitaramuka","Ruyogoro","Nyankurazo","Rugabo","Kananira","Mirango","Mafu","Musakazi","Nkanda","Nyarugati","Kamira","Mwika","Cumba","Runini","Muramba","Rukongwa","Gikingo","Butezi","Mashitsi","Nyagatovu","Kibande","Bwitoyi","Kigomero","Ruyaga","Musenyi","Nyagasebeyi"]
        
        Prov_Rumonge=["Bugarama","Burambi","Buyengero","Muhuta","Rumonge"]
        
        Col_Bugarama=["Kagona","Kayombe","Nyabungere","Mugendo","Bugarama","Cashi","Zingi Nyaruyaga","Ruteme","Mihororo","Magara I","Magara II","Gitwaro","Kazigo","Burangwa","Bambo"]
        Col_Burambi=["Bisaka","Gahinda","Gitaramuka","Rwaniro","Gitongwe","Buhinyuza","Busaga","Gitaba","Gakonko","Rutwenzi","Gatobo","Murara","Murenge","Muzi","Busura","Rumonyi","Buyenzi","Maramvya","Magana","Gishiha","Gisenyi"]
        Col_Buyengero=["Mudende","Kirama","Gasenyi","Sebeyi","Kinama","Kanyinya","Nkizi","Mujigo","Nyamurunga","Gitsinda","Runyinya","Mabanza","Banda","Nyacambuko","Karambi","Rubirizi"]
        Col_Muhuta=["Mubone","Nyabwayi","Burazi","Murago","Rubura","Gasebeyi","Canda","Busenge","Gihondo","Rutongo","Masara","Kanzaganya","Higiro","Sakonga","Ruyobera","Kinyovu","Kibingo","Mubanga","Muhuta","Ruringe","Bitwe","Gitunga","Gatwenzi","Rutunga","Nyangushwe","Nkuba","Buyenzi","Buringa","Gabaniro","Gasange","Gitaza","Kirombwe","Gakuyo","Kizuga"]
        Col_Rumonge=["Kizuka","Mwange","Gatwe","Centre-Ville","Minago","Mutambara","Rukinga","Mugomere","Kagongo","Gatete","Muhanda","Gashahsa","Gitwe","Karagara","Rutumo","Muhuzu","Muturirwa","Karonke","Kanenge","Nyakuguma","Mayengo","Cabara","Mugara","Busebwa","Nyagasaka","Murambi","Mibanda"]
        
        Prov_Rutana =["Bukemba","Giharo","Gitanga","Mpinga-Kayove","Musongati","Rutana"]
        
        Col_Bukemba=["Bugiga","Bukemba","Murama Rugwe","Muyombwe","Butare","Ruranga","Rubanga","Kabanga","Gihofi","Sosumo"]
        Col_Giharo=["Muzye","Nkaka","Gatonga","Kabingo","Mwebeya","Rubanga","Shasha","Kigunda","Butezi","Kanyererwe","Buhogo","Giharo","Bayaga","Mutwana","Nkurye","Kibimba","Gakungu","Mura","Nyamateke","Murara","Ngomante","Nyabakara","Nyembuye","Murehe","Buyaga","Shembe","Murembera","Mugombwa","Gitanga","Bukeno","Musenyi"]
        Col_Gitanga=["Ngoma","Nyagisabwe","Kazeba","Maramvya","Kabago","Nyabikenke","Cikinga","Ntuku","Museno","Kiremba","Bigina","Gitanga","Gisenyi","Nyakuguma","Muyaga","Cunda","Kinzanza","Nyamabuye","Rukobe","Kabanga","Samahuge","Musongati","Kivoma","Mutsindozi","Gatwaro"]
        Col_Mpinga_Kayove=["Bubanga","Nyakazu","Nyakabanga","Gasasa","Kiguhu","Juragati","Rorero","Kayove","Musotera","Maganahe","Gasenga","Mirehe","Kagoma","Rasa","Buranga","Munyinya","Mbuye","Ngarama","Kibanda","Butamya","Gitaba","Gihera","Mpinga","Ntonzi","Muganza","Mugondo","Bayumpu","Gasozi","Rutoke","Ngara","Butambara","Gihinga"]
        Col_Musongati=["Munywero","Musagara","Rugunga","Nyangazi","Shanga","Nyanza","Mabawe","Ngoma","Mungwa","Nyabibuye","Cero","Karera","Gisasa","Mbuza","Nyabigozi","Nyabisindu","Makakwe","Runyoni","Kamaramagambo","Buhinga","Yove","Kagunga","Gatakazi","Rusunu","Giheta","Maganahe"]
        Col_Rutana=["Gifunzo","Nyanzuki","Kivoga","Rushemeza","Maramvya","Mika","Rutana Urbain","Kayove","Nyarubimba","Gitaramuka","Ramvya","Musenyi","Matutu","Gitaba","Mwayi","Gaterama","Nyamure","Bugunga","Gatongati","Kinganda","Buta","Mungwa","Gasakuza","Karibu","Jomati","Ruregeya","Gakobe","Shoti","Rushungura","Rusunu","Butovyi","Rongero","Karinzi","Butambara","Kibizi","Nyarubere","Rutana Rural","Gaseri","Ntuku"]
        
        Prov_Ruyigi=["Butaganzwa","Butezi","Bweru","Gisuru","Kinyinya","Nyabitsinda","Ruyigi"]
        
        Col_Butezi=["Rugoti","Mugogo","Gitwa","Nkonwe","Muyange","Kirasira","Sorere","Senga","Gashurushuru","Rutegama","Munyinya","Mubira","Nombe","Rubaragaza","Bwagiriza"]
        Col_Bweru=["Busuma","Masama","Ntunda","Nzozi","Bweru","Gashawe","Mubavu","Mibanga","Nyarunazi","Ruvyagira","Nkanda","Caga","Kanisha","Gasenyi","Nyamugari","Rubavu","Busoro","Gatwaro","Kirambi","Bigombo"]
        Col_Gisuru=["Nyabitaka","Muvumu","Nyarumanga","Nkurubuye","Kireka","Kigamba","Mwegereza","Iteka","Gahinga","Nyabitare","Migende","Rukobe","Kinama","Muhindo","Itaba","Gakangaga","Bunyambo","Nyabigabiro","Itahe","Rwerambere","Kavumwe","Butarangira","Ndemeka","Kabuyenge","Kabingo","Ruyaga","Rusange","Rubanga","Nyabigozi","Nyakirunga","Ruhuni","Nyakivumu","Caga","Kinanira","Munyinya","Rutonde","Iyogero","Murehe","Gisuru","Bugama","Ntende","Gacokwe","Musha"]
        Col_Kinyinya=["Kibari","Gasunu","Bugongo","Muvumu","Gataba","Nyamigina","Mayanza","Kigangabuko","Munazi","Nyamusasa","Kabanga","Ruveri","Nyamunazi","Musumba","Vumwe","Kinyinya","Karindo","Nyakibere"]
        Col_Nyabitsinda=["Ruharo","Nyaruganda","Remba","Bwome","Nyakiyoga","Nyakibingo","Muramba","Nyagitika","Bihembe","Mureba","Mago","Murehe","Nyarumuri","Gatare Gasenyi","Nyamasenga","Nyagahanda","Ndago","Kirungu","Nyabitsinda"]
        Col_Ruyigi=["Bisinde","Bugarama","Rutonganika","Rutimbura","Kazimya","Nyabigugo","Karambi","Kigamba","Ruyigi rural","Dutwe","Ngarama","Rukaragata","Kirambi","Gisoro","Nyagutoha","Nyarunazi","Buruhukiro","Migege","Bunogera","Nganji","Gasanda","Sanzu C U","Ruhwago","Gahemba"]

        PE = ["Forage","Puit","Source"]

        title = Label(self, text="Requête isoligne",bd=15, relief= RAISED, font=('Antiqua', 15, "bold"),bg='cyan', fg='black')
        title.place(x=0,y=0,width=810)


        Loc_frame = LabelFrame(self, text="Localisation", font=("times new roman",15), bg="white")
        Loc_frame.place(x=5, y=60, width=400, height=600)

        lbl_prov = Label(Loc_frame, text="Province :", font=("times new roman", 12, "bold"), bg="white")
        lbl_prov.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        txt_prov = ttk.Combobox(Loc_frame, font=("times new roman",10),values= province, width=15, state="readonly")
        txt_prov.grid(row=0, column=1, sticky=W, padx=0, pady=2)
        txt_prov.current(0)
        
        
        lbl_comm = Label(Loc_frame, text="Commune :", font=("times new roman", 12, "bold"), bg="white")
        lbl_comm.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        txt_comm = ttk.Combobox(Loc_frame,font=("times new roman",10), width=15, state="readonly")
        txt_comm.grid(row=1, column=1, sticky=W, padx=0, pady=2)
        
        lbl_coln = Label(Loc_frame, text="Coline:", font=("times new roman", 12, "bold"), bg="white")
        lbl_coln.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        txt_coln = ttk.Combobox(Loc_frame, font=("times new roman",10), width=15, state="readonly")
        txt_coln.grid(row=2, column=1, sticky=W, padx=0, pady=2)
        
        
        txt_PE = ttk.Combobox(Loc_frame, font=("times new roman",10),values=PE, width=25, state="readonly")
        txt_PE.grid(row=3, column=0, sticky=W, padx=5, pady=2)
        txt_PE.current(1)

        SelPE_btn = Button(Loc_frame, text="Toutes",cursor="hand2", font=("Times new roman",10, "bold"),width=15, bg="beige", fg="black")
        SelPE_btn.grid(row=3,column=1, sticky=W, padx=0, pady=2)

        #######################Fonction communes#################################################

        #################Bubanza#########################

        def fonctionComm(event):
            if txt_comm.get()=="Bubanza":
                txt_coln.config(values=Col_Bubanza)  
                txt_coln.current(0)
                 
            elif txt_comm.get()=="Gihanga":        
                txt_coln.config(values=Col_Gihanga)  
                txt_coln.current(0)
            
            elif txt_comm.get()=="Musigati":        
                txt_coln.config(values=Col_Musigati) 
                txt_coln.current(0)
             
            elif txt_comm.get()=="Mpanda":        
                txt_coln.config(values=Col_Mpanda)  
                txt_coln.current(0)
              
            elif txt_comm.get()=="Rugazi":        
                txt_coln.config(values=Col_Rugazi)  
                txt_coln.current(0)

            elif txt_comm.get()=="Gihanga":        
                txt_coln.config(values=Col_Gihanga)  
                txt_coln.current(0)

    ##################Bujumbura Marie###################################

            elif txt_comm.get()=="Muha":
                txt_coln.config(values=Col_Muha) 
                txt_coln.current(0)
                 
            elif txt_comm.get()=="Mukaza":        
                txt_coln.config(values=Col_Mukaza)  
                txt_coln.current(0)
            
            elif txt_comm.get()=="Ntahangwa":        
                txt_coln.config(values=Col_Ntahangwa) 
                txt_coln.current(0)

################### Bujumbura Rural######################## 
          
            elif txt_comm.get()=="Isale":        
                txt_coln.config(values=Col_Isale)  
                txt_coln.current(0)
              
            elif txt_comm.get()=="Kabezi":        
                txt_coln.config(values=Col_Kabezi)  
                txt_coln.current(0)

            elif txt_comm.get()=="Kanyosha":        
                txt_coln.config(values=Col_Kanyosha) 
                txt_coln.current(0)

            elif txt_comm.get()=="Mubimbi":        
                txt_coln.config(values=Col_Mubimbi) 
                txt_coln.current(0)
             
            elif txt_comm.get()=="Mugongomanga":        
                txt_coln.config(values=Col_Mugongomanga)  
                txt_coln.current(0)
              
            elif txt_comm.get()=="Mukike":        
                txt_coln.config(values=Col_Mukike)  
                txt_coln.current(0)

            elif txt_comm.get()=="Mutambu":        
                txt_coln.config(values=Col_Mutambu)  
                txt_coln.current(0)

            elif txt_comm.get()=="Mutimbuzi":        
                txt_coln.config(values=Col_Mutimbuzi)  
                txt_coln.current(0)

            elif txt_comm.get()=="Nyabiraba":        
                txt_coln.config(values=Col_Nyabiraba)  
                txt_coln.current(0)
               
####################################Bururi################################### 
           
            elif txt_comm.get()=="Bururi":        
                txt_coln.config(values=Col_Bururi)  
                txt_coln.current(0)
              
            elif txt_comm.get()=="Matana":        
                txt_coln.config(values=Col_Matana)  
                txt_coln.current(0)

            elif txt_comm.get()=="Mugamba":        
                txt_coln.config(values=Col_Mugamba) 
                txt_coln.current(0)

            elif txt_comm.get()=="Rutovu":        
                txt_coln.config(values=Col_Rutovu) 
                txt_coln.current(0)
             
            elif txt_comm.get()=="Songa":        
                txt_coln.config(values=Col_Songa)  
                txt_coln.current(0)
              
            elif txt_comm.get()=="Vyanda":        
                txt_coln.config(values=Col_Vyanda)  
                txt_coln.current(0)
    #####################################Cankuzo######################     
            
            elif txt_comm.get()=="Cankuzo":        
                txt_coln.config(values=Col_Cankuzo)  
                txt_coln.current(0)
              
            elif txt_comm.get()=="Cendajuru":        
                txt_coln.config(values=Col_Cendajuru)  
                txt_coln.current(0)

            elif txt_comm.get()=="Gisagara":        
                txt_coln.config(values=Col_Gisagara) 
                txt_coln.current(0)

            elif txt_comm.get()=="Kigamba":        
                txt_coln.config(values=Col_Kigamba) 
                txt_coln.current(0)
             
            elif txt_comm.get()=="Mishiha":        
                txt_coln.config(values=Col_Mishiha)  
                txt_coln.current(0)
    ##################################Cibitoke#########################        

            elif txt_comm.get()=="Buganda":        
                txt_coln.config(values=Col_Buganda)  
                txt_coln.current(0)
              
            elif txt_comm.get()=="Bukinanyana":        
                txt_coln.config(values=Col_Bukinanyana)  
                txt_coln.current(0)

            elif txt_comm.get()=="Mabayi":        
                txt_coln.config(values=Col_Mabayi) 
                txt_coln.current(0)

            elif txt_comm.get()=="Mugina":        
                txt_coln.config(values=Col_Mugina) 
                txt_coln.current(0)
             
            elif txt_comm.get()=="Murwi":        
                txt_coln.config(values=Col_Murwi)  
                txt_coln.current(0)

            elif txt_comm.get()=="Rugombo":        
                txt_coln.config(values=Col_Rugombo)  
                txt_coln.current(0)

    ##################################Gitega######################

            elif txt_comm.get()=="Bugendana":        
                txt_coln.config(values=Col_Bugendana)  
                txt_coln.current(0)
              
            elif txt_comm.get()=="Bukirasazi":        
                txt_coln.config(values=Col_Bukirasazi)  
                txt_coln.current(0)

            elif txt_comm.get()=="Buraza":        
                txt_coln.config(values=Col_Buraza) 
                txt_coln.current(0)

            elif txt_comm.get()=="Giheta":        
                txt_coln.config(values=Col_Giheta) 
                txt_coln.current(0)
             
            elif txt_comm.get()=="Gishubi":        
                txt_coln.config(values=Col_Gishubi) 
                txt_coln.current(0)

            elif txt_comm.get()=="Gitega":        
                txt_coln.config(values=Col_Gitega)  
                txt_coln.current(0)

            elif txt_comm.get()=="Makebuko":        
                txt_coln.config(values=Col_Makebuko)  
                txt_coln.current(0)
              
            elif txt_comm.get()=="Itaba":        
                txt_coln.config(values=Col_Itaba)  
                txt_coln.current(0)

            elif txt_comm.get()=="Mutaho":        
                txt_coln.config(values=Col_Mutaho) 
                txt_coln.current(0)

            elif txt_comm.get()=="Nyarusange":        
                txt_coln.config(values=Col_Nyarusange) 
                txt_coln.current(0)
             
            elif txt_comm.get()=="Ryansoro":        
                txt_coln.config(values=Col_Ryansoro)  
                txt_coln.current(0)


#######################Karuzi##########################################

            elif txt_comm.get()=="Bugenyuzi":        
                txt_coln.config(values=Col_Bugenyuzi)  
                txt_coln.current(0)
              
            elif txt_comm.get()=="Buhiga":        
                txt_coln.config(values=Col_Buhiga)  
                txt_coln.current(0)

            elif txt_comm.get()=="Gihogazi":        
                txt_coln.config(values=Col_Gihogazi)
                txt_coln.current(0)

            elif txt_comm.get()=="Mutumba":        
                txt_coln.config(values=Col_Mutumba)
                txt_coln.current(0)
             
            elif txt_comm.get()=="Nyabikere":        
                txt_coln.config(values=Col_Nyabikere)  
                txt_coln.current(0)

            elif txt_comm.get()=="Shombo":        
                txt_coln.config(values=Col_Shombo)  
                txt_coln.current(0)
              
            elif txt_comm.get()=="Gitaramuka":        
                txt_coln.config(values=Col_Gitaramuka)  
                txt_coln.current(0)

    ############################Kayanza##############################################

            elif txt_comm.get()=="Butaganzwa":        
                txt_coln.config(values=Col_Butaganzwa)  
                txt_coln.current(0)
              
            elif txt_comm.get()=="Gahombo":        
                txt_coln.config(values=Col_Gahombo)  
                txt_coln.current(0)

            elif txt_comm.get()=="Gatara":        
                txt_coln.config(values=Col_Gatara) 
                txt_coln.current(0)

            elif txt_comm.get()=="Kabarore":        
                txt_coln.config(values=Col_Kabarore)
                txt_coln.current(0)
             
            elif txt_comm.get()=="Kayanza":        
                txt_coln.config(values=Col_Kayanza)  
                txt_coln.current(0)

            elif txt_comm.get()=="Matongo":        
                txt_coln.config(values=Col_Matongo)  
                txt_coln.current(0)

            elif txt_comm.get()=="Muhanga":        
                txt_coln.config(values=Col_Muhanga)  
                txt_coln.current(0)
              
            elif txt_comm.get()=="Muruta":        
                txt_coln.config(values=Col_Muruta)  
                txt_coln.current(0)

            elif txt_comm.get()=="Rango":        
                txt_coln.config(values=Col_Rango)  
                txt_coln.current(0)

##############################Kirundo######################## 

            elif txt_comm.get()=="Bugabira":        
                txt_coln.config(values=Col_Bugabira)  
                txt_coln.current(0)

            elif txt_comm.get()=="Busoni":        
                txt_coln.config(values=Col_Busoni)
                txt_coln.current(0)
             
            elif txt_comm.get()=="Bwambarangwe":        
                txt_coln.config(values=Col_Bwambarangwe)  
                txt_coln.current(0)

            elif txt_comm.get()=="Gitobe":        
                txt_coln.config(values=Col_Gitobe)  
                txt_coln.current(0)

            elif txt_comm.get()=="Kirundo":        
                txt_coln.config(values=Col_Kirundo)  
                txt_coln.current(0)
              
            elif txt_comm.get()=="Ntega":        
                txt_coln.config(values=Col_Ntega)  
                txt_coln.current(0)

            elif txt_comm.get()=="Vumbi":        
                txt_coln.config(values=Col_Vumbi)
                txt_coln.current(0)

#####################################Makamba########################################################

            elif txt_comm.get()=="Kayogoro":        
                txt_coln.config(values=Col_Kayogoro)
                txt_coln.current(0)
             
            elif txt_comm.get()=="Kibago":        
                txt_coln.config(values=Col_Kibago)  
                txt_coln.current(0)

            elif txt_comm.get()=="Mabanda":        
                txt_coln.config(values=Col_Mabanda)  
                txt_coln.current(0)

            elif txt_comm.get()=="Makamba":        
                txt_coln.config(values=Col_Makamba)  
                txt_coln.current(0)
              
            elif txt_comm.get()=="Nyanza-Lac":        
                txt_coln.config(values=Col_Nyanza-Lac)  
                txt_coln.current(0)

            elif txt_comm.get()=="Vugizo":        
                txt_coln.config(values=Col_Vugizo)
                txt_coln.current(0)  

##########################################Muramvya###########################################################  

            elif txt_comm.get()=="Bukeye":        
                txt_coln.config(values=Col_Bukeye)
                txt_coln.current(0)
             
            elif txt_comm.get()=="Kiganda":        
                txt_coln.config(values=Col_Kiganda)  
                txt_coln.current(0)

            elif txt_comm.get()=="Mbuye":        
                txt_coln.config(values=Col_Mbuye)  
                txt_coln.current(0)

            elif txt_comm.get()=="Muramvya":        
                txt_coln.config(values=Col_Muramvya)  
                txt_coln.current(0)
              
            elif txt_comm.get()=="Rutegama":        
                txt_coln.config(values=Col_Rutegama)  
                txt_coln.current(0)   
                
####################################Muyinga##################################################################
        
            elif txt_comm.get()=="Buhinyuza":        
                txt_coln.config(values=Col_Buhinyuza)
                txt_coln.current(0)
             
            elif txt_comm.get()=="Butihinda":        
                txt_coln.config(values=Col_Butihinda)  
                txt_coln.current(0)

            elif txt_comm.get()=="Gashoho":        
                txt_coln.config(values=Col_Gashoho)  
                txt_coln.current(0)

            elif txt_comm.get()=="Gasorwe":        
                txt_coln.config(values=Col_Gasorwe)  
                txt_coln.current(0)
              
            elif txt_comm.get()=="Giteranyi":        
                txt_coln.config(values=Col_Giteranyi)  
                txt_coln.current(0)

            elif txt_comm.get()=="Muyinga":        
                txt_coln.config(values=Col_Muyinga)  
                txt_coln.current(0)
              
            elif txt_comm.get()=="Mwakiro":        
                txt_coln.config(values=Col_Mwakiro)  
                txt_coln.current(0)  

#########################################Mwaro####################################################
        
            elif txt_comm.get()=="Bisoro":        
                txt_coln.config(values=Col_Bisoro)
                txt_coln.current(0)
             
            elif txt_comm.get()=="Gisozi":        
                txt_coln.config(values=Col_Gisozi)  
                txt_coln.current(0)

            elif txt_comm.get()=="Kayokwe":        
                txt_coln.config(values=Col_Kayokwe)  
                txt_coln.current(0)

            elif txt_comm.get()=="Ndava":        
                txt_coln.config(values=Col_Ndava)  
                txt_coln.current(0)
              
            elif txt_comm.get()=="Nyabihanga":        
                txt_coln.config(values=Col_Nyabihanga)  
                txt_coln.current(0)

            elif txt_comm.get()=="Rusaka":        
                txt_coln.config(values=Col_Rusaka)  
                txt_coln.current(0)

#########################################Ngozi####################################################################
     
            elif txt_comm.get()=="Busiga":        
                txt_coln.config(values=Col_Busiga)
                txt_coln.current(0)
             
            elif txt_comm.get()=="Gashikanwa":        
                txt_coln.config(values=Col_Gashikanwa)  
                txt_coln.current(0)

            elif txt_comm.get()=="Kiremba":        
                txt_coln.config(values=Col_Kiremba)  
                txt_coln.current(0)

            elif txt_comm.get()=="Marangara":        
                txt_coln.config(values=Col_Marangara)  
                txt_coln.current(0)
              
            elif txt_comm.get()=="Mwumba":        
                txt_coln.config(values=Col_Mwumba)  
                txt_coln.current(0)

            elif txt_comm.get()=="Ngozi":        
                txt_coln.config(values=Col_Ngozi)  
                txt_coln.current(0)
            elif txt_comm.get()=="Nyamurenza":        
                txt_coln.config(values=Col_Nyamurenza)
                txt_coln.current(0)
             
            elif txt_comm.get()=="Ruhororo":        
                txt_coln.config(values=Col_Ruhororo)  
                txt_coln.current(0)

            elif txt_comm.get()=="Tangara":        
                txt_coln.config(values=Col_Tangara)  
                txt_coln.current(0)
#########################################RUMONGE########################################################################
            elif txt_comm.get()=="Bugarama":        
                txt_coln.config(values=Col_Bugarama)  
                txt_coln.current(0)
              
            elif txt_comm.get()=="Burambi":        
                txt_coln.config(values=Col_Burambi)  
                txt_coln.current(0)

            elif txt_comm.get()=="Buyengero":        
                txt_coln.config(values=Col_Buyengero)  
                txt_coln.current(0)

            elif txt_comm.get()=="Muhuta":        
                txt_coln.config(values=Col_Muhuta)  
                txt_coln.current(0)

            elif txt_comm.get()=="Rumonge":        
                txt_coln.config(values=Col_Rumonge)  
                txt_coln.current(0)

    ####################################Rutana############################################################################
            elif txt_comm.get()=="Bukemba":        
                txt_coln.config(values=Col_Bukemba)  
                txt_coln.current(0)
              
            elif txt_comm.get()=="Giharo":        
                txt_coln.config(values=Col_Giharo)  
                txt_coln.current(0)

            elif txt_comm.get()=="Gitanga":        
                txt_coln.config(values=Col_Gitanga)  
                txt_coln.current(0)

            elif txt_comm.get()=="Mpinga-Kayove":        
                txt_coln.config(values=Col_Mpinga-Kayove)  
                txt_coln.current(0)

            elif txt_comm.get()=="Musongati":        
                txt_coln.config(values=Col_Musongati)  
                txt_coln.current(0)

            elif txt_comm.get()=="Rutana":        
                txt_coln.config(values=Col_Rutana)  
                txt_coln.current(0)

##########################################Ruyigi###############################################################

            elif txt_comm.get()=="Butaganzwa":        
                txt_coln.config(values=Col_Butaganzwa)  
                txt_coln.current(0)
              
            elif txt_comm.get()=="Butezi":        
                txt_coln.config(values=Col_Butezi)  
                txt_coln.current(0)

            elif txt_comm.get()=="Bweru":        
                txt_coln.config(values=Col_Bweru)  
                txt_coln.current(0)

            elif txt_comm.get()=="Gisuru":        
                txt_coln.config(values=Col_Gisuru)  
                txt_coln.current(0)

            elif txt_comm.get()=="Kinyinya":        
                txt_coln.config(values=Col_Kinyinya)  
                txt_coln.current(0)

            elif txt_comm.get()=="Nyabitsinda":        
                txt_coln.config(values=Col_Nyabitsinda)  
                txt_coln.current(0)

            elif txt_comm.get()=="Ruyigi":        
                txt_coln.config(values=Col_Ruyigi)  
                txt_coln.current(0)

        txt_comm.bind("<<ComboboxSelected>>",fonctionComm) 

   ###############################################Fonction Province#####################################################         
        def fonctionprov(event):
            if txt_prov.get()=="Bubanza":
                txt_comm.config(values=Prov_Bubanza) 
                txt_comm.current(0)
                print("Test ")             
    
            elif txt_prov.get()=="Bujumbura Marie":        
                txt_comm.config(values=Prov_Bujumbura_Mairie)  
                txt_comm.current(0)
                print("test Bujumbura")
                               
            elif txt_prov.get()=="Bujumbura Rural":
                txt_comm.config(values=Prov_Bujumbura_rural)
                txt_comm.current(0)

            elif txt_prov.get()=="Bururi":
                txt_comm.config(values=Prov_Bururi)
                txt_comm.current(0)

            elif txt_prov.get()=="Cankuzo":
                txt_comm.config(values=Prov_Cankuzo)
                txt_comm.current(0)
        
            elif txt_prov.get()=="Cibitoke":
                txt_comm.config(values=Prov_Cibitoke)
                txt_comm.current(0)

            elif txt_prov.get()=="Gitega":
                txt_comm.config(values=Prov_Gitega)
                txt_comm.current(0)

            elif txt_prov.get()=="Karuzi":
                txt_comm.config(values=Prov_Karuzi)
                txt_comm.current(0)

            elif txt_prov.get()=="Kayanza":
                txt_comm.config(values=Prov_Kayanza)
                txt_comm.current(0)

            elif txt_prov.get()=="Kirundo":
                txt_comm.config(values=Prov_Kirundo)
                txt_comm.current(0)

            elif txt_prov.get()=="Makamba":
                txt_comm.config(values=Prov_Makamba)
                txt_comm.current(0)

            elif txt_prov.get()=="Muramvya":
                txt_comm.config(values=Prov_Muramvya)
                txt_comm.current(0)
        
            elif txt_prov.get()=="Muyinga":
                txt_comm.config(values=Prov_Muyinga)
                txt_comm.current(0)
        
            elif txt_prov.get()=="Mwaro":
                txt_comm.config(values=Prov_Mwaro)
                txt_comm.current(0)
        
            elif txt_prov.get()=="Rumonge":
                txt_comm.config(values=Prov_Rumonge)
                txt_comm.current(0)
        
            elif txt_prov.get()=="Ngozi":
                txt_comm.config(values=Prov_Ngozi)
                txt_comm.current(0)


            elif txt_prov.get()=="Rutana":
                txt_comm.config(values=Prov_Rutana)
                txt_comm.current(0)

            elif txt_prov.get()=="Ruyigi":
                txt_comm.config(values=Prov_Ruyigi)
                txt_comm.current(0)
            else:
                txt_comm.set("Choisir une province") 


        txt_prov.bind("<<ComboboxSelected>>",fonctionprov)

        aff_frame = Frame(Loc_frame,bd=5, relief=GROOVE, bg="white", width=260,height=410)
        aff_frame.grid(stick=W,padx=5,pady=10)

        txt_aff_frame= ttk.Entry(aff_frame, font=("times new roman",12, "bold"),state="readonly")
        txt_aff_frame.place(x=0, y = 0,width=250,height=400)
        
        lbl_NbreStat = Label(self, text="Nombre de stations :", font=("times new roman", 12, "bold"), bg="silver")
        lbl_NbreStat.place(x=5, y=665)

        txt_NbreStat= ttk.Entry(self, font=("times new roman",12, "bold"), state="readonly")
        txt_NbreStat.place(x= 200, y = 665)

        DatD_frame = LabelFrame(self, text="Date de début", font=("times new roman",12), bg="white")
        DatD_frame.place(x=405, y=60, width=200, height=55)

        txt_ecri_dat_deb = DateEntry(DatD_frame, font=("times new roman", 15),width=17, bg="lightyellow", state="readonly", locale='fr_FR',date_pattern = 'dd/mm/yyyy')
        txt_ecri_dat_deb.grid(row=0, column=0, sticky=W, padx=0, pady=0)

        DatF_frame = LabelFrame(self, text="Date de fin", font=("times new roman",12), bg="white")
        DatF_frame.place(x=605, y=60, width=200, height=55)

        txt_ecri_dat_fin = DateEntry(DatF_frame, font=("times new roman", 15),width=17, bg="lightyellow", state="readonly", locale='fr_FR',date_pattern = 'dd/mm/yyyy')
        txt_ecri_dat_fin.grid(row=0, column=0, sticky=W, padx=0, pady=0)

        Param_frame = LabelFrame(self, text="Paramètres", font=("times new roman",12), bg="white")
        Param_frame.place(x=405, y=115, width=400, height=400)
        
        txt_Parm  = ttk.Combobox(Param_frame, font=("times new roman",10),values=["mesure_eaux","qualité_de_l_eau","exploitation_forage"], state="readonly")
        txt_Parm .grid(row=0, column=0, sticky=W, padx=5, pady=2)
        txt_Parm .current(0)

        Sav_btn = Button(Param_frame, text="Toutes",cursor="hand2", font=("Times new roman",10, "bold"), bg="beige", fg="black")
        Sav_btn.grid(row=0,column=1, sticky=W, padx=0, pady=2)

        Param_frame2 = Frame(Param_frame, bd=5, relief=GROOVE, bg="white",width=315,height=340)
        Param_frame2.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        txt_Param_frame2= ttk.Entry(Param_frame2, font=("times new roman",12, "bold"),state="readonly")
        txt_Param_frame2.place(x=0, y = 0,width=305,height=325)


        CalcAdd_frame = LabelFrame(self, text="Calcul Additionnel", font=("times new roman",12), bg="white")
        CalcAdd_frame.place(x=405, y=515, width=400, height=60)

        btn_pp =ttk.Checkbutton(CalcAdd_frame,text="Minimum & Maximum")
        btn_pp.grid(row=0, column=0, sticky=W, padx=15, pady=2)

        CalcAdd_frame = LabelFrame(self, text="Dossier d'exportation ", font=("times new roman",12), bg="white")
        CalcAdd_frame.place(x=405, y=575, width=400, height=60)

        btn_frame = Frame(self, bd=5, relief=GROOVE, bg="white")
        btn_frame.place(x=405, y=637, width=400, height=50)

        Sav_btn = Button(btn_frame, text="Enregistrer",cursor="hand2", font=("Times new roman",13, "bold"),width=15, bg="green", fg="black")
        Sav_btn.grid(row=0,column=0, sticky=W, padx=20, pady=2)

        Abrt = Button(btn_frame,text="Quiter",cursor="hand2", font=("Times new roman",13, "bold"),width=15, bg="red", fg="black")
        Abrt.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        #scroll_y = Scrollbar(aff_frame, orient=VERTICAL)
        #scroll_y.pack(Fill=Y,side=RIGHT)
        #scroll_y.config(command = aff_frame.yview)



if __name__ =="__main__":
    w = RequeteIso()
    w.mainloop()
