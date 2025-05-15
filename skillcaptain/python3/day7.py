import mysql.connector

connection = mysql.connector.connect(
    host ='localhost',
    user ='root',
    password ='MySecurePassword123!',
    database = 'my_database',
)


cursor = connection.cursor()
student_name = "ekta"
cursor.execute("SELECT * FROM student where name = %s",(student_name,))


rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
connection.close()