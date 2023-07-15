from tkinter import *
import tkinter as tk
import datetime

import sqlite3 
con = sqlite3.connect("assignment3FINAL.db")
cur = con.cursor()

today = datetime.date.today()
year = today.year #gets current year for grad year

#cur.execute("INSERT INTO STUDENT VALUES(101,'Kaleb','Pelletier','COMP_ENG','pelletierk3',2024);")
#cur.execute("INSERT INTO STUDENT VALUES(102,'Matt','Auger','COMP_ENG','augerm',2024);")
#cur.execute("DELETE FROM INSTRUCTOR WHERE LAST_NAME='Fourier';")
# cur.execute("UPDATE ADMIN\n"+
#             "SET TITLE='Vice-President'\n"+
#            "WHERE ID=3002\n")
#cur.execute("INSERT INTO LOGIN (EMAIL, PASSWORD, ID) SELECT EMAIL, NULL, ID FROM INSTRUCTOR;")
            
           

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
    def searchCourse(self,course):
        print("Searching " + course)


class Admin(User):
    def __init__(self,ID, f_name, l_name, title,email,office):
        User.__init__(self,f_name,l_name,ID)
        self.title = title
        self.email = email
        self.office = office

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
    # def searchCourse(self,course):
    #     print("Searching " + course)
    def printCourse(self,course):
        print("Printing course" + course)

class Student(User):
    def __init__(self, ID, f_name, l_name, major, email, exp_grad,password):
        User.__init__(self,f_name, l_name, ID)
        self.id = ID
        self.first = f_name
        self.last = l_name
        self.major = major
        self.email = email
        self.exp_grad_year = exp_grad
        self.password = password
    def __init__(self, ID, f_name, l_name, major, email, exp_grad):
        User.__init__(self,f_name, l_name, ID)
        self.id = ID
        self.first = f_name
        self.last = l_name
        self.major = major
        self.email = email
        self.exp_grad_year = exp_grad

    def addToDataBase(self):
        cur.execute("INSERT INTO STUDENT VALUES("+str(self.id)+",'"+self.first+"','"+self.last+"','"+self.major+"',"
                    +"'"+self.email+"',"+str(self.exp_grad_year)+");")
        cur.execute("INSERT INTO LOGIN VALUES('"+self.email+"','"+self.password+"',"+str(self.id)+");")

    def searchCourse(self,course):
        print("Searching " + course)

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
    def __init__(self, ID,f_name, l_name,title,email,department,yearOfHire ):
        User.__init__(self,f_name, l_name, ID)
        self.title = title
        self.email = email
        self.department = department
        self.yearOfHire = yearOfHire

    def searchCourse(self,course):
        print("Searching " + course)
    def printSchedule(self):
        print("Printing Schedule")
    def printClassList(self):
        print("Printing Class list")

window = Tk()

#mainWindow = Toplevel()
#mainWindow.withdraw() #Hides window

mainEmailInput= tk.Entry(window)#username/email input1
mainPasswordInput = tk.Entry(window) #password


def create(fName,lName,major,password):
    email = lName + fName[0]
    email = email.lower()

    statement = f"SELECT ID from STUDENT WHERE FIRST_NAME='{fName}';"
    test = cur.execute(statement)
    print(test)
    if not cur.fetchone:
        print("USER EXISTS")
    else:
        cur.execute("SELECT ID FROM STUDENT")
        idList = cur.fetchall()
        currID = idList[-1][0]
        newID = currID + 1
        gradyear = year + 4
        s = Student(newID,fName,lName,major,email,gradyear,password)
        s.addToDataBase()





def createNew():
    mainWindow = Toplevel(window)
    mainWindow.geometry("500x500")
    tk.Label(mainWindow, text="Create New User").grid(row=0)
    tk.Label(mainWindow, text="First Name").grid(row=1)
    tk.Label(mainWindow, text="Last Name").grid(row=2)
    tk.Label(mainWindow, text="Password").grid(row=3)
    tk.Label(mainWindow,text= "Major").grid(row = 4)

    inFirstName = tk.Entry(mainWindow)
    inLastName = tk.Entry(mainWindow)
    inPassword = tk.Entry(mainWindow)
    inMajor = tk.Entry(mainWindow)

    inFirstName.grid(row=1, column=1)
    inLastName.grid(row=2, column=1)
    inPassword.grid(row=3,column=1)
    inMajor.grid(row=4, column=1)

    b3 = tk.Button(mainWindow, text=' Create ',command= lambda:[create(inFirstName.get(),inLastName.get(),inMajor.get(),inPassword.get()),mainWindow.destroy()])
    b3.grid(row=5,column=1)


def getLoginInfo():
    mainWindow = Toplevel(window)
    mainWindow.geometry("400x400")

    #loop through the data tables to check if they exist

    cur.execute(f"SELECT LOGIN.ID\nFROM LOGIN\nWHERE LOGIN.PASSWORD = '{mainPasswordInput.get()}'") 
    loginID = cur.fetchall()

    userN = mainEmailInput.get()
    cur.execute(f"SELECT LOGIN.ID\nFROM LOGIN\nWHERE LOGIN.EMAIL = '{userN}'")
    userID = cur.fetchall()

    #CHECKS ID WITH EMAIL AND PASSWORD TO CHECK FOR MATCH
    if(loginID != userID):
        print("Log in Failed")
    else:
        userID = str(userID[0][0]) #gets first number of ID as string 
        status = userID[0] # this will give 1,2,3 based on status of user 
        

        if(status == '1'):
            mainWindow.title("Student")
            cur.execute(f"SELECT *\nFROM STUDENT\nWHERE ID={userID} ")
            student = cur.fetchall()
            s = Student(student[0][0],student[0][1],student[0][2],student[0][3],student[0][4],student[0][5])
            course_entry_search = tk.Entry(mainWindow)
            course_entry_search.grid(row=0,column=1)
            
            b1 = tk.Button(mainWindow, text=' Search Course ',command= lambda:[s.searchCourse(course_entry_search.get())]).grid(row=0,column=0)

            b2 = tk.Button(mainWindow, text=' Print Schedule ',command= lambda:[s.printSchedule()]).grid(row=1,column=0)

            course_entry = tk.Entry(mainWindow)
            course_entry.grid(row=2,column=1)
            b3 = tk.Button(mainWindow, text=' Add Course ',command= lambda:[s.addCourseToSemesterSchedule(course_entry.get())]).grid(row=2,column=0)

            drop_course_entry = tk.Entry(mainWindow)
            drop_course_entry.grid(row=3,column=1)
            b4 = tk.Button(mainWindow, text=' Drop Course ',command= lambda:[s.dropCourseFromSemesterSchedule(drop_course_entry.get())]).grid(row=3,column=0)


        if(status == "3"):
            mainWindow.title("Admin")
            cur.execute(f"SELECT *\nFROM ADMIN\nWHERE ID={userID} ")
            admin = cur.fetchall()
            a = Admin(admin[0][0],admin[0][1],admin[0][2],admin[0][3],admin[0][4],admin[0][5])

            createCourseEntry = tk.Entry(mainWindow)
            createCourseEntry.grid(row=0,column=1)
            b1 = tk.Button(mainWindow, text=' Create Course ',command= lambda:[a.createCourse(createCourseEntry.get())]).grid(row=0,column=0)

            removeCourseEntry = tk.Entry(mainWindow)
            removeCourseEntry.grid(row=1,column=1)
            b2 = tk.Button(mainWindow, text=' Remove Course ',command= lambda:[a.removeCourse(removeCourseEntry.get())]).grid(row=1,column=0)

            addUserEntry = tk.Entry(mainWindow)
            addUserEntry.grid(row=2,column=1)
            b3 = tk.Button(mainWindow, text=' Add User ',command= lambda:[a.addUser(addUserEntry.get())]).grid(row=2,column=0)

            removeUserEntry = tk.Entry(mainWindow)
            removeUserEntry.grid(row=3,column=1)
            b4 = tk.Button(mainWindow, text=' Remove User ',command= lambda:[a.removeUser(removeUserEntry.get())]).grid(row=3,column=0)

            addStudentEntry = tk.Entry(mainWindow)
            addStudentEntry.grid(row=4,column=1)
            b5 = tk.Button(mainWindow, text=' Add Student ',command= lambda:[a.addStudent(addStudentEntry.get())]).grid(row=4,column=0)

            removeStudentEntry = tk.Entry(mainWindow)
            removeStudentEntry.grid(row=5,column=1)
            b6 = tk.Button(mainWindow, text=' Remove Student ',command= lambda:[a.removeStudent(removeStudentEntry.get())]).grid(row=5,column=0)

            createRosterEntry = tk.Entry(mainWindow)
            createRosterEntry.grid(row=6,column=1)
            b7 = tk.Button(mainWindow, text=' Create Roster ',command= lambda:[a.createRoster(createRosterEntry.get())]).grid(row=6,column=0)

            searchRosterEntry = tk.Entry(mainWindow)
            searchRosterEntry.grid(row=7,column=1)
            b8 = tk.Button(mainWindow, text=' Search Roster ',command= lambda:[a.searchRoster(searchRosterEntry.get())]).grid(row=7,column=0)

            printRosterEntry = tk.Entry(mainWindow)
            printRosterEntry.grid(row=8,column=1)
            b9 = tk.Button(mainWindow, text=' Print Roster ',command= lambda:[a.printRoster(printRosterEntry.get())]).grid(row=8,column=0)

            printCourseEntry = tk.Entry(mainWindow)
            printCourseEntry.grid(row=9,column=1)
            b10 = tk.Button(mainWindow, text=' Print Course ',command= lambda:[a.printCourse(printCourseEntry.get())]).grid(row=9,column=0)

        if(status == "2"):
            mainWindow.title("Instructor")
            cur.execute(f"SELECT *\nFROM INSTRUCTOR\nWHERE ID={userID} ")
            instructor = cur.fetchall()
            i = Instructor(instructor[0][0],instructor[0][1],instructor[0][2],instructor[0][3],instructor[0][4],instructor[0][5],instructor[0][6])
            #searchCourse(course) printSchedule printClassList
            course_entry_search = tk.Entry(mainWindow)
            course_entry_search.grid(row=0,column=1)
            
            b1 = tk.Button(mainWindow, text=' Search Course ',command= lambda:[i.searchCourse(course_entry_search.get())]).grid(row=0,column=0)
            b2 = tk.Button(mainWindow, text=' Print Schedule ',command= lambda:[i.printSchedule()]).grid(row=1,column=0)
            b3 = tk.Button(mainWindow, text=' Print Class List ',command= lambda:[i.printClassList()]).grid(row=2,column=0)


            


        userN = ""
        mainWindow.deiconify() #Shows window

    


def main():
    window.title("Lepord Web")
    window.geometry("500x500")

    tk.Label(window, text="Lepord Web").grid(row=0)
    tk.Label(window, text="Username").grid(row=1)
    tk.Label(window, text="Password").grid(row=2)

    Loginbtn = Button(window,text="Log In",command = getLoginInfo)
    createNewUser = Button(window,text ="Create New",command = createNew)


    mainEmailInput.grid(row=1, column=1)
    mainPasswordInput.grid(row=2, column=1)
    Loginbtn.grid(row=3)
    createNewUser.grid(row=3,column=1)
    window.mainloop()


   
    con.commit()
    con.close()


if __name__ == "__main__":
    
    main()