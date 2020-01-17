#Caitlin Settles and Ty Farris
import statistics
import sys

class Student:
    def __init__(self, last_name, first_name, grade, classroom,
                 bus, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.grade = int(grade)
        self.classroom = int(classroom)
        self.bus = int(bus)
        self.gpa = float(gpa.strip())
        
        

    def __repr__(self):
        return f'{self.last_name}, {self.first_name}'

class Teacher:
    def __init(self, last_name, first_name, classroom):
        self.first_name = first_name
        self.last_name = last_name
        self.classroom = int(classroom.strip())

def parse_file(file_name):
    students = []
    with open(file_name) as f:
        for line in f:
            data = line.split(',')
            students.append(Student(*data))
    return students

#NR1
def search_classroom(class_num):
    print('\t', end='')
    print(*(x for x in filter(lambda x: x.classroom == class_num, students)), sep = "\n\t")

#NR2
def search_teacher_classroom(class_num):
    print('\t', end='')
    print(*(x for x in filter(lambda x: x.classroom == class_num, teachers)), sep = "\n\t")

#NR3
def search_teacher_grade(grade):
    print('\t', end='')
    print(*(x for x in filter(lambda x: x.grade == grade, teachers)), sep = "\n\t")

#NR4
def search_enrollments():
    for t in teachers:
        count = 0
        for s in students:
            if t.classroom == s.classroom:
                count++
    print('\t', end='')  
    print(f'\t{t.classroom}:{count}')     

#NR5
#commmand == 1 then grade level of student
#command == 2 then teacher teaching the student
#command == 3 then bus route student is on
def search_gpa_performance(command): 
    if command == 1:
        for i in range(7):
            data = map(lambda x: x.gpa, filter(lambda x: x.grade == i, students))
            analyze_gpa(data)
    if command == 2:
        classes = set(map(lambda x: x.classroom, teachers))
        for c in classes:
            data = append(map(lambda x: x.gpa, filter(lambda x: x.classroom == c, students)))
            analyze_gpa(data)
    if command == 3:
        bus = set(map(lambda x: x.bus, students))
        for b in bus:
            data = map(lambda x: x.gpa, filter(lambda x: x.bus == b, students))
            analyze_gpa(data)

def analyze_gpa(data):
    def print_gpa(mean, median, mode):
        print(f'\tmean: {mean}')
        print(f'\tmedian: {median}')
        print(f'\tmode: {mode}')

    if len(data) == 0:
        print_gpa(0, 0, 0)
    else:
        mean = statistics.mean(data)
        median = statistics.median(data)
        mode = statistics.mode(data)
        print_gpa(mean, median, mode)


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
    print("Invalid command. Below are the following options.\n %s" % options)

if __name__ == '__main__':
    try:
        students = parse_file('list.txt')
        teachers = parse_file('teachers.txt')
    except:
        exit("unrecognized file format")

    command = [""]

    while command[0] not in ("Quit", "Q"):
        query = input("")
        command = query.split("Enter in command >> ")
        if any('#' in x for x in command) or (len(command) == 1 and not command[0].strip()):
            continue
        else:
            print(query)

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
        elif len(command) == 2 and command[0] in ("Classroom", "C"):
            search_classroom(command[1])

        else:
            invalidCommand()
