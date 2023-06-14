import psycopg2






conn = psycopg2.connect(database="hydrogeyology",host="192.168.88.201",user="fulgencen",password="79166956",port="5432")
cursor = conn.cursor()

                        print"base des donnée trouvé"