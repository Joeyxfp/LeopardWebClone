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
    def __init__(self, f_name, l_name, ID):
        User.__init__(self,f_name,l_name,ID)

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

    def addToDataBase(self):
        cur.execute("INSERT INTO STUDENT VALUES("+str(self.id)+",'"+self.first+"','"+self.last+"','"+self.major+"',"
                    +"'"+self.email+"',"+str(self.exp_grad_year)+");")
        cur.execute("INSERT INTO LOGIN VALUES('"+self.email+"','"+self.password+"',"+self.id+");")

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

    b3 = tk.Button(mainWindow, text=' Create ',
                   command= lambda:[create(inFirstName.get(),inLastName.get(),inMajor.get(),inPassword.get()),mainWindow.destroy()])
    b3.grid(row=5,column=1)


def getLoginInfo():
    mainWindow = Toplevel()
    mainWindow.geometry("800x800")

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

    mainEmailInput.grid(row=1, column=1)
    mainPasswordInput.grid(row=2, column=1)
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