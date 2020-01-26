import csv
import datetime

def isFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

if __name__== "__main__":
    outFile = open("CUSTOM-populate.sql", "w")
   
    #teams
    with open('Teams.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        
        #reads the next row
        next(reader) 

        for row in reader:
            for i in range(len(row)):
                row[i] = row[i].strip()
                if not row[i].isdigit() and not isFloat(row[i]):
                    try:
                        row[i] = '\"' + datetime.datetime.strptime(row[i], "%d-%b-%y").strftime("%Y-%m-%d") + '\"'
                    except:
                        row[i] = '\"' + row[i] + '\"'

            if len(row) > 0:
                outFile.write("INSERT INTO teams (Id, TeamName)\n")
                outFile.write("VALUES ("  + ', '.join(row) + ");\n\n")

    #players
    with open('Players.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        
        #reads the next row
        next(reader) 

        for row in reader:
            for i in range(len(row)):
                row[i] = row[i].strip()
                if not row[i].isdigit() and not isFloat(row[i]):
                    try:
                        row[i] = '\"' + datetime.datetime.strptime(row[i], "%d-%b-%y").strftime("%Y-%m-%d") + '\"'
                    except:
                        row[i] = '\"' + row[i] + '\"'

            if len(row) > 0:
                outFile.write("INSERT INTO players (SoFifaId, Name, Nationality, Team, TeamPosition)\n")
                outFile.write("VALUES ("  + ', '.join(row) + ");\n\n")

    #characteristics
    with open('Characteristics.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        
        #reads the next row
        next(reader) 

        for row in reader:
            for i in range(len(row)):
                row[i] = row[i].strip()
                if not row[i].isdigit() and not isFloat(row[i]):
                    try:
                        row[i] = '\"' + datetime.datetime.strptime(row[i], "%m/%d/%y").strftime("%Y-%m-%d") + '\"'
                    except:
                        row[i] = '\"' + row[i] + '\"'

            if len(row) > 0:
                outFile.write("INSERT INTO characteristics (Id, Age, Weight, Height, BodyType, BirthDate)\n")
                outFile.write("VALUES ("  + ', '.join(row) + ");\n\n")

    outFile.close();
