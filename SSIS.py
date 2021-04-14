"""
CSC151N ASSIGNMENT: SIMPLE STUDENT INFORMATION SYSTEM
         MAICA A. APIAG    BS-STATISTICS 
                 APRIL 14, 2021
"""

from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import csv


#Main Window
root = Tk()
root.title('Student Information System')

frame = LabelFrame(root, bg ="#eaebeb", font=('Palatino Linotype',20,'bold'),text="Student Information System", fg="#104c70",padx=100, pady=80)
frame.pack(padx=20, pady=20)

#Clicking the add button
def add():
    top=Toplevel()
    top.title('ADD STUDENTS')
    
    StdID = StringVar()
    Name = StringVar()
    Gender = StringVar()
    Course = StringVar()
    YearLevel = StringVar()
    
    MainFrame = Frame(top, bg="#eaebeb")
    MainFrame.grid()
    
    DataFrame = Frame(MainFrame,bd=1, width=1300, height=400, padx=20, pady=20, bg ="#eaebeb")
    DataFrame.pack(side=BOTTOM)
    
    StudInf=LabelFrame(DataFrame, width=1000, height=600, padx=20, bg="#eaebeb", font=('Palatino Linotype',20,'bold'),text="Student's Information", fg="#104c70")
    StudInf.pack(side=LEFT)
    
    SILabel = Label(StudInf, font=('Palatino Linotype',13, 'bold'),text="Student ID  ", padx=2, pady=2, bg ="#eaebeb", fg="#104c70")
    SILabel.grid(row=0, column=0, sticky=W)
    ID = Entry(StudInf, font=('Palatino Linotype',13),textvariable=StdID, width=39)
    ID.grid(row=0, column=1, pady=8)
    
    FLabel = Label(StudInf, font=('Palatino Linotype',13, 'bold'),text="Name", padx=2, pady=2, bg="#eaebeb", fg="#104c70")
    FLabel.grid(row=1, column=0, sticky=W)
    name = Entry(StudInf, font=('Palatino Linotype',13),textvariable=Name, width=39)
    name.grid(row=1, column=1, pady=8)
    
    CLabel = Label(StudInf, font=('Palatino Linotype',13, 'bold'),text="Course ", padx=2, pady=2, bg="#eaebeb", fg="#104c70")
    CLabel.grid(row=2, column=0, sticky=W)
    course = Entry(StudInf, font=('Palatino Linotype',13),textvariable=Course, width=39)
    course.grid(row=2, column=1, pady=8)
    
    YLabel = Label(StudInf, font=('Palatino Linotype',13, 'bold'),text="Year Level ", padx=2, pady=2, bg="#eaebeb", fg="#104c70")
    YLabel.grid(row=3, column=0, sticky=W)
    ylevel = ttk.Combobox(StudInf, font=('Palatino Linotype',13),state='readonly', width=37)
    ylevel['values']=('','1st Year','2nd Year','3rd Year','4th Year')
    ylevel.current(0)
    ylevel.grid(row=3, column=1, pady=8)

    GLabel = Label(StudInf, font=('Palatino Linotype',13, 'bold'),text="Gender ", padx=2, pady=2, bg="#eaebeb", fg="#104c70")
    GLabel.grid(row=4, column=0, sticky=W)
    gender = ttk.Combobox(StudInf, font=('Palatino Linotype',13),state='readonly', width=37)
    gender['values']=('','Female','Male')
    gender.current(0)
    gender.grid(row=4, column=1, pady=8)
    
    #ADD NEW STUDENT
    def addData():
        with open('ssis.csv', "a", newline="") as file:
            csvfile = csv.writer(file)
            if  ID.get() == "" or name.get() == "" or gender.get() == "" or course.get() == "" or ylevel.get()== "":
                tkinter.messagebox.showinfo("Student Information System","Please Fill In the Box")
            else:
                csvfile.writerow([ID.get(),name.get(),course.get(),ylevel.get(), gender.get()])
                tkinter.messagebox.showinfo("Student Information System","Student Recorded Successfully")
                top.destroy()
    
    submit=Button(StudInf, text="SUBMIT",command=addData, font=('Palatino Linotype', 15,'bold'), bg="#104c70", fg="white")
    submit.grid(row=5, column=0, columnspan=3,pady=8)
 
#from the Main Window -- VIEW
def view():
    this=Toplevel(bg="white")
    this.geometry("940x510")
    this.title('VIEW STUDENTS')
    
    mainFrame = LabelFrame(this, bg="#eaebeb")
    mainFrame.pack(padx=20, pady=20)
    
    Label(mainFrame, text="List of Students", font = ('Palatino Linotype', 30, 'bold'),fg="#104c70",bg="#eaebeb", width=35).grid(row=0,column=0, columnspan=5, pady=10)

    def viewList():
        for i in tree.get_children():
            tree.delete(i)
        with open("ssis.csv","r") as file:
            listStudents = csv.reader(file)
            counter = 0
            for student in listStudents:
                tree.insert(parent='',  index='end', iid=counter,
                            values=(student[0],student[1],student[2],student[3],student[4]))
                counter += 1
    #SEARCH
    def search():
        for i in tree.get_children():
            tree.delete(i)
        with open("ssis.csv","r") as file:
            listStudents = csv.reader(file)
            search = searchbar.get()
            counter = 0
            for student in listStudents:
                if student[0].startswith(search):
                    tree.insert(parent='',  index='end', iid=counter,
                                values=(student[0],student[1],student[2],student[3],student[4]))
                counter += 1
                
    #DELETE
    def delete():
        selected = tree.focus()
        stud_id = tree.item(selected, "values")[0]

        with open("ssis.csv", newline="") as file:
            reader = csv.reader(file)
            data = list(reader)
        x = [stud_id in student for student in data]
        index = [i for i, y in enumerate(x) if y]
        if sum(x) > 1:
            pass
        elif sum(x) == 1:
            index = index[0]

        del data[index]

        with open("ssis.csv", "w", newline="") as file:
            writer = csv.writer(file)
            for student in data:
                writer.writerow(student)

        viewList()
                
    #UPDATE STUDENT
    def update(index):
        def thisUpdate(studentList):
            with open('ssis.csv','w',newline='') as file:
                newList = csv.writer(file)
                for i in range(len(studentList)):
                    print(studentList[i])
                    if i == index:
                        newList.writerow([ID.get(),name.get(),course.get(),ylevel.get(), gender.get()])
                        continue
                    newList.writerow(studentList[i])
            top.destroy()
            viewList()
        
        #POP-UP WINDOW FOR UPDATING STUDENT
        top=Toplevel()
        top.title('UPDATE STUDENT')
        studentList= []
        studentInfo = []
        with open('ssis.csv','r') as file:
                students = csv.reader(file)
                x=0
                for student in students:
                        if x == index:
                            studentInfo = student
                        studentList.append(student)
                        x+=1
        StdID = StringVar()
        Name = StringVar()
        Gender = StringVar()
        Course = StringVar()
        YearLevel = StringVar()
            
        MainFrame2 = Frame(top, bg="#eaebeb")
        MainFrame2.grid()
            
        DataFrame2 = Frame(MainFrame2,bd=1, width=1300, height=400, padx=20, pady=20, bg ="#eaebeb")
        DataFrame2.pack(side=BOTTOM)
            
        DataAdd2=LabelFrame(DataFrame2, width=1000, height=600, padx=20, bg="#eaebeb", font=('Palatino Linotype',20,'bold'),text="Student's Information", fg="#104c70")
        DataAdd2.pack(side=LEFT)
            
        SILable = Label(DataAdd2, font=('Palatino Linotype',13, 'bold'),text="Student ID  ", padx=2, pady=2, bg ="#eaebeb", fg="#104c70")
        SILable.grid(row=0, column=0, sticky=W)
        ID = Entry(DataAdd2, font=('Palatino Linotype',13),textvariable=StdID, width=39)
        ID.grid(row=0, column=1, pady=8)
            
        FLable = Label(DataAdd2, font=('Palatino Linotype',13, 'bold'),text="Name  ", padx=2, pady=2, bg="#eaebeb", fg="#104c70")
        FLable.grid(row=1, column=0, sticky=W)
        name = Entry(DataAdd2, font=('Palatino Linotype',13),textvariable=Name, width=39)
        name.grid(row=1, column=1, pady=8)
            
        CLable = Label(DataAdd2, font=('Palatino Linotype',13, 'bold'),text="Course ", padx=2, pady=2, bg="#eaebeb", fg="#104c70")
        CLable.grid(row=2, column=0, sticky=W)
        course = Entry(DataAdd2, font=('Palatino Linotype',13),textvariable=Course, width=39)
        course.grid(row=2, column=1, pady=8)
            
        YLable = Label(DataAdd2, font=('Palatino Linotype',13, 'bold'),text="Year Level ", padx=2, pady=2, bg="#eaebeb", fg="#104c70")
        YLable.grid(row=3, column=0, sticky=W)
        ylevel = ttk.Combobox(DataAdd2, font=('Palatino Linotype',13),state='readonly', width=37)
        ylevel['values']=('','1st Year','2nd Year','3rd Year','4th Year')
        ylevel.current(0)
        ylevel.grid(row=3, column=1, pady=8) 

        GLable = Label(DataAdd2, font=('Palatino Linotype',13, 'bold'),text="Gender ", padx=2, pady=2, bg="#eaebeb", fg="#104c70")
        GLable.grid(row=4, column=0, sticky=W)
        gender = ttk.Combobox(DataAdd2, font=('Palatino Linotype',13),state='readonly', width=37)
        gender['values']=('','Female','Male')
        gender.current(0)
        gender.grid(row=4, column=1, pady=8)

        submit=Button(DataAdd2, text="UPDATE", command=lambda:thisUpdate(studentList), font=('Palatino Linotype', 15,'bold'), bg="#104c70", fg="white")
        submit.grid(row=5, column=0, columnspan=3,pady=8)
       
        ID.insert(0, studentInfo[0])
        name.insert(0, studentInfo[1])
        course.insert(0, studentInfo[2])
        if studentInfo[3] == "1st Year":
            ylevel.current(1)
        elif studentInfo[3] == "2nd Year":
            ylevel.current(2)
        elif studentInfo[3] == "3rd Year":
            ylevel.current(3)
        elif studentInfo[3] == "4th Year":
            ylevel.current(4)
        if studentInfo[4] == "Female":
            gender.current(1)
        elif studentInfo[4] == "Male":
            gender.current(2)
    
    #BUTTONS IN VIEW WINDOW    
    searchbar = Entry(mainFrame,font=('Palatino Linotype',12), width=40)
    searchbar.grid(row=1, column=0, padx=10, pady=5)
    searchbutton = Button(mainFrame, text="SEARCH",bg="#104c70", fg="white", font=('Palatino Linotype',9,'bold'), width=15, command=search)
    searchbutton.grid(row=1, column=1, padx=5, pady=5)
    
    viewButton = Button(mainFrame, text="VIEW ALL", bg="#104c70", fg="white", font=('Palatino Linotype',9,'bold'),width=15, command=viewList)
    viewButton.grid(row=1, column=2, padx=5, pady=5)
    
    edit = Button(mainFrame, text="EDIT",bg="#104c70", fg="white", font=('Palatino Linotype',9,'bold'), width=15, state=DISABLED, command=lambda:update(int(tree.focus())))
    edit.grid(row=1, column=3, padx=5, pady=5)
    
    delete = Button(mainFrame, text="DELETE",bg="#104c70", fg="white", font=('Palatino Linotype',9,'bold'), state=DISABLED, width=15, command=delete)
    delete.grid(row=1, column=4, padx=5, pady=5)
    
    #TREE VIEW
    tree = ttk.Treeview(mainFrame, height=15)
    tree.grid(row=2, column=0, columnspan=5, padx=10, pady=10)
    
    s = ttk.Style(root)
    s.configure("Treeview.Heading", font=('Palatino Linotype',11,'bold'))
    s.configure(".", font=('Palatino Linotype',12))
        
    tree['columns'] = ("ID number", "Name","Course","Year Level","Gender")

    tree.column('#0',width=0, stretch=NO)
    tree.column("ID number", anchor=CENTER, width=125)
    tree.column("Name", anchor=W, width=300)
    tree.column("Course", anchor=W, width=250)
    tree.column("Year Level", anchor=W, width=100)
    tree.column("Gender", anchor=W, width=100)

    tree.heading("ID number", text="ID number", anchor=CENTER)
    tree.heading("Name", text="Name", anchor=CENTER)
    tree.heading("Course", text="Course", anchor=CENTER)
    tree.heading("Year Level", text="Year Level", anchor=CENTER)
    tree.heading("Gender", text="Gender", anchor=CENTER)
    
    def clicked(*args):
        edit['state'] = NORMAL
        delete['state'] = NORMAL
        
    tree.bind("<Button-1>", clicked)
    viewList()

#BUTTONS IN THE MAIN WINDOW    
add = Button(frame, text="ADD STUDENTS",command=add, bg="#104c70", fg="white", font=('Palatino Linotype',15), padx=35)
add.pack(padx=30, pady=5)

view = Button(frame, text="VIEW STUDENTS",command=view,bg="#104c70", fg="white",font=('Palatino Linotype',15), padx=32)
view.pack(padx=30, pady=5)

close = Button(frame, text="CLOSE APP",command=root.destroy, bg="#104c70", fg="white",font=('Palatino Linotype',15), padx=60)
close.pack(padx=30, pady=5)

root.mainloop()
