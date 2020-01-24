--albumss, band, instruments, performance, songs, tracklists, vocals
DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS bands;
DROP TABLE IF EXISTS instruments;
DROP TABLE IF EXISTS performance;
DROP TABLE IF EXISTS songs;
DROP TABLE IF EXISTS tracklists;
DROP TABLE IF EXISTS vocals;

CREATE TABLE albums(
   AId INTEGER NOT NULL PRIMARY KEY,
   Title VARCHAR(50) NOT NULL,
   Year INTEGER NOT NULL,
   Label VARCHAR(50) NOT NULL
);

CREATE TABLE bands(
   Id INTEGER NOT NULL PRIMARY KEY,
   Firstname VARCHAR(20) NOT NULL,
   Lastname VARCHAR(20) NOT NULL
);

CREATE TABLE instruments(
   SongId INTEGER NOT NULL,  
   BandmateId INTEGER NOT NULL,
   Instrument VARCHAR(20) NOT NULL
);

CREATE TABLE performance(
   SongId INTEGER NOT NULL,
   BandmateId INTEGER NOT NULL,
   StagePosition VARCHAR(15)
);

CREATE TABLE songs(
   SongId INTEGER NOT NULL PRIMARY KEY,
   Title VARCHAR(50), NOT NULL
);

CREATE TABLE tracklists(
   AlbumId INTEGER NOT NULL,
   Position INTEGER NOT NULL,
   SongId INTEGER NOT NULL
);

CREATE TABLE vocals(
   SongId INTEGER NOT NULL,
   Bandmate INTEGER NOT NULL,
   Type VARCHAR(15) NOT NULL
);
