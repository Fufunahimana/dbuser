import psycopg2




'''
server = '192.168.88.201'
db = "hydrogeology"
user= "postgres"
pwd = "Igebu99"
port = 5432

query="SELECT *, st_contains(geometry(geom),geometry(ST_GeomFromText('POINT (30.0002 -3.0321)', 4326))) FROM geo_communes WHERE st_contains(geometry(geom),geometry(ST_GeomFromText('POINT (30.0002 -3.0321)', 4326)));"
query2= "SELECT *, st_contains(geometry(geom),geometry(ST_GeomFromText('POINT (30.0002 -3.0321)', 4326))) FROM geo_collines WHERE st_contains(geometry(geom),geometry(ST_GeomFromText('POINT (30.0002 -3.0321)', 4326)));"
query3= "SELECT * from tbl_localisation where colline like 'Buhororo II' and id like 'FO-%' ORDER BY id ASC"    
mydb = psycopg2.connect(host="192.168.88.201",database="hydrogeology", user="postgres", password="igebu99")
if mydb:
    print("connection etablie")
   
    mycursor = mydb.cursor()
    mycursor.execute(query)
    rows = mycursor.fetchall()

    mycursor.execute(query2)
    rows2 = mycursor.fetchall()

    mycursor.execute(query3)
    rows3 = mycursor.fetchall()


    for k in rows:
        print(k[2])

    for i in rows2:
                print(i[2])
    
    id_holder=[]

    for j in rows3:
           id_holder.append((j[0]))

    print(len(id_holder))
    if len(rows3)<10:
          new_id=f'00{len(rows3)}'
    if len(rows3)>=10 and len(rows3)<100 :
          new_id=f'0{len(rows3)}'
    if len(rows3)>=100:
          new_id=f'{len(rows3)}'            


    print(id_holder)
    last_id=id_holder[len(rows3)-1]
    new_id=f'{last_id[0:10]}{new_id}'
    print("NOUVEAU FORAGE",new_id)







    
def setId(activite,self,event):
           if activite=="Forage":
                 query3= f"select * from tbl_localisation where colline like '{self.txt_coln.get()}' and id like 'FO-%' ORDER BY id ASC"           
           if activite=="Puit":
                 query3= f"select * from tbl_localisation where colline like '{self.txt_coln.get()}' and id like 'PU-%' ORDER BY id ASC"
           if activite=="Source":
                query3= f"select * from tbl_localisation where colline like '{self.txt_coln.get()}' and id like 'SR-%' ORDER BY id ASC"
                mycursor.execute(query3)
                rows3 = mycursor.fetchall()
                id_holder=[]
                for j in rows3:
                    id_holder.append((j[0]))
                if len(rows3)<10:
                      new_id=f'00{len(rows3)}'
                if len(rows3)>=10 and len(rows3)<100 :
                      new_id=f'0{len(rows3)}'
                if len(rows3)>=100:
                      new_id=f'{len(rows3)}'            
                last_id=id_holder[len(rows3)-1]
                new_id=f'{last_id[0:10]}{new_id}'
                self.txt_id.delete(0,END)
                self.txt_id.insert(0,new_id)
                
psycopg2.OperationalError: connection to server at "192.168.88.201", port 5432 failed: Connection timed out (0x0000274C/10060)                 


host="192.168.88.201"
db= "hydrogeology"
userM="postgres"
password= "igebu99"  
mydb = psycopg2.connect(host=host,database=db, user=userM, password=password)
query1= f"select id from tbl_localisation where province like 'Cankuzo' and commune like 'Mishiha' and colline like 'Mishiha' and type_point_d_eau like 'Source'"
query2= f"select count(*) from tbl_localisation where province like 'Cankuzo' and commune like 'Mishiha' and colline like 'Mishiha' and type_point_d_eau like 'Source'"
query3= f"select id from tbl_localisation where province like 'Cankuzo' and type_point_d_eau like 'Forage'"
mycursor = mydb.cursor()
mycursor.execute(query1)
result1 = mycursor.fetchall()
mycursor.execute(query2)
result2 = mycursor.fetchone()

mycursor.execute(query3)
result3 = mycursor.fetchall()

print(result2)

for i in result1:
     print(*i)
      
for k in result3:
      print(*k)
'''      


mydb = psycopg2.connect(host="192.168.88.201",database="hydrogeology", user="postgres", password="igebu99")

query1= f"select usename, passwd from pg_user where usename like 'fulgencen'"

query2=f"SELECT CURRENT_USER"
mycursor = mydb.cursor()
mycursor.execute(query1)
row = mycursor.fetchall()

mydb = psycopg2.connect(host="192.168.88.201",database="hydrogeology", user="postgres", password="igebu99")
query2=f"SELECT CURRENT_USER"
mycursor = mydb.cursor()
mycursor.execute(query2)
row2 = mycursor.fetchall()

for i in row:
      print(*i)
      
for k in row2:
      print(*k)



      
      
