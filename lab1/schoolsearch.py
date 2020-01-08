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
    command = input("Enter in a command: ")
    command = command.split(" ")

    while command[0] != "Quit" and command[0] != "Q":
        if len(command) <= 3 and (command[0] == "Student" or command[0] == "S"):
            if command[2] == "B" or command[2] == "Bus":
                print("Bus")

        elif len(command) <= 2 and (command[0] == "Teacher" or command[0] == "T"):
            print("Teacher")

        elif len(command) <= 2 and (command[0] == "Bus" or command[0] == "B"):
            print("Bus")

        elif len(command) <= 3 and (command[0] == "Grade" or command[0] == "G"):
            if command[2] == "High" or command[2] == "H":
                print("High")
            if command[2] == "Low" or command[2] == "L":
                print("Low") 

        elif len(command) <= 2 and (command[0] == "Average" or command[0] == "A"):
            print("Average")

        elif len(command) == 1 and (command[0] == "Info" or command[0] == "I"):
            print("Info")

        elif len(command) == 1 and (command[0] == "Quit" or command[0] == "Q"):
            print("Quit")

        else:
            print("Invalid input. ")
        
        command = input("Enter in a command: ")
        command = command.split(" ")

    if len(command) > 1 and (command[0] != "Quit" or command[0] != "Q"):
        print("Invalid command. Restart program.")
