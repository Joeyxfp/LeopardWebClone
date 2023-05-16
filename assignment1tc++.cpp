//Jonathan Daermann
//-----------------
// USING C++
// PROS: -mutliple inheritance is easier thus we reuse signifigantly less code. 
//       -C++ is a fast language in theory this is a pro however for our use i dont know if its relivent 
//       - use of protected and public makes software more secure 
//
// CONS: -difficult to read and understand
//       -use of protected and public can make code more complicated
//       -code is signifigantly harder to write with use of pointers and comlicated methods. 
//       -C++ is very strict when it comes to datatypes and say printing a line with an intiger is a massive work around for now i set ID as a string 
//

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class User {
public:
    User(string first_name, string last_name, string i_d) { //definging user and its attributes
        _first_name = first_name;
        _last_name = last_name;
        _id = i_d;
    }

    string get_full_info() {  //we add a function get full name this will allow other classes later to get the full name
        return _first_name + " " + _last_name + " ID: " + _id;
    }
    void setfirstname(string Name) {
        _first_name = Name;
    }
    void setLastname(string Name) {
        _last_name = Name;
    }
    void setLastname(int id) {
        _id = id;
    }
protected:
    string _first_name;
    string _last_name;
    string _id;
public:
    vector<string> _classes;
    vector<string> _courses;

};

class Student : public User { //creating class student inherited from class user
public:
    Student(string first_name, string last_name, string id) : User(first_name, last_name, id) {}

    void add_class(string class_name) { //fuction to add classes pushback is similar to python append and adds it to the end
        _classes.push_back(class_name);
    }

    void drop_class(string class_name) { //drop class funciton first checks for class, if its in the list it removes it, 
        auto it = find(_classes.begin(), _classes.end(), class_name); //if the class is not in the list it tells the user its not in the schedule
        if (it != _classes.end()) {
            _classes.erase(it);
        }
        else {
            cout << class_name << " is not in your schedule." << endl;
        }
    }

    void print_schedule() {  //function to print class schedule first checks size of the array to see how many classes there are then loops through and prints all the classes
        cout << "Schedule for " << _first_name << " " << _last_name << ":" << endl;
        for (int i = 0; i < _classes.size(); i++) {
            cout << i + 1 << ". " << _classes[i] << endl;
        }
    }
    void print_classlist() {  //function to print class list first checks size of the array to see how many classes there are then loops through and prints all the classes
        cout << "Classes Avaliable :" << endl;
        for (int i = 0; i < _courses.size(); i++) {
            cout << i + 1 << ". " << _courses[i] << endl;
        }
    }

};

class Instructor : public User { //class instructor derived from user 
public:
    Instructor(string first_name, string last_name, string id) : User(first_name, last_name, id) {}

    void add_class(string class_name) {
        _classes.push_back(class_name);
    }

    void remove_class(string class_name) {  //function that loops through class list and erases the class if found
        auto it = find(_classes.begin(), _classes.end(), class_name);
        if (it != _classes.end()) {
            _classes.erase(it);
        }
        else {
            cout << class_name << " is not in your schedule." << endl;
        }
    }
    void print_classlist() {  //function to print class list first checks size of the array to see how many classes there are then loops through and prints all the classes
        cout << "Classes Avaliable :" << endl;
        for (int i = 0; i < _courses.size(); i++) {
            cout << i + 1 << ". " << _courses[i] << endl;
        }
    }
    void print_roster(string class_name, vector<Student> students) {    //function to print class roster 
        cout << "Roster for " << class_name << ":" << endl;             //will need to update and think on how to tie into SQL database 
        for (int i = 0; i < students.size(); i++) {
            auto it = find(students[i]._classes.begin(), students[i]._classes.end(), class_name);
            if (it != students[i]._classes.end()) {
                cout << students[i].get_full_info() << endl;
            }
        }
    }


};

class Admin : public User
{
public:
    Admin(string first_name, string last_name, string id) : User(first_name, last_name, id) {}

    void add_course(string course_name) {
        _courses.push_back(course_name);
    }

    void remove_course(string course_name) {
        auto it = find(_courses.begin(), _courses.end(), course_name);
        if (it != _courses.end()) {
            _courses.erase(it);
        }
        else {
            cout << course_name << " does not exist." << endl;
        }
    }

    void add_user(User* user) { //function to add user, we use a pointer to hold temp info until values get entered 
        std::cout << "You add added user" << user << endl;
    }

    void remove_user(int user_id) {  //function to remove user, if user does not exist it returns telling the admin that

        std::cout << "User with ID " << user_id << " has been removes" << endl;
    }

    void add_student_to_class(Student& student, string class_name) {
        std::cout << "the student is now in " << class_name << endl;
    }
    void print_classlist() {  //function to print class list first checks size of the array to see how many classes there are then loops through and prints all the classes
        cout << "Classes Avaliable :" << endl;
        for (int i = 0; i < _courses.size(); i++) {
            cout << i + 1 << ". " << _courses[i] << endl;
        }
    }
};

int main()
{
    
    User A234324("Mike", "Lilo", "34");
    
    std::cout << A234324.get_full_info() << endl;
    
    A234324.setfirstname("Josh");
  
    std::cout << A234324.get_full_info() << endl;

    Student A434("Joey", "Daermann", "00430400");

    A434.print_schedule();
    A434.add_class("Math");
    A434.add_class("Science");
    A434.print_schedule();

};