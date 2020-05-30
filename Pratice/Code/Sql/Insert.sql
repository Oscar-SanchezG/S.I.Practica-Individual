#Llenado de tablas previo
use cinema_db;
#Directores
INSERT INTO directors (d_fname, d_sname1, d_sname2) VALUES ('Oscar','Perez','Sanchez');
INSERT INTO directors (d_fname, d_sname1, d_sname2) VALUES ('Carlos','Peña','Romo');
INSERT INTO directors (d_fname, d_sname1, d_sname2) VALUES ('Lucia','Ortega','Mares');
INSERT INTO directors (d_fname, d_sname1, d_sname2) VALUES ('Maria','Luna','Sanchez');
INSERT INTO directors (d_fname, d_sname1, d_sname2) VALUES ('Eduardo','Flores','Venegas');

#Clasificaciones
INSERT INTO classifications (id_classification, c_descrip) VALUES ('B15','Adolecentes');
INSERT INTO classifications (id_classification, c_descrip) VALUES ('A','Niños');
INSERT INTO classifications (id_classification, c_descrip) VALUES ('C','Adultos');
INSERT INTO classifications (id_classification, c_descrip) VALUES ('R','ContenidoSencible');
INSERT INTO classifications (id_classification, c_descrip) VALUES ('B','preadolencentes');

#Lenguajes
INSERT INTO languages (id_language, l_descrip) VALUES ('esp','español');
INSERT INTO languages (id_language, l_descrip) VALUES ('ing','ingles');
INSERT INTO languages (id_language, l_descrip) VALUES ('fran','frances');
INSERT INTO languages (id_language, l_descrip) VALUES ('esp-lat','latino');
INSERT INTO languages (id_language, l_descrip) VALUES ('fran-ca','canada');

#Actores
INSERT INTO actors (a_fname, a_sname1, a_sname2) VALUES ('Pedro','Perez','Rogriguez');
INSERT INTO actors (a_fname, a_sname1, a_sname2) VALUES ('Leonardo','Flores','Rogriguez');
INSERT INTO actors (a_fname, a_sname1, a_sname2) VALUES ('Abraham','Gallardo','Sanchez');
INSERT INTO actors (a_fname, a_sname1, a_sname2) VALUES ('Pedro', 'Perez', 'Rogriguez');
INSERT INTO actors (a_fname, a_sname1, a_sname2) VALUES ('Pedro', 'Perez', 'Rogriguez');

#Generos
INSERT INTO genres (g_name, g_descrip) VALUES ('Triller','miedo');
INSERT INTO genres (g_name, g_descrip) VALUES ('Drama','Llanto');
INSERT INTO genres (g_name, g_descrip) VALUES ('Comedia','Risas');
INSERT INTO genres (g_name, g_descrip) VALUES ('CYFY','Ciencia_ficcion');
INSERT INTO genres (g_name, g_descrip) VALUES ('Independiente','Interesante');

#salas
INSERT INTO halls (h_name, h_nseat) VALUES ('VIP', '20');
INSERT INTO halls (h_name, h_nseat) VALUES ('Normal', '30');
INSERT INTO halls (h_name, h_nseat) VALUES ('Imax', '40');
INSERT INTO halls (h_name, h_nseat) VALUES ('Premium', '15');

#Servicios
INSERT INTO services (s_name, s_descrip) VALUES ('4D', 'Servicio_4D');
INSERT INTO services (s_name, s_descrip) VALUES ('SR', 'Sonido_envolvente');
INSERT INTO services (s_name, s_descrip) VALUES ('Barra', 'Servicio_comida');
INSERT INTO services (s_name, s_descrip) VALUES ('Barra2', 'Servicio_bebida');

#Horarios
INSERT INTO shedule (sh_ini, sh_end) VALUES ('10:00','12:00');
INSERT INTO shedule (sh_ini, sh_end) VALUES ('12:00','14:00');
INSERT INTO shedule (sh_ini, sh_end) VALUES ('16:00','18:00');
INSERT INTO shedule (sh_ini, sh_end) VALUES ('18:00','20:00');
INSERT INTO shedule (sh_ini, sh_end) VALUES ('22:00','23:59');

#Admin
INSERT INTO admins (ad_fname, ad_sname1, ad_sname2, ad_pass) VALUES ('Andres', 'Cabrera', 'Munguia', '1234');
INSERT INTO admins (ad_fname, ad_sname1, ad_sname2, ad_pass) VALUES ('Ivan', 'Cantreras', 'Munguia', '1234');
INSERT INTO admins (ad_fname, ad_sname1, ad_sname2, ad_pass) VALUES ('Ulises', 'Solorzano', 'Soto', '1234');
INSERT INTO admins (ad_fname, ad_sname1, ad_sname2, ad_pass) VALUES ('Israel', 'Alvarado', 'Izquierdo', '1234');
INSERT INTO admins (ad_fname, ad_sname1, ad_sname2, ad_pass) VALUES ('Saul', 'Lopez', 'Cabrera', '1234');

#Asientos
INSERT INTO seats (s_row, s_col) VALUES ('A', '1');
INSERT INTO seats (s_row, s_col) VALUES ('A', '2');
INSERT INTO seats (s_row, s_col) VALUES ('A', '3');
INSERT INTO seats (s_row, s_col) VALUES ('A', '4');
INSERT INTO seats (s_row, s_col) VALUES ('A', '5');
INSERT INTO seats (s_row, s_col) VALUES ('A', '6');
INSERT INTO seats (s_row, s_col) VALUES ('A', '7');
INSERT INTO seats (s_row, s_col) VALUES ('A', '8');
INSERT INTO seats (s_row, s_col) VALUES ('B', '1');
INSERT INTO seats (s_row, s_col) VALUES ('B', '2');
INSERT INTO seats (s_row, s_col) VALUES ('B', '3');
INSERT INTO seats (s_row, s_col) VALUES ('B', '4');
INSERT INTO seats (s_row, s_col) VALUES ('B', '5');
INSERT INTO seats (s_row, s_col) VALUES ('B', '6');
INSERT INTO seats (s_row, s_col) VALUES ('B', '7');
INSERT INTO seats (s_row, s_col) VALUES ('B', '8');
INSERT INTO seats (s_row, s_col) VALUES ('C', '1');
INSERT INTO seats (s_row, s_col) VALUES ('C', '2');
INSERT INTO seats (s_row, s_col) VALUES ('C', '3');
INSERT INTO seats (s_row, s_col) VALUES ('C', '4');
INSERT INTO seats (s_row, s_col) VALUES ('C', '5');
INSERT INTO seats (s_row, s_col) VALUES ('C', '6');
INSERT INTO seats (s_row, s_col) VALUES ('C', '7');
INSERT INTO seats (s_row, s_col) VALUES ('C', '8');
INSERT INTO seats (s_row, s_col) VALUES ('D', '1');
INSERT INTO seats (s_row, s_col) VALUES ('D', '2');
INSERT INTO seats (s_row, s_col) VALUES ('D', '3');
INSERT INTO seats (s_row, s_col) VALUES ('D', '4');
INSERT INTO seats (s_row, s_col) VALUES ('D', '5');
INSERT INTO seats (s_row, s_col) VALUES ('D', '6');
INSERT INTO seats (s_row, s_col) VALUES ('D', '7');
INSERT INTO seats (s_row, s_col) VALUES ('D', '8');
INSERT INTO seats (s_row, s_col) VALUES ('E', '1');
INSERT INTO seats (s_row, s_col) VALUES ('E', '2');
INSERT INTO seats (s_row, s_col) VALUES ('E', '3');
INSERT INTO seats (s_row, s_col) VALUES ('E', '4');
INSERT INTO seats (s_row, s_col) VALUES ('E', '5');
INSERT INTO seats (s_row, s_col) VALUES ('E', '6');
INSERT INTO seats (s_row, s_col) VALUES ('E', '7');
INSERT INTO seats (s_row, s_col) VALUES ('E', '8');
INSERT INTO seats (s_row, s_col) VALUES ('F', '1');
INSERT INTO seats (s_row, s_col) VALUES ('F', '2');
INSERT INTO seats (s_row, s_col) VALUES ('F', '3');
INSERT INTO seats (s_row, s_col) VALUES ('F', '4');
INSERT INTO seats (s_row, s_col) VALUES ('F', '5');
INSERT INTO seats (s_row, s_col) VALUES ('F', '6');
INSERT INTO seats (s_row, s_col) VALUES ('F', '7');
INSERT INTO seats (s_row, s_col) VALUES ('F', '8');
INSERT INTO seats (s_row, s_col) VALUES ('G', '1');
INSERT INTO seats (s_row, s_col) VALUES ('G', '2');
INSERT INTO seats (s_row, s_col) VALUES ('G', '3');
INSERT INTO seats (s_row, s_col) VALUES ('G', '4');
INSERT INTO seats (s_row, s_col) VALUES ('G', '5');
INSERT INTO seats (s_row, s_col) VALUES ('G', '6');
INSERT INTO seats (s_row, s_col) VALUES ('G', '7');
INSERT INTO seats (s_row, s_col) VALUES ('G', '8');
INSERT INTO seats (s_row, s_col) VALUES ('H', '1');
INSERT INTO seats (s_row, s_col) VALUES ('H', '2');
INSERT INTO seats (s_row, s_col) VALUES ('H', '3');
INSERT INTO seats (s_row, s_col) VALUES ('H', '4');
INSERT INTO seats (s_row, s_col) VALUES ('H', '5');
INSERT INTO seats (s_row, s_col) VALUES ('H', '6');
INSERT INTO seats (s_row, s_col) VALUES ('H', '7');
INSERT INTO seats (s_row, s_col) VALUES ('H', '8');

#Peliculas
INSERT INTO movies (m_name, m_year, m_sinopsis, m_premiere, m_subtitle, m_minutos, m_director, m_language, m_classification) 
VALUES ('Piratas', '2005', 'Piratas', '1', '0', '150', '1', 'esp', 'C');
INSERT INTO movies (m_name, m_year, m_sinopsis, m_premiere, m_subtitle, m_minutos, m_director, m_language, m_classification) 
VALUES ('Piratas2', '2006', 'Piratas', '0', '1', '180', '2', 'ing', 'B15');
INSERT INTO movies (m_name, m_year, m_sinopsis, m_premiere, m_subtitle, m_minutos, m_director, m_language, m_classification) 
VALUES ('Piratas3', '2007', 'Piratas', '1', '0', '120', '1', 'ing', 'A');
INSERT INTO movies (m_name, m_year, m_sinopsis, m_premiere, m_subtitle, m_minutos, m_director, m_language, m_classification) 
VALUES ('Piratas4', '2008', 'Piratas', '0', '1', '131', '3', 'fran', 'B15');
INSERT INTO movies (m_name, m_year, m_sinopsis, m_premiere, m_subtitle, m_minutos, m_director, m_language, m_classification) 
VALUES ('RYF', '2009', 'carros', '1', '0', '150', '2', 'esp', 'C');
INSERT INTO movies (m_name, m_year, m_sinopsis, m_premiere, m_subtitle, m_minutos, m_director, m_language, m_classification) 
VALUES ('RYF2', '2010', 'carros', '0', '1', '150', '3', 'esp', 'A');
INSERT INTO movies (m_name, m_year, m_sinopsis, m_premiere, m_subtitle, m_minutos, m_director, m_language, m_classification) 
VALUES ('RYF3', '2015', 'carros', '1', '0', '150', '4', 'ing', 'B');
INSERT INTO movies (m_name, m_year, m_sinopsis, m_premiere, m_subtitle, m_minutos, m_director, m_language, m_classification) 
VALUES ('RYF4', '2019', 'carros', '0', '1', '150', '5', 'esp', 'B');

#Salas-servicios
INSERT INTO halls_services (id_hall, id_service) VALUES ('1','1' );
INSERT INTO halls_services (id_hall, id_service) VALUES ('2','1' );
INSERT INTO halls_services (id_hall, id_service) VALUES ('3','1' );
INSERT INTO halls_services (id_hall, id_service) VALUES ('4','1' );
INSERT INTO halls_services (id_hall, id_service) VALUES ('1','2' );
INSERT INTO halls_services (id_hall, id_service) VALUES ('4','2' );
INSERT INTO halls_services (id_hall, id_service) VALUES ('4','3' );

#pelicula,genero
INSERT INTO movie_genres (id_movie, id_genre) VALUES ('1', '4');
INSERT INTO movie_genres (id_movie, id_genre) VALUES ('2', '3');
INSERT INTO movie_genres (id_movie, id_genre) VALUES ('3', '2');
INSERT INTO movie_genres (id_movie, id_genre) VALUES ('4', '1');
INSERT INTO movie_genres (id_movie, id_genre) VALUES ('5', '2');
INSERT INTO movie_genres (id_movie, id_genre) VALUES ('6', '3');
INSERT INTO movie_genres (id_movie, id_genre) VALUES ('7', '4');
INSERT INTO movie_genres (id_movie, id_genre) VALUES ('8', '5');
INSERT INTO movie_genres (id_movie, id_genre) VALUES ('2', '4');
INSERT INTO movie_genres (id_movie, id_genre) VALUES ('6', '3');
INSERT INTO movie_genres (id_movie, id_genre) VALUES ('9', '2');
INSERT INTO movie_genres (id_movie, id_genre) VALUES ('4', '1');

#pelicula-actor
INSERT INTO movie_actors (id_movie, id_actor) VALUES ('1', '4');
INSERT INTO movie_actors (id_movie, id_actor) VALUES ('2', '5');
INSERT INTO movie_actors (id_movie, id_actor) VALUES ('3', '4');
INSERT INTO movie_actors (id_movie, id_actor) VALUES ('4', '3');
INSERT INTO movie_actors (id_movie, id_actor) VALUES ('5', '2');
INSERT INTO movie_actors (id_movie, id_actor) VALUES ('6', '1');
INSERT INTO movie_actors (id_movie, id_actor) VALUES ('7', '2');
INSERT INTO movie_actors (id_movie, id_actor) VALUES ('8', '3');
INSERT INTO movie_actors (id_movie, id_actor) VALUES ('9', '4');
INSERT INTO movie_actors (id_movie, id_actor) VALUES ('10', '5');





