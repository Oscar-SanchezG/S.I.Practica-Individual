from mysql import connector
class Model:
	"""
	*****************************************
	* A data model with MySQL for a movies DB*
	*****************************************
	"""
	def __init__(self, config_db_file='config.txt'):
		self.config_db_file = config_db_file
		self.config_db = self.read_config_db()
		self.connect_to_db()

	def read_config_db(self):
		d = {}
		with open(self.config_db_file) as f_r:
			for line in f_r:
				(key, val) = line.strip().split(':')
				d[key] = val
		return d 

	def connect_to_db(self):
		self.cnx = connector.connect(**self.config_db)
		self.cursor = self.cnx.cursor()

	def close_db(self):
		self.cnx.close()

	

	def read_all_movies_c(self):
	 	try:
	 		sql = 'SELECT * FROM movies where m_premiere = 1'
	 		self.cursor.execute(sql)
	 		records = self.cursor.fetchall()
	 		return records
	 	except connector.Error as err:
	 		return err

	"""
	********************
	* director methods *
	********************
	"""
	def create_director(self, name, sname1, sname2):
		try:
			sql = 'INSERT INTO directors (`d_fname`, `d_sname1`, `d_sname2`) VALUES (%s, %s, %s)'
			vals = (name, sname1, sname2)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def read_a_director(self, id_director):
	 	try:
	 		sql = 'SELECT * FROM directors WHERE id_director = %s'
	 		vals = (id_director,)
	 		self.cursor.execute(sql, vals)
	 		record = self.cursor.fetchone()
	 		return record
	 	except connector.Error as err:
	 		return err

	def read_all_directors(self):
	 	try:
	 		sql = 'SELECT * FROM directors'
	 		self.cursor.execute(sql)
	 		records = self.cursor.fetchall()
	 		return records
	 	except connector.Error as err:
	 		return err
	 	    	

	def update_director(self, fields, vals):
		try:
			sql = 'UPDATE directors SET '+','.join(fields)+' WHERE id_director = %s'
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True 
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def delete_director(self, id_director):
		try:
			sql = 'DELETE FROM directors WHERE id_director = %s'
			vals = (id_director,)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			count = self.cursor.rowcount
			return count
		except connector.Error as err:
			self.cnx.rollback()
			return err

	"""
	***************************
	* Classifications methods *
	***************************
	"""
	def create_classification(self, id_classification, c_descrip):
		try:
			sql = 'INSERT INTO classifications (`id_classification`, `c_descrip`) VALUES (%s, %s)'
			vals = (id_classification, c_descrip)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def read_a_classification(self, id_classification):
	 	try:
	 		sql = 'SELECT * FROM classifications WHERE id_classification = %s'
	 		vals = (id_classification,)
	 		self.cursor.execute(sql, vals)
	 		record = self.cursor.fetchone()
	 		return record
	 	except connector.Error as err:
	 		return err

	def read_all_classifications(self):
	 	try:
	 		sql = 'SELECT * FROM classifications'
	 		self.cursor.execute(sql)
	 		records = self.cursor.fetchall()
	 		return records
	 	except connector.Error as err:
	 		return err
	 	    	

	def update_classification(self, fields, vals):
		try:
			sql = 'UPDATE classifications SET '+','.join(fields)+' WHERE id_classification = %s'
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True 
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def delete_classification(self, id_classification):
		try:
			sql = 'DELETE FROM classifications WHERE id_classification = %s'
			vals = (id_classification,)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			count = self.cursor.rowcount
			return count
		except connector.Error as err:
			self.cnx.rollback()
			return err
	
	"""
	*********************
	* Languages methods *
	*********************
	"""
	def create_language(self, id_language, l_descrip):
		try:
			sql = 'INSERT INTO languages (`id_language`, `l_descrip`) VALUES (%s, %s)'
			vals = (id_language, l_descrip)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def read_a_language(self, id_language):
	 	try:
	 		sql = 'SELECT * FROM languages WHERE id_language = %s'
	 		vals = (id_language,)
	 		self.cursor.execute(sql, vals)
	 		record = self.cursor.fetchone()
	 		return record
	 	except connector.Error as err:
	 		return err

	def read_all_languages(self):
	 	try:
	 		sql = 'SELECT * FROM languages'
	 		self.cursor.execute(sql)
	 		records = self.cursor.fetchall()
	 		return records
	 	except connector.Error as err:
	 		return err
	 	    	

	def update_language(self, fields, vals):
		try:
			sql = 'UPDATE languages SET '+','.join(fields)+' WHERE id_language = %s'
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True 
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def delete_language(self, id_language):
		try:
			sql = 'DELETE FROM languages WHERE id_language = %s'
			vals = (id_language,)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			count = self.cursor.rowcount
			return count
		except connector.Error as err:
			self.cnx.rollback()
			return err
	
	"""
	******************
	* Actors methods *
	******************
	"""

	def create_actor(self, name, sname1, sname2):
		try:
			sql = 'INSERT INTO actors (`a_fname`, `a_sname1`, `a_sname2`) VALUES (%s, %s, %s)'
			vals = (name, sname1, sname2)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def read_a_actor(self, id_actor):
	 	try:
	 		sql = 'SELECT * FROM actors WHERE id_actor = %s'
	 		vals = (id_actor,)
	 		self.cursor.execute(sql, vals)
	 		record = self.cursor.fetchone()
	 		return record
	 	except connector.Error as err:
	 		return err

	def read_all_actors(self):
	 	try:
	 		sql = 'SELECT * FROM actors'
	 		self.cursor.execute(sql)
	 		records = self.cursor.fetchall()
	 		return records
	 	except connector.Error as err:
	 		return err
	 	    	     

	def update_actor(self, fields, vals):
		try:
			sql = 'UPDATE actors SET '+','.join(fields)+' WHERE id_actor = %s'
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True 
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def delete_actor(self, id_actor):
		try:
			sql = 'DELETE FROM actors WHERE id_actor = %s'
			vals = (id_actor,)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			count = self.cursor.rowcount
			return count
		except connector.Error as err:
			self.cnx.rollback()
			return err

	"""
	******************
	* Genres methods *
	******************
	"""

	def create_genre(self, name, g_descrip):
		try:
			sql = 'INSERT INTO genres (`g_name`, `g_descrip`) VALUES (%s, %s)'
			vals = (name, g_descrip)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def read_a_genre(self, id_genre):
	 	try:
	 		sql = 'SELECT * FROM genres WHERE id_genre = %s'
	 		vals = (id_genre,)
	 		self.cursor.execute(sql, vals)
	 		record = self.cursor.fetchone()
	 		return record
	 	except connector.Error as err:
	 		return err

	def read_all_genres(self):
	 	try:
	 		sql = 'SELECT * FROM genres'
	 		self.cursor.execute(sql)
	 		records = self.cursor.fetchall()
	 		return records
	 	except connector.Error as err:
	 		return err
	 	    	   

	def update_genre(self, fields, vals):
		try:
			sql = 'UPDATE genres SET '+','.join(fields)+' WHERE id_genre = %s'
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True 
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def delete_genre(self, id_genre):
		try:
			sql = 'DELETE FROM genres WHERE id_genre = %s'
			vals = (id_genre,)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			count = self.cursor.rowcount
			return count
		except connector.Error as err:
			self.cnx.rollback()
			return err

	"""
	********************
	* Halls methods *
	********************
	"""
	def create_hall(self, h_name, h_nseat):
		try:
			sql = 'INSERT INTO halls (`h_name`, `h_nseat`) VALUES (%s, %s)'
			vals = (h_name, h_nseat)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def read_a_hall(self, id_hall):
	 	try:
	 		sql = 'SELECT * FROM halls WHERE id_hall = %s'
	 		vals = (id_hall,)
	 		self.cursor.execute(sql, vals)
	 		record = self.cursor.fetchone()
	 		return record
	 	except connector.Error as err:
	 		return err

	def read_all_halls(self):
	 	try:
	 		sql = 'SELECT * FROM halls'
	 		self.cursor.execute(sql)
	 		records = self.cursor.fetchall()
	 		return records
	 	except connector.Error as err:
	 		return err
	 	    	

	def update_hall(self, fields, vals):
		try:
			sql = 'UPDATE halls SET '+','.join(fields)+' WHERE id_hall = %s'
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True 
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def delete_hall(self, id_hall):
		try:
			sql = 'DELETE FROM halls WHERE id_hall = %s'
			vals = (id_hall,)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			count = self.cursor.rowcount
			return count
		except connector.Error as err:
			self.cnx.rollback()
			return err

	"""
	*************************
	* Services-Hall methods *
	*************************
	"""
	def create_service(self, s_name, s_descrip):
		try:
			sql = 'INSERT INTO services (`s_name`, `s_descrip`) VALUES (%s, %s)'
			vals = (s_name, s_descrip)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def read_a_service(self, id_service):
	 	try:
	 		sql = 'SELECT * FROM services WHERE id_service = %s'
	 		vals = (id_service,)
	 		self.cursor.execute(sql, vals)
	 		record = self.cursor.fetchone()
	 		return record
	 	except connector.Error as err:
	 		return err

	def read_all_services(self):
	 	try:
	 		sql = 'SELECT * FROM services'
	 		self.cursor.execute(sql)
	 		records = self.cursor.fetchall()
	 		return records
	 	except connector.Error as err:
	 		return err
	 	    	

	def update_service(self, fields, vals):
		try:
			sql = 'UPDATE services SET '+','.join(fields)+' WHERE id_service = %s'
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True 
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def delete_service(self, id_service):
		try:
			sql = 'DELETE FROM services WHERE id_service = %s'
			vals = (id_service,)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			count = self.cursor.rowcount
			return count
		except connector.Error as err:
			self.cnx.rollback()
			return err

	"""
	*******************
	* shedule methods *
	*******************
	"""

	def create_shedule(self, sh_ini, sh_end):
		try:
			sql = 'INSERT INTO shedule (`sh_ini`, `sh_end`) VALUES (%s, %s)'
			vals = (sh_ini, sh_end)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def read_a_shedule(self, id_shedule):
	 	try:
	 		sql = 'SELECT * FROM shedule WHERE id_shedule = %s'
	 		vals = (id_shedule,)
	 		self.cursor.execute(sql, vals)
	 		record = self.cursor.fetchone()
	 		return record
	 	except connector.Error as err:
	 		return err

	def read_all_shedule(self):
	 	try:
	 		sql = 'SELECT * FROM shedule'
	 		self.cursor.execute(sql)
	 		records = self.cursor.fetchall()
	 		return records
	 	except connector.Error as err:
	 		return err
	 	    	   

	def update_shedule(self, fields, vals):
		try:
			sql = 'UPDATE shedule SET '+','.join(fields)+' WHERE id_shedule = %s'
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True 
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def delete_shedule(self, id_shedule):
		try:
			sql = 'DELETE FROM shedule WHERE id_shedule = %s'
			vals = (id_shedule,)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			count = self.cursor.rowcount
			return count
		except connector.Error as err:
			self.cnx.rollback()
			return err

	"""
	************************
	* Administrator methods*
	************************
	"""
	def create_admin(self, ad_fname, ad_sname1, ad_sname2, ad_pass):
		try:
			sql = 'INSERT INTO admins (`ad_fname`, `ad_sname1`, `ad_sname2`, `ad_pass`) VALUES (%s, %s, %s, %s)'
			vals = (ad_fname, ad_sname1, ad_sname2, ad_pass)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def read_a_admin(self, id_admin):
	 	try:
	 		sql = 'SELECT * FROM admins WHERE id_admin = %s'
	 		vals = (id_admin,)
	 		self.cursor.execute(sql, vals)
	 		record = self.cursor.fetchone()
	 		return record
	 	except connector.Error as err:
	 		return err

	def read_all_admins(self):
	 	try:
	 		sql = 'SELECT * FROM admins'
	 		self.cursor.execute(sql)
	 		records = self.cursor.fetchall()
	 		return records
	 	except connector.Error as err:
	 		return err
	 	    	

	def update_admin(self, fields, vals):
		try:
			sql = 'UPDATE admins SET '+','.join(fields)+' WHERE id_admin = %s'
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True 
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def delete_admin(self, id_admin):
		try:
			sql = 'DELETE FROM admins WHERE id_admin = %s'
			vals = (id_admin,)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			count = self.cursor.rowcount
			return count
		except connector.Error as err:
			self.cnx.rollback()
			return err

	"""
	****************
	* Movie methods*
	****************
	"""
	def create_movie(self, m_name, m_year, m_sinopsis, m_premiere, m_subtitle, m_minutos, m_director, m_language, m_classification):
		try:
			sql = 'INSERT INTO movies (`m_name`, `m_year`, `m_sinopsis`, `m_premiere`, `m_subtitle`, `m_minutos`, `m_director`, `m_language`, `m_classification`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
			vals = (m_name, m_year, m_sinopsis, m_premiere, m_subtitle, m_minutos, m_director, m_language, m_classification)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def read_a_movie(self, id_movie):
	 	try:
	 		sql = 'SELECT * FROM movies WHERE id_movie = %s'
	 		vals = (id_movie,)
	 		self.cursor.execute(sql, vals)
	 		record = self.cursor.fetchone()
	 		return record
	 	except connector.Error as err:
	 		return err

	def read_all_movies(self):
	 	try:
	 		sql = 'SELECT * FROM movies'
	 		self.cursor.execute(sql)
	 		records = self.cursor.fetchall()
	 		return records
	 	except connector.Error as err:
	 		return err
	 	    	

	def update_movie(self, fields, vals):
		try:
			sql = 'UPDATE movies SET '+','.join(fields)+' WHERE id_movie = %s'
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True 
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def delete_movie(self, id_movie):
		try:
			sql = 'DELETE FROM movie WHERE id_movie = %s'
			vals = (id_movie,)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			count = self.cursor.rowcount
			return count
		except connector.Error as err:
			self.cnx.rollback()
			return err

	"""
	************************
	* Hall-services methods*
	************************
	"""

	def create_hall_service(self, id_hall, id_service):
		try:
			sql = 'INSERT INTO halls_services (`id_hall`, `id_service`) VALUES (%s, %s)'
			vals = (id_hall, id_service)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def read_all_halls_services(self):
	 	try:
	 		sql = 'SELECT * FROM halls_services'
	 		self.cursor.execute(sql)
	 		records = self.cursor.fetchall()
	 		return records
	 	except connector.Error as err:
	 		return err

	"""
	************************
	* movie-actors methods*
	************************
	"""

	def create_movie_actor(self, id_hall, id_service):
		try:
			sql = 'INSERT INTO movie_actors (`id_movie`, `id_actor`) VALUES (%s, %s)'
			vals = (id_hall, id_service)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def read_all_movies_actors(self):
	 	try:
	 		sql = 'SELECT * FROM movie_actors'
	 		self.cursor.execute(sql)
	 		records = self.cursor.fetchall()
	 		return records
	 	except connector.Error as err:
	 		return err

	"""
	************************
	* movie-genres methods*
	************************
	"""

	def create_movie_genre(self, id_movie, id_genre):
		try:
			sql = 'INSERT INTO movie_genres (`id_movie`, `id_genre`) VALUES (%s, %s)'
			vals = (id_movie, id_genre)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def read_all_movies_genres(self):
	 	try:
	 		sql = 'SELECT * FROM movie_genres'
	 		self.cursor.execute(sql)
	 		records = self.cursor.fetchall()
	 		return records
	 	except connector.Error as err:
	 		return err

	def read_a_pass(self,id_admin, ad_pass):
		try:
	 		sql = 'SELECT * FROM admins WHERE id_admin=%s and ad_pass = %s'
	 		vals = (id_admin, ad_pass)
	 		self.cursor.execute(sql, vals)
	 		record = self.cursor.fetchone()
	 		return record
		except connector.Error as err:
	 		return err		

	"""
	***********************
	* Actors Projections *
	***********************
	"""

	def create_projection(self, p_fecha, p_hall, p_movie, p_shedule, p_seat, p_flag):
		try:
			sql = 'INSERT INTO movie_hall_shedule_seat (`p_fecha`, `p_hall`, `p_movie`, `p_shedule`, `p_seat`, `p_flag`) VALUES (%s, %s, %s, %s, %s, %s)'
			vals = (p_fecha, p_hall, p_movie, p_shedule, p_seat, p_flag)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def read_a_projection(self, id_projection):
	 	try:
	 		sql = 'SELECT * FROM movie_hall_shedule_seat WHERE id_projection = %s'
	 		vals = (id_projection,)
	 		self.cursor.execute(sql, vals)
	 		record = self.cursor.fetchone()
	 		return record
	 	except connector.Error as err:
	 		return err

	def read_all_projections(self):
	 	try:
	 		sql = 'SELECT * FROM movie_hall_shedule_seat'
	 		self.cursor.execute(sql)
	 		records = self.cursor.fetchall()
	 		return records
	 	except connector.Error as err:
	 		return err
	 	    	     

	def update_projection(self, fields, vals):
		try:
			sql = 'UPDATE movie_hall_shedule_seat SET '+','.join(fields)+' WHERE id_projection = %s'
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True 
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def delete_projection(self, id_projection):
		try:
			sql = 'DELETE FROM movie_hall_shedule_seat WHERE id_projection = %s'
			vals = (id_projection,)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			count = self.cursor.rowcount
			return count
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def create_projection_for_day(self, p_fecha, p_hall, p_movie, p_shedule, p_seat, p_flag):
		try:
			sql = 'INSERT INTO movie_hall_shedule_seat (`p_fecha`, `p_hall`, `p_movie`, `p_shedule`, `p_seat`, `p_flag`) VALUES (%s, %s, %s, %s, %s, %s)'
			vals = (p_fecha, p_hall, p_movie, p_shedule, p_seat, p_flag)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def read_seats_hall(self, id_hall):
		try:
			sql = 'SELECT * FROM halls WHERE id_hall = %s'
			vals = (id_hall,)
			self.cursor.execute(sql, vals)
			record = self.cursor.fetchone()
			return record
		except connector.Error as err:
			return err

	"""
	*******************
	* tikets methods *
	*******************
	"""

	def create_tiket(self, t_projection, t_price):
		try:
			sql = 'INSERT INTO tikets (`t_projection`, `t_price`) VALUES (%s, %s)'
			vals = (t_projection, t_price)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def read_a_tikets(self, id_tiket):
	 	try:
	 		sql = 'SELECT * FROM tikets WHERE id_tiket = %s'
	 		vals = (id_tiket,)
	 		self.cursor.execute(sql, vals)
	 		record = self.cursor.fetchone()
	 		return record
	 	except connector.Error as err:
	 		return err

	def read_all_tikets(self):
	 	try:
	 		sql = 'SELECT * FROM tikets'
	 		self.cursor.execute(sql)
	 		records = self.cursor.fetchall()
	 		return records
	 	except connector.Error as err:
	 		return err
	 	    	   

	def update_tiket(self, fields, vals):
		try:
			sql = 'UPDATE tikets SET '+','.join(fields)+' WHERE id_tiket = %s'
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			return True 
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def delete_tiket(self, id_tiket):
		try:
			sql = 'DELETE FROM tikets WHERE id_tiket = %s'
			vals = (id_tiket,)
			self.cursor.execute(sql, vals)
			self.cnx.commit()
			count = self.cursor.rowcount
			return count
		except connector.Error as err:
			self.cnx.rollback()
			return err

	def read_movies_fecha(self, fecha):
		try:
			sql = ('SELECT MOVIE.m_name,MHSS.p_fecha,SHEDULE.sh_ini,SHEDULE.sh_end FROM movie_hall_shedule_seat MHSS LEFT JOIN movies MOVIE ON MHSS.P_movie = MOVIE.id_movie LEFT JOIN shedule SHEDULE ON MHSS.p_shedule = SHEDULE.id_sheduleWHERE MHSS.p_fecha >= %s ')
			vals = (fecha,)
			self.cursor.execute(sql, vals)
			records = self.cursor.fetchall()
			return records
		except connector.Error as err:
			return err       
	
	def read_movies_hora(self, hora):
		try:
			sql = ('SELECT MOVIE.m_name,MHSS.p_fecha,SHEDULE.sh_ini,SHEDULE.sh_end FROM movie_hall_shedule_seat MHSS LEFT JOIN movies MOVIE ON MHSS.P_movie = MOVIE.id_movie LEFT JOIN shedule SHEDULE ON MHSS.p_shedule = SHEDULE.id_shedule WHERE SHEDULE.sh_ini >= 20:07:00 %s ')
			vals = (hora,)
			self.cursor.execute(sql, vals)
			records = self.cursor.fetchall()
			return records
		except connector.Error as err:
			return err    