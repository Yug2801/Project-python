from os import system
import mysql.connector

dataBase = mysql.connector.connect(host="127.0.0.1", port="3307", user="root", password="Yug@28012003", auth_plugin="mysql_native_password",database="YUG")




def Add_Employ():
    print("{:>60}".format("-->>Add Employee Record<<--"))
    Id = input("Enter Employee Id: ")
    Name = input("Enter Employee Name: ")
    Email_Id = input("Enter Employee Email ID: ")
    Phone_no = input("Enter Employee Phone No.: ")
    Address = input("Enter Employee Address: ")
    Post = input("Enter Employee Post: ")
    Salary = input("Enter Employee Salary: ")
    data = (Id, Name, Email_Id, Phone_no, Address, Post, Salary)
    sql = 'insert into employeedata values(%s,%s,%s,%s,%s,%s,%s)'
    c = dataBase.cursor()
    c.execute(sql, data)
    dataBase.commit()
    print("Successfully Added Employee Record")
    press = input("Press Any Key To dataBasetinue..")
    menu()

def Display():
    print("{:>60}".format("-->> Display Employee Record <<--"))

    sql = 'select * from employeedata'
    c = dataBase.cursor()

  
    c.execute(sql)

    r = c.fetchall()
    for i in r:
        print("Employee Id: ", i[0])
        print("Employee Name: ", i[1])
        print("Employee Email Id: ", i[2])
        print("Employee Phone No.: ", i[3])
        print("Employee Address: ", i[4])
        print("Employee Post: ", i[5])
        print("Employee Salary: ", i[6])
        print("\n")
    press = input("Press Any key To dataBasetinue..")
    menu()
    
def Update():
    print("{:>60}".format("-->> Update Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    Email_Id = input("Enter Employee Email ID: ")
    Phone_no = input("Enter Employee Phone No.: ")
    Address = input("Enter Employee Address: ")
     
    sql = 'UPDATE employeedata set Email_Id = %s, Phone_no = %s, Address = %s where Id = %s'
    data = (Email_Id, Phone_no, Address, Id)
    c = dataBase.cursor()
    c.execute(sql, data)
    dataBase.commit()
    print("Updated Employee Record")
    press = input("Press Any Key To dataBasetinue..")
    menu()

def  Promote():
    Id = input("Enter Employee Id: ")
    print("                         *************************")
    print("                         -->> PROMOTE EMPLOYEE<<--")
    print("                         *************************")
    print("1. To Update Post")
    print("2. To Update Salary")
    
    ah=int(input("Enter  the operation: "))
    if ah==1:
        post=input("Enter the New Post of the Employee:")
        sql = 'select Post from employeedata where Id=%s'
        data=(Id,)
        c=dataBase.cursor()
        c.execute(sql,data)
        r = c.fetchone()
        t=post
        sql = 'update employeedata set Post = %s where Id = %s'
        d = (t, Id)

        c.execute(sql, d)
        
    elif ah==2:
        Amount  = int(input("Enter Increase Salary: "))
    
        sql = 'select Salary from  employeedata where Id=%s'
        data = (Id,)
        c = dataBase.cursor()
        
       
        c.execute(sql,data)
        
        
        r = c.fetchone()
        t = r[0]+Amount
        
        sql = 'update employeedata set Salary = %s where Id = %s'
        d = (t, Id)

        c.execute(sql, d)

    

    dataBase.commit()
    print("Employee Promoted")
    press = input("Press Any key To continue..")
    menu()
    
def Remove():
    Id = input("Enter Employee Id: ")
    sql = 'delete from employeedata where Id = %s'
    data = (Id,)
    c = dataBase.cursor()

    c.execute(sql, data)

    dataBase.commit()
    print("Employee Removed")
    press = input("Press Any key To Continue..")
    menu()

def Search():
    print("{:>60}".format("-->> Search Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    sql = 'select * from employeedata where Id = %s'
    data = (Id,)
    c = dataBase.cursor()
        
    c.execute(sql,data)

    r = c.fetchall()
    for i in r:
        print("Employee Id: ", i[0])
        print("Employee Name: ", i[1])
        print("Employee Email Id: ", i[2])
        print("Employee Phone No.: ", i[3])
        print("Employee Address: ", i[4])
        print("Employee Post: ", i[5])
        print("Employee Salary: ", i[6])
        print("\n")
    press = input("Press Any key To Continue..")
    menu()

def menu():
    print("                         ***********************************")
    print("                         -->> Employee Management System<<--")
    print("                         ***********************************")
    print("1. Add Employee")
    print("2. Display Employee Record")
    print("3. Update Emplyee Record")
    print("4. Promote Emplyee Record")
    print("5. Remove Emplyee Record")
    print("6. Search Emplyee Record")
    print("7. Exit")
    print("                        -->> Choice option [1,2,3,4,5,6,7] <<--")
    ch=int(input("Enter  the operation"))
    if ch==1:
        Add_Employ()
    elif ch==2:
        Display()
    elif ch==3:
        Update()
    elif ch==4:
        Promote()
    elif ch==5:
        Remove()
    elif ch==6:
        Search()
    elif ch == 7:
        system("cls")
        print("{:>60}".format("Have A NIce Day :)"))
        exit(0)
    else:
        print("Invalid Choice!")
        press = input("Press Any key To dataBasetinue..")
        menu()
    



menu()
