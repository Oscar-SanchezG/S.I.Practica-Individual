from model.model import Model 
from view.view import View 


class Controller:
	"""
	********************************
	* A controller for a Cinema DB *
	********************************
	"""
	def __init__(self):
		self.model = Model()
		self.view = View()
	

	def start(self):
		#self.view.start()
		#self.main_menu()

		self.view.start()
		self.view.ask('Una aventura te espera: ')
		id_admin = input()
		self.view.ask('Pass:')
		ad_pass = input()
		adpass=self.model.read_a_pass(id_admin,ad_pass)
		if type(adpass) == tuple:
			self.view.show_a_admin(adpass)

			self.main_menu()
		else:
			self.client_menu()
		
			
			
		

	


	"""
	***********************
	* General controllers *
	***********************
	"""
	def client_menu(self):
		o = '0'
		while o != '10':
			self.view.main_client()
			self.view.option('10')
			o = input()
			if o == '1':
				self.estrenos_menu()
			elif o == '2':
				self.genres_menu()
			elif o == '3':
				self.read_all_movies()
			elif o == '4':
				self.read_fecha_menu()
			elif o == '5':
				self.read_fecha_hora()
			elif o == '6':
				self.halls_menu()
			elif o == '7':
				self.services_menu()
			elif o == '8':
				self.create_tiket()
			elif o == '9':
				self.create_projection()
			elif o == '10':
				self.view.end()
			else:
				self.view.not_valid_option()
		return

	def estrenos_menu(self):
		movies = self.model.read_all_movies_c()
		if type(movies) == list:
			self.view.show_movie_header('  Todas las peliculas  ')
			for movie in movies:
				self.view.show_a_movie(movie)
			self.view.show_movie_midder()
			self.view.show_movie_footer()
		else:
			self.view.error('PROBLEMA AL LEER LAS PELICULAS. REVISA.')
		return

	def read_fecha_menu(self):
		self.view.ask('Fecha:')
		fecha = input()
		movies = self.model.read_movies_fecha(fecha)
		if type(movies) == list:
			self.view.show_movie_header(' PELICULA de '+year+' ')
			for movie in movies:
				self.view.show_a_movie(movie)
			self.view.show_movie_midder()
			self.view.show_movie_footer()
		else:
			self.view.error('PROBLEMA al LEER LAS PELICULAS. REVISA.')
		return

	def read_fecha_hora(self):
		self.view.ask('hora:')
		hora= input()
		movies = self.model.read_movies_hora(hora)
		if type(movies) == list:
			self.view.show_movie_header(' PELICULA de '+year+' ')
			for movie in movies:
				self.view.show_a_movie(movie)
			self.view.show_movie_midder()
			self.view.show_movie_footer()
		else:
			self.view.error('PROBLEMA al LEER LAS PELICULAS. REVISA.')
		return




	def main_menu(self):
		o = '0'
		while o != '13':
			self.view.main_menu()
			self.view.option('13')
			o = input()
			if o == '1':
				self.directors_menu()
			elif o == '2':
				self.classifications_menu()
			elif o == '3':
				self.languages_menu()
			elif o == '4':
				self.actors_menu()
			elif o == '5':
				self.genres_menu()
			elif o == '6':
				self.halls_menu()
			elif o == '7':
				self.services_menu()
			elif o == '8':
				self.shedule_menu()
			elif o == '9':
				self.movies_menu()
			elif o == '10':
				self.projections_menu()
			elif o == '11':
				self.tikets_menu()
			elif o == '12':
				self.admins_menu()
			elif o == '13':
				self.view.end()
			else:
				self.view.not_valid_option()
		return

	def update_lists(self, fs, vs):
		fields = []
		vals = []
		for f,v in zip(fs,vs):
			if v!= '':
				fields.append(f+' = %s')
				vals.append(v)
		return fields,vals

	"""
	*****************************
	* Controllers for directors *
	*****************************
	"""
	def directors_menu(self):
		o = '0'
		while o != '5':
			self.view.directors_menu()
			self.view.option('5')
			o = input()
			if o == '1':
				self.create_director()
			elif o == '2':
				self.read_all_directors()
			elif o == '3':
				self.update_director()
			elif o == '4':
				self.delete_director()
			elif o == '5':
				return
			else:
				self.view.not_valid_option()
		return

	def ask_director(self):
		self.view.ask('Nombre: ')
		name = input()
		self.view.ask('A.Paterno: ')
		sname1 = input()
		self.view.ask('A.Materno: ')
		sname2 = input()
		
		return[name, sname1, sname2]

	def create_director(self):
		name, sname1, sname2 = self.ask_director()
		out = self.model.create_director(name, sname1, sname2)
		if out == True:
			self.view.ok(name+' '+sname1, 'agrego')
		else:
			self.view.error('No se pudo agregar Director. REVISA')
		return

	def read_all_directors(self):
		directors = self.model.read_all_directors()
		if type(directors) == list:
			self.view.show_director_header('  Todos los Directores  ')
			for director in directors:
				self.view.show_a_director(director)
			self.view.show_director_midder()
			self.view.show_director_footer()
		else:
			self.view.error('PROBLEMA AL LEER LOS DIRECTORES. REVISA.')
		return


	def update_director(self):
		self.view.ask('ID del Director a modificar: ')
		id_director = input()
		director = self.model.read_a_director(id_director)
		if type(director) == tuple:
			self.view.show_director_header('Datos del Director'+id_director+' ')
			self.view.show_a_director(director)
			self.view.show_director_midder()
			self.view.show_director_footer()
		else:
			if director == None:
				self.view.error('El Director no existe')
			else:
				self.view.error('Problemas al leer el Director, REVISA')
			return
		self.view.msg('Ingresa los valores a modificar:(vacio para dejarlo igual)')
		whole_vals = self.ask_director()
		fields, vals = self.update_lists(['d_fname','d_sname1','d_sname2',], whole_vals)
		vals.append(id_director)
		vals = tuple(vals)
		out = self.model.update_director(fields, vals)
		if out == True:
			self.view.ok(id_director, 'actualizo')
		else:
			self.view.error('No se pudo actualizar el DIRECTOR. REVISA')
		return

	def delete_director(self):
		self.view.ask('ID_Director a borrar: ')
		id_director = input()
		count = self.model.delete_director(id_director)
		if count !=0:
			self.view.ok(id_director, 'borro')
		else:
			if count == 0:
				self.view.error('El Director no existe')
			else:
				self.view.error('Problemas al leer el Director. REVISA')
		return

	"""
	**********************************
	* Controllers for Classification *
	**********************************
	"""
	def classifications_menu(self):
		o = '0'
		while o != '5':
			self.view.classifications_menu()
			self.view.option('5')
			o = input()
			if o == '1':
				self.create_clasification()
			elif o == '2':
				self.read_all_classifications()
			elif o == '3':
				self.update_clasification()
			elif o == '4':
				self.delete_clasification()
			elif o == '5':
				return
			else:
				self.view.not_valid_option()
		return

	def ask_clasification(self):
		self.view.ask('ID: ')
		id_classification = input()
		self.view.ask('Descripcion: ')
		c_descrip = input()
		return[id_classification, c_descrip]

	def create_clasification(self):
		id_classification, c_descrip = self.ask_clasification()
		out = self.model.create_classification(id_classification, c_descrip)
		if out == True:
			self.view.ok(id_classification+' '+c_descrip, 'agrego')
		else:
			self.view.error('No se pudo agregar la clasificacion. REVISA')
		return

	def read_all_classifications(self):
		classitications = self.model.read_all_classifications()
		if type(classitications) == list:
			self.view.show_classification_header('  Todos las clasificaciones  ')
			for classification in classitications:
				self.view.show_a_classification(classification)
			self.view.show_classification_midder()
			self.view.show_classification_footer()
		else:
			self.view.error('Problema al leer las clasificaciones. REVISA.')
		return


	def update_clasification(self):
		self.view.ask('ID de la clasificacion a modificar: ')
		id_classification = input()
		classification = self.model.read_a_classification(id_classification)
		if type(classification) == tuple:
			self.view.show_classification_header('Datos de la clasificacion'+id_classification+' ')
			self.view.show_a_classification(classification)
			self.view.show_classification_midder()
			self.view.show_classification_footer()
		else:
			if classification == None:
				self.view.error('La clasificacion no existe')
			else:
				self.view.error('Problemas al leer la clasificacion, REVISA')
			return
		self.view.msg('Ingresa los valores a modificar:(vacio para dejarlo igual)')
		whole_vals = self.ask_clasification()
		fields, vals = self.update_lists(['id_classification','c_descrip'], whole_vals)
		vals.append(id_classification)
		vals = tuple(vals)
		out = self.model.update_classification(fields, vals)
		if out == True:
			self.view.ok(id_classification, 'actualizo')
		else:
			self.view.error('No se pudo actualizar la clasificacion. REVISA')
		return

	def delete_clasification(self):
		self.view.ask('Id_classificacion a borrar: ')
		id_classification = input()
		count = self.model.delete_classification(id_classification)
		if count !=0:
			self.view.ok(id_classification, 'borro')
		else:
			if count == 0:
				self.view.error('La clasidicacion no existe')
			else:
				self.view.error('Problemas al las clasificaciones. REVISA')
		return

	"""
	**********************************
	* Controllers for Languages *
	**********************************
	"""
	def languages_menu(self):
		o = '0'
		while o != '5':
			self.view.languages_menu()
			self.view.option('5')
			o = input()
			if o == '1':
				self.create_language()
			elif o == '2':
				self.read_all_languages()
			elif o == '3':
				self.update_language()
			elif o == '4':
				self.delete_language()
			elif o == '5':
				return
			else:
				self.view.not_valid_option()
		return

	def ask_language(self):
		self.view.ask('ID: ')
		id_language = input()
		self.view.ask('Descripcion: ')
		l_descrip = input()
		return[id_language, l_descrip]

	def create_language(self):
		id_language, l_descrip = self.ask_language()
		out = self.model.create_language(id_language, l_descrip)
		if out == True:
			self.view.ok(id_language+' '+l_descrip, 'agrego')
		else:
			self.view.error('No se pudo agregar el lenguaje. REVISA')
		return

	def read_all_languages(self):
		languages = self.model.read_all_languages()
		if type(languages) == list:
			self.view.show_language_header('  Todos los lenguajes  ')
			for language in languages:
				self.view.show_a_language(language)
			self.view.show_language_midder()
			self.view.show_language_footer()
		else:
			self.view.error('Problema al leer los lenguajes. REVISA.')
		return


	def update_language(self):
		self.view.ask('ID del lenguaje a modificar: ')
		id_language = input()
		language = self.model.read_a_language(id_language)
		if type(language) == tuple:
			self.view.show_language_header('Datos del lenguaje'+id_language+' ')
			self.view.show_a_language(language)
			self.view.show_language_midder()
			self.view.show_language_footer()
		else:
			if language == None:
				self.view.error('El lenguaje no existe')
			else:
				self.view.error('Problemas al leer el lenguaje, REVISA')
			return
		self.view.msg('Ingresa los valores a modificar:(vacio para dejarlo igual)')
		whole_vals = self.ask_language()
		fields, vals = self.update_lists(['id_language','l_descrip'], whole_vals)
		vals.append(id_language)
		vals = tuple(vals)
		out = self.model.update_language(fields, vals)
		if out == True:
			self.view.ok(id_language, 'actualizo')
		else:
			self.view.error('No se pudo actualizar el lenguaje. REVISA')
		return

	def delete_language(self):
		self.view.ask('Id_lenguaje a borrar: ')
		id_language = input()
		count = self.model.delete_language(id_language)
		if count !=0:
			self.view.ok(id_language, 'borro')
		else:
			if count == 0:
				self.view.error('El lenguaje no existe')
			else:
				self.view.error('Problemas al los lenguajes. REVISA')
		return

	"""
	**************************
	* Controllers for actors *
	**************************
	"""
	def actors_menu(self):
		o = '0'
		while o != '5':
			self.view.actors_menu()
			self.view.option('5')
			o = input()
			if o == '1':
				self.create_actor()
			elif o == '2':
				self.read_all_actors()
			elif o == '3':
				self.update_actor()
			elif o == '4':
				self.delete_actor()
			elif o == '5':
				return
			else:
				self.view.not_valid_option()
		return

	def ask_actor(self):
		self.view.ask('Nombre: ')
		name = input()
		self.view.ask('A.Paterno: ')
		sname1 = input()
		self.view.ask('A.Materno: ')
		sname2 = input()
		return[name, sname1, sname2]

	def create_actor(self):
		name, sname1, sname2 = self.ask_actor()
		out = self.model.create_actor(name, sname1, sname2)
		if out == True:
			self.view.ok(name+' '+sname1, 'agrego')
		else:
			self.view.error('No se pudo agregar el actor. REVISA')
		return

	def read_a_actor(self):
		self.view.ask('ID_Actor: ')
		id_actor = input()
		actor = self.model.read_a_actor(id_actor)
		if type(actor) == tuple:
			self.view.show_actor_header('  Datos del Director '+id_actor+' ')
			self.view.show_a_actor(actor)
			self.view.show_actor_midder()
			self.view.show_actor_footer()
		else:
			if actor == None:
				self.view.error('EL ACTOR NO EXISTE')
			else:
				self.view.error('PROBLEMA AL LEER ACTOR. REVISA.')
		return

	def read_all_actors(self):
		actors = self.model.read_all_actors()
		if type(actors) == list:
			self.view.show_actor_header('  Todos los Actores  ')
			for actor in actors:
				self.view.show_a_actor(actor)
			self.view.show_actor_midder()
			self.view.show_actor_footer()
		else:
			self.view.error('PROBLEMA AL LEER LOS ACTORES. REVISA.')
		return

	def update_actor(self):
		self.view.ask('ID del Actor a modificar: ')
		id_actor = input()
		actor = self.model.read_a_actor(id_actor)
		if type(actor) == tuple:
			self.view.show_actor_header('Datos del Actor'+id_actor+' ')
			self.view.show_a_actor(actor)
			self.view.show_actor_midder()
			self.view.show_actor_footer()
		else:
			if actor == None:
				self.view.error('El Actor no existe')
			else:
				self.view.error('Problemas al leer el Actor, REVISA')
			return
		self.view.msg('Ingresa los valores a modificar:(vacio para dejarlo igual)')
		whole_vals = self.ask_actor()
		fields, vals = self.update_lists(['a_fname','a_sname1','a_sname2','c_nationality'], whole_vals)
		vals.append(id_actor)
		vals = tuple(vals)
		out = self.model.update_actor(fields, vals)
		if out == True:
			self.view.ok(id_actor, 'actualizo')
		else:
			self.view.error('No se pudo actualizar el Actor. REVISA')
		return

	def delete_actor(self):
		self.view.ask('ID_Actor a borrar: ')
		id_actor = input()
		count = self.model.delete_actor(id_actor)
		if count !=0:
			self.view.ok(id_actor, 'borro')
		else:
			if count == 0:
				self.view.error('El Actor no existe')
			else:
				self.view.error('Problemas al leer el Actor. REVISA')
		return

	"""
	**************************
	* Controllers for genres *
	**************************
	"""
	def genres_menu(self):
		o = '0'
		while o != '5':
			self.view.genres_menu()
			self.view.option('5')
			o = input()
			if o == '1':
				self.create_genre()
			elif o == '2':
				self.read_all_genres()
			elif o == '3':
				self.update_genre()
			elif o == '4':
				self.delete_genre()
			elif o == '5':
				return
			else:
				self.view.not_valid_option()
		return

	def ask_genre(self):
		self.view.ask('Nombre: ')
		name = input()
		self.view.ask('Descripcion: ')
		g_descrip = input()
		return[name, g_descrip]

	def create_genre(self):
		name, g_descrip = self.ask_genre()
		out = self.model.create_genre(name, g_descrip)
		if out == True:
			self.view.ok(name+' '+g_descrip, 'agrego')
		else:
			self.view.error('No se pudo agregar el Genero. REVISA')
		return


	def read_all_genres(self):
		genres = self.model.read_all_genres()
		if type(genres) == list:
			self.view.show_genre_header('  Todos los Generos  ')
			for genre in genres:
				self.view.show_a_genre(genre)
			self.view.show_genre_midder()
			self.view.show_genre_footer()
		else:
			self.view.error('PROBLEMA AL LEER LOS Generos. REVISA.')
		return


	def update_genre(self):
		self.view.ask('ID del Genero a modificar: ')
		id_genre = input()
		genre = self.model.read_a_genre(id_genre)
		if type(genre) == tuple:
			self.view.show_genre_header('Datos del Genero'+id_genre+' ')
			self.view.show_a_genre(genre)
			self.view.show_genre_midder()
			self.view.show_genre_footer()
		else:
			if genre == None:
				self.view.error('El Genero no existe')
			else:
				self.view.error('Problemas al leer el Genero, REVISA')
			return
		self.view.msg('Ingresa los valores a modificar:(vacio para dejarlo igual)')
		whole_vals = self.ask_genre()
		fields, vals = self.update_lists(['g_name','g_descrip'], whole_vals)
		vals.append(id_genre)
		vals = tuple(vals)
		out = self.model.update_genre(fields, vals)
		if out == True:
			self.view.ok(id_genre, 'actualizo')
		else:
			self.view.error('No se pudo actualizar el Genero. REVISA')
		return

	def delete_genre(self):
		self.view.ask('ID_Genero a borrar: ')
		id_genre = input()
		count = self.model.delete_genre(id_genre)
		if count !=0:
			self.view.ok(id_genre, 'borro')
		else:
			if count == 0:
				self.view.error('El Genero no existe')
			else:
				self.view.error('Problemas al leer el Genero. REVISA')
		return

	"""
	*************************
	* Controllers for halls *
	*************************
	"""
	def halls_menu(self):
		o = '0'
		while o != '7':
			self.view.halls_menu()
			self.view.option('7')
			o = input()
			if o == '1':
				self.create_hall()
			elif o == '2':
				self.read_all_halls()
			elif o == '3':
				self.update_hall()
			elif o == '4':
				self.delete_hall()
			elif o == '5':
				self.create_hall_service()
			elif o == '6':
				self.read_all_halls_services()
			elif o == '7':
				return
			else:
				self.view.not_valid_option()
		return

	def ask_hall(self):
		self.view.ask('Nombre: ')
		h_name = input()
		self.view.ask('No.Asientos: ')
		h_nseat = input()
		return[h_name, h_nseat]

	def create_hall(self):
		h_name, h_nseat = self.ask_hall()
		out = self.model.create_hall(h_name, h_nseat)
		if out == True:
			self.view.ok(h_name+' '+h_nseat, 'agrego')
		else:
			self.view.error('No se pudo agregar la sala. REVISA')
		return

	def read_all_halls(self):
		halls = self.model.read_all_halls()
		if type(halls) == list:
			self.view.show_hall_header('  Todos las salas  ')
			for hall in halls:
				self.view.show_a_hall(hall)
			self.view.show_hall_midder()
			self.view.show_hall_footer()
		else:
			self.view.error('PROBLEMA AL LEER LAS SALAS. REVISA.')
		return


	def update_hall(self):
		self.view.ask('ID a modificar: ')
		id_hall = input()
		hall = self.model.read_a_hall(id_hall)
		if type(hall) == tuple:
			self.view.show_hall_header('Datos de la sala'+id_hall+' ')
			self.view.show_a_hall(hall)
			self.view.show_hall_midder()
			self.view.show_hall_footer()
		else:
			if hall == None:
				self.view.error('La sala no existe')
			else:
				self.view.error('Problemas al leer la sala, REVISA')
			return
		self.view.msg('Ingresa los valores a modificar:(vacio para dejarlo igual)')
		whole_vals = self.ask_hall()
		fields, vals = self.update_lists(['h_name','h_nseat'], whole_vals)
		vals.append(id_hall)
		vals = tuple(vals)
		out = self.model.update_hall(fields, vals)
		if out == True:
			self.view.ok(id_hall, 'actualizo')
		else:
			self.view.error('No se pudo actualizar la sala. REVISA')
		return

	def delete_hall(self):
		self.view.ask('ID a borrar: ')
		id_hall = input()
		count = self.model.delete_hall(id_hall)
		if count !=0:
			self.view.ok(id_hall, 'borro')
		else:
			if count == 0:
				self.view.error('La sala no existe')
			else:
				self.view.error('Problemas al leer la sala. REVISA')
		return

	"""
	**********************************
	* Controllers for halls-services *
	**********************************
	"""
	def services_menu(self):
		o = '0'
		while o != '5':
			self.view.services_menu()
			self.view.option('5')
			o = input()
			if o == '1':
				self.create_service()
			elif o == '2':
				self.read_all_services()
			elif o == '3':
				self.update_service()
			elif o == '4':
				self.delete_service()
			elif o == '5':
				return
			else:
				self.view.not_valid_option()
		return

	def ask_service(self):
		self.view.ask('Nombre: ')
		s_name = input()
		self.view.ask('Descripcion: ')
		s_descrip = input()
		return[s_name, s_descrip]

	def create_service(self):
		s_name, s_descrip = self.ask_service()
		out = self.model.create_service(s_name, s_descrip)
		if out == True:
			self.view.ok(s_name+' '+s_descrip, 'agrego')
		else:
			self.view.error('No se pudo agregar el servicio a sala. REVISA')
		return

	def read_all_services(self):
		services = self.model.read_all_services()
		if type(services) == list:
			self.view.show_service_header('  Todos los servicios  ')
			for service in services:
				self.view.show_a_service(service)
			self.view.show_service_midder()
			self.view.show_service_footer()
		else:
			self.view.error('PROBLEMA AL LEER LOS SERVICIOS. REVISA.')
		return


	def update_service(self):
		self.view.ask('ID a modificar: ')
		id_service = input()
		service = self.model.read_a_service(id_service)
		if type(service) == tuple:
			self.view.show_service_header('Datos del servicio'+id_service+' ')
			self.view.show_a_service(service)
			self.view.show_service_midder()
			self.view.show_service_footer()
		else:
			if hall == None:
				self.view.error('El servicio no existe')
			else:
				self.view.error('Problemas al leer el servicio, REVISA')
			return
		self.view.msg('Ingresa los valores a modificar:(vacio para dejarlo igual)')
		whole_vals = self.ask_service()
		fields, vals = self.update_lists(['s_name','s_descrip'], whole_vals)
		vals.append(id_service)
		vals = tuple(vals)
		out = self.model.update_service(fields, vals)
		if out == True:
			self.view.ok(id_service, 'actualizo')
		else:
			self.view.error('No se pudo actualizar el servicio. REVISA')
		return

	def delete_service(self):
		self.view.ask('ID a borrar: ')
		id_service = input()
		count = self.model.delete_service(id_service)
		if count !=0:
			self.view.ok(id_service, 'borro')
		else:
			if count == 0:
				self.view.error('El servicio no existe')
			else:
				self.view.error('Problemas al leer el servicio. REVISA')
		return

	"""
	***************************
	* Controllers for shedule *
	***************************
	"""
	def shedule_menu(self):
		o = '0'
		while o != '5':
			self.view.shedule_menu()
			self.view.option('5')
			o = input()
			if o == '1':
				self.create_shedule()
			elif o == '2':
				self.read_all_shedule()
			elif o == '3':
				self.update_shedule()
			elif o == '4':
				self.delete_shedule()
			elif o == '5':
				return
			else:
				self.view.not_valid_option()
		return

	def ask_shedule(self):
		self.view.ask('Hora inicial: ')
		sh_ini = input()
		self.view.ask('Hora final: ')
		sh_end = input()
		return[sh_ini, sh_end]

	def create_shedule(self):
		sh_ini, sh_end = self.ask_shedule()
		out = self.model.create_shedule(sh_ini, sh_end)
		if out == True:
			self.view.ok(sh_ini+' '+sh_end, 'agrego')
		else:
			self.view.error('No se pudo agregar el horario. REVISA')
		return


	def read_all_shedule(self):
		shedules = self.model.read_all_shedule()
		if type(shedules) == list:
			self.view.show_shedule_header('  Todos los Horarios  ')
			for shedule in shedules:
				self.view.show_a_shedule(shedule)
			self.view.show_shedule_midder()
			self.view.show_shedule_footer()
		else:
			self.view.error('PROBLEMA AL LEER LOS HORARIOS. REVISA.')
		return


	def update_shedule(self):
		self.view.ask('ID del Genero a modificar: ')
		id_shedule = input()
		shedule = self.model.read_a_shedule(id_shedule)
		if type(shedule) == tuple:
			self.view.show_shedule_header('Datos del Horario'+id_shedule+' ')
			self.view.show_a_shedule(shedule)
			self.view.show_shedule_midder()
			self.view.show_shedule_footer()
		else:
			if shedule == None:
				self.view.error('El horario no existe')
			else:
				self.view.error('Problemas al leer el horario, REVISA')
			return
		self.view.msg('Ingresa los valores a modificar:(vacio para dejarlo igual)')
		whole_vals = self.ask_shedule()
		fields, vals = self.update_lists(['sh_ini','sh_end'], whole_vals)
		vals.append(id_shedule)
		vals = tuple(vals)
		out = self.model.update_shedule(fields, vals)
		if out == True:
			self.view.ok(id_shedule, 'actualizo')
		else:
			self.view.error('No se pudo actualizar el horario. REVISA')
		return

	def delete_shedule(self):
		self.view.ask('ID a borrar: ')
		id_shedule = input()
		count = self.model.delete_shedule(id_shedule)
		if count !=0:
			self.view.ok(id_shedule, 'borro')
		else:
			if count == 0:
				self.view.error('El Horario no existe')
			else:
				self.view.error('Problemas al leer el horario. REVISA')
		return

	"""
	*****************************
	* Controllers for admins *
	*****************************
	"""
	def admins_menu(self):
		o = '0'
		while o != '5':
			self.view.admins_menu()
			self.view.option('5')
			o = input()
			if o == '1':
				self.create_admin()
			elif o == '2':
				self.read_all_admins()
			elif o == '3':
				self.update_admin()
			elif o == '4':
				self.delete_admin()
			elif o == '5':
				return
			else:
				self.view.not_valid_option()
		return

	def ask_admin(self):
		self.view.ask('Nombre: ')
		ad_fname = input()
		self.view.ask('A.Paterno: ')
		ad_sname1 = input()
		self.view.ask('A.Materno: ')
		ad_sname2 = input()
		self.view.ask('Pass: ')
		ad_pass = input()
		return[ad_fname, ad_sname1, ad_sname2, ad_pass]

	def create_admin(self):
		ad_fname, ad_sname1, ad_sname2, ad_pass = self.ask_admin()
		out = self.model.create_admin(ad_fname, ad_sname1, ad_sname2, ad_pass)
		if out == True:
			self.view.ok(ad_fname+' '+ad_sname1, 'agrego')
		else:
			self.view.error('No se pudo agregar el administrador. REVISA')
		return

	def read_all_admins(self):
		admins = self.model.read_all_admins()
		if type(admins) == list:
			self.view.show_admin_header('  Todos los adminstradores  ')
			for admin in admins:
				self.view.show_a_admin(admin)
			self.view.show_admin_midder()
			self.view.show_admin_footer()
		else:
			self.view.error('PROBLEMA AL LEER LOS ADMINSTRADORES. REVISA.')
		return


	def update_admin(self):
		self.view.ask('ID a modificar: ')
		id_admin = input()
		admin = self.model.read_a_admin(id_admin)
		if type(admin) == tuple:
			self.view.show_admin_header('Datos del administrador'+id_admin+' ')
			self.view.show_a_admin(admin)
			self.view.show_admin_midder()
			self.view.show_admin_footer()
		else:
			if admin == None:
				self.view.error('El Admistrador no existe')
			else:
				self.view.error('Problemas al leer el administrador, REVISA')
			return
		self.view.msg('Ingresa los valores a modificar:(vacio para dejarlo igual)')
		whole_vals = self.ask_admin()
		fields, vals = self.update_lists(['ad_fname','ad_sname1','ad_sname2','ad_pass'], whole_vals)
		vals.append(id_admin)
		vals = tuple(vals)
		out = self.model.update_admin(fields, vals)
		if out == True:
			self.view.ok(id_admin, 'actualizo')
		else:
			self.view.error('No se pudo actualizar el administrador. REVISA')
		return

	def delete_admin(self):
		self.view.ask('ID a borrar: ')
		id_admin = input()
		count = self.model.delete_admin(id_admin)
		if count !=0:
			self.view.ok(id_admin, 'borro')
		else:
			if count == 0:
				self.view.error('El administrador no existe')
			else:
				self.view.error('Problemas al leer el administrador. REVISA')
		return

		"""
	**************************
	* Controllers for Movies *
	**************************
	"""
	def movies_menu(self):
		o = '0'
		while o != '9':
			self.view.movies_menu()
			self.view.option('9')
			o = input()
			if o == '1':
				self.create_movie()
			elif o == '2':
				self.read_all_movies()
			elif o == '3':
				self.update_movie()
			elif o == '4':
				self.delete_movie()
			elif o == '5':
				self.create_actor_movie()
			elif o == '6':
				self.read_all_movies_actors()
			elif o == '7':
				self.create_actor_genre()
			elif o == '8':
				self.read_all_movies_genres()
			elif o == '9':
				return
			else:
				self.view.not_valid_option()
		return

	def ask_movie(self):
		self.view.ask('Nombre: ')
		m_name = input()
		self.view.ask('Año: ')
		m_year = input()
		self.view.ask('Sinopsis: ')
		m_sinopsis = input()
		self.view.ask('Premiere: ')
		m_premiere = input()
		self.view.ask('Subtitulos: ')
		m_subtitle = input()
		self.view.ask('Duracion: ')
		m_minutos = input()
		self.view.ask('Director: ')
		m_director = input()
		self.view.ask('Lenguaje: ')
		m_language = input()
		self.view.ask('Clasificacion: ')
		m_classification = input()
		return[m_name, m_year, m_sinopsis, m_premiere, m_subtitle, m_minutos, m_director, m_language, m_classification]

	def create_movie(self):
		m_name, m_year, m_sinopsis, m_premiere, m_subtitle, m_minutos, m_director, m_language, m_classification = self.ask_movie()
		out = self.model.create_movie(m_name, m_year,m_sinopsis, m_premiere, m_subtitle, m_minutos, m_director, m_language, m_classification)
		if out == True:
			self.view.ok(m_name+' '+m_year, 'agrego')
		else:
			self.view.error('No se pudo agregar la pelicula. REVISA')
		return

	

	def read_all_movies(self):
		movies = self.model.read_all_movies()
		if type(movies) == list:
			self.view.show_movie_header('  Todas las peliculas  ')
			for movie in movies:
				self.view.show_a_movie(movie)
			self.view.show_movie_midder()
			self.view.show_movie_footer()
		else:
			self.view.error('PROBLEMA AL LEER LAS PELICULAS. REVISA.')
		return

	

	def update_movie(self):
		self.view.ask('ID de la pelucula a modificar: ')
		id_movie = input()
		movie = self.model.read_a_movie(id_movie)
		if type(movie) == tuple:
			self.view.show_movie_header('Datos de la pelicula'+id_movie+' ')
			self.view.show_a_movie(movie)
			self.view.show_movie_midder()
			self.view.show_movie_footer()
		else:
			if movie == None:
				self.view.error('La pelicula no existe')
			else:
				self.view.error('Problemas al leer la pelicula, REVISA')
			return
		self.view.msg('Ingresa los valores a modificar:(vacio para dejarlo igual)')
		whole_vals = self.ask_movie()
		fields, vals = self.update_lists(['m_name','m_year','m_sinopsis','m_premiere','m_subtitle', 'm_minutos', 'm_director', 'm_language', 'm_classification'], whole_vals)
		vals.append(id_movie)
		vals = tuple(vals)
		out = self.model.update_movie(fields, vals)
		if out == True:
			self.view.ok(id_movie, 'actualizo')
		else:
			self.view.error('No se pudo actualizar la pelucula. REVISA')
		return

	def delete_movie(self):
		self.view.ask('ID Pelicula a borrar: ')
		id_movie = input()
		count = self.model.delete_movie(id_movie)
		if count !=0:
			self.view.ok(id_movie, 'borro')
		else:
			if count == 0:
				self.view.error('La pelicula no existe')
			else:
				self.view.error('Problemas al leer la pelicula. REVISA')
		return
	"""
	*********************************
	* Controllers for halls-sercies *
	*********************************
	"""
	def ask_hall_sercice(self):
		self.view.ask('Id Sala: ')
		id_hall = input()
		self.view.ask('Id Servicio: ')
		id_service = input()
		return[id_hall, id_service]

	def create_hall_service(self):
		self.read_all_services()
		self.read_all_halls()
		id_hall, id_service = self.ask_hall_sercice()
		out = self.model.create_hall_service(id_hall, id_service)
		if out == True:
			self.view.ok(id_hall+' '+id_service, 'agrego')
		else:
			self.view.error('No se pudo agregar el administrador. REVISA')
		return

	def read_all_halls_services(self):
		self.read_all_halls()
		self.read_all_services()
		admins = self.model.read_all_halls_services()
		if type(admins) == list:
			self.view.show_hall_header('  Todos los servicios  ')
			for admin in admins:
				self.view.show_a_hall_service(admin)
			self.view.show_admin_midder()
			self.view.show_admin_footer()
		else:
			self.view.error('PROBLEMA AL LEER LOS SERVICIOS. REVISA.')
		return

	"""
	*********************************
	* Controllers for movies-actors *
	*********************************
	"""
	def ask_movie_actor(self):
		self.view.ask('Id movie: ')
		id_movie = input()
		self.view.ask('Id actor: ')
		id_actor = input()
		return[id_movie, id_actor]

	def create_actor_movie(self):
		self.read_all_actors()
		self.read_all_movies()
		id_movie, id_actor = self.ask_movie_actor()
		out = self.model.create_movie_actor(id_movie, id_actor)
		if out == True:
			self.view.ok(id_movie+' '+id_actor, 'agrego')
		else:
			self.view.error('No se pudo agregar el actor. REVISA')
		return

	def read_all_movies_actors(self):
		self.read_all_actors()
		self.read_all_movies()
		admins = self.model.read_all_movies_actors()
		if type(admins) == list:
			self.view.show_hall_header('  Todos los actores y peliculas  ')
			for admin in admins:
				self.view.show_a_movie_actor(admin)
			self.view.show_admin_midder()
			self.view.show_admin_footer()
		else:
			self.view.error('PROBLEMA AL LEER LOS ACTORES. REVISA.')
		return

	"""
	*********************************
	* Controllers for movies-genres *
	*********************************
	"""
	def ask_movie_genre(self):
		self.view.ask('Id Pelicula: ')
		id_movie = input()
		self.view.ask('Id Genero: ')
		id_genre = input()
		return[id_movie, id_genre]

	def create_actor_genre(self):
		self.read_all_genres()
		self.read_all_movies()
		id_movie, id_genre = self.ask_movie_genre()
		out = self.model.create_movie_genre(id_movie, id_genre)
		if out == True:
			self.view.ok(id_movie+' '+id_genre, 'agrego')
		else:
			self.view.error('No se pudo agregar el genero. REVISA')
		return

	def read_all_movies_genres(self):
		self.read_all_actors()
		self.read_all_movies()
		admins = self.model.read_all_movies_genres()
		if type(admins) == list:
			self.view.show_hall_header('  Todos los actores y generos  ')
			for admin in admins:
				self.view.show_a_movie_genre(admin)
			self.view.show_admin_midder()
			self.view.show_admin_footer()
		else:
			self.view.error('PROBLEMA AL LEER LOS GENEROS. REVISA.')
		return

	"""
	**************************
	* Controllers for Projections *
	**************************
	"""
	def projections_menu(self):
		o = '0'
		while o != '5':
			self.view.projections_menu()
			self.view.option('5')
			o = input()
			if o == '1':
				self.create_projection()
			elif o == '2':
				self.read_all_projections()
			elif o == '3':
				self.update_projection()
			elif o == '4':
				self.delete_projection()
			elif o == '5':
				self.create_projection_for_day()
			elif o == '6':
				return
			else:
				self.view.not_valid_option()
		return

	def ask_projection(self):
		self.view.ask('Fecha: ')
		p_fecha = input()
		self.view.ask('Sala: ')
		p_hall = input()
		self.view.ask('Pelicula: ')
		p_movie = input()
		self.view.ask('Horario: ')
		p_shedule = input()
		self.view.ask('Asiento: ')
		p_seat = input()
		self.view.ask('Ocupado: ')
		p_flag = input()
		return[p_fecha, p_hall, p_movie, p_shedule, p_seat, p_flag]

	def create_projection(self):
		p_fecha, p_hall, p_movie, p_shedule, p_seat, p_flag = self.ask_projection()
		out = self.model.create_projection(p_fecha, p_hall, p_movie, p_shedule, p_seat, p_flag)
		if out == True:
			self.view.ok(p_movie+' '+p_hall, 'agrego')
		else:
			self.view.error('No se pudo agregar el actor. REVISA')
		return

	def read_a_actor(self):
		self.view.ask('ID: ')
		id_projection = input()
		projection = self.model.read_a_projection(id_projection)
		if type(projection) == tuple:
			self.view.show_projection_header('  Datos de la projeccion '+id_projection+' ')
			self.view.show_a_projection(projection)
			self.view.show_projection_midder()
			self.view.show_projection_footer()
		else:
			if projection == None:
				self.view.error('LA PROJECTION NO EXISTE')
			else:
				self.view.error('PROBLEMA AL LEER LA PROJECTION. REVISA.')
		return

	def read_all_projections(self):
		projections = self.model.read_all_projections()
		if type(projections) == list:
			self.view.show_projection_header('  Todos las proyeccion  ')
			for projection in projections:
				self.view.show_a_projection(projection)
			self.view.show_projection_midder()
			self.view.show_projection_footer()
		else:
			self.view.error('PROBLEMA AL LEER LAS PROYECCIONES. REVISA.')
		return

	def update_projection(self):
		self.view.ask('ID a modificar: ')
		id_projection = input()
		projection = self.model.read_a_projection(id_projection)
		if type(projection) == tuple:
			self.view.show_projection_header('Datos de la projecion'+id_projection+' ')
			self.view.show_a_projection(projection)
			self.view.show_projection_midder()
			self.view.show_projection_footer()
		else:
			if projection == None:
				self.view.error('La projeccion no exite no existe')
			else:
				self.view.error('Problemas al leer la projeccion, REVISA')
			return
		self.view.msg('Ingresa los valores a modificar:(vacio para dejarlo igual)')
		whole_vals = self.ask_projection()
		fields, vals = self.update_lists(['p_fecha','p_hall','p_movie','p_shedule', 'p_seat', 'p_flag'], whole_vals)
		vals.append(id_projection)
		vals = tuple(vals)
		out = self.model.update_projection(fields, vals)
		if out == True:
			self.view.ok(id_projection, 'actualizo')
		else:
			self.view.error('No se pudo actualizar la projection. REVISA')
		return

	def delete_projection(self):
		self.view.ask('ID a borrar: ')
		id_projection = input()
		count = self.model.delete_projection(id_projection)
		if count !=0:
			self.view.ok(id_projection, 'borro')
		else:
			if count == 0:
				self.view.error('La projeccion no existe')
			else:
				self.view.error('Problemas al leer la projeccion. REVISA')
		return

	def ask_projection(self):
		self.view.ask('Fecha: ')
		p_fecha = input()
		self.view.ask('Sala: ')
		p_hall = input()
		self.view.ask('Pelicula: ')
		p_movie = input()
		self.view.ask('Horario: ')
		p_shedule = input()
		self.view.ask('Asiento: ')
		p_seat = input()
		self.view.ask('Ocupado: ')
		p_flag = input()
		return[p_fecha, p_hall, p_movie, p_shedule, p_seat, p_flag]

	def create_projection_for_day(self):
		self.view.ask('Fecha:')
		p_fecha = input()
		self.view.ask('Pelicula:')
		p_movie = input()
		self.view.ask('Horario:')
		p_shedule = input()
		self.view.ask('Bandera:')
		p_flag = input()
		self.view.ask('ID sala: ')
		id_hall = input()
		nseat=self.model.read_seats_hall(id_hall)
		print('Numeros de asientos:', nseat)
		p_hall=id_hall
		int(nseat[2])
		j=nseat[2]
		i=1
		int(i)
		while i != j:
			p_seat = i
			out = self.model.create_projection(p_fecha, p_hall, p_movie, p_shedule, p_seat, p_flag)
			if out == True:
				self.view.ok(p_movie+' '+p_hall, 'agrego')
			else:
				self.view.error('No se pudo agregar el actor. REVISA')
			i=i+1
		return

	"""
	**************************
	* Controllers for tikets *
	**************************
	"""
	def tikets_menu(self):
		o = '0'
		while o != '5':
			self.view.tikets_menu()
			self.view.option('5')
			o = input()
			if o == '1':
				self.create_tiket()
			elif o == '2':
				self.read_all_tikets()
			elif o == '3':
				self.update_tiket()
			elif o == '4':
				self.delete_tiket()
			elif o == '5':
				return
			else:
				self.view.not_valid_option()
		return

	def ask_tiket(self):
		self.view.ask('id_projeccion: ')
		t_projection = input()
		self.view.ask('Price: ')
		t_price = input()
		return[t_projection, t_price]

	def create_tiket(self):
		t_projection, t_price = self.ask_tiket()
		out = self.model.create_tiket(t_projection, t_price)
		if out == True:
			self.view.ok(t_projection+' '+t_price, 'agrego')
		else:
			self.view.error('No se pudo agregar el tiket. REVISA')
		return


	def read_all_tikets(self):
		tikets = self.model.read_all_tikets()
		if type(tikets) == list:
			self.view.show_tikets_header('  Todos los Tikets  ')
			for tiket in tikets:
				self.view.show_a_tiket(tiket)
			self.view.show_tiket_midder()
			self.view.show_tiket_footer()
		else:
			self.view.error('PROBLEMA AL LEER LOS TIKETS. REVISA.')
		return


	def update_tiket(self):
		self.view.ask('ID a modificar: ')
		id_tiket = input()
		tiket = self.model.read_a_tikets(id_tiket)
		if type(tiket) == tuple:
			self.view.show_tiket_header('Datos del tiket'+id_tiket+' ')
			self.view.show_a_tiket(tiket)
			self.view.show_tiket_midder()
			self.view.show_tiket_footer()
		else:
			if tiket == None:
				self.view.error('El tiket no existe')
			else:
				self.view.error('Problemas al leer el tiket, REVISA')
			return
		self.view.msg('Ingresa los valores a modificar:(vacio para dejarlo igual)')
		whole_vals = self.ask_tiket()
		fields, vals = self.update_lists(['t_projection','t_price'], whole_vals)
		vals.append(id_tiket)
		vals = tuple(vals)
		out = self.model.update_tiket(fields, vals)
		if out == True:
			self.view.ok(id_tiket, 'actualizo')
		else:
			self.view.error('No se pudo actualizar el tiket. REVISA')
		return

	def delete_tiket(self):
		self.view.ask('ID a borrar: ')
		id_tiket = input()
		count = self.model.delete_tiket(id_tiket)
		if count !=0:
			self.view.ok(id_tiket, 'borro')
		else:
			if count == 0:
				self.view.error('El tiket no existe')
			else:
				self.view.error('Problemas al leer el tiket. REVISA')
		return
