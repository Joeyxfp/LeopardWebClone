#things to keep in mind
# classes need to have code and name and time contraints 
# cant allow user to schedule classes with time conflicts or more then 20 credits 

#Jonathan Daermann
#-----------------
# USING Python
#PROS: -Python has many built in libraries that make using SQL very easy
#      -Python is the most simple of the 3 making it easy to read and write
#      -super function allows us to limit re-used code
#
# CONS: -might be difficult to keep secure
#       
#       
fall2043 = ["History", "Science", "Math"]

class User: #base user class 
    def __init__(self, first_name, last_name, id): #init function 
        self._first_name = first_name
        self._last_name = last_name
        self._id = id
    
    def set_first_name(self, first_name): #function to set firstname
        self._first_name = first_name
    
    def set_last_name(self, last_name): #function to set lastname
        self._last_name = last_name
    
    def set_id(self, id): #function to set ID
        self._id = id
    
    def print_info(self): #function to print the info 
        print(f"FirstName = {self._first_name}")
        print(f"LastName  = {self._last_name}")
        print(f"ID        = {self._id}")


class Student(User): #class student derived from user 
    def __init__(self, first_name, last_name, id):
        super().__init__(first_name, last_name, id) #using super function to copy init class from user
        self._classes = [] #setting classes as empty array
    
    def add_class(self, class_name): #function to add class to classlist 
        self._classes.append(class_name)
    
    def drop_class(self, class_name): #function to remove class 
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
        #if user in self._users:
        #    self._users.remove(user)
        #else:
        #    print(f"{user} does not exist in the system.")
        print(f"you are trying to remove {user} ")
        #is will give us a weird number as we are trying to remove a global object from a local list will change with database inplementation
    
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

#Tests below 


#init a user called mike
User1 = User("Mike", "Smith", 12345)
User1.print_info()
#changing his first name to john
User1.set_first_name("John")
Student1 = Student("Matt", "Like", 12445)
Student1.add_class("History")
Student1.add_class("Science")
Student1.print_schedule()
Student1.search_class("History", fall2043)
Admin = Admin("Mrs", "Admin", 1)
Admin.remove_user(User1)