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