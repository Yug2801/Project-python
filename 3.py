from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from os import system
import mysql.connector





class Employee :
  
  def __init__(self,root):
    self.root=root
    self.root.geometry("1530x790+0+0")
    self.root.title('Employee management System')


    self.var_id=StringVar()
    self.var_dep=StringVar()
    self.var_name=StringVar()
    self.var_email=StringVar()
    self.var_add=StringVar()
    self.var_phn=StringVar()
    self.var_salary=StringVar()

    self.var_search=StringVar()
    lbl_title=Label(self.root,text='Employee Management System', font=('times new roman',37,'bold'))
    lbl_title.place(x=0,y=0,width=1530,height=50)

    Main_=Frame(self.root,bd=2,relief=RIDGE,bg='white')
    Main_.place(x=10,y=170,width=1500,height=560)


    # upper
    upper_frame=LabelFrame(Main_,bd=2,relief=RIDGE,bg='white',text='Employee Information',font=('times new roman',11,'bold'),fg='red')
    upper_frame.place(x=10,y=10,width=1480,height=270)
    
    lbl_dpt=Label(upper_frame,text='Department',font=('arial',14,'bold'),width=17)
    lbl_dpt.grid(row=0,column=0,padx=2,sticky=W)

    
    combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_dep,font=('arial',11,'bold'),width=17,state='readonly')
    combo_dep['value']=('Select Department','HR','SOTWARE ENGINEER','MANAGER')
    combo_dep.current(0)
    combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)
    

    lbl_name=Label(upper_frame,text='Name',font=('arial',14,'bold'),width=17)
    lbl_name.grid(row=1,column=0,padx=2,sticky=W)
    
    txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=('arial',11,'bold'))
    txt_name.grid(row=1,column=1,padx=2,pady=7)

    lbl_id=Label(upper_frame,text='ID',font=('arial',14,'bold'),width=17)
    lbl_id.grid(row=1,column=3,padx=2,sticky=W)
    
    txt_id=ttk.Entry(upper_frame,textvariable=self.var_id,width=22,font=('arial',11,'bold'))
    txt_id.grid(row=1,column=4,padx=2,pady=7)


    lbl_mail=Label(upper_frame,text='Email-id',font=('arial',14,'bold'),width=17)
    lbl_mail.grid(row=2,column=0,padx=2,sticky=W)
    txt_mail=ttk.Entry(upper_frame,textvariable=self.var_email,width=22,font=('arial',11,'bold'))
    txt_mail.grid(row=2,column=1,padx=2,pady=7)

    lbl_phn=Label(upper_frame,text='Phone Number',font=('arial',14,'bold'),width=17)
    lbl_phn.grid(row=3,column=0,padx=2,sticky=W)

    txt_phn=ttk.Entry(upper_frame,textvariable=self.var_phn,width=22,font=('arial',11,'bold'))
    txt_phn.grid(row=3,column=1,padx=2,pady=7)

    lbl_add=Label(upper_frame,text='Address',font=('arial',14,'bold'),width=17)
    lbl_add.grid(row=4,column=0,padx=2,sticky=W)

    txt_add=ttk.Entry(upper_frame,textvariable=self.var_add,width=22,font=('arial',11,'bold'))
    txt_add.grid(row=4,column=1,padx=2,pady=7)

    lbl_salary=Label(upper_frame,text='Salary',font=('arial',14,'bold'),width=17)
    lbl_salary.grid(row=5,column=0,padx=2,sticky=W)

    txt_salary=ttk.Entry(upper_frame,textvariable=self.var_salary,width=22,font=('arial',11,'bold'))
    txt_salary.grid(row=5,column=1,padx=2,pady=7)

    #button

    button_frame=Frame(upper_frame,bd=3,relief=RIDGE,bg='white')
    button_frame.place(x=1290,y=0,width=170,height=270)
    
    btn_add=Button(button_frame,text='Save',command=self.add_data,font=('arial',15,'bold'),width=13,bg='blue',fg='white')
    btn_add.grid(row=0,column=0,padx=2,pady=2)

    btn_update=Button(button_frame,text='Update',command=self.update,font=('arial',15,'bold'),width=13,bg='blue',fg='white')
    btn_update.grid(row=1,column=0,padx=2,pady=2)

    btn_clear=Button(button_frame,text='Clear',command=self.reset,font=('arial',15,'bold'),width=13,bg='blue',fg='white')
    btn_clear.grid(row=2,column=0,padx=2,pady=2)

    btn_delete=Button(button_frame,text='Delete',command=self.delete,font=('arial',15,'bold'),width=13,bg='blue',fg='white')
    btn_delete.grid(row=3,column=0,padx=2,pady=2)

    # lower
    lower_frame=LabelFrame(Main_,bd=2,relief=RIDGE,bg='white',text='Employee Information Table',font=('times new roman',11,'bold'),fg='red')
    lower_frame.place(x=10,y=280,width=1480,height=270)
    
    Search_frame=LabelFrame(lower_frame,bd=2,relief=RIDGE,bg='white',text='Search Employee Information',font=('times new roman',11,'bold'),fg='red')
    Search_frame.place(x=0,y=0,width=1450,height=60)

    search_by=Label(Search_frame,text='Enter ID: ',font=('arial',14,'bold'),width=17)
    search_by.grid(row=0,column=0,padx=5,sticky=W)

    
    txt_add=ttk.Entry(Search_frame,textvariable=self.var_search,width=22,font=('arial',11,'bold'))
    txt_add.grid(row=0,column=1,padx=2,pady=7)

    btn_search=Button(Search_frame,text='Search',command=self.search,font=('arial',15,'bold'),width=13,bg='blue',fg='white')
    btn_search.grid(row=0,column=2,padx=2,pady=2)


   
# ================Employee Table======================

    table_frame=Frame(lower_frame ,bd=2,relief=RIDGE,bg='white',)
    table_frame.place(x=0,y=60,width=1480,height=180)
    
    scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

    self.employee_table=ttk.Treeview(table_frame,column=("id","dep","name","email","Phone number","address","Salary"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x.config(command=self.employee_table.xview)
    scroll_y.config(command=self.employee_table.yview)

    self.employee_table.heading('id',text='ID')
    self.employee_table.heading('dep',text='Department')
    self.employee_table.heading('name',text='Name')

    self.employee_table.heading('Phone number',text='Phone Number')
    self.employee_table.heading('email',text='Email')
    
    self.employee_table.heading('address',text='Address')
    self.employee_table.heading('Salary',text='Salary')
    

    self.employee_table['show']='headings'
    self.employee_table.column("id",width=100)
    self.employee_table.column("dep",width=100)
    self.employee_table.column("name",width=100)
    self.employee_table.column("Phone number",width=100)
    self.employee_table.column("email",width=100)
    self.employee_table.column("address",width=100)
    self.employee_table.column("Salary",width=100)
    self.employee_table.pack(fill=BOTH,expand=1)

    self.employee_table.bind("<ButtonRelease>",self.get_cursor)
    self.fetch()

    #===function
  def add_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                dataBase = mysql.connector.connect(host="127.0.0.1", port="3307", user="root", password="Yug@28012003", auth_plugin="mysql_native_password",database="YUG")
                data = (self.var_id.get(),
                  self.var_dep.get(),
    self.var_name.get(),
    self.var_email.get(),
    self.var_add.get(),
    self.var_phn.get(),
    self.var_salary.get())
                sql = 'insert into employedata values(%s,%s,%s,%s,%s,%s,%s)'
                c = dataBase.cursor()
                c.execute(sql, data)
                dataBase.commit()
                self.fetch()
                dataBase.close()
                messagebox.showinfo('Success','Employee has been added',parent=self.root)
            except Exception as es:
              messagebox.showerror('Error',f'Due to :{str(es)}',parent=self.root)

  def fetch(self):
    dataBase = mysql.connector.connect(host="127.0.0.1", port="3307", user="root", password="Yug@28012003", auth_plugin="mysql_native_password",database="YUG")
    c = dataBase.cursor()   
    c.execute('select * from employedata')
    data=c.fetchall()
    if len(data)!=0:
      self.employee_table.delete(*self.employee_table.get_children())
      for i in data:
        self.employee_table.insert("",END,values=i)
      dataBase.commit()
    dataBase.close()

  def get_cursor(self,event=""):
    cursor_row=self.employee_table.focus()
    content=self.employee_table.item(cursor_row)
    data=content['values']


    self.var_id.set(data[0])
    self.var_dep.set(data[1])
    self.var_name.set(data[2])
    self.var_email.set(data[3])
    self.var_phn.set(data[4])
    self.var_add.set(data[5])
    self.var_salary.set(data[6])

  def update(self):
    if self.var_dep.get()=="" :
       messagebox.showerror('Error','All fields are required')
    else:
       try:
          update=messagebox.askyesno('Update','Are you sure update this employee data')
          if update>0:
            dataBase = mysql.connector.connect(host="127.0.0.1", port="3307", user="root", password="Yug@28012003", auth_plugin="mysql_native_password",database="YUG")
            c = dataBase.cursor()      
            c.execute('update employedata set Post=%s,NAME=%s,Email_Id=%s,Phone_no=%s,Address=%s,Salary=%s where ID =%s',(
                  self.var_dep.get(),
                  self.var_name.get(),
                   self.var_email.get(),
                     self.var_add.get(),
                    self.var_phn.get(),
                   self.var_salary.get(),
                   self.var_id.get()
              
            ))
          else:
            if not update:
              return
          dataBase.commit()
          self.fetch()
          dataBase.close()
          messagebox.showinfo('success','Employee Successfully updated',parent=self.root)

       except Exception as ex:
        messagebox.showerror('Error',f'Due to :{str(ex)}',parent=self.root)

  def delete(self):
    if self.var_dep.get()=="" :
       messagebox.showerror('Error','All fields are required')
    else:
       try:
          Delete1=messagebox.askyesno('Delete','Are you sure delete this employee data')
          if Delete1>0:
            dataBase = mysql.connector.connect(host="127.0.0.1", port="3307", user="root", password="Yug@28012003", auth_plugin="mysql_native_password",database="YUG")
            c = dataBase.cursor()      
            c.execute('delete from employedata where ID LIKE ' +str(self.var_id.get()
           ))
              
            
          else:
            if not Delete1:
              return
          dataBase.commit()
          self.fetch()
          self.fetch()
          self.fetch()
          dataBase.close()
          messagebox.showinfo('success','Employee Successfully deleted',parent=self.root)

       except Exception as ex:
        messagebox.showerror('Error',f'Due to :{str(ex)}',parent=self.root)
  
  def reset(self):
    self.var_id.set("")
    self.var_dep.set("Select Department")
    self.var_name.set("")
    self.var_email.set("")
    self.var_phn.set("")
    self.var_add.set("")
    self.var_salary.set("")

  
    
  def search(self):
    if self.var_dep.get()=="" :
       messagebox.showerror('Error','All fields are required')
    else:
       try:
          
            dataBase = mysql.connector.connect(host="127.0.0.1", port="3307", user="root", password="Yug@28012003", auth_plugin="mysql_native_password",database="YUG")
            c = dataBase.cursor()      
            c.execute("select * from employedata where ID LIKE " +str(self.var_search.get()))
            rows=c.fetchall()
            if len(rows)!=0:
              self.employee_table.delete(*self.employee_table.get_children())
              for i in rows:
                self.employee_table.insert("",END,values=i)
              
            dataBase.commit()
         
            dataBase.close()
           
       except Exception as ex:
        messagebox.showerror('Error',f'Due to :{str(ex)}',parent=self.root)
  

        
           

     
          
       
        

if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()
 
