from tkinter import *
from tkinter import ttk
from db import DataBase
from tkinter import messagebox
from tkinter import Toplevel, Button, Tk, Menu  



def main():    

    pm=Tk()
    pm.title('Prison')
    pm.geometry('1310x515+0+0')
    pm.resizable(False,False)
    pm.configure(bg='#1f2e2e')##1f2e2e

    entries_frame=Frame(pm,bg='#1f2e2e')
    entries_frame.place(x=1,y=1,width=1310,height=510)
    title=Label(entries_frame,text='Prison BR',font=('Calibri',20,'bold'),bg='#1f2e2e',fg='white')
    title.place(x=575,y=25)

    btn_frame=Frame(entries_frame,bg='#1f2e2e',bd=1,relief=SOLID)
    btn_frame.place(x=475,y=150,width=335,height=279)

    def prisoners():
        pm.destroy()
        db=DataBase("Persons.db")
        
        #ساوينا القياس واحد 
        pr=Tk()
        pr.title('Prison')
        pr.geometry('1310x515+0+0')
        pr.resizable(False,False)
        pr.configure(bg='#1f2e2e')##1f2e2e
        

        firstName=StringVar()
        father=StringVar()
        lastName=StringVar()
        gender=StringVar()
        birthYear=StringVar()

        fromD=StringVar()
        toD=StringVar()

        txtKilll=StringVar()

        


        #label frames قسم جزء منشان الازرار و الانبوت
        entries_frame=Frame(pr,bg='#1f2e2e')
        entries_frame.place(x=1,y=1,width=360,height=510)
        title=Label(entries_frame,text='Prison BR',font=('Calibri',20,'bold'),bg='#1f2e2e',fg='white')
        title.place(x=120,y=15)
        
        entries_frame2=Frame(pr,bg='#1f2e2e')
        entries_frame2.place(x=350,y=400,width=800,height=200)
        
        entries_frame3=Frame(pr,bg='#1f2e2e')
        entries_frame3.place(x=750,y=400,width=800,height=200)
        
        
        #end prisoners between two times
        def getData(event):
            selected_row=tv.focus()
            data=tv.item(selected_row)
            global row 
            row=data["values"]
            firstName.set(row[1])
            father.set(row[2])
            lastName.set(row[3])
            gender.set(row[4])
            birthYear.set(row[5])
            txtAddress.delete(1.0,END)
            txtAddress.insert(END,row[6])

        def displayAll():
            tv.delete(*tv.get_children())
            for row in db.fetch():
                tv.insert("",END,values=row)


        def delete():
            db.remove(row[0])
            Clear()
            displayAll()

        def Clear():
            firstName.set("")
            father.set("")
            lastName.set("")
            gender.set("")
            birthYear.set("")
            txtAddress.delete(1.0,END)

        def add_Prisoner():
            if txtFName.get()=="" or txtLName.get()=="" or txtFather.get()=="" or txtBirth.get()=="" or txtAddress.get(1.0,END)=="":
                messagebox.showerror("Error","Pleace Fill all the Entry")
                return 
            db.insert(
                txtFName.get(),
                txtFather.get(),
                txtLName.get(),
                comboGender.get(),
                txtBirth.get(),
                txtAddress.get(1.0,END))
            messagebox.showinfo("Success","Added new Prisoner")
            Clear()
            displayAll()
        def Update():
            if txtFName.get()=="" or txtLName.get()=="" or txtFather.get()=="" or txtBirth.get()=="" or txtAddress.get(1.0,END)=="":
                messagebox.showerror("Error","Pleace Fill all the Entry")
                return 
            db.update(
                row[0],
                txtFName.get(),
                txtFather.get(),
                txtLName.get(),
                comboGender.get(),
                txtBirth.get(),
                txtAddress.get(1.0,END))
            messagebox.showinfo("Success","The Prisoner Data is Updated")
            Clear()
            displayAll()
        def printIt():
            db.printToExcel()
            messagebox.showinfo("Success","The Prisoner Data is Saved")
        def deleteFilePrison():
                import os
                if os.path.exists("PrisonerFile.xlsx"):
                    os.remove("PrisonerFile.xlsx")
                    messagebox.showinfo("Success","The Data Deleted")
                else:
                    messagebox.showinfo("Success","The Data Does not exist")
            
        def prisonBetween():
            tv.delete(*tv.get_children())
            for row in db.PrisonBetween(txtFrom.get(),txtTo.get()):
                tv.insert("",END,values=row)
        def showPrisonKilling():
            tv.delete(*tv.get_children())
            for row in db.showPrisonByOffence(txtKill.get()):
                tv.insert("",END,values=row)
            
        menubar = Menu(pr)  
        file = Menu(menubar, tearoff=0)  
        file.add_command(label="New")  
        file.add_command(label="Open")  
        file.add_command(label="Save")  
        file.add_command(label="Save as...")  
        file.add_command(label="Close")  
        
        file.add_separator()  
        
        file.add_command(label="Exit", command=pr.quit)  
        
        menubar.add_cascade(label="File", menu=file)  
        edit = Menu(menubar, tearoff=0)  
        edit.add_command(label="Undo")  
        
        edit.add_separator()  
        
        edit.add_command(label="Cut")  
        edit.add_command(label="Copy")  
        edit.add_command(label="Paste")  
        edit.add_command(label="Delete")  
        edit.add_command(label="Select All")  
        
        menubar.add_cascade(label="Edit", menu=edit)  
        
        menubar.add_cascade(label="Main", command=main)  
        
        pr.config(menu=menubar)  

        # btnhidee=Button(entries_frame,text='Export',bg='white',bd=1,relief=SOLID,cursor='hand2',command=printIt)
        # btnhidee.place(x=110,y=10)
        #عنوان الانبوات
        lblFName=Label(entries_frame,text="FirstName",font=('Calibri',16),bg='#1f2e2e',fg='white')##1f2e2e
        lblFName.place(x=10,y=80)
        #الانبوت من نوع انتري يعني ادخال يدوي 😁
        txtFName=Entry(entries_frame,textvariable=firstName,width=20,bd=0,relief=SOLID,font=('Calibari',16))
        txtFName.place(x=120,y=80)

        lblFather=Label(entries_frame,text="Father",font=('Calibri',16),bg='#1f2e2e',fg='white')
        lblFather.place(x=10,y=130)
        txtFather=Entry(entries_frame,textvariable=father,width=20,bd=0,relief=SOLID,font=('Calibari',16))#527a7a
        txtFather.place(x=120,y=130)


        lblLName=Label(entries_frame,text="LastName",font=('Calibri',16),bg='#1f2e2e',fg='white')
        lblLName.place(x=10,y=180)
        txtLName=Entry(entries_frame,textvariable=lastName,width=20,bd=0,relief=SOLID,font=('Calibari',16))
        txtLName.place(x=120,y=180)

        lblGender=Label(entries_frame,text="Gender",font=('Calibri',16),bg='#1f2e2e',fg='white')
        lblGender.place(x=10,y=230)


        comboGender=ttk.Combobox(entries_frame,textvariable=gender,state='readonly',width=20,font=('Calibri',16))
        comboGender['values']=("Male","Female")
        comboGender.place(x=120,y=230)

        lblBirth=Label(entries_frame,text="BirthYear",font=('Calibri',16),bg='#1f2e2e',fg='white')
        lblBirth.place(x=10,y=280)
        txtBirth=Entry(entries_frame,textvariable=birthYear,width=20,bd=0,relief=SOLID,font=('Calibari',16))
        txtBirth.place(x=120,y=280)

        lblAddress=Label(entries_frame,text="Address: ",font=('Calibri',16),bg='#1f2e2e',fg='white')
        lblAddress.place(x=10,y=330)
        txtAddress=Text(entries_frame,width=23,height=1,bd=0,relief=SOLID,font=('Calibri',16))
        txtAddress.place(x=120,y=330)

        

        #buttons frame الازرار و تزبيط قياساتها 
        btn_frame=Frame(entries_frame,bg='#1f2e2e',bd=1,relief=SOLID)
        btn_frame.place(x=10,y=400,width=335,height=100)

        btnAdd=Button(btn_frame,
                    text='Insert Prisoner',
                    width=14,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    command=add_Prisoner

                    ).place(x=4,y=5)
        btnEdit=Button(btn_frame,
                    text='Update Prisoner',
                    width=14,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    command=Update
                    ).place(x=4,y=50)

        btnDelete=Button(btn_frame,
                    text='Delete Prisoner',
                    width=14,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    command=delete
                    ).place(x=170,y=5)
        btnClear=Button(btn_frame,
                    text='Clear Prisoners',
                    width=14,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    command=Clear
                    ).place(x=170,y=50)
        
        #button for prison between 
        btn_frame1=Frame(entries_frame2,bg='#1f2e2e',bd=1,relief=SOLID)
        btn_frame1.place(x=13,y=1,width=380,height=100)
        txtFrom=Entry(entries_frame2,textvariable=fromD,width=15,bd=0,relief=SOLID,font=('Calibari',12))
        txtFrom.place(x=250,y=10)

        txtTo=Entry(entries_frame2,textvariable=toD,width=15,bd=0,relief=SOLID,font=('Calibari',12))
        txtTo.place(x=250,y=50)

        
        btnBetween=Button(btn_frame1,
                    text='Show Prisoner',
                    width=15,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    command=prisonBetween

                    ).place(x=5,y=5)
        btndisplay=Button(btn_frame1,
                        text='Display All',
                        width=15,
                        height=1,
                        font=('Calibri',16),
                        fg='white',
                        bg='#001a33',
                        bd=0,
                        command=displayAll

                        ).place(x=5,y=50)
        
        btn_frame3=Frame(entries_frame3,bg='#1f2e2e',bd=1,relief=SOLID)
        btn_frame3.place(x=8,y=1,width=185,height=100)
        txtKill=Entry(entries_frame3,textvariable=txtKilll,width=18,bd=0,relief=SOLID,font=('Calibari',12))
        txtKill.place(x=21,y=60)

        
        
        btnKill=Button(btn_frame3,
                    text='Show PKill',
                    width=15,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    command=showPrisonKilling

                    ).place(x=5,y=5)
        #for printData
        btn_frame2=Frame(entries_frame3,bg='#1f2e2e',bd=1,relief=SOLID)
        btn_frame2.place(x=200,y=1,width=204,height=100)
        btnPrint=Button(btn_frame2,
                    text='Export Data',
                    width=17,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    command=printIt

                    ).place(x=4,y=5)
        btnDeleteDate=Button(btn_frame2,
                    text='Delete File',
                    width=17,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    command=deleteFilePrison

                    ).place(x=4,y=50)
        
        tree_frame=Frame(pr,bg='white')
        tree_frame.place(x=365,y=1,width=940,height=395)
        style=ttk.Style()
        style.configure("mystyle.Treeview",font=('Calibri',13),rowheight=50)
        style.configure("mystyle.Treeview.Heading",font=('Calibari',13))

        tv=ttk.Treeview(tree_frame,column=(1,2,3,4,5,6,7),style="mystyle.Treeview" )
        tv.heading("1",text="ID")
        tv.column("1",width="60")

        tv.heading("2",text="FirstName")
        tv.column("2",width="140")

        tv.heading("3",text="Father")
        tv.column("3",width="140")

        tv.heading("4",text="LastName")
        tv.column("4",width="140")

        tv.heading("5",text="Gender")
        tv.column("5",width="120")

        tv.heading("6",text="BarthYear")
        tv.column("6",width="140")

        tv.heading("7",text="Address")
        tv.column("7",width="200")

        tv['show']='headings'
        tv.bind("<ButtonRelease-1>",getData)
        tv.place(x=1,y=1,height=610,width=975)

        displayAll()


        pr.mainloop()

    btnPrisoners=Button(btn_frame,
                text='Prisoners',
                width=29,
                height=1,
                font=('Calibri',16),
                fg='white',
                bg='#001a33',
                bd=0,
                command=prisoners

                ).place(x=4,y=5)

    def OffencePage():
        db=DataBase("Persons.db")
        pm.destroy()
        #ساوينا القياس واحد 
        pr=Tk()
        pr.title('Offence')
        pr.geometry('1310x515+0+0')
        pr.resizable(False,False)
        pr.configure(bg='#1f2e2e')##1f2e2e


        namee=StringVar()
        
        #label frames قسم جزء منشان الازرار و الانبوت
        entries_frame=Frame(pr,bg='#1f2e2e')
        entries_frame.place(x=1,y=1,width=360,height=510)
        title=Label(entries_frame,text='Prison BR',font=('Calibri',20,'bold'),bg='#1f2e2e',fg='white')
        title.place(x=120,y=15)
        
        entries_frame2=Frame(pr,bg='#1f2e2e')
        entries_frame2.place(x=350,y=400,width=800,height=200)
        
        # def hide():
        #     pr.geometry("360x515+0+0")

        # def show():
        #     pr.geometry('1310x515+0+0')
        #هدول كانوا لاخفاء الجدول و اظهارو

        #هدول الزرار واحد بس شغال منشان التنقل بين الصفحات 


        # btnhidee=Button(entries_frame,text='Visit',bg='white',bd=1,relief=SOLID,cursor='hand2',command=pg.VisitPage)
        # btnhidee.place(x=160,y=10)

        # btnhidee=Button(entries_frame,text='Visiting',bg='white',bd=1,relief=SOLID,cursor='hand2',command=Visiting)
        # btnhidee.place(x=210,y=10)


        # btnhide=Button(entries_frame,text='Visiting',bg='white',bd=1,relief=SOLID,cursor='hand2',command=Visiting)
        # btnhide.place(x=260,y=10)
        
        # btnshow=Button(entries_frame,text='Visiting',bg='white',bd=1,relief=SOLID,cursor='hand2',command=Visiting)
        # btnshow.place(x=310,y=10)
        #نهاية الزرار

        def getData(event):
            selected_row=tv.focus()
            data=tv.item(selected_row)
            global row 
            row=data["values"]
            namee.set(row[1])
            
        def displayAll():
            tv.delete(*tv.get_children())
            for row in db.fetchO():
                tv.insert("",END,values=row)


        def delete():
            db.removeO(row[0])
            Clear()
            displayAll()

        def Clear():
            namee.set("")
            
        def add_Offence():
            if txtName.get()=="":
                messagebox.showerror("Error","Pleace Fill all the Entry")
                return 
            db.insertO(
                txtName.get()
                )
            messagebox.showinfo("Success","Added new Offence")
            Clear()
            displayAll()
        def Update():
            if txtName.get()=="" :
                messagebox.showerror("Error","Pleace Fill all the Entry")
                return 
            db.updateO(
                row[0],
                txtName.get()
                )
            messagebox.showinfo("Success","The Offence Data is Updated")
            Clear()
            displayAll()
        def printIt():
            db.printToExcelO()
            messagebox.showinfo("Success","The Offence Data is Saved")
        def deleteFileOffen():
                import os
                if os.path.exists("OffenceFile.xlsx"):
                    os.remove("OffenceFile.xlsx")
                    messagebox.showinfo("Success","The Data Deleted")
                else:
                    messagebox.showinfo("Success","The Data Does not exist")
        
        menubar = Menu(pr)  
        file = Menu(menubar, tearoff=0)  
        file.add_command(label="New")  
        file.add_command(label="Open")  
        file.add_command(label="Save")  
        file.add_command(label="Save as...")  
        file.add_command(label="Close")  
        
        file.add_separator()  
        
        file.add_command(label="Exit", command=pr.quit)  
        
        menubar.add_cascade(label="File", menu=file)  
        edit = Menu(menubar, tearoff=0)  
        edit.add_command(label="Undo")  
        
        edit.add_separator()  
        
        edit.add_command(label="Cut")  
        edit.add_command(label="Copy")  
        edit.add_command(label="Paste")  
        edit.add_command(label="Delete")  
        edit.add_command(label="Select All")  
        
        menubar.add_cascade(label="Edit", menu=edit)  
        menubar.add_cascade(label="Main", command=main)  
                
        pr.config(menu=menubar)  

        # btnhidee=Button(entries_frame,text='Export',bg='white',bd=1,relief=SOLID,cursor='hand2',command=printIt)
        # btnhidee.place(x=110,y=10)
        #عنوان الانبوات
        lblName=Label(entries_frame,text="Name Offence",font=('Calibri',16),bg='#1f2e2e',fg='white')##1f2e2e
        lblName.place(x=10,y=80)
        #الانبوت من نوع انتري يعني ادخال يدوي 😁
        txtName=Entry(entries_frame,textvariable=namee,width=20,font=('Calibari',16))
        txtName.place(x=120,y=80)

        #buttons frame الازرار و تزبيط قياساتها 
        btn_frame=Frame(entries_frame,bg='#1f2e2e',bd=1,relief=SOLID)
        btn_frame.place(x=10,y=400,width=335,height=100)

        btnAdd=Button(btn_frame,
                    text='Insert Offence',
                    width=14,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    command=add_Offence
                    ).place(x=4,y=5)

        btnEdit=Button(btn_frame,
                    text='Update Offence',
                    width=14,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    command=Update
                    ).place(x=4,y=50)
        btnDelete=Button(btn_frame,
                    text='Delete Offence',
                    width=14,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    command=delete
                    ).place(x=170,y=5)
        btnClear=Button(btn_frame,
                    text='Export Offence',
                    width=14,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    command=printIt
                    ).place(x=170,y=50)
        #button for prison between 
        btn_frame1=Frame(entries_frame2,bg='#1f2e2e',bd=1,relief=SOLID)
        btn_frame1.place(x=13,y=1,width=380,height=100)
        txtFrom=Entry(entries_frame2,width=15,bd=0,relief=SOLID,font=('Calibari',12))
        txtFrom.place(x=250,y=10)

        txtTo=Entry(entries_frame2,width=15,bd=0,relief=SOLID,font=('Calibari',12))
        txtTo.place(x=250,y=50)

        
        btnBetween=Button(btn_frame1,
                    text='Show Prisoner',
                    width=15,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    

                    ).place(x=5,y=5)
        btn_frame2=Frame(entries_frame2,bg='#1f2e2e',bd=1,relief=SOLID)
        btn_frame2.place(x=400,y=1,width=204,height=100)
        btnPrint=Button(btn_frame2,
                    text='Export Data',
                    width=17,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    command=printIt

                    ).place(x=4,y=5)
        btnDeleteDate=Button(btn_frame2,
                    text='Delete File',
                    width=17,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    command=deleteFileOffen

                    ).place(x=4,y=50)
        
        # Table Frame عرض الجدول 
        #for printData
        # Table Frame عرض الجدول 

        tree_frame=Frame(pr,bg='white')
        tree_frame.place(x=365,y=1,width=940,height=395)
        style=ttk.Style()
        style.configure("mystyle.Treeview",font=('Calibri',13),rowheight=50)
        style.configure("mystyle.Treeview.Heading",font=('Calibari',13))

        tv=ttk.Treeview(tree_frame,column=(1,2),style="mystyle.Treeview" )
        tv.heading("1",text="ID")
        tv.column("1",width="60")

        tv.heading("2",text="Name")
        tv.column("2",width="140")


        tv['show']='headings'
        tv.bind("<ButtonRelease-1>",getData)
        tv.place(x=1,y=1,height=610,width=975)

        displayAll()


        pr.mainloop()

    btnOffence=Button(btn_frame,
                text='Offence',
                width=29,
                height=1,
                font=('Calibri',16),
                fg='white',
                bg='#001a33',
                bd=0,
                command=OffencePage

                ).place(x=4,y=95)

    def ConvictsPage():
        db=DataBase("Persons.db")
        pm.destroy()
        #ساوينا القياس واحد 
        pr=Tk()
        pr.title('Convicts')
        pr.geometry('1310x515+0+0')
        pr.resizable(False,False)
        pr.configure(bg='#1f2e2e')##1f2e2e


        fromDate=StringVar()
        toDate=StringVar()
        PersonId=StringVar()
        OffensId=StringVar()
        


        #label frames قسم جزء منشان الازرار و الانبوت
        entries_frame=Frame(pr,bg='#1f2e2e')
        entries_frame.place(x=1,y=1,width=360,height=510)
        title=Label(entries_frame,text='Prison BR',font=('Calibri',20,'bold'),bg='#1f2e2e',fg='white')
        title.place(x=120,y=15)

        entries_frame2=Frame(pr,bg='#1f2e2e')
        entries_frame2.place(x=350,y=400,width=800,height=200)
        
        
        def getData(event):
            selected_row=tv.focus()
            data=tv.item(selected_row)
            global row 
            row=data["values"]
            fromDate.set(row[1])
            toDate.set(row[2])
            PersonId.set(row[3])
            OffensId.set(row[4])
            
        def displayAll():
            tv.delete(*tv.get_children())
            for row in db.fetchC():
                tv.insert("",END,values=row)


        def delete():
            db.removeC(row[0])
            Clear()
            displayAll()

        def Clear():
            fromDate.set("")
            toDate.set("")
            PersonId.set("")
            OffensId.set("")
            
        def add_Convicts():
            if txtFDate.get()=="" or txtTDate.get()=="" or txtPID.get()=="" or txtOID.get()=="" :
                messagebox.showerror("Error","Pleace Fill all the Entry")
                return 
            db.insertC(
                txtFDate.get(),
                txtTDate.get(),
                txtPID.get(),
                txtOID.get())               
            messagebox.showinfo("Success","Added new Convicts")
            Clear()
            displayAll()
        def Update():
            if txtFDate.get()=="" or txtTDate.get()=="" or txtPID.get()=="" or txtOID.get()=="" :
                messagebox.showerror("Error","Pleace Fill all the Entry")
                return 
            db.updateC(
                row[0],
                txtFDate.get(),
                txtTDate.get(),
                txtPID.get(),
                txtOID.get(),
                )
            messagebox.showinfo("Success","The Convict Data is Updated")
            Clear()
            displayAll()
        def printIt():
            db.printToExcelC()
            messagebox.showinfo("Success","The Convict Data is Saved")
        def deleteFileConv():
                import os
                if os.path.exists("ConvictsFile.xlsx"):
                    os.remove("ConvictsFile.xlsx")
                    messagebox.showinfo("Success","The Data Deleted")
                else:
                    messagebox.showinfo("Success","The Data Does not exist")
        
        menubar = Menu(pr)  
        file = Menu(menubar, tearoff=0)  
        file.add_command(label="New")  
        file.add_command(label="Open")  
        file.add_command(label="Save")  
        file.add_command(label="Save as...")  
        file.add_command(label="Close")  
        
        file.add_separator()  
        
        file.add_command(label="Exit", command=pr.quit)  
        
        menubar.add_cascade(label="File", menu=file)  
        edit = Menu(menubar, tearoff=0)  
        edit.add_command(label="Undo")  
        
        edit.add_separator()  
        
        edit.add_command(label="Cut")  
        edit.add_command(label="Copy")  
        edit.add_command(label="Paste")  
        edit.add_command(label="Delete")  
        edit.add_command(label="Select All")  
        
        menubar.add_cascade(label="Edit", menu=edit)  
        menubar.add_cascade(label="Main", command=main)  
          
        
        pr.config(menu=menubar)  

        #عنوان الانبوات
        lblFDate=Label(entries_frame,text="From Date",font=('Calibri',16),bg='#1f2e2e',fg='white')##1f2e2e
        lblFDate.place(x=10,y=80)
        #الانبوت من نوع انتري يعني ادخال يدوي 😁
        txtFDate=Entry(entries_frame,textvariable=fromDate,width=20,font=('Calibari',16))
        txtFDate.place(x=120,y=80)

        lblTDate=Label(entries_frame,text="To Date",font=('Calibri',16),bg='#1f2e2e',fg='white')
        lblTDate.place(x=10,y=130)
        txtTDate=Entry(entries_frame,textvariable=toDate,width=20,font=('Calibari',16))
        txtTDate.place(x=120,y=130)


        lblPID=Label(entries_frame,text="PersonId",font=('Calibri',16),bg='#1f2e2e',fg='white')
        lblPID.place(x=10,y=180)
        txtPID=Entry(entries_frame,textvariable=PersonId,width=20,font=('Calibari',16))
        txtPID.place(x=120,y=180)

        lblOID=Label(entries_frame,text="OffenceId",font=('Calibri',16),bg='#1f2e2e',fg='white')
        lblOID.place(x=10,y=230)
        
        txtOID=Entry(entries_frame,textvariable=OffensId,width=20,font=('Calibari',16))
        txtOID.place(x=120,y=230)

        
        #buttons frame الازرار و تزبيط قياساتها 
        btn_frame=Frame(entries_frame,bg='#1f2e2e',bd=1,relief=SOLID)
        btn_frame.place(x=10,y=400,width=335,height=100)

        btnAdd=Button(btn_frame,
                    text='Insert Convict',
                    width=14,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    command=add_Convicts

                    ).place(x=4,y=5)
        btnEdit=Button(btn_frame,
                    text='Update Convict',
                    width=14,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    command=Update
                    ).place(x=4,y=50)

        btnDelete=Button(btn_frame,
                    text='Delete Prisoner',
                    width=14,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    command=delete
                    ).place(x=170,y=5)
        btnClear=Button(btn_frame,
                    text='Export Prisoners',
                    width=14,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    command=printIt
                    ).place(x=170,y=50)
        
        # Table Frame عرض الجدول 
        
        btn_frame1=Frame(entries_frame2,bg='#1f2e2e',bd=1,relief=SOLID)
        btn_frame1.place(x=13,y=1,width=380,height=100)
        txtFrom=Entry(entries_frame2,width=15,bd=0,relief=SOLID,font=('Calibari',12))
        txtFrom.place(x=250,y=10)

        txtTo=Entry(entries_frame2,width=15,bd=0,relief=SOLID,font=('Calibari',12))
        txtTo.place(x=250,y=50)

        
        btnBetween=Button(btn_frame1,
                    text='Show Prisoner',
                    width=15,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    

                    ).place(x=5,y=5)
        
        # Table Frame عرض الجدول 
        #for printData
        btn_frame2=Frame(entries_frame2,bg='#1f2e2e',bd=1,relief=SOLID)
        btn_frame2.place(x=400,y=1,width=204,height=100)
        txtFrom=Entry(entries_frame2,width=15,bd=0,relief=SOLID,font=('Calibari',12))
        txtFrom.place(x=250,y=10)
        btnPrint=Button(btn_frame2,
                    text='Export Data',
                    width=17,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    command=printIt

                    ).place(x=4,y=5)
        btnDeleteDate=Button(btn_frame2,
                    text='Delete File',
                    width=17,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    command=deleteFileConv

                    ).place(x=4,y=50)
        
        tree_frame=Frame(pr,bg='white')
        tree_frame.place(x=365,y=1,width=940,height=395)
        style=ttk.Style()
        style.configure("mystyle.Treeview",font=('Calibri',13),rowheight=50)
        style.configure("mystyle.Treeview.Heading",font=('Calibari',13))

        tv=ttk.Treeview(tree_frame,column=(1,2,3,4,5),style="mystyle.Treeview" )
        tv.heading("1",text="ID")
        tv.column("1",width="60")

        tv.heading("2",text="FromDate")
        tv.column("2",width="140")

        tv.heading("3",text="ToDate")
        tv.column("3",width="140")

        tv.heading("4",text="PersonID")
        tv.column("4",width="140")

        tv.heading("5",text="OffenceID")
        tv.column("5",width="120")


        tv['show']='headings'
        tv.bind("<ButtonRelease-1>",getData)
        tv.place(x=1,y=1,height=610,width=975)

        displayAll()


        pr.mainloop()

    btnConvicts=Button(btn_frame,
                text='Convcts',
                width=29,
                height=1,
                font=('Calibri',16),
                fg='white',
                bg='#001a33',
                bd=0,
                command=ConvictsPage

                ).place(x=4,y=140)

    def DungeonPage():
        db=DataBase("Persons.db")
        pm.destroy()
        #ساوينا القياس واحد 
        pr=Tk()
        pr.title('Dungeon')
        pr.geometry('1310x515+0+0')
        pr.resizable(False,False)
        pr.configure(bg='#1f2e2e')##1f2e2e


        namee=StringVar()
        sizee=StringVar()
        
        #label frames قسم جزء منشان الازرار و الانبوت
        entries_frame=Frame(pr,bg='#1f2e2e')
        entries_frame.place(x=1,y=1,width=360,height=510)
        title=Label(entries_frame,text='Prison BR',font=('Calibri',20,'bold'),bg='#1f2e2e',fg='white')
        title.place(x=120,y=15)

        entries_frame2=Frame(pr,bg='#1f2e2e')
        entries_frame2.place(x=350,y=400,width=800,height=200)
        
        def getData(event):
            selected_row=tv.focus()
            data=tv.item(selected_row)
            global row 
            row=data["values"]
            namee.set(row[1])
            sizee.set(row[2])

        def displayAll():
            tv.delete(*tv.get_children())
            for row in db.fetchD():
                tv.insert("",END,values=row)


        def delete():
            db.removeD(row[0])
            Clear()
            displayAll()

        def Clear():
            namee.set("")
            sizee.set("")
            

        def add_Dungeon():
            if txtNamee.get()=="" or txtSize.get()=="":
                messagebox.showerror("Error","Pleace Fill all the Entry")
                return 
            db.insertD(
                txtNamee.get(),
                txtSize.get(),
                )
            messagebox.showinfo("Success","Added new Dungeon")
            Clear()
            displayAll()
        def Update():
            if txtNamee.get()=="" or txtSize.get()=="":
                messagebox.showerror("Error","Pleace Fill all the Entry")
                return 
            db.update(
                row[0],
                txtNamee.get(),
                txtSize.get(),
                )
            messagebox.showinfo("Success","The Dungeon Data is Updated")
            Clear()
            displayAll()
        def printIt():
            db.printToExcelD()
        def deleteFileDun():
                import os
                if os.path.exists("DungeonFile.xlsx"):
                    os.remove("DungeonFile.xlsx")
                    messagebox.showinfo("Success","The Data Deleted")
                else:
                    messagebox.showinfo("Success","The Data Does not exist")
        
        menubar = Menu(pr)  
        file = Menu(menubar, tearoff=0)  
        file.add_command(label="New")  
        file.add_command(label="Open")  
        file.add_command(label="Save")  
        file.add_command(label="Save as...")  
        file.add_command(label="Close")  
        
        file.add_separator()  
        
        file.add_command(label="Exit", command=pr.quit)  
        
        menubar.add_cascade(label="File", menu=file)  
        edit = Menu(menubar, tearoff=0)  
        edit.add_command(label="Undo")  
        
        edit.add_separator()  
        
        edit.add_command(label="Cut")  
        edit.add_command(label="Copy")  
        edit.add_command(label="Paste")  
        edit.add_command(label="Delete")  
        edit.add_command(label="Select All")  
        
        menubar.add_cascade(label="Edit", menu=edit)  
        menubar.add_cascade(label="Main", command=main)  
        
        pr.config(menu=menubar)  

        #عنوان الانبوات
        lblNamee=Label(entries_frame,text="Name",font=('Calibri',16),bg='#1f2e2e',fg='white')##1f2e2e
        lblNamee.place(x=10,y=80)
        #الانبوت من نوع انتري يعني ادخال يدوي 😁
        txtNamee=Entry(entries_frame,textvariable=namee,width=20,font=('Calibari',16))
        txtNamee.place(x=120,y=80)

        lblSize=Label(entries_frame,text="Size",font=('Calibri',16),bg='#1f2e2e',fg='white')
        lblSize.place(x=10,y=130)
        txtSize=Entry(entries_frame,textvariable=sizee,width=20,font=('Calibari',16))
        txtSize.place(x=120,y=130)


        #buttons frame الازرار و تزبيط قياساتها 
        btn_frame=Frame(entries_frame,bg='#1f2e2e',bd=1,relief=SOLID)
        btn_frame.place(x=10,y=400,width=335,height=100)

        btnAdd=Button(btn_frame,
                    text='Insert Dungeon',
                    width=14,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    command=add_Dungeon

                    ).place(x=4,y=5)
        btnEdit=Button(btn_frame,
                    text='Update Dungeon',
                    width=14,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    command=Update
                    ).place(x=4,y=50)

        btnDelete=Button(btn_frame,
                    text='Delete Dungeon',
                    width=14,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    command=delete
                    ).place(x=170,y=5)
        btnClear=Button(btn_frame,
                    text='Clear Prisoners',
                    width=14,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    command=Clear
                    ).place(x=170,y=50)
#button for prison between 
        btn_frame1=Frame(entries_frame2,bg='#1f2e2e',bd=1,relief=SOLID)
        btn_frame1.place(x=13,y=1,width=380,height=100)
        txtFrom=Entry(entries_frame2,width=10,bd=0,relief=SOLID,font=('Calibari',12))
        txtFrom.place(x=250,y=10)

        lblFrom=Label(entries_frame2,text="Name",font=('Calibri',12),bg='#1f2e2e',fg='white')
        lblFrom.place(x=200,y=10)
        

        
        btnBetween=Button(btn_frame1,
                    text='Show Prisoner',
                    width=15,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    

                    ).place(x=5,y=5)
        # Table Frame عرض الجدول 
        #for printData
        btn_frame2=Frame(entries_frame2,bg='#1f2e2e',bd=1,relief=SOLID)
        btn_frame2.place(x=400,y=1,width=204,height=100)
        txtFrom=Entry(entries_frame2,width=15,bd=0,relief=SOLID,font=('Calibari',12))
        txtFrom.place(x=250,y=10)
        btnPrint=Button(btn_frame2,
                    text='Export Data',
                    width=17,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    command=printIt

                    ).place(x=4,y=5)
        btnDeleteDate=Button(btn_frame2,
                    text='Delete File',
                    width=17,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    command=deleteFileDun

                    ).place(x=4,y=50)
        
        
        # Table Frame عرض الجدول 

        tree_frame=Frame(pr,bg='white')
        tree_frame.place(x=365,y=1,width=940,height=395)
        style=ttk.Style()
        style.configure("mystyle.Treeview",font=('Calibri',13),rowheight=50)
        style.configure("mystyle.Treeview.Heading",font=('Calibari',13))

        tv=ttk.Treeview(tree_frame,column=(1,2,3),style="mystyle.Treeview" )
        tv.heading("1",text="ID")
        tv.column("1",width="60")

        tv.heading("2",text="Name")
        tv.column("2",width="140")

        tv.heading("3",text="Size")
        tv.column("3",width="140")


        tv['show']='headings'
        tv.bind("<ButtonRelease-1>",getData)
        tv.place(x=1,y=1,height=610,width=975)

        displayAll()


        pr.mainloop()

    btnDungeon=Button(btn_frame,
                text='Dungeon',
                width=29,
                height=1,
                font=('Calibri',16),
                fg='white',
                bg='#001a33',
                bd=0,
                command=DungeonPage

                ).place(x=4,y=185)

    def DungeonMovesPage():
        db=DataBase("Persons.db")
        pm.destroy()
        #ساوينا القياس واحد 
        pr=Tk()
        pr.title('DungeonMoves')
        pr.geometry('1310x515+0+0')
        pr.resizable(False,False)
        pr.configure(bg='#1f2e2e')##1f2e2e


        DungeonId=StringVar()
        PersonId=StringVar()
        fromDate=StringVar()
        
        prisonNaem=StringVar()



        #label frames قسم جزء منشان الازرار و الانبوت
        entries_frame=Frame(pr,bg='#1f2e2e')
        entries_frame.place(x=1,y=1,width=360,height=510)
        title=Label(entries_frame,text='Prison BR',font=('Calibri',20,'bold'),bg='#1f2e2e',fg='white')
        title.place(x=120,y=15)

        entries_frame2=Frame(pr,bg='#1f2e2e')
        entries_frame2.place(x=350,y=400,width=800,height=200)
        

        def getData(event):
            selected_row=tv.focus()
            data=tv.item(selected_row)
            global row 
            row=data["values"]
            DungeonId.set(row[1])
            PersonId.set(row[2])
            fromDate.set(row[3])
            
        def displayAll():
            tv.delete(*tv.get_children())
            for row in db.fetchdm():
                tv.insert("",END,values=row)


        def delete():
            db.removedm(row[0])
            Clear()
            displayAll()

        def Clear():
            DungeonId.set("")
            PersonId.set("")
            fromDate.set("")
            
        def add_Prisoner():
            if txtDID.get()=="" or txtPID.get()=="" or txtFD.get()=="":
                messagebox.showerror("Error","Pleace Fill all the Entry")
                return 
            db.insertdm(
                txtDID.get(),
                txtPID.get(),
                txtFD.get(),
                )
            messagebox.showinfo("Success","Added new DungeonMoves")
            Clear()
            displayAll()
        def Update():
            if txtDID.get()=="" or txtPID.get()=="" or txtFD.get()=="" :
                messagebox.showerror("Error","Pleace Fill all the Entry")
                return 
            db.updatedm(
                row[0],
                txtDID.get(),
                txtPID.get(),
                txtFD.get(),
                )
            messagebox.showinfo("Success","The DungeonMoves Data is Updated")
            Clear()
            displayAll()
        def showPrisonMpving():
            tv.delete(*tv.get_children())
            for row in db.namePerMov(txtFrom.get()):
                tv.insert("",END,values=row)
        
        def printIt():
            db.printToExcel()
            messagebox.showinfo("Success","The DungeonMoves Data is Saved")

        def deleteFileDunMo():
                import os
                if os.path.exists("DungeonMovesFile.xlsx"):
                    os.remove("DungeonMovesFile.xlsx")
                    messagebox.showinfo("Success","The Data Deleted")
                else:
                    messagebox.showinfo("Success","The Data Does not exist")
        
        menubar = Menu(pr)  
        file = Menu(menubar, tearoff=0)  
        file.add_command(label="New")  
        file.add_command(label="Open")  
        file.add_command(label="Save")  
        file.add_command(label="Save as...")  
        file.add_command(label="Close")  
        
        file.add_separator()  
        
        file.add_command(label="Exit", command=pr.quit)  
        
        menubar.add_cascade(label="File", menu=file)  
        edit = Menu(menubar, tearoff=0)  
        edit.add_command(label="Undo")  
        
        edit.add_separator()  
        
        edit.add_command(label="Cut")  
        edit.add_command(label="Copy")  
        edit.add_command(label="Paste")  
        edit.add_command(label="Delete")  
        edit.add_command(label="Select All")  
        
        menubar.add_cascade(label="Edit", menu=edit)  
        menubar.add_cascade(label="Main", command=main)  
        
        pr.config(menu=menubar)  

        #عنوان الانبوات
        lblDID=Label(entries_frame,text="DungeonID",font=('Calibri',16),bg='#1f2e2e',fg='white')##1f2e2e
        lblDID.place(x=10,y=80)
        #الانبوت من نوع انتري يعني ادخال يدوي 😁
        txtDID=Entry(entries_frame,textvariable=DungeonId,width=20,font=('Calibari',16))
        txtDID.place(x=120,y=80)

        lblPID=Label(entries_frame,text="PersonID",font=('Calibri',16),bg='#1f2e2e',fg='white')
        lblPID.place(x=10,y=130)
        txtPID=Entry(entries_frame,textvariable=PersonId,width=20,font=('Calibari',16))
        txtPID.place(x=120,y=130)


        lblFD=Label(entries_frame,text="FromDate",font=('Calibri',16),bg='#1f2e2e',fg='white')
        lblFD.place(x=10,y=180)
        txtFD=Entry(entries_frame,textvariable=fromDate,width=20,font=('Calibari',16))
        txtFD.place(x=120,y=180)

        #buttons frame الازرار و تزبيط قياساتها 
        btn_frame=Frame(entries_frame,bg='#1f2e2e',bd=1,relief=SOLID)
        btn_frame.place(x=10,y=400,width=335,height=100)

        btnAdd=Button(btn_frame,
                    text='Insert Prisoner',
                    width=14,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    command=add_Prisoner

                    ).place(x=4,y=5)
        btnEdit=Button(btn_frame,
                    text='Update Prisoner',
                    width=14,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    command=Update
                    ).place(x=4,y=50)

        btnDelete=Button(btn_frame,
                    text='Delete DID',
                    width=14,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    command=delete
                    ).place(x=170,y=5)
        btnClear=Button(btn_frame,
                    text='Export DID',
                    width=14,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    command=printIt
                    ).place(x=170,y=50)
#button for prison between 
        btn_frame1=Frame(entries_frame2,bg='#1f2e2e',bd=1,relief=SOLID)
        btn_frame1.place(x=13,y=1,width=380,height=100)
        txtFrom=Entry(entries_frame2,textvariable=prisonNaem,width=15,bd=0,relief=SOLID,font=('Calibari',12))
        txtFrom.place(x=250,y=10)

        
        
        btnPmov=Button(btn_frame1,
                    text='Prisoner Moves',
                    width=15,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    command=showPrisonMpving

                    ).place(x=5,y=5)
        # Table Frame عرض الجدول 
        #for printData
        btn_frame2=Frame(entries_frame2,bg='#1f2e2e',bd=1,relief=SOLID)
        btn_frame2.place(x=400,y=1,width=204,height=100)
        txtFrom=Entry(entries_frame2,width=15,bd=0,relief=SOLID,font=('Calibari',12))
        txtFrom.place(x=250,y=10)
        btnPrint=Button(btn_frame2,
                    text='Export Data',
                    width=17,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    command=printIt

                    ).place(x=4,y=5)
        btnDeleteDate=Button(btn_frame2,
                    text='Delete File',
                    width=17,
                    height=1,
                    font=('Calibri',16),
                    fg='white',
                    bg='#001a33',
                    bd=0,
                    command=deleteFileDunMo

                    ).place(x=4,y=50)
        
        # Table Frame عرض الجدول 

        tree_frame=Frame(pr,bg='white')
        tree_frame.place(x=365,y=1,width=940,height=395)
        style=ttk.Style()
        style.configure("mystyle.Treeview",font=('Calibri',13),rowheight=50)
        style.configure("mystyle.Treeview.Heading",font=('Calibari',13))

        tv=ttk.Treeview(tree_frame,column=(1,2,3,4),style="mystyle.Treeview" )
        tv.heading("1",text="ID")
        tv.column("1",width="60")

        tv.heading("2",text="DungeonID")
        tv.column("2",width="140")

        tv.heading("3",text="PersonID")
        tv.column("3",width="140")

        tv.heading("4",text="fromDate")
        tv.column("4",width="140")

        tv['show']='headings'
        tv.bind("<ButtonRelease-1>",getData)
        tv.place(x=1,y=1,height=610,width=975)

        displayAll()


        pr.mainloop()

    btnDungeonMoves=Button(btn_frame,
                text='DungeonMoves',
                width=29,
                height=1,
                font=('Calibri',16),
                fg='white',
                bg='#001a33',
                bd=0,
                command=DungeonMovesPage

                ).place(x=4,y=230)

    def VisitPage():

            pm.destroy()
            db=DataBase("Persons.db")
            
            pr=Tk()
            
            pr.title("Visitings")
            pr.geometry('1310x515+0+0')
            pr.resizable(False,False)
            pr.configure(bg='#1f2e2e')#1f2e2e

            DateVisited=StringVar()
            PersonId=StringVar()
            VisitorName=StringVar()
            MountOfMinutes=StringVar()
            
            fromDate=StringVar()
            toDate=StringVar()


            entries_frame=Frame(pr,bg='#1f2e2e')
            entries_frame.place(x=1,y=1,width=360,height=510)
            title=Label(entries_frame,text='Prison BR',font=('Calibri',20,'bold'),bg='#1f2e2e',fg='white')
            title.place(x=120,y=15)

            entries_frame2=Frame(pr,bg='#1f2e2e')
            entries_frame2.place(x=350,y=400,width=800,height=200)

            
        
            # start menubar
            menubar = Menu(pr)  
            file = Menu(menubar, tearoff=0)  
            file.add_command(label="New")  
            file.add_command(label="Open")  
            file.add_command(label="Save")  
            file.add_command(label="Export")
            file.add_command(label="Save as...")  
            file.add_command(label="Close")
            
            
            
            file.add_separator()  
            
            file.add_command(label="Exit", command=pr.quit)  
            
            menubar.add_cascade(label="File", menu=file)  
            edit = Menu(menubar, tearoff=0)  
            edit.add_command(label="Undo")  
            
            edit.add_separator()  
            
            edit.add_command(label="Cut")  
            edit.add_command(label="Copy")  
            edit.add_command(label="Paste")  
            edit.add_command(label="Delete")  
            edit.add_command(label="Select All")  
            
            menubar.add_cascade(label="Edit", menu=edit)  
            menubar.add_cascade(label="Main", command=main)  
        
            pr.config(menu=menubar)  

            # end menubar
            

            def getData(event):
                selected_row=tv.focus()
                data=tv.item(selected_row)
                global row 
                row=data["values"]
                DateVisited.set(row[1])
                PersonId.set(row[2])
                VisitorName.set(row[3])
                MountOfMinutes.set(row[4])
                

            def displayAll():
                tv.delete(*tv.get_children())
                for row in db.fetchV():
                    tv.insert("",END,values=row)


            def delete():
                db.removeV(row[0])
                Clear()
                displayAll()

            def Clear():
                DateVisited.set("")
                PersonId.set("")
                VisitorName.set("")
                MountOfMinutes.set("")

            def add_Visitor():
                if txtDV.get()=="" or txtPI.get()=="" or txtLVN.get()=="":
                    messagebox.showerror("Error","Pleace Fill all the Entry")
                    return 
                db.insertV(
                    txtDV.get(),
                    txtPI.get(),
                    txtLVN.get(),
                    txtM.get())
                messagebox.showinfo("Success","Added new Visitor")
                Clear()
                displayAll()
            def Update():
                if txtDV.get()=="" or txtPI.get()=="" or txtLVN.get()=="":
                    messagebox.showerror("Error","Pleace Fill all the Entry")
                    return 
                db.updateV(
                    row[0],
                    txtDV.get(),
                    txtPI.get(),
                    txtLVN.get(),
                    txtM.get())
                messagebox.showinfo("Success","The Visitor Data is Updated")
                Clear()
                displayAll()
            def showVisitorsBetween():
                tv.delete(*tv.get_children())
                for row in db.VisitingBetween(txtFrom.get(),txtTo.get()):
                    tv.insert("",END,values=row)
            
            def printIt():
                db.printToExcelV()
                messagebox.showinfo("Success","The Visitor Data is Saved")
            def deleteFileVisit():
                import os
                if os.path.exists("VisitingsFile.xlsx"):
                    os.remove("VisitingsFile.xlsx")
                    messagebox.showinfo("Success","The Data Deleted")
                else:
                    messagebox.showinfo("Success","The Data Does not exist")
            #عنوان الانبوات
            lblDV=Label(entries_frame,text="DateVisited",font=('Calibri',12),bg='#1f2e2e',fg='white')
            lblDV.place(x=10,y=80)
            #الانبوت من نوع انتري يعني ادخال يدوي 😁
            txtDV=Entry(entries_frame,textvariable=DateVisited,width=18,font=('Calibari',16))
            txtDV.place(x=120,y=80)

            lblPI=Label(entries_frame,text="PersonId",font=('Calibri',12),bg='#1f2e2e',fg='white')
            lblPI.place(x=10,y=130)
            txtPI=Entry(entries_frame,textvariable=PersonId,width=18,font=('Calibari',16))
            txtPI.place(x=120,y=130)


            lblLVN=Label(entries_frame,text="VisitorName",font=('Calibri',12),bg='#1f2e2e',fg='white')
            lblLVN.place(x=10,y=180)
            txtLVN=Entry(entries_frame,textvariable=VisitorName,width=18,font=('Calibari',16))
            txtLVN.place(x=120,y=180)

            lblM=Label(entries_frame,text="Minutes",font=('Calibri',12),bg='#1f2e2e',fg='white')
            lblM.place(x=10,y=230)
            txtM=Entry(entries_frame,textvariable=MountOfMinutes,width=18,font=('Calibari',16))
            txtM.place(x=120,y=230)

            #buttons frame الازرار و تزبيط قياساتها 
            btn_frame=Frame(entries_frame,bg='#1f2e2e',bd=1,relief=SOLID)
            btn_frame.place(x=10,y=400,width=335,height=100)

            btnAddV=Button(btn_frame,
                        text='Insert Visitor',
                        width=14,
                        height=1,
                        font=('Calibri',16),
                        fg='white',
                        bg='#001a33',
                        bd=0,
                        command=add_Visitor

                        ).place(x=4,y=5)
            btnEditV=Button(btn_frame,
                        text='Update Visitor',
                        width=14,
                        height=1,
                        font=('Calibri',16),
                        fg='white',
                        bg='#001a33',#001a33
                        bd=0,
                        command=Update
                        ).place(x=4,y=50)

            btnDeleteV=Button(btn_frame,
                        text='Delete Visitor',
                        width=14,
                        height=1,
                        font=('Calibri',16),
                        fg='white',
                        bg='#001a33',
                        bd=0,
                        command=delete
                        ).place(x=170,y=5)
            btnClearV=Button(btn_frame,
                        text='Print Visitor',
                        width=14,
                        height=1,
                        font=('Calibri',16),
                        fg='white',
                        bg='#001a33',
                        bd=0,
                        command=printIt
                        ).place(x=170,y=50)
            #button for Vistor between 
            btn_frame1=Frame(entries_frame2,bg='#1f2e2e',bd=1,relief=SOLID)
            btn_frame1.place(x=13,y=1,width=380,height=100)
            lblf=Label(entries_frame2,text="from Date",font=('Calibri',12),bg='#1f2e2e',fg='white')
            lblf.place(x=280,y=8)
            
            txtFrom=Entry(entries_frame2,width=15,bd=0,textvariable=fromDate,relief=SOLID,font=('Calibari',12))
            txtFrom.place(x=250,y=30)
            lblt=Label(entries_frame2,text="to Date",font=('Calibri',12),bg='#1f2e2e',fg='white')
            lblt.place(x=290,y=50)
            
            txtTo=Entry(entries_frame2,width=15,bd=0,textvariable=toDate,relief=SOLID,font=('Calibari',12))
            txtTo.place(x=250,y=75)

            
            btnBetweeen=Button(btn_frame1,
                        text='Show Visitors By',
                        width=15,
                        height=1,
                        font=('Calibri',16),
                        fg='white',
                        bg='#001a33',
                        bd=0,
                        command=showVisitorsBetween

                        ).place(x=5,y=5)
            btndisplay=Button(btn_frame1,
                        text='Display All',
                        width=15,
                        height=1,
                        font=('Calibri',16),
                        fg='white',
                        bg='#001a33',
                        bd=0,
                        command=displayAll

                        ).place(x=5,y=50)
            # Table Frame عرض الجدول 
            #for printData
            btn_frame2=Frame(entries_frame2,bg='#1f2e2e',bd=1,relief=SOLID)
            btn_frame2.place(x=400,y=1,width=204,height=100)
            btnPrint=Button(btn_frame2,
                        text='Export Data',
                        width=17,
                        height=1,
                        font=('Calibri',16),
                        fg='white',
                        bg='#001a33',
                        bd=0,
                        command=printIt

                        ).place(x=4,y=5)
            btnDeleteDate=Button(btn_frame2,
                        text='Delete File',
                        width=17,
                        height=1,
                        font=('Calibri',16),
                        fg='white',
                        bg='#001a33',
                        bd=0,
                        command=deleteFileVisit

                        ).place(x=4,y=50)
            
            # Table Frame عرض الجدول 

            tree_frame=Frame(pr,bg='white')
            tree_frame.place(x=365,y=1,width=940,height=395)
            style=ttk.Style()
            style.configure("mystyle.Treeview",font=('Calibri',13),rowheight=50)
            style.configure("mystyle.Treeview.Heading",font=('Calibari',13))

            tv=ttk.Treeview(tree_frame,column=(1,2,3,4,5),style="mystyle.Treeview" )
            tv.heading("1",text="ID")
            tv.column("1",width="60")

            tv.heading("2",text="DateVisited")
            tv.column("2",width="140")

            tv.heading("3",text="PersonId")
            tv.column("3",width="140")

            tv.heading("4",text="VisitorName")
            tv.column("4",width="140")

            tv.heading("5",text="MountOfMinuts")
            tv.column("5",width="140")
            tv['show']='headings'
            tv.bind("<ButtonRelease-1>",getData)
            tv.place(x=1,y=1,height=610,width=975)

            displayAll()


            pr.mainloop()

    btnVisitings=Button(btn_frame,
                text='Visitings',
                width=29,
                height=1,
                font=('Calibri',16),
                fg='white',
                bg='#001a33',
                bd=0,
                command=VisitPage
                
                ).place(x=4,y=50)

    pm.mainloop()
m=main()