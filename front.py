from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk


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
    
    txt_id=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=('arial',11,'bold'))
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

    button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
    button_frame.place(x=1290,y=0,width=170,height=270)
    
    btn_add=Button(button_frame,text='Save',font=('arial',15,'bold'),width=13,bg='blue',fg='white')
    btn_add.grid(row=0,column=0,padx=2,pady=2)

    btn_update=Button(button_frame,text='Update',font=('arial',15,'bold'),width=13,bg='blue',fg='white')
    btn_update.grid(row=1,column=0,padx=2,pady=2)

    btn_clear=Button(button_frame,text='Clear',font=('arial',15,'bold'),width=13,bg='blue',fg='white')
    btn_clear.grid(row=2,column=0,padx=2,pady=2)

    btn_delete=Button(button_frame,text='Delete',font=('arial',15,'bold'),width=13,bg='blue',fg='white')
    btn_delete.grid(row=3,column=0,padx=2,pady=2)

    btn_promote=Button(button_frame,text='Promote',font=('arial',15,'bold'),width=13,bg='blue',fg='white')
    btn_promote.grid(row=4,column=0,padx=2,pady=2)
    
    # lower
    lower_frame=LabelFrame(Main_,bd=2,relief=RIDGE,bg='white',text='Employee Information Table',font=('times new roman',11,'bold'),fg='red')
    lower_frame.place(x=10,y=280,width=1480,height=270)
    
    Search_frame=LabelFrame(lower_frame,bd=2,relief=RIDGE,bg='white',text='Search Employee Information',font=('times new roman',11,'bold'),fg='red')
    Search_frame.place(x=0,y=0,width=1450,height=60)

    search_by=Label(Search_frame,text='Enter ID: ',font=('arial',14,'bold'),width=17)
    search_by.grid(row=0,column=0,padx=5,sticky=W)
    txt_add=ttk.Entry(Search_frame,width=22,font=('arial',11,'bold'))
    txt_add.grid(row=0,column=1,padx=2,pady=7)

    btn_promote=Button(Search_frame,text='Search',font=('arial',15,'bold'),width=13,bg='blue',fg='white')
    btn_promote.grid(row=0,column=2,padx=2,pady=2)

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
    self.employee_table.heading('email',text='Email')
    self.employee_table.heading('Phone number',text='Phone Number')
    self.employee_table.heading('address',text='Address')
    self.employee_table.heading('Salary',text='Salary')
    

    self.employee_table['show']='headings'
    self.employee_table.column("id",width=100)
    self.employee_table.column("dep",width=100)
    self.employee_table.column("name",width=100)
    self.employee_table.column("email",width=100)
    self.employee_table.column("Phone number",width=100)
    self.employee_table.column("address",width=100)
    self.employee_table.column("Salary",width=100)

    self.employee_table.pack(fill=BOTH,expand=1)
if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()
 
