from tkinter import *
import tkinter as tk

import sqlite3 
con = sqlite3.connect("assignment3FINAL.db")
cur = con.cursor()

#adding schedule table for students created by Joey
sql_command = """
CREATE TABLE SEMESTERSCHEDULE (  
CRN CHAR(5) NOT NULL,
INSTRUCTORID CHAR(5) NOT NULL,
STUDENTID CHAR(5), 
PRIMARY KEY (CRN, STUDENTID, INSTRUCTORID)
);
"""
cur.execute(sql_command) 
            
            
           

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
    def getID(self):
        return self.ID

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
    
    def createCourse(self, cur):
        #add course created by joey
        while(1):
            if input("Press 1 to add a course. Press 2 to exit") == '2' : 
                return
            crn = input('course CRN: ')
            name = input("Course title: ")
            department = input("Department: ")
            time = input("Class time: ") 
            days = input('Class days: ')
            sem = input('Semester: ')
            year = input('Year: ')
            credits = input('Credits: ')
            instructorId = input('Instructor Id: ')
            try:
                cur.execute("""INSERT INTO course VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');""" % (crn, name, department, time, days, year, credits, sem, instructorId)) 
                con.commit()
            except:
                print("Invalid INPUT")
    def removeCourse(self, cur):
        #remove course created by joey
        while(1):
            if input("Press 1 to remove a course. Press 2 to exit") == '2' :
                 return
            crn = input("Input the course CRN: ")
            try:
                cur.execute("""SELECT * FROM course WHERE crn = '%s';""" %crn)
                print("Course selected: %s" %cur.fetchall())
                confirm = input("To delete type 'DELETE'")
                match confirm:
                    case 'DELETE':
                        cur.execute("""DELETE FROM course WHERE crn = '%s';""" %crn)
                        con.commit()
                    case _:
                        pass
            except:
                print("INVALID INPUT")


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
    
    def addCourseToSemesterSchedule(self, cur):
        #add course to semester schedule created by Joey
        if input("Press 1 to add a course to Schedule, Press 2 to exit") == '2' : 
            return #currently asks for input but we can change to buttons with tkinter menu
        crn = input('Course CRN: ')
        cur.execute("SELECT * FROM COURSE WHERE CRN = '%s';" % (crn))
        course = cur.fetchone()
        if course == None:
            print("Invalid CRN") 
        else:
            try: #attempt to add course 
                cur.execute("""INSERT INTO SEMESTERSCHEDULE VALUES('%s', '%s', '%s');""" % (crn, course[8], self.getID()))
                con.commit()
            except: #if course already exists it tells the user 
                print('Course already in schedule')
    def dropCourseFromSemesterSchedule(self, cur):
        #remove course from schedule created by joey
        if input("Press 1 to drop a course, Press 2 to exit") == '2' : 
            return
        crn = input('Course CRN: ')
        cur.execute("SELECT * FROM COURSE WHERE CRN = '%s';" % (crn))
        course = cur.fetchone()
        if course == None:
            print("Invalid CRN") 
        else:
            try:
                cur.execute("""DELETE FROM SEMESTERSCHEDULE WHERE CRN='%s';""" % (crn))
                con.commit()
            except:
                print('Course not in schedule')

class Instructor(User):
    def __init__(self, f_name, l_name, ID):
        User.__init__(self,f_name, l_name, ID)

    def searchCourse(self,course):
        print("Searching " + course)
    def printSchedule(self):
        print("Printing Schedule")
    def printClassList(self):
        print("Printing Class list")
    def instructorPrintSchedule(self, cursor):
        #prints instructors schedule created by joey
        cur.execute("""SELECT * FROM COURSE WHERE INSTRUCTORID = '%s';""" % self.getID())
        allClasses = cursor.fetchall()
        if(allClasses == None):
            print("No classes found.")
        else:
            for course in allClasses:
                printCourse(course)

    def searchRosters(self, cur):
      #prints roster for instructor created by joey
      while(1):
          if input("Press 1 to Search courses. Pess 2 to exit ") == '2' : 
            return
          crn = input('Please enter a course CRN: ')
          try:
              cur.execute("SELECT STUDENTID FROM SEMESTERSCHEDULE WHERE CRN='%s';" %crn)
              students = cur.fetchall()
              for person in students:
                  cur.execute("SELECT SURNAME, NAME FROM STUDENT WHERE ID='%s';" %person)
                  student = cur.fetchall()
                  for i in student:
                      print(i)
          except:
              print("Invalid Input")
    
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
    
def printCourse(course): 
    print('Course Name: ' + course[1])
    print('CRN: ' + course[0])
    print('Department: ' + course[2])
    print('Time: ' + course[3])
    print('Days of the Week: ' + course[4])
    print('Semester: ' + course[5])
    print('Year: ' + str(course[6]))
    print('Credits: ' + str(course[7]))
    print(' ')

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