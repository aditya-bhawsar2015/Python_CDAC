import pymysql

connection = pymysql.connect(host="localhost", port=3306, user="root", password="root", database="dai03")

mycursor = connection.cursor()

mycursor.execute("insert into customers values (1,'John Doe', 30, 't', 50000.00)")

connection.commit()

mycursor.close()
connection.close()
