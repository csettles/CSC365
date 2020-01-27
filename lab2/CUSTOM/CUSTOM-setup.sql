--teams, players and characteristics of fifa players
DROP TABLE IF EXISTS characteristics;
DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS teams;

CREATE TABLE teams(
   Id INTEGER NOT NULL PRIMARY KEY,
   TeamName VARCHAR(200) NOT NULL,
   UNIQUE (TeamName)
);

CREATE TABLE players(
   SoFifaId INTEGER NOT NULL PRIMARY KEY,
   Name VARCHAR(100) NOT NULL,
   Nationality VARCHAR(50) NOT NULL,
   Team VARCHAR(200) NOT NULL,
   TeamPosition VARCHAR(10) NOT NULL,
   FOREIGN KEY (Team) REFERENCES teams(TeamName)
);

CREATE TABLE characteristics(
   Id INTEGER NOT NULL,
   Age INTEGER NOT NULL,
   Weight INTEGER NOT NULL,
   Height INTEGER NOT NULL,
   BodyType VARCHAR(20) NOT NULL,
   BirthDate DATE NOT NULL,
   PRIMARY KEY(Age, Weight, Height, BirthDate),
   FOREIGN KEY (Id) REFERENCES players(SoFifaId)
);


