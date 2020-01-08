class Student:
    def __init__(self, first_name, last_name, grade, classroom,
                 bus, gpa, teacher_first_name, teacher_last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.grade = int(grade)
        self.gpa = gpa
        self.classroom = int(classroom)
        self.bus = int(bus)
        self.teacher_first_name = teacher_first_name
        self.teacher_last_name = teacher_last_name

def parse_file(file_name):
    students = []
    with open(file_name) as f:
        for line in f:
            data = line.split(',')
            students.append(Student(*data))

if __name__ == '__main__':
    parse_file('students.txt')