import re
import cowsay
import json

def validate_student_id(student_id):
    #REGEX:Ensures ID starts with STU- followed by 5 digits.
    #WHY? To prevent incorrect data entry in the database.
    pattern = r'^STU-/d{5}$'
    return bool(re.match(pattern, student_id))

def welcome_user(name):
    #Library Usage: Uses cowsay to welcome the user with a friendly message.
    #WHY? To improve user experience and make the application more engaging.
    cowsay.cow(f"Welcome to the Student Management Systen, {name}!")

def save_to_json(data, filename="data.json"):
    #File I/O and JSON: Saves data
    #WHY? To prevent data loss and allow for easy data retrieval if needed.
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

#Setup: Creates an utility library with REGEX validation and JSON support.(Workshops 7 & 8)