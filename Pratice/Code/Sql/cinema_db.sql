#Definition of the schema fo the DB
#This is a DB for managing imformation about "cinema"

#Create the DB
DROP DATABASE IF EXISTS cinema_db;
CREATE DATABASE IF NOT EXISTS cinema_db;

#Select the database to work with
USE cinema_db;

#Create the kernel tables:director, actor and genres
CREATE TABLE IF NOT EXISTS directors(
id_director int NOT NULL AUTO_INCREMENT,
d_fname VARCHAR(35) NOT NULL,
d_sname1 VARCHAR(35) NOT NULL,
d_sname2 VARCHAR(35),
PRIMARY KEY(id_director)
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS classifications(
id_classification int NOT NULL,
c_descrip VARCHAR(35) NOT NULL,
PRIMARY KEY(id_classification)
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS languages(
id_language int NOT NULL AUTO_INCREMENT,
l_name VARCHAR (35) NOT NULL,
l_pais VARCHAR(35),
PRIMARY KEY(id_language)
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS actors(
id_actor int NOT NULL AUTO_INCREMENT,
a_fname VARCHAR(35) NOT NULL,
a_sname1 VARCHAR(35) NOT NULL,
a_sname2 VARCHAR(35),
PRIMARY KEY(id_actor)
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS genres(
id_genre INT NOT NULL AUTO_INCREMENT,
g_name VARCHAR(35) NOT NULL,
g_descrip VARCHAR(250),
PRIMARY KEY(id_genre)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS movies(
id_movie INT NOT NULL AUTO_INCREMENT,
m_name VARCHAR(35) NOT NULL,
m_year int NOT NULL,
m_sinopsis VARCHAR(250),
m_premiere BOOLEAN NOT NULL,
m_subtitle BOOLEAN NOT NULL,
m_minutos INT,
m_director INT,
m_language INT,
m_classification INT,
PRIMARY KEY(id_movie),
CONSTRAINT fkdiector FOREIGN KEY(m_director)
	REFERENCES directors(id_director)
    ON DELETE CASCADE
    ON UPDATE CASCADE,

CONSTRAINT fklanguage FOREIGN KEY(m_language)
	REFERENCES languages(id_language)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    
CONSTRAINT fkclassification FOREIGN KEY(m_classification)
	REFERENCES classifications(id_classification)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS movie_actors(
id_movie INT NOT NULL,
id_actor INT NOT NULL,
PRIMARY KEY(id_movie, id_actor),
CONSTRAINT fkmovie_act FOREIGN KEY(id_movie)
	REFERENCES movies(id_movie)
	ON DELETE CASCADE
	ON UPDATE CASCADE,
CONSTRAINT fkactor FOREIGN KEY(id_actor)
	REFERENCES actors(id_actor)
	ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS movie_genres(
id_movie INT NOT NULL,
id_genre INT NOT NULL,
PRIMARY KEY(id_movie, id_genre),
CONSTRAINT fkmovie_gen FOREIGN KEY(id_movie)
	REFERENCES movies(id_movie)
	ON DELETE CASCADE
	ON UPDATE CASCADE,
CONSTRAINT fkgenre FOREIGN KEY(id_genre)
	REFERENCES genres(id_genre)
	ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS seats(
id_seat int NOT NULL AUTO_INCREMENT,
s_row VARCHAR(2) NOT NULL,
s_col INT(2) NOT NULL,
PRIMARY KEY(id_seat)
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS halls(
id_hall int NOT NULL AUTO_INCREMENT,
h_name VARCHAR(2) NOT NULL,
h_nseat INT(2) NOT NULL,
PRIMARY KEY(id_hall)
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS services(
id_service int NOT NULL AUTO_INCREMENT,
s_name VARCHAR(35) NOT NULL,
s_descrip VARCHAR(35) NOT NULL,
PRIMARY KEY(id_service)
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS halls_services(
id_hall INT NOT NULL,
id_service INT NOT NULL,
PRIMARY KEY(id_hall, id_service),
CONSTRAINT fkhall_service FOREIGN KEY(id_hall)
	REFERENCES halls(id_hall)
	ON DELETE CASCADE
	ON UPDATE CASCADE,
CONSTRAINT fkservice_hall FOREIGN KEY(id_service)
	REFERENCES services(id_service)
	ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS shedule(
id_shedule int NOT NULL AUTO_INCREMENT,
sh_ini TIME NOT NULL,
sh_end TIME NOT NULL,
PRIMARY KEY(id_shedule)
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS movie_hall_shedule_seat(
id_projection int NOT NULL AUTO_INCREMENT,
p_fecha DATE NOT NULL,
p_hall INT NOT NULL,
p_movie int NOT NULL,
p_shedule INT NOT NULL,
p_seat INT NOT NULL,
p_flag BOOLEAN,
PRIMARY KEY(id_projection),
CONSTRAINT fkhall FOREIGN KEY(p_hall)
	REFERENCES halls(id_hall)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
CONSTRAINT fkmovie FOREIGN KEY(p_movie)
	REFERENCES movies(id_movie)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
CONSTRAINT fkshedule FOREIGN KEY(p_shedule)
	REFERENCES shedule(id_shedule)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
CONSTRAINT fkseat FOREIGN KEY(p_seat)
	REFERENCES seats(id_seat)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS tikets(
id_tiket int NOT NULL AUTO_INCREMENT,
t_proyection INT NOT NULL,
t_price INT NOT NULL,
PRIMARY KEY(id_tiket)
)ENGINE = InnoDB;
