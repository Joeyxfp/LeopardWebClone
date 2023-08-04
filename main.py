from tkinter import *
import tkinter as tk
import datetime
import unittest 
from unittest import mock
from unittest.mock import patch


import sqlite3 
con = sqlite3.connect("assignment3FINAL.db")
cur = con.cursor()

today = datetime.date.today()
year = today.year #gets current year for grad year


     
loginStatus = False    
Testing = False

#Written by Kaleb
class TestCases(unittest.TestCase):
    
    def test_log_in(self):
        Testing = True # if true automatically press the log in button 
        mainEmailInput.insert(0,"newtoni") #valid username
        mainPasswordInput.insert(0,"a")# valid password
        main(Testing)
        self.assertEqual(loginStatus,True,"Log In Failed")

    def test_searchAllCoursesParam(self):
        with mock.patch('builtins.input',side_effect=['1',11051]):
            searchParam(cur)

    def test_searchall(self):
        searchAll(cur)
    
    def test_addCourse(self):
        with mock.patch('builtins.input',side_effect=['1',"12010","Object Oriented Programming","BSCE","3:00","2","2023","4","Spring","2002","2"]):
            a = Admin(3001,"Margaret","Hamilton","President","hamiltonm","Dobbs 1600")
            print('-------Course created-----\n')
            a.createCourse(cur)
    def test_removeCourse(self):
        with mock.patch('builtins.input',side_effect=['1',"12010","DELETE","2"]):
            print('-------Course Removed-----\n')
            a = Admin(3001,"Margaret","Hamilton","President","hamiltonm","Dobbs 1600")
            a.removeCourse(cur)
    def test_addCourseSemSchedule(self):
        with mock.patch('builtins.input',side_effect=['1',"11051","2"]):
            print('-------Course Added to schedule-----\n')
            s = Student("1001","Issac","Newton","BSAS","newtoni","1668","a")
            s.addCourseToSemesterSchedule(cur)
    def test_removeCourseSemSchedule(self):
        with mock.patch('builtins.input',side_effect=['1',"11051","2"]):
            print('-------Course Dropped-----\n')
            s = Student("1001","Issac","Newton","BSAS","newtoni","1668","a")
            s.dropCourseFromSemesterSchedule(cur)
    def test_printCourseRoster(self):
       print("----SCHEDULE-------\n")
       i = Instructor("2002","Nelson","Patrick","Full Prof.","parickn","HUSS","1994")
       i.instructorPrintSchedule(cur)

    

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
        
            if input("Press 1 to add a course. Press 2 to exit") == '2' : 
                return
            crn = input('course CRN: ')
            name = input("Course title: ")
            department = input("Department: ")
            time = input("Class time: ") 
            days = input('Class days: ')
            year = input('Year: ')
            credits = input('Credits: ')
            sem = input('Semester: ')
            instructorId = input('Instructor Id: ')
            cur.execute("INSERT INTO COURSE VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (crn, name, department, time, days, year, credits, sem,instructorId)) 
            con.commit()
    def createCourseGUI(self):
        createcourse_window = Toplevel()
        createcourse_window.title('Create Course')
        createcourse_window.geometry("400x400")


        crnEntry = tk.Entry(createcourse_window)
        crnEntry.grid(row=0,column=1)
        e1 = tk.Label(createcourse_window, text=' CRN: ').grid(row=0,column=0)
        #crn = crnEntry.get()

        nameEntry = tk.Entry(createcourse_window)
        nameEntry.grid(row=1,column=1)
        e2 = tk.Label(createcourse_window, text='Course Title: ').grid(row=1,column=0)
        #name = nameEntry.get()

        departmentEntry = tk.Entry(createcourse_window)
        departmentEntry.grid(row=2,column=1)
        e3 = tk.Label(createcourse_window, text=' Department: ').grid(row=2,column=0)
        #department = departmentEntry.get()

        timeEntry = tk.Entry(createcourse_window)
        timeEntry.grid(row=3,column=1)
        e4 = tk.Label(createcourse_window, text=' Time: ').grid(row=3,column=0)
        #time = timeEntry.get()

        daysEntry = tk.Entry(createcourse_window)
        daysEntry.grid(row=4,column=1)
        e5 = tk.Label(createcourse_window, text=' Days: ').grid(row=4,column=0)
        #days = daysEntry.get()

        yearEntry = tk.Entry(createcourse_window)
        yearEntry.grid(row=5,column=1)
        e6 = tk.Label(createcourse_window, text=' Year: ').grid(row=5,column=0)
        #year = yearEntry.get()

        creditsEntry = tk.Entry(createcourse_window)
        creditsEntry.grid(row=6,column=1)
        e7 = tk.Label(createcourse_window, text=' Credits: ').grid(row=6,column=0)
        #credits = creditsEntry.get()

        semEntry = tk.Entry(createcourse_window)
        semEntry.grid(row=7,column=1)
        e8 = tk.Label(createcourse_window, text=' Semester: ').grid(row=7,column=0)
        #sem = semEntry.get()

        IIDEntry = tk.Entry(createcourse_window)
        IIDEntry.grid(row=8,column=1)
        e9 = tk.Label(createcourse_window, text=' Instructor ID: ').grid(row=8,column=0)
        #IID = IIDEntry.get()

       # b = tk.Button(createcourse_window, text = 'Create Course', command = cur.execute("INSERT INTO COURSE VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (crnEntry.get(), nameEntry.get(), departmentEntry.get(), timeEntry.get(), daysEntry.get(), yearEntry.get(), creditsEntry.get(), semEntry.get(),IIDEntry.get()))).grid(row = 9, column = 0)










       





    def removeCourse(self, cur):
        #remove course created by joey
        while(1):
            if input("Press 1 to remove a course. Press 2 to exit") == '2' :
                 return
            crn = input("Input the course CRN: ")
            try:
                cur.execute("""SELECT * FROM course WHERE CRN = '%s';""" %crn)
                print("Course selected: %s" %cur.fetchall())
                confirm = input("To delete type 'DELETE'")
                match confirm:
                    case 'DELETE':
                        cur.execute("""DELETE FROM COURSE WHERE CRN = '%s';""" %crn)
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

    def printall(self):
        print ("Printing all courses avaliable. ")

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
    
    def getID(self):
        return self.id
    def addToDataBase(self):
        cur.execute("INSERT INTO STUDENT VALUES("+str(self.id)+",'"+self.first+"','"+self.last+"','"+self.major+"',"
                    +"'"+self.email+"',"+str(self.exp_grad_year)+");")
        cur.execute("INSERT INTO LOGIN VALUES('"+self.email+"','"+self.password+"',"+str(self.id)+");")

    def searchCourse(self,course):
        print("Searching " + course)

    def printSchedule(self):
        print("Printing Schedule")
        schedule_window = Toplevel()
        schedule_window.title("Student Schedule")
        
    def addCourseToSemesterSchedule(self, cur):
        
        if input("Press 1 to add a course to Schedule, Press 2 to exit") == '2' : 
            return #currently asks for input but we can change to buttons with tkinter menu
        crn = input('Course CRN: ')
        cur.execute("SELECT * FROM COURSE WHERE CRN = '%s';" % (crn))
        course = cur.fetchone()
        if course == None:
            print("Invalid CRN") 
        else: 
            try:
                cur.execute("""INSERT INTO SEMESTERSCHEDULE VALUES('%s', '%s', '%s');""" % (crn, course[1], self.getID()))
                con.commit()
            except: #if course already exists it tells the user 
                print('Course already in schedule')
    def dropCourseFromSemesterSchedule(self, cur):
        
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
    def log_in(self):
        mainEmailInput.insert(0,self.email)
        mainPasswordInput.insert(0,self.password)
        Loginbtn.invoke()
        

class Instructor(User):
    def __init__(self, ID,f_name, l_name,title,email,department,yearOfHire ):
        User.__init__(self,f_name, l_name, ID)
        self.title = title
        self.email = email
        self.department = department
        self.yearOfHire = yearOfHire

    def getID(self):
        return self.id

    def searchCourse(self,course):
        print("Searching " + course)
    def printSchedule(self, cur):
        schedule_window = Toplevel()
        schedule_window.title("Instructor Schedule")
        # Retrieve the schedule for the instructor from the database
        #cur.execute("SELECT * FROM COURSE WHERE INSTRUCTORID = '%s';" % self.getID())
        #cur.execute(f"SELECT LOGIN.ID\nFROM LOGIN\nWHERE LOGIN.EMAIL = '{userN}'")

        cur.execute("SELECT * FROM COURSE WHERE INSTRUCTORID = '%s'" % self.getID())

        schedule = cur.fetchall()

        
        if schedule:
            for course in schedule:
                course_info = f"Course Name: {course[1]}\n"\
                              f"Department: {course[2]}\n" \
                              f"Time: {course[3]}\n" \
                              f"Days of the Week: {course[4]}\n\n"
                tk.Label(schedule_window, text=course_info).pack()
                              
        else:
            tk.Label(schedule_window, text="No courses in schedule.").pack()



    def printClassList(self):
        classlist_window = Toplevel()
        classlist_window.title("Class List")
        print("Printing Class list")
        cur.execute("SELECT TITLE FROM COURSE WHERE INSTRUCTORID = '%s';" %self.getID())
        coursetitle = cur.fetchall()

        for i in range (len(coursetitle)):
            cur.execute("SELECT ID FROM SEMESTERSCHEDULE WHERE Course = '%s';" %coursetitle[i] )
            
            classlist = cur.fetchall()
            

            studentlist_info = ""
            tk.Label(classlist_window, text = (coursetitle[i][0])).pack()
            print(coursetitle[i])
            for j in range(len(classlist)):

                    

                cur.execute("SELECT FIRST_NAME, LAST_NAME FROM STUDENT WHERE ID ='%s';" %classlist[j])
                studentlist = cur.fetchall()
                studentlist_info = studentlist_info + studentlist[0][0] + " " + studentlist[0][1] + "\n"
            
            tk.Label(classlist_window, text = studentlist_info).pack()






        # if classlist & coursetitle:
        #     for semesterschedule in classlist:
        #         classlist = f"CRN: {semesterschedule[0]}\n"\
        #                     f"Course: {semesterschedule[1]}\n"\
        #                     f"ID: {semesterschedule[2]}\n"
        # tk.Label(classlist_window, text = classlist).pack()
    def instructorPrintSchedule(self, cur):
        
        cur.execute("""SELECT * FROM COURSE WHERE INSTRUCTORID = '%s';""" % self.getID())
        allClasses = cur.fetchall()
        if(allClasses == None):
            print("No classes found.")
        else:
            for course in allClasses:
                printCourse(course)

    def searchRosters(self, cur):
    
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

def searchAll(cursor):
    cursor.execute("SELECT * FROM course;")
    courses = cursor.fetchall()
    for course in courses:
        printCourse(course) 

window = Tk()

def printCourse(course):
    print('Course Name: ' + str(course[1]))
    print('CRN: ' + str(course[0]))
    print('Department: ' + str(course[2]))
    print('Time: ' + str(course[3]))
    print('Days of the Week: ' + str(course[4]))
    print('Semester: ' + str(course[5]))
    print('Year: ' + str(course[6]))
    print('Credits: ' + str(course[7]))
    print(' ')

def searchParam(cursor):
   
    print('Params: 1-CRN, 2-TITLE, 3-DEPARTMENT, 4-TIME, 5-DAYS, 6-SEMESTER, 7-YEAR, 8-CREDITS, 9-INSTRUCTORID')      #There is no case statement for 'Time'
    param = input("Enter a parameter: ")
    match param:
        case '1':
            crn = input("Enter a CRN: ")
            cursor.execute("SELECT * FROM COURSE WHERE CRN='%s';" %crn)
            courses = cursor.fetchall()
            for course in courses:
                printCourse(course)
        case '2':
            time = input("Enter the start time of the course in the format 10:00:00 : ")
            cursor.execute("SELECT * FROM COURSE WHERE TIME='%s';" %time)
            courses = cursor.fetchall()
            for course in courses:
                printCourse(course)
        case '3':
            title = input("Enter a title: ")
            cursor.execute("SELECT * FROM COURSE WHERE TITLE='%s';" %title)
            courses = cursor.fetchall()
            for course in courses:
                printCourse(course)
        case '4':
            department = input("Enter a department: ")
            cursor.execute("SELECT * FROM COURSE WHERE DEPARTMENT='%s';" %department)
            courses = cursor.fetchall()
            for course in courses:
                printCourse(course)
        case '5':
            daysOfWeek = input("Enter a days of week: ")
            cursor.execute("SELECT * FROM COURSE WHERE DAYSOFWEEK='%s';" %daysOfWeek)
            courses = cursor.fetchall()
            for course in courses:
                printCourse(course)
        case '6':
            semester = input("Enter a semester: ")
            cursor.execute("SELECT * FROM COURSE WHERE SEMESTER='%s';" %semester)
            courses = cursor.fetchall()
            for course in courses:
                printCourse(course)
        case '7':
            year = input("Enter a year: ")
            cursor.execute("SELECT * FROM COURSE WHERE YEAR='%s';" %year)
            courses = cursor.fetchall()
            for course in courses:
                printCourse(course)
        case '8':
            credits = input("Enter a credits: ")
            cursor.execute("SELECT * FROM COURSE WHERE CREDITS='%s';" %credits)
            courses = cursor.fetchall()
            for course in courses:
                printCourse(course)
        case '9':
            instructorID = input("Enter an instructor ID: ")
            cursor.execute("SELECT * FROM COURSE WHERE INSTRUCTORID='%s';" %instructorID)
            courses = cursor.fetchall()
            for course in courses:
                printCourse(course)
        case _:
            print(f'"{param}"Not a valid param')




#mainWindow = Toplevel()
#mainWindow.withdraw() #Hides window

mainEmailInput= tk.Entry(window)#username/email input1

mainPasswordInput = tk.Entry(window) #password




def create(fName,lName,major,password):
    #Written by Kaleb 
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
    #Written by Kaleb 
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
    #Written by Kaleb
   


    #loop through the data tables to check if they exist

    cur.execute(f"SELECT LOGIN.ID\nFROM LOGIN\nWHERE LOGIN.PASSWORD = '{mainPasswordInput.get()}'") 
    loginID = cur.fetchall()

    userN = mainEmailInput.get()
    cur.execute(f"SELECT LOGIN.ID\nFROM LOGIN\nWHERE LOGIN.EMAIL = '{userN}'")
    userID = cur.fetchall()

    #CHECKS ID WITH EMAIL AND PASSWORD TO CHECK FOR MATCH
   
    if(loginID != userID or not loginID):
        print("Log in Failed")
        loginfail = tk.Label(window, text = "Log in Failed :(", fg = '#f00',font = ("Ariel", 25), height = 10).place(x = 100, y = 100)
    else:
        

        mainWindow = Toplevel(window)
        mainWindow.geometry("400x400")
    
        global loginStatus
        loginStatus = True
        userID = str(userID[0][0]) #gets first number of ID as string 
        status = userID[0] # this will give 1,2,3 based on status of user 
        

        if(status == '1'):
            mainWindow.title("Student")
            cur.execute(f"SELECT *\nFROM STUDENT\nWHERE ID={userID} ")
            student = cur.fetchall()
            s = Student(student[0][0],student[0][1],student[0][2],student[0][3],student[0][4],student[0][5],mainPasswordInput.get())
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
            b1 = tk.Button(mainWindow, text=' Create Course ',command= lambda:[a.createCourseGUI()]).grid(row=0,column=0)

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
            b2 = tk.Button(mainWindow, text=' Print Schedule ', command=lambda: [i.printSchedule(cur)]).grid(row=1, column=0)
            b3 = tk.Button(mainWindow, text=' Print Class List ',command= lambda:[i.printClassList()]).grid(row=2,column=0)

            


            


        userN = ""
        mainWindow.deiconify() #Shows window

    
Loginbtn = Button(window,text="Log In",command = getLoginInfo)


def main(Testing):
    #Written by Kaleb
    window.title("Lepord Web")
    window.geometry("500x500")

    tk.Label(window, text="Lepord Web").grid(row=0)
    tk.Label(window, text="Username").grid(row=1)
    tk.Label(window, text="Password").grid(row=2)

    #Loginbtn = Button(window,text="Log In",command = lambda:[getLoginInfo])
    if(Testing):
        Loginbtn.invoke()
        window.after(2000,lambda:window.destroy())
    createNewUser = Button(window,text ="Create New",command = createNew)
    mainEmailInput.grid(row=1, column=1)
    mainPasswordInput.grid(row=2, column=1)
    Loginbtn.grid(row=3)
    createNewUser.grid(row=3,column=1)
    window.mainloop()


   
    # con.commit()
    # con.close()


if __name__ == "__main__":
    
    main(Testing)
    #unittest.main()
    con.commit()
    con.close()