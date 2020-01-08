import statistics

class Student:
    def __init__(self, last_name, first_name, grade, classroom,
                 bus, gpa, teacher_last_name, teacher_first_name):
        self.first_name = first_name
        self.last_name = last_name
        self.grade = int(grade)
        self.gpa = float(gpa)
        self.classroom = int(classroom)
        self.bus = int(bus)
        self.teacher_first_name = teacher_first_name
        self.teacher_last_name = teacher_last_name

    def __repr__(self):
        return f'{self.last_name}, {self.first_name}'

def parse_file(file_name):
    students = []
    with open(file_name) as f:
        for line in f:
            data = line.split(',')
            students.append(Student(*data))
    return students

def search_lastname(students, last_name, bus=False):
    def print_student(x):
        if bus:
            return f'\t{x.last_name}, {x.first_name}: BUS {x.bus}'
        return f'\t{x.last_name}, {x.first_name}'
    
    print(*(print_student(x) for x in
            filter(lambda x: x.last_name == last_name, students)), sep = '\n')

def search_teacher(students, teacher_last_name):
    print('', *filter(lambda x: x.teacher_last_name == teacher_last_name, students), sep="\n\t")

def search_grade(students, grade, high=None):
    result = filter(lambda x: x.grade == grade, students)
    if high != None and high:
        result = max(result, key=lambda x: x.gpa)
        print(f'\n\t{result}: gpa={result.gpa} teacher={result.teacher_last_name}, {result.teacher_first_name}')
    elif high != None and not high:
        result = min(result, key=lambda x: x.gpa)
        print(f'\n\t{result}: gpa={result.gpa} teacher={result.teacher_last_name}, {result.teacher_first_name}')
    else:
        print('', *result, sep="\n\t")

def search_bus(students, bus):
    print('', *(f'{x}: grade={x.grade} classroom={x.classroom}' for x in filter(lambda x: x.bus == bus, students)), sep="\n\t")

def search_average(students, grade):
    average = 0.0
    try:
        average = statistics.mean(map(lambda x: x.gpa, filter(lambda x: x.grade == grade, students)))
    except statistics.StatisticsError:
        pass
    print(f'\tgrade level {grade}: {average:.3} average')

def info(students):
    for i in range(7):
        print(f'\t{i}:', len(list(filter(lambda x: x.grade == i, students))))

if __name__ == '__main__':
    try:
        students = parse_file('students.txt')
    except:
        exit("students.txt: unrecognized file format")

    command = ""

    while command[0] != "Quit" and command[0] != "Q":
        command = input("Enter in a command: ").split(" ")

        if len(command) <= 3 and (command[0] == "Student" or command[0] == "S"):
            if command[2] == "B" or command[2] == "Bus":
                search_lastname(command[1], True)
            else:
                search_lastname(command[1])

        elif len(command) <= 2 and (command[0] == "Teacher" or command[0] == "T"):
            search_teacher(students, command[1])

        elif len(command) <= 2 and (command[0] == "Bus:" or command[0] == "B:"):
            try:
                i = int(command[1])
            except:
                continue

            search_bus(students, i)

        elif len(command) <= 3 and (command[0] == "Grade" or command[0] == "G"):
            try:
                i = int(command[1])
            except:
                continue

            if command[2] == "High" or command[2] == "H":
                search_grade(students, i, True)
            if command[2] == "Low" or command[2] == "L":
                search_grade(students, i, False)

        elif len(command) <= 2 and (command[0] == "Average" or command[0] == "A"):
            try:
                i = int(command[1])
            except:
                continue
            search_average(students, i)

        elif len(command) == 1 and (command[0] == "Info" or command[0] == "I"):
            info(students)

        elif len(command) == 1 and (command[0] == "Quit" or command[0] == "Q"):
            exit()

        else:
            print("Invalid input. ")

    if len(command) > 1 and (command[0] != "Quit" or command[0] != "Q"):
        print("Invalid command. Restart program.")
