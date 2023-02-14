DROP TABLE IF EXISTS circuits CASCADE;
DROP TABLE IF EXISTS constructors CASCADE;
DROP TABLE IF EXISTS drivers CASCADE;
DROP TABLE IF EXISTS seasons CASCADE;
DROP TABLE IF EXISTS status CASCADE;
DROP TABLE IF EXISTS constructor_results CASCADE;
DROP TABLE IF EXISTS constructor_standings CASCADE;
DROP TABLE IF EXISTS driver_standings CASCADE;
DROP TABLE IF EXISTS lap_times CASCADE;
DROP TABLE IF EXISTS pit_stops CASCADE;
DROP TABLE IF EXISTS qualifying CASCADE;
DROP TABLE IF EXISTS races CASCADE;
DROP TABLE IF EXISTS results CASCADE;
DROP TABLE IF EXISTS meta CASCADE;
DROP TABLE IF EXISTS call_constraints CASCADE;

CREATE TABLE meta(
table_name VARCHAR(100) NOT NULL,
last_call BIGINT  NOT NULL,
last_call_response INTEGER,
num_rows_pulled INTEGER,
num_rows_modified INTEGER,
next_offset INTEGER
);

CREATE TABLE call_constraints(
table_name VARCHAR(100) NOT NULL,
cooldown_period_s INTEGER NOT NULL
);

CREATE TABLE circuits(
circuitId  INTEGER NOT NULL PRIMARY KEY, 
circuitRef VARCHAR(100) NOT NULL, 
name       VARCHAR(250) NOT NULL, 
location   VARCHAR(100) NOT NULL, 
country    VARCHAR(100) NOT NULL, 
lat        DECIMAL NOT NULL, 
lng        DECIMAL NOT NULL, 
alt        INTEGER, 
url        VARCHAR(250)
);

 CREATE TABLE constructors(
constructorId  INTEGER NOT NULL PRIMARY KEY,
constructorRef VARCHAR(100) NOT NULL,
name           VARCHAR(100) NOT NULL,
nationality    VARCHAR(100),
url            VARCHAR(100)
);

CREATE TABLE drivers(
driverId    INTEGER NOT NULL PRIMARY KEY,
driverRef   VARCHAR(100) NOT NULL,
number      INTEGER,
code        VARCHAR(3),
forename    VARCHAR(100) NOT NULL,
surname     VARCHAR(100) NOT NULL,
dob         DATE NOT NULL,
nationality VARCHAR(100) NOT NULL,
url         VARCHAR(100)
);

CREATE TABLE seasons(
year INTEGER NOT NULL PRIMARY KEY,
url  VARCHAR(150)
);

CREATE TABLE status(
statusId INTEGER NOT NULL PRIMARY KEY, 
status  VARCHAR(150)
);

CREATE TABLE races(
raceId INTEGER NOT NULL PRIMARY KEY, 
year    INTEGER NOT NULL REFERENCES seasons(year), 
round  INTEGER NOT NULL, 
circuitId INTEGER NOT NULL REFERENCES circuits(circuitId), 
name VARCHAR(100) NOT NULL, 
date DATE NOT NULL, 
time TIME, 
url VARCHAR(150) NOT NULL
);


CREATE TABLE constructor_results(
constructorResultsId INTEGER NOT NULL PRIMARY KEY, 
raceId               INTEGER NOT NULL REFERENCES races(raceId), 
constructorId        INTEGER NOT NULL REFERENCES constructors(constructorId), 
points               DECIMAL NOT NULL,  
status               CHAR
);

CREATE TABLE constructor_standings(
constructorStandingsId INTEGER NOT NULL PRIMARY KEY, 
raceId                 INTEGER NOT NULL REFERENCES races(raceId), 
constructorId          INTEGER NOT NULL REFERENCES constructors(constructorId), 
points                 DECIMAL NOT NULL, 
position               INTEGER NOT NULL, 
positionText           VARCHAR(10) NOT NULL, 
wins                   INTEGER NOT NULL
);

CREATE TABLE driver_standings(
driverStandingsId INTEGER NOT NULL PRIMARY KEY, 
raceId            INTEGER NOT NULL REFERENCES races(raceId), 
driverId          INTEGER NOT NULL REFERENCES drivers(driverId), 
points            DECIMAL NOT NULL, 
position          INTEGER NOT NULL, 
positionText      VARCHAR(3) NOT NULL, 
wins              INTEGER NOT NULL
);

CREATE TABLE lap_times(
raceId       INTEGER NOT NULL REFERENCES races(raceId), 
driverId     INTEGER NOT NULL REFERENCES drivers(driverId), 
lap          INTEGER NOT NULL, 
position     INTEGER NOT NULL,
time         TIME NOT NULL, 
milliseconds INTEGER NOT NULL
);

CREATE TABLE pit_stops(
raceId       INTEGER NOT NULL REFERENCES races(raceId), 
driverId     INTEGER NOT NULL REFERENCES drivers(driverId), 
stop         INTEGER NOT NULL, 
lap          INTEGER NOT NULL, 
time         INTERVAL NOT NULL, 
duration     INTERVAL, 
milliseconds INTEGER NOT NULL
);

CREATE TABLE qualifying(
qualifyId INTEGER NOT NULL PRIMARY KEY, 
raceId    INTEGER NOT NULL REFERENCES races(raceId), 
driverId  INTEGER NOT NULL REFERENCES drivers(driverId), 
constructorId INTEGER NOT NULL REFERENCES constructors(constructorId), 
number INTEGER, 
position INTEGER NOT NULL, 
q1 TIME, 
q2 TIME, 
q3 TIME
);

CREATE TABLE results(
resultId        INTEGER NOT NULL PRIMARY KEY, 
raceId          INTEGER NOT NULL REFERENCES races(raceId), 
driverId        INTEGER NOT NULL REFERENCES drivers(driverId), 
constructorId   INTEGER NOT NULL REFERENCES constructors(constructorId), 
number          INTEGER, 
grid            INTEGER, 
position        INTEGER, 
positionText    VARCHAR(10), 
positionOrder   INTEGER, 
points          DECIMAL, 
laps            INTEGER, 
time            VARCHAR(50), 
milliseconds    INTEGER, 
fastestLap      INTEGER, 
rank            INTEGER, 
fastestlapTime  TIME, 
fastestLapSpeed DECIMAL, 
statusId        INTEGER NOT NULL REFERENCES status(statusId)
);
