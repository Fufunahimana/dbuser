import psycopg2





server = '192.168.88.201'
db = "hydrogeology"
user= "postgres"
pwd = "Igebu99"
port = 5432


conn = psycopg2.connect(host="192.168.88.201",database="hydrogeology", user="postgres", password="igebu99")
conn.close()

if conn:
    print("connection etablie")
