#have user login 
#if user admin display admin tools
#if user instructor display instructor tools
#if user student display student tools 
#have logout page 


class User:
    def __init__(self, first_name, last_name, id):
        self._first_name = first_name
        self._last_name = last_name
        self._id = id
    
    def set_first_name(self, first_name):
        self._first_name = first_name
    
    def set_last_name(self, last_name):
        self._last_name = last_name
    
    def set_id(self, id):
        self._id = id
    
    def print_info(self):
        print(f"FirstName = {self._first_name}")
        print(f"LastName  = {self._last_name}")
        print(f"ID        = {self._id}")


class Student(User):
    def __init__(self, first_name, last_name, id):
        super().__init__(first_name, last_name, id)
        self._classes = []
    
    def add_class(self, class_name):
        self._classes.append(class_name)
    
    def drop_class(self, class_name):
        if class_name in self._classes:
            self._classes.remove(class_name)
        else:
            print(f"{class_name} is not in your schedule.")
    
    def print_schedule(self):
        print(f"Schedule for {self._first_name} {self._last_name}:")
        for i, class_name in enumerate(self._classes):
            print(f"{i+1}. {class_name}")
    def search_class(self, class_name, overall_classes):
        if class_name in overall_classes:
            print(f"{class_name} is available.")
        else:
            print(f"{class_name} is not available.")



class Instructor(User):
    def __init__(self, first_name, last_name, id):
        super().__init__(first_name, last_name, id)
        self._classes = []
    
    def add_class(self, class_name):
        self._classes.append(class_name)
    
    def drop_class(self, class_name):
        if class_name in self._classes:
            self._classes.remove(class_name)
        else:
            print(f"{class_name} is not in your class list.")
    
    def print_classes(self):
        print(f"Classes taught by {self._first_name} {self._last_name}:")
        for i, class_name in enumerate(self._classes):
            print(f"{i+1}. {class_name}")
    
    def search_class(self, class_name, overall_classes):
        if class_name in self._classes:
            print(f"{class_name} is taught by {self._first_name} {self._last_name}.")
        else:
            super().search_class(class_name, overall_classes)
    
    def print_schedule(self):
        super().print_schedule()


class Admin(User):
    def __init__(self, first_name, last_name, id):
        super().__init__(first_name, last_name, id)
        self._courses = []
        self._users = []
    
    def add_course(self, course_name):
        if course_name not in self._courses:
            self._courses.append(course_name)
        else:
            print(f"{course_name} already exists in the system.")
    
    def remove_course(self, course_name):
        if course_name in self._courses:
            self._courses.remove(course_name)
        else:
            print(f"{course_name} does not exist in the system.")
    
    def add_user(self, user):
        if isinstance(user, User):
            self._users.append(user)
        else:
            print(f"{user} is not a User object.")
    
    def remove_user(self, user):
        if user in self._users:
            self._users.remove(user)
        else:
            print(f"{user} does not exist in the system.")
    
    def add_student_to_course(self, student, course_name):
        if course_name in self._courses:
            student.add_class(course_name)
        else:
            print(f"{course_name} does not exist in the system.")
    
    def remove_student_from_course(self, student, course_name):
        if course_name in self._courses:
            student.drop_class(course_name)
        else:
            print(f"{course_name} does not exist in the system.")
    
    def print_roster(self, course_name):
        if course_name in self._courses:
            print(f"Roster for {course_name}:")
            for user in self._users:
                if isinstance(user, Student) and course_name in user.get_classes():
                    print(f"{user._first_name} {user._last_name}")
        else:
            print(f"{course_name} does not exist in the system.")
    
    def print_courses(self):
        print("Courses in the system:")
        for i, course_name in enumerate(self._courses):
            print(f"{i+1}. {course_name}")
    
    def search_course(self, course_name):
        if course_name in self._courses:
            print(f"{course_name} is in the system.")
        else:
            print(f"{course_name} does not exist in the system.")


# search by some parameter,
# insert, 
# print all, 
# create table (as with the course relation), 
# update, 
# and remove. 
# A menu and functions will make this simpler



'''
ID
First name
Last name
Expected Grad year
major 
email
'''
import sqlite3

# database file connection
database = sqlite3.connect("assignment3.db") 
  
# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers  
cursor = database.cursor() 
  
# SQL command to create a table in the database 

'''
sql_command = """CREATE TABLE STUDENT(  
ID INTEGER PRIMARY KEY NOT NULL,
FIRST_NAME TEXT NOT NULL,
LAST_NAME TEXT NOT NULL,
MAJOR TEXT NOT NULL,
EMAIL TEXT NOT NULL,
EXPECTED_GRAD_YEAR INTEGER NOT NULL)
;"""

sql_command = """CREATE TABLE INSTRUCTOR(  
ID INTEGER PRIMARY KEY NOT NULL,
FIRST_NAME TEXT NOT NULL,
LAST_NAME TEXT NOT NULL,
TITLE TEXT NOT NULL,
EMAIL TEXT NOT NULL,
DEPARTMENT TEXT NOT NULL,
YEAR_OF_HIRE INTEGER NOT NULL)
;"""


sql_command = """CREATE TABLE ADMIN(  
ID INTEGER PRIMARY KEY NOT NULL,
FIRST_NAME TEXT NOT NULL,
LAST_NAME TEXT NOT NULL,
TITLE TEXT NOT NULL,
EMAIL TEXT NOT NULL,
OFFICE TEXT NOT NULL)
;"""

sql_command = """CREATE TABLE COURSE(  
CRN INTEGER PRIMARY KEY NOT NULL,
TITLE TEXT NOT NULL,
DEPARTMENT TEXT NOT NULL,
TIME TEXT NOT NULL,
DAYS_OF_WEEK TEXT NOT NULL,
YEAR INTEGER NOT NULL,
CREDITS INTEGER NOT NULL,
SEMESTER TEXT NOT NULL)
;"""

sql_command = """CREATE TABLE COURSE_TIMES(  
CRN INTEGER PRIMARY KEY NOT NULL,
MONDAY_START INTEGER NULL,
MONDAY_END INTEGER NULL,
TUESDAY_START INTEGER NULL,
TUESDAY_END INTEGER NULL,
WEDNESDAY_START INTEGER NULL,
WEDNESDAY_END INTEGER NULL,
THURSDAY_START INTEGER NULL,
THURSDAY_END INTEGER NULL,
FRIDAY_START INTEGER NULL,
FRIDAY_END INTEGER NULL)
;"""
'''
#execute the statement 
 




sql_command = """INSERT INTO STUDENT VALUES(1076, 'ADA', 'LOVELACE', 'COMPUTER_ENGINEERING', 'LOVELACEA@WIT.EDU', 2024);"""
cursor.execute(sql_command) 
'''
def remove_course(self, CRN):
    cursor.execute("""SELECT CRN FROM COURSE""")
    query_result = cursor.fetchall()
    if CRN in query_result:
        sql_Delete_query = """DELETE FROM COURSE WHERE id = %s"""  #we need to remove from time table too but not for now
        cursor.execute(sql_Delete_query, (CRN,))
    else:
        print(f"{CRN} does not exist in the system.")

def add_course(self, CRN):
    cursor.execute("""SELECT CRN FROM COURSE""")
    query_result = cursor.fetchall()
    if CRN in query_result:
        print(f"{CRN} already exists in the system.")
    else:
        #use tkinter buttons to add course
'''
# QUERY FOR ALL

#print("Entire table")
#cursor.execute("""SELECT * FROM STUDENT""")
#query_result = cursor.fetchall()
  
#for i in query_result:
#	print(i)


# QUERY FOR SOME
#print("Only those born prior to 1950")
#cursor.execute("""SELECT * FROM PROGRAMMER WHERE BIRTHYEAR < 1950""")
#query_result = cursor.fetchall()

#for i in query_result:
#	print(i)

# ADDING FROM USER INPUT
#uid = "6"
#fname = input("First name of a famous programmer: ")
#lname = input("Last name of the same programmer: ")
#birthyear = input("Birth year of the same programmer: ") 

#cursor.execute("""INSERT INTO PROGRAMMER VALUES('%s', '%s', '%s', '%s');""" % (uid, fname, lname, birthyear))

#print("Entire table")
#cursor.execute("""SELECT * FROM PROGRAMMER""")
#query_result = cursor.fetchall()
  
#for i in query_result:
#	print(i)

# To save the changes in the files. Never skip this.  
# If we skip this, nothing will be saved in the database. 
database.commit() 
  
# close the connection 
database.close() 
