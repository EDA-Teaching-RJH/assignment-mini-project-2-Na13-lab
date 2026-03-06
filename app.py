from utils import validate_student_id, welcome_user, save_to_json
#This imports the databse created before in the utils.py file, which contains an utility library

#BASE CLASS: The foundation for any person in the system.
class Person:
    def __init__(self, name):
        self._name = name #Protected attribute to store the name of the person.
    @property
    def name(self):
        return self._name #Getter method to access the name of the person.

#Inheritance: Student class inherits from Person, allowing us to reuse the name attribute and methods.
class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name) #Calls parents constructor 
        
        if validate_student_id(student_id):
            self.student_id = student_id
        else:
            raise ValueError("Invalid Student ID format!") 
        #Prevents the object from being created with an invalid student ID.
        #WHY? To ensure that only valid student IDs are accepted, maintaining data integrity in the system.

        self.grades = [] #List to store the grades of the students.
        def add_grade(self, grade):
            if 0 <= grade <= 100:
                self.grades.append(grade) #Adds a grade to the student's grade list. 
                #WHY? To allow for the recording of student performance in the system.
#Implementation of inheritance and getters/setters to manage student data effectively.(Workshop 9)

import matplotlib.pyplot as plt
#This imports the matplotlib library, which is used for creating visualizations such as charts and graphs.

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students =[] 
    #Manages course information and student enrollment, allowing us to keep track of which students are enrolled in which courses.
    #WHY? To organise students into courses, making it easier to track their progress and performance.
    def enroll(self, student):
        self.students.append(student)

    def plot_performance(self): #Visualises grade trends using matplotlib. #WHY? To track student progress.
        for s in self.students:
            plt.plot(s.grades, label=s.name, marker='o')
            plt.title(f"Performance in {self.course_name}")
            plt.ylabel("Grades")
            plt.legend()
            plt.show()    
if __name__ == "__main__":
    welcome_user("Instructor")
    try: 
        student_a = Student("Nuno", "STU-00001")
        student_a.add_grade(75)
        student_a.add_grade(85) #This creates a student object and adds grades to it.
        #WHY> To demonstrate the creation of a student and record their grades in the system.
        python_class = Course("Advanced Python")
        python_class.enroll(student_a) #This creates a course and enrolls the student in.
        #WHY? To organise the student into a course and save their grades to track their performance.
        save_to_json({"course": python_class.course_name, "student": student_a.name, "grades": student_a.grades})
        python_class.plot_performance() #Plots the performance of the student in the course using matplotlib. 
    except ValueError as e:
        print(f"Error:{e}") #try statements must have an except block to handle potential errors.
#This code added course class and matplotlib visualisation to track student performance.