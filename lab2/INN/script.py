import csv
import datetime

def isFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

if __name__== "__main__":
    outFile = open("INN-populate.sql", "w")
   
    #rooms
    with open('Rooms.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        
        #reads the next row
        next(reader) 

        for row in reader:
            for i in range(len(row)):
                row[i] = row[i].strip()
                if not row[i].isdigit() and not isFloat(row[i]):
                    row[i] = '\"' + row[i] + '\"'

            if len(row) > 0:
                outFile.write("INSERT INTO rooms (RoomId, RoomName, Beds, BedType, MaxOccupancy, BasePrice, Decor)\n")
                outFile.write("VALUES ("  + ', '.join(row) + ");\n\n")

    #reservations
    with open('Reservations.csv', newline='') as csvfile:
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
                outFile.write("INSERT INTO reservations (Code, Room, CheckIn, CheckOut, Rate, LastName, FirstName, Adults, Kids)\n")
                outFile.write("VALUES ("  + ', '.join(row) + ");\n\n")


    outFile.close();
