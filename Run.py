import Tools.databaseTools as db
import Tools.ttktools as tools 
import Tools.Design as des

def prepare_DB():    
    db.create_db("Company")
    db.create_table("Employee","Emp_Id","INT",40)
    db.addcolumn("Employee","Emp_Name","varchar",40)
    db.addcolumn("Employee","Address","varchar",40)
    db.addcolumn("Employee","salary","int",40)
    
def Refresh():
    id.set(db.getautonumber("Employee" , "Emp_Id"))
    name.set("")
    address.set("")
    salary.set(0)
    if len(frame.winfo_children()) == 4:
        frame.winfo_children()[3].destroy()        
    info = tools.Table(frame,["ID","Name","Address","Salary"],db.GetAllTableData("Employee") , "#EEEEEE" , "#D3DCE3")
    info.grid(row=0,column=1,rowspan=2, sticky="n" , padx=des.PAD1 , pady=des.PAD1)
    box1.winfo_children()[3].focus()  
    box2.winfo_children()[0].config(state='enable')
    box2.winfo_children()[1].config(state='disable')
    box2.winfo_children()[2].config(state='disable')
    

 
try:    

    prepare_DB()
    
    frame = tools.form(height=400,width=1200)

    box1 = tools.frame(frame)
    box1.grid(row=0,column=0, padx=des.PAD1 , pady=des.PAD1)

    box2 = tools.frame(frame)
    box2.grid(row=1,column=0, padx=des.PAD1 , pady=des.PAD1)    

    box3 = tools.frame(frame)    
    box3.grid(row=2,column=0, padx=des.PAD1 , pady=des.PAD1)    

    id = tools.intVar(db.getautonumber("Employee" , "Emp_Id"))
    name = tools.strVar()
    address = tools.strVar()
    salary = tools.intVar()
    searchtype = tools.intVar()
    
    

    def add():                
        if not isempty():
            if not db.isexist(id.get(),"Emp_Id","Employee"):
                db.execute("insert into Employee values (%d,'%s','%s',%d)"%(id.get(),name.get(),address.get(),salary.get()))                
                Refresh()
            else:
                tools.msg("Employee is already exist")                 
        else:
            tools.msg("Empty values is not accepted") 

    def find():        
        wantedId = tools.inbox("Enter Employee ID",True)        
        if wantedId.strip()!="":
            if db.isexist(wantedId,"Emp_Id","Employee"):
                empdata = db.GetData("select * from Employee where Emp_Id = " + wantedId)[0]
                id.set(empdata[0])
                name.set(empdata[1])
                address.set(empdata[2])
                salary.set(empdata[3])
                            
                box2.winfo_children()[0].config(state='disable')
                box2.winfo_children()[1].config(state='enable')
                box2.winfo_children()[2].config(state='enable')
            else:
                tools.msg("no Employee with that id exist") 
        else:
            tools.msg("Empty values is not accepted")         
    def update():
        if not isempty():  
            if db.isexist(id.get(),"Emp_Id","Employee"):
                db.execute("update Employee set Emp_Name='%s', Address='%s',salary=%d where Emp_Id = %d"%(name.get(),address.get(),salary.get(),id.get()))            
                Refresh()        
            else:
                if tools.askbox("no Employee with that id exist would you like to add"):                     
                    add()
                
        else:
            tools.msg("Empty values is not accepted")         
    
    
    def Delete():
        if not isempty():  
            if db.isexist(id.get(),"Emp_Id","Employee"):
                if tools.askbox("Are you sure you want to delete"):                     
                    db.execute("delete from Employee where Emp_Id = '%d'"%(id.get()))            
                    Refresh()        
            else:
                tools.msg("no Employee with that id")
                    
                
        else:
            tools.msg("Empty values is not accepted")      
    def Exit():
        frame.destroy()
    def clear():
        Refresh()

    def search():        
        target = box3.winfo_children()[5].get()
        if len(frame.winfo_children()) == 4:
            if searchtype.get()==0:
                frame.winfo_children()[3].destroy()        
                info = tools.Table(frame,["ID","Name","Address","Salary"],db.GetData("select * from Employee where Emp_Id like '%"+ target + "%'") , "#EEEEEE" , "#D3DCE3")
                info.grid(row=0,column=1,rowspan=2, sticky="n" , padx=des.PAD1 , pady=des.PAD1)
            elif searchtype.get()==1:            
                frame.winfo_children()[3].destroy()        
                info = tools.Table(frame,["ID","Name","Address","Salary"],db.GetData("select * from Employee where Emp_Name like '%"+ target + "%'") , "#EEEEEE" , "#D3DCE3")
                info.grid(row=0,column=1,rowspan=2, sticky="n" , padx=des.PAD1 , pady=des.PAD1)
            elif searchtype.get()==2:
                frame.winfo_children()[3].destroy()        
                info = tools.Table(frame,["ID","Name","Address","Salary"],db.GetData("select * from Employee where Address like '%"+ target + "%'") , "#EEEEEE" , "#D3DCE3")
                info.grid(row=0,column=1,rowspan=2, sticky="n" , padx=des.PAD1 , pady=des.PAD1)
            elif searchtype.get()==3:
                frame.winfo_children()[3].destroy()        
                info = tools.Table(frame,["ID","Name","Address","Salary"],db.GetData("select * from Employee where salary like '%"+ target + "%'") , "#EEEEEE" , "#D3DCE3")
                info.grid(row=0,column=1,rowspan=2, sticky="n" , padx=des.PAD1 , pady=des.PAD1)        
    

    def isempty():
        return name.get().strip()=="" or address.get().strip()=="" or salary.get()==0
        
    tools.label(box1 , "Employee ID : ").grid(row=0,column=0 , sticky="e" , pady=des.PAD0)
    tools.textbox(box1,id,True,True).grid(row=0,column=1)
    
    tools.label(box1 , "Employee Name : ").grid(row=1,column=0 , sticky="e",pady=des.PAD0)
    tools.textbox(box1,name).grid(row=1,column=1)

    tools.label(box1 , "Employee address : ").grid(row=2,column=0 , sticky="e",pady=des.PAD0)
    tools.textbox(box1,address).grid(row=2,column=1)

    tools.label(box1 , "Employee salary : ").grid(row=3,column=0 , sticky="e",pady=des.PAD0)
    tools.textbox(box1,salary,True).grid(row=3,column=1)       

    names = ("Add","update","Delete","Find","clear")
    Commands = (add,update,Delete,find,clear)


    for i in range(0,len(names)):                    
            tools.button(form=box2 , text=names[i]   ,command=Commands[i]).grid(row=0,column=i, padx=des.PAD4)
        
    tools.button(form=box2 , text="Close" ,command=Exit).grid(row=1,column=0 , columnspan=5 , pady=des.PAD1) 

    
    tools.label(box3 , "Search By : ").grid(row=0,column=0 , sticky="w" , pady=des.PAD0)

    tools.radio(box3,"ID"      , 0,searchtype).grid(row=0,column=1 , sticky="w" , pady=des.PAD0)
    tools.radio(box3,"Name"    , 1,searchtype).grid(row=0,column=2 , sticky="w" , pady=des.PAD0)
    tools.radio(box3,"Address" , 2,searchtype).grid(row=0,column=3 , sticky="w" , pady=des.PAD0)
    tools.radio(box3,"salary"  , 3,searchtype).grid(row=0,column=4 , sticky="w" , pady=des.PAD0)

    s = tools.textbox(box3)
    s.grid(row=1,column=0 , columnspan=3)    
    s.bind('<Return>',lambda _:search())  
    tools.button(box3 , "Search" ,command=search).grid(row=1,column=3 , columnspan=2 , pady=des.PAD1) 

    
    tools.bgall(frame, des.BACKGROUND)
    tools.fgall(frame,des.FOREGROUND)
    tools.fontall(frame,des.FONT1)
    tools.justifyall(frame,"center")   
    Refresh()
    frame.mainloop()
except BaseException as ex:
    print(ex)
    input("")
