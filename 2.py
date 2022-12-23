import mysql.connector

dataBase = mysql.connector.connect(host="127.0.0.1", port="3307", user="root", password="Yug@28012003", auth_plugin="mysql_native_password",database="YUG")

cursorObject = dataBase.cursor()

# creating table
empdata = """CREATE TABLE EMPDATA (
                 ID INTEGER(100) NOT NULL,
                 NAME  VARCHAR(20) NOT NULL,
                 Email_Id VARCHAR(50),
                 Phone_no INTEGER(10) NOT NULL,
                 Address VARCHAR(50),
                 Post VARCHAR(50),
                 Salary INTEGER(50)
                 )"""

cursorObject.execute(empdata)

dataBase.close()
