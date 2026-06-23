def is_snake_case(string):
    for ch in string:
        if not (ch.islower() or ch.isdigit() or ch == '_'):
            return False
    return True

students = {}

while True:
    line = input()

    if is_snake_case(line):
        picked_course = line
        break

    name, id, course = line.split(":")
    course = course.replace(" ", "_")
    students[name] = (id, course)

for key, value in students.items():
    id, course = value

    if course == picked_course:
        print(f"{key} - {id}")
