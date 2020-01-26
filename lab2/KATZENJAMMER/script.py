import csv
import datetime

def isFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

if __name__== "__main__":
    outFile = open("KATZENJAMMER-populate.sql", "w")
   
    #bands
    with open('Band.csv', newline='') as csvfile:
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
                outFile.write("INSERT INTO bands (Id, Firstname, Lastname)\n")
                outFile.write("VALUES ("  + ', '.join(row) + ");\n\n")

    #songs
    with open('Songs.csv', newline='') as csvfile:
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
                outFile.write("INSERT INTO songs (SongId, Title)\n")
                outFile.write("VALUES ("  + ', '.join(row) + ");\n\n")

    #albums
    with open('Albums.csv', newline='') as csvfile:
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
                outFile.write("INSERT INTO albums (AId, Title, Year, Label, Type)\n")
                outFile.write("VALUES ("  + ', '.join(row) + ");\n\n")

    #instruments
    with open('Instruments.csv', newline='') as csvfile:
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
                outFile.write("INSERT INTO instruments (SongId, BandmateId, Instrument)\n")
                outFile.write("VALUES ("  + ', '.join(row) + ");\n\n")

    #performance
    with open('Performance.csv', newline='') as csvfile:
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
                outFile.write("INSERT INTO performance (SongId, Bandmate, StagePosition)\n")
                outFile.write("VALUES ("  + ', '.join(row) + ");\n\n")

    #vocals
    with open('Vocals.csv', newline='') as csvfile:
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
                outFile.write("INSERT INTO vocals (SongId, Bandmate, Type)\n")
                outFile.write("VALUES ("  + ', '.join(row) + ");\n\n")

    #tracklists
    with open('Tracklists.csv', newline='') as csvfile:
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
                outFile.write("INSERT INTO tracklists (AlbumId, Position, SongId)\n")
                outFile.write("VALUES ("  + ', '.join(row) + ");\n\n")


    outFile.close();
