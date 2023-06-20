from tkinter import *
import tkinter as tk

import sqlite3 
con = sqlite3.connect("assignment3FINAL.db")
cur = con.cursor()
cur.execute("INSERT INTO STUDENT VALUES(101,'Kaleb','Pelletier','COMP_ENG','pelletierk3',2024);")
cur.execute("INSERT INTO STUDENT VALUES(102,'Matt','Auger','COMP_ENG','augerm',2024);")
cur.execute("DELETE FROM INSTRUCTOR WHERE LAST_NAME='Fourier';")
cur.execute("UPDATE ADMIN\n"+
            "SET TITLE='Vice-President'\n"+
           "WHERE ID=3002\n")
            
            
            
            
           

class User(object):
    def __init__(self,f_name,l_name,ID):
        self.first = f_name
        self.last = l_name
        self.id = ID

    def setFirstName(self,first_name):
        self.first = first_name
    def setLastName(self,last_name):
        self.last = last_name
    def setID(self,ID):
        self.id = ID
    def printInfo(self):
        print("First Name: ",self.first)
        print("Last Name: ",self.last)
        print("ID: ",self.id)


class Admin(User):
    def __init__(self, f_name, l_name, ID):
        User.__init__(self,f_name,l_name,ID)

    def addCourse(self,course):
        print(course+" added")
    def removeCourse(self,course):
        print(course+" removed")
    def addUser(self,user):
        print(user+" added to system")
    def removeUser(self,user):
        print(user+" removed from system")
    def addStudent(self, user):
        print(user + " added to system")
    def removeStudent(self, user):
        print(user+" removed from system")
    def createRoster(self, roster):
        print("Creating roster named " + roster)
    def searchRoster(self, roster):
        print("Searching "+roster)
    def printRoster(self,roster):
        print("Printing roster"+ roster)
    def searchCourse(self,course):
        print("Searching " + course)
    def printCourse(self,course):
        print("Printing course" + course)

class Student(User):
    def __init__(self, f_name, l_name, ID):
        User.__init__(self,f_name, l_name, ID)

    def searchCourse(self,course):
        print("Searching " + course)
    def addCourse(self,course):
        print(course+" added")
    def dropCourse(self,course):
        print(course+" dropped")
    def printSchedule(self):
        print("Printing Schedule")

class Instructor(User):
    def __init__(self, f_name, l_name, ID):
        User.__init__(self,f_name, l_name, ID)

    def searchCourse(self,course):
        print("Searching " + course)
    def printSchedule(self):
        print("Printing Schedule")
    def printClassList(self):
        print("Printing Class list")

window = Tk()

#mainWindow = Toplevel()
#mainWindow.withdraw() #Hides window

input1= tk.Entry(window)
input2 = tk.Entry(window)

def createNew():
    mainWindow = Toplevel()
    mainWindow.geometry("500x500")
    tk.Label(mainWindow, text="Create New User").grid(row=0)
    tk.Label(mainWindow, text="First Name").grid(row=1)
    tk.Label(mainWindow, text="Last Name").grid(row=2)
    tk.Label(mainWindow,text= "Major").grid(row = 3)


def getLoginInfo():
    mainWindow = Toplevel()
    mainWindow.geometry("800x800")

    #loop through the data tables to check if they exist 
    userN = input1.get()
    if(userN == "1"):
        mainWindow.title("Student")
    if(userN == "2"):
        mainWindow.title("Admin")
    if(userN == "3"):
        mainWindow.title("Teacher")
    userN = ""
    mainWindow.deiconify() #Shows window
    #mainWindow.mainloop()
    


    #tk.Label(window, text=userN).grid(row=4)
    


def main():
    window.title("Lepord Web")
    window.geometry("500x500")

    tk.Label(window, text="Lepord Web").grid(row=0)
    tk.Label(window, text="Username").grid(row=1)
    tk.Label(window, text="Password").grid(row=2)

    Loginbtn = Button(window,text="Log In",command = getLoginInfo)
    createNewUser = Button(window,text ="Create New",command = createNew)

    

    # username = input1.get()
    # password = input2.get()
    # if(username != "" ):
    #     mainWindow = Tk()

    input1.grid(row=1, column=1)
    input2.grid(row=2, column=1)
    Loginbtn.grid(row=3)
    createNewUser.grid(row=3,column=1)
    window.mainloop()

    
    # user = User("KP","J",1)
    # user.setFirstName("Kale")
    # user.setLastName("Pel")
    # user.setID(2)
    # user.printInfo()

    # admin = Admin("Kaleb","P",1)
    # admin.addCourse("programming")
    # admin.removeCourse("programming")
    # admin.searchCourse("programming")
    # admin.printCourse("programming")
    # admin.addUser("Q")
    # admin.removeUser("Q")
    # admin.addStudent("student1")
    # admin.removeStudent("student1")
    # admin.createRoster("Roster1")
    # admin.searchRoster("Roster1")
    # admin.printRoster("Roster1")

    # student = Student("Matt","A",100)
    # student.addCourse("APC")
    # student.dropCourse("APC")
    # student.searchCourse("APC")
    # student.printSchedule()

    # instructor = Instructor("Mike","C",200)
    # instructor.printSchedule()
    # instructor.searchCourse("DCD")
    # instructor.printClassList()


    cur.execute("SELECT TITLE\nFROM COURSE\nWHERE COURSE.TITLE ='Geology'")
    geo = cur.fetchall()

    cur.execute("SELECT DEPARTMENT\nFROM COURSE\nWHERE COURSE.SEMESTER ='Fall'")
    dep = cur.fetchall()


    cur.execute("SELECT * FROM COURSE")
    course = cur.fetchall()


    cur.execute("SELECT COURSE.TITLE,INSTRUCTOR.LAST_NAME\nFROM COURSE,INSTRUCTOR\nWHERE COURSE.DEPARTMENT = INSTRUCTOR.DEPARTMENT")
    teacherList = cur.fetchall()

    print(teacherList)
    #print(geo)
    #print(dep)
    #print(course)
    con.commit()
    con.close()


if __name__ == "__main__":
    
    main()