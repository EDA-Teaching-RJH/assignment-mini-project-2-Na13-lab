from utils import validate_student_id, welcome_user, save_to_json
#This imports the databse created before in the utils.py file, which contains an utility library

#BASE CLASS: The foundation for any person in the system.
class Person:
    def __init__(self, name):
        self._name = name #Protected attribute to store the name of the person.
    @property
    def name(self):
        return self._name #Getter method to access the name of the person.
