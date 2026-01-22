import json
def save_student(student_list):
    with open("studentRecordsManager.json", "w") as file:
        json.dump(student_list, file, indent = 2)
def load_students():
    try:
        with open("studentRecordsManager.json", "r") as file:
            students = json.load(file)
            return students
    except FileNotFoundError:
        return []
students = [
    {"name": "Riya", "grade": "A", "age": 20},
    {"name": "John", "grade": "B", "age": 21}
]
save_student(students)              
loaded_students = load_students()
print(loaded_students)
