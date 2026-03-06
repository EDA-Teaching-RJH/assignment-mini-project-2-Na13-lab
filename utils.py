import re
import cowsay
import json

def validate_student_id(student_id):
    #REGEX:Ensures ID starts with STU- followed by 5 digits.
    #WHY? To prevent incorrect data entry in the database.
    pattern = r'^STU-/d{5}$'
    return bool(re.match(pattern, student_id))