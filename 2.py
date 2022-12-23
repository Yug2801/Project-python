
import sys
import mysql.connector

dataBase = mysql.connector.connect(host="localhost",user="root", password="Coder#04",database="Sojal")


def Add_Employ():
    print("{:>60}".format("-->>Add Employee Record<<--"))
    Id = int(input("Enter Employee Id: "))
    c=dataBase.cursor()
    c.execute("select * from empdata")
    data=c.fetchall()
    for row in data:
        if(row[0]==Id):
            print("Employee Already Exists......")
            menu()
    
   
    Name = input("Enter Employee Name: ")
    Email_Id = input("Enter Employee Email ID: ")
    Phone_no = int(input("Enter Employee Phone No.: "))
    Address = input("Enter Employee Address: ")
    Post = input("Enter Employee Post: ")
    Salary = int(input("Enter Employee Salary: "))
    data = (Id, Name, Email_Id, Phone_no, Address, Post, Salary)
    sql = 'insert into empdata values(%s,%s,%s,%s,%s,%s,%s)'
    c = dataBase.cursor()
    c.execute(sql, data)
    dataBase.commit()
    print("Successfully Added Employee Record")
    menu()

def Display():
    print("{:>60}".format("-->> Display Employee Record <<--"))

    sql = 'select * from empdata'
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
    menu()
    
def Update():
    print("                         ***********************************")
    print("                         -->> MODIFY EMPLOYEE DETAILS : <<--")
    print("                         ***********************************")
    print("1. Modify email address")
    print("2. Modify Phone_no address")
    print("3. Modify address address")
    print("4. Go back to main menu")
    print("                        -->> Choice option [1,2,3] <<--")
    
    ch=int(input("Enter the operation"))
    Id = input("Enter Employee Id: ")
    if ch==1:
        Email_Id = input("Enter new Email ID: ")
        sql = "UPDATE empdata set Email_Id = '{}' where Id = {}".format(Email_Id,Id)
        c = dataBase.cursor()
        c.execute(sql)
        dataBase.commit()
    elif ch==2:
        Phone_no = int(input("Enter new Phone No.: "))
        sql = "UPDATE empdata set Phone_no = {} where Id = {}".format(Phone_no,Id)
        c = dataBase.cursor()
        c.execute(sql)
        dataBase.commit() 
    elif ch==3:
        Address = input("Enter Employee Address: ")
        sql = "UPDATE empdata set Address = '{}' where Id = {}".format(Address,Id)
        c = dataBase.cursor()
        c.execute(sql)
        dataBase.commit()
    elif ch==4:
        menu()
    else:
        print("Enter Valid Choice.....")
        Update()
        
    print("Updated Employee Record")
    d=input("Do you want to update more details (Y/N)")
    if(d=='Y' or d=='y'):
        Update()
    

def  Promote():
    Id = input("Enter Employee Id: ")
    Amount  = int(input("Enter Increase Salary: "))
    
    sql = 'select Salary from empdata where Id=%s'
    data = (Id,)
    c = dataBase.cursor()
        
       
    c.execute(sql,data)
        
        
    r = c.fetchone()
    t = r[0]+Amount
        
    sql = 'update empdata set Salary = %s where Id = %s'
    d = (t, Id)

    c.execute(sql, d)

    dataBase.commit()
    print("Employee Promoted")
    menu()
    
def Remove():
    Id = input("Enter Employee Id: ")
    sql = 'delete from empdata where Id = %s'
    data = (Id,)
    c = dataBase.cursor()

    c.execute(sql, data)

    dataBase.commit()
    print("Employee Removed")
    menu()

def Search():
    print("{:>60}".format("-->> Search Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    sql = 'select * from empdata where Id = %s'
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
        print("{:>60}".format("Have A NIce Day :)"))
        sys.exit()
    else:
        print("Invalid Choice!")
        menu()
    



menu()
