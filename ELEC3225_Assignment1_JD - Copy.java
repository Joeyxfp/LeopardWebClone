import java.util.List;
import java.util.ArrayList;

//Jonathan Daermann
//-----------------
// USING JAVA 
// Note* All classes are within this one file, to compile and run my tests I put them into seperate java files. 
//
//
//
// PROS: -not to difficult to read and understand
//       -tieing in the code for inheritance is fairly simple and gives less errors then other languages
//       - use of private and public makes software more secure 
//
// CONS: -inheriting from multiple classes is difficult thus we reuse alot of code since we inherite mainly from User
//     to combat this we might make a more advanced parent class that holds all the re-used functions like class search 
//       - use of private and public can make code more complicated
//       -All classes must be on diffrent files, this makes the code more clean however if working with others can make things go south quick



public class User {
    private String firstName; //setting attribute first name (string)
    private String lastName; //setting attribute last name (string)
    private int id; //setting attribute id (intiger)

    public User(String firstName, String lastName, int id) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.id = id;
    }

    public void setFirstName(String firstName) { //function to set first name
        this.firstName = firstName;
    }

    public void setLastName(String lastName) { //function to set last name
        this.lastName = lastName;
    }
    
    public void getfirstName() { 
        System.out.println(firstName);
    }
    
    public void getLastName() { 
        System.out.println(lastName);
    }
    public void setId(int id) {    //function to set id 
        this.id = id;
    }

    public void printInfo() {   //function to print all the info 
        System.out.println("First Name: " + firstName);
        System.out.println("Last Name: " + lastName);
        System.out.println("ID: " + id);
    }
}
public class Student extends User 
{ //making student an inheritance of User
    private List<String> courses;
    
    private String firstName; //setting attribute first name (string)
    private String lastName; //setting attribute last name (string)
    private int id; //setting attribute id (intiger)
    
    public Student(String firstName, String lastName, int id) {
        super(firstName, lastName, id);
        this.courses = new ArrayList<>();
    }
    
    
    public String getFirstName() { 
        return(firstName);
    }
    
    public String getLastName() { 
        return(lastName);
    }

    public void addCourse(String course) { //function to add course 
        this.courses.add(course);
    }

    public void dropCourse(String course) { //function to remove course 
        this.courses.remove(course);
    }

    public void printSchedule() { //function to print schedule 
        System.out.println("Schedule for " + getFirstName() + " " + getLastName() + ":");
        for (String course : courses) { //for loop that prints all courses in the list of cources tied to student
            System.out.println("- " + course);
        }
    }
    public List<String> getCourses(){
        return courses;
    }
    public List<String> searchCourses(String keyword) {
        List<String> classList = new ArrayList<>();

        // Adding class names to the list
        classList.add("ClassA");
        classList.add("ClassB");

        // Printing the class names
        return classList;
       
    }
}


public class Instructor extends User { // making class instructor an extension of User
    private List<String> courses;
    private List<Student> students;

    private String firstName; //setting attribute first name (string)
    private String lastName; //setting attribute last name (string)
    private int id; //setting attribute id (intiger)
    
    public Instructor(String firstName, String lastName, int id) {
        super(firstName, lastName, id);
        this.courses = new ArrayList<>(); //creating array to store class list 
        this.students = new ArrayList<>(); //creating variable to store students for roster
    }

    private String getFirstName() { 
        return(firstName);
    }
    
    public String getLastName() { 
        return(lastName);
    }
    public void addCourse(String course) {
        this.courses.add(course);
    }

    public void removeCourse(String course) {
        this.courses.remove(course);
    }

    public void printSchedule() {
        System.out.println("Schedule for " + getFirstName() + " " + getLastName() + ":");
        for (String course : courses) {
            System.out.println("- " + course);
        }
    }
    public List<String> getAllCourses() {
        return this.courses;
    }
}

public class Admin {
    private List<String> courses;
    private List<User> users;

    public Admin() {
        this.courses = new ArrayList<>();
        this.users = new ArrayList<>(); //function to keep a list if users 
    }

    public void addCourse(String course) {
        this.courses.add(course);
    }

    public void removeCourse(String course) {
        this.courses.remove(course);
    }

    public void addUser(User user) {
        this.users.add(user);
    }

    public void removeUser(User user) {
        this.users.remove(user);
    }

    public void addStudentToCourse(Student student, String course) {
        for (User user : users) {
            if (user instanceof Instructor) {
                Instructor instructor = (Instructor) user;
                if (instructor.getCourses().contains(course)) {
                    instructor.addStudent(student);
                    student.addCourse(course);
                }
            }
        }
    }
    public void removeStudentFromCourse(Student student, String course) {
        for (User user : users) {
            if (user instanceof Instructor) {
                Instructor instructor = (Instructor) user;
                if (instructor.getCourses().contains(course)) {
                    instructor.removeStudent(student);
                    student.dropCourse(course);
                }
            }
        }
    }

    public List<String> searchCourses(String keyword) {
        List<String> classList = new ArrayList<>();

        // Adding class names to the list
        classList.add("ClassA");
        classList.add("ClassB");

        // Printing the class names
        return classList;
       
    }

    public List<String> getRoster(String course) {
        List<String> roster = new ArrayList<>();
        for (User user : users) {
            if (user instanceof Student) {
                Student student = (Student) user;
                if (student.getCourses().contains(course)) {
                    roster.add(student.getFirstName() + " " + student.getLastName());
                }
            }
        }
        return roster;
    }

    public List<String> getAllCourses() {
        return this.courses;
    }
}
public class Main 
{
    public static void main(String[] args) {
        User A1231 = new User("Mike", "Smith", 12345);
        A1231.printInfo();
        Admin admin = new Admin();
        admin.addCourse("History");
        admin.addCourse("Science");
        admin.getAllCourses();
        A1231.setFirstName("Jake");
        A1231.printInfo();


    }
}


