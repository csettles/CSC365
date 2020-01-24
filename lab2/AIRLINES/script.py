import csv

if __name__== "__main__":
    outFile = open("AIRLINES-populate.sql", "w")
    
    with open('airlines.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        
        #reads the next row
        next(reader) 

        for row in reader:
            for i in range(len(row)):
                row[i] = '\'' + row[i] + '\''

            if len(row) > 0:
                outFile.write("INSERT INTO airlines (Id, Airline, Abbreviation, Country)\n")
                outFile.write("VALUES ("  + ', '.join(row) + ");\n\n")


    with open('airports100.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        
        #reads the next row
        next(reader) 

        for row in reader:
            for i in range(len(row)):
                row[i] = '\'' + row[i] + '\''

            if len(row) > 0:
                outFile.write("INSERT INTO airports (City, AirportCode, AirportName, Country, CountryAbbrev)\n")
                outFile.write("VALUES ("  + ', '.join(row) + ");\n\n")

    with open('flights.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        
        #reads the next row
        next(reader) 

        for row in reader:
            for i in range(len(row)):
                row[i] = '\'' + row[i] + '\''

            if len(row) > 0:
                outFile.write("INSERT INTO flights (Airline, FlightNo, SourceAirport, DestAirport)\n")
                outFile.write("VALUES ("  + ', '.join(row) + ");\n\n")

    outFile.close();
