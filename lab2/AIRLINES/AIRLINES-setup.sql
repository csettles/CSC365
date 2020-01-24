--Airlines, Airports and Flights
DROP TABLE IF EXISTS flights;
DROP TABLE IF EXISTS airports;
DROP TABLE IF EXISTS airlines;

CREATE TABLE airlines(
   Id INTEGER NOT NULL PRIMARY KEY,
   Airline VARCHAR(100) NOT NULL,
   Abbreviation VARCHAR(100) NOT NULL,
   Country VARCHAR(100) NOT NULL
);

CREATE TABLE airports(
   City VARCHAR(50) NOT NULL,
   AirportCode VARCHAR(3) NOT NULL PRIMARY KEY,
   AirportName VARCHAR(50) NOT NULL,
   Country VARCHAR(50) NOT NULL,
   CountryAbbrev VARCHAR(10) NOT NULL
);

CREATE TABLE flights(
   Airline INTEGER NOT NULL,
   FlightNo INTEGER NOT NULL,
   SourceAirport VARCHAR(3) NOT NULL,
   DestAirport VARCHAR(3) NOT NULL,
   FOREIGN KEY (SourceAirport) REFERENCES airports(AirportCode),
   FOREIGN KEY (DestAirport) REFERENCES airports(AirportCode),
   FOREIGN KEY (Airline) REFERENCES airlines(Id),
   PRIMARY KEY (FlightNo, Airline)
);
