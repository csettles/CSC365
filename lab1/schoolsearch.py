#Caitlin Settles and Ty Farris
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
        self.teacher_first_name = teacher_first_name.strip()
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
            return f'\t{x.last_name}, {x.first_name}, {x.bus}'
        return f'\t{x.last_name}, {x.first_name}, {x.grade}, {x.classroom}, {x.teacher_last_name}, {x.teacher_first_name}'
    
    print(*(print_student(x) for x in
            filter(lambda x: x.last_name == last_name, students)), sep = '\n')

def search_teacher(students, teacher_last_name):
    print('\t', end='')
    print(*filter(lambda x: x.teacher_last_name == teacher_last_name, students), sep="\n\t")

def search_grade(students, grade, high=None):

    result = [x for x in students if x.grade == grade]

    if  len(result) != 0 and high != None and high:
        result = max(result, key=lambda x: x.gpa)
        print(f'\t{result}: {result.bus}, {result.gpa}, {result.teacher_last_name}, {result.teacher_first_name}')
    elif len(result) != 0 and high != None and not high:
        result = min(result, key=lambda x: x.gpa)
        print(f'\t{result}: {result.bus}, {result.gpa}, {result.teacher_last_name}, {result.teacher_first_name}')
    else:
        print('\t', end='')
        print(*result, sep="\n\t")

def search_bus(students, bus):
    print('\t', end='')
    print(*(f'{x}: {x.grade}, {x.classroom}' for x in filter(lambda x: x.bus == bus, students)), sep="\n\t")

def search_average(students, grade):
    average = 0.0
    try:
        average = statistics.mean(map(lambda x: x.gpa, filter(lambda x: x.grade == grade, students)))
    except statistics.StatisticsError:
        pass
    print(f'\tgrade level {grade}: {average:.3} average')

def info(students):
    print("    Grade: Number of Students")
    for i in range(7):
        print(f'\t{i}:', len(list(filter(lambda x: x.grade == i, students))))

def invalidCommand():
    options = """ 
    S[tudent]: <lastname> [B[us]]\n
    T[eacher]: <lastname>\n
    B[us]: <number>\n
    G[rade]: <number> [H[igh]|L[ow]]\n
    A[verage]: <number>\n
    I[nfo]\n
    Q[uit]
    """
    print("Invalid command. Below are the following options.\n %s" %options)

if __name__ == '__main__':
    try:
        students = parse_file('students.txt')
    except:
        exit("students.txt: unrecognized file format")

    command = [""]

    while command[0] not in ("Quit", "Q"):
        command = input("Enter a command >> ").split(" ")

        if len(command) <= 3 and command[0] in ("Student:", "S:"):
            if len(command) == 2:
                search_lastname(students, command[1])
            elif len(command) == 3 and command[2] in ("B", "Bus"):
                search_lastname(students, command[1], True)
            else:
                invalidCommand()

        elif len(command) == 2 and command[0] in ("Teacher:", "T:"):
            search_teacher(students, command[1])

        elif len(command) == 2 and command[0] in ("Bus:", "B:"):
            try:
                i = int(command[1])
            except:
                invalidCommand()
                continue

            search_bus(students, i)

        elif len(command) <= 3 and command[0] in ("Grade:", "G:"):
            try:
                i = int(command[1])
            except:
                invalidCommand()
                continue
            if len(command) == 3:
                if command[2] in ("High", "H"):
                    search_grade(students, i, True)
                elif command[2] in ("Low", "L"):
                    search_grade(students, i, False)
                else:
                    invalidCommand()
            else:
                search_grade(students, i)

        elif len(command) <= 2 and command[0] in ("Average:", "A:"):
            try:
                i = int(command[1])
            except:
                invalidCommand()
                continue
            search_average(students, i)

        elif len(command) == 1 and command[0] in ("Info", "I"):
            info(students)

        elif len(command) == 1 and command[0] in ("Quit", "Q"):
            exit()

        else:
            invalidCommand()
