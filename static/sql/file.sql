/* DATABASE CREATION IN COMMAND LINE 
mysql -u root
GRANT ALL PRIVILEGES ON *.* TO 'db_user'@'localhost' IDENTIFIED BY 'P@s$w0rd123!';
\q
mysql -u db_user -p
CREATE DATABASE db_name; */



/* CHUNK 1: RUN— CREATE DB AND COLUMNS */ 
CREATE TABLE LeagueSearch ( id int(11) NOT NULL AUTO_INCREMENT, 
League varchar(200) NOT NULL DEFAULT '', 
Sport varchar(50) DEFAULT NULL,
primary key (id) 
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/* CHUNK 2: RUN— ADD DATA TO COLUMNS */ 
INSERT INTO TestingDB.LeagueSearch(League, Sport, Revenue)
Values ('LaLiga', 'Soccer', '2.8 B € mil'),
('NBA', 'Basketball', '7,707 € mil'),
('NFL', 'Football', '14,077 € mil'),
('Premier League', 'Soccer', '5,864 € mil'),
('MLB', 'Baseball', '9,780 € mil'),
('NHL', 'Ice hockey', '4,570 € mil'),
('Formula One', 'Auto racing', '2,022 € mil')

/* CHUNK 3: RUN— DISPLAY TABLE*/ 
SELECT * FROM TestingDB.LeagueSearch


/* CHUNK 4: DO NOT RUN— MODIFY TABLE */ 
ALTER TABLE LeagueSearch
ADD Revenue varchar(255);

/* CHUNK 5: DO NOT RUN— DELETE DATA IN TABLE */ 
TRUNCATE TABLE LeagueSearch;

