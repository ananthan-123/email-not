import psycopg2
from datetime import date

today = date.today()

try:
    connection = psycopg2.connect(user = "emailnotuser",
                                  password = "password",
                                  host = "localhost",
                                  port = "",
                                  database = "emailnot")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM dataModel WHERE activated = True AND date = "+today)
    rows = cursor.fetchall()

    with open("/home/ananthan/email/cronlog.txt", "w") as file1:
        for i in rows:
            file1.write(rows,"\n")

    # cursor.execute("DELETE FROM dataModel WHERE activated = True AND date < "+today)

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")






# */15 * * * * /usr/bin/python script.py





    
