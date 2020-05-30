class View:
	"""
	*************************
	* A view for a Cinema DB *
	*************************
	"""
	def start(self):
		print('=============================================')
		print('=         ¡Bienvenido a Cinemax!            =')
		print('=       ¡Para comenzar la aventura!         =')
		print('=         ¡Preciona 2 veces enter!          =')
		print('=   ¡Si eres uno de nuestros supervisores!  =')
		print('=     ¡Digita tu ID seguido de tu clave!    =')
		print('=============================================')

	def end(self):
		print('=================================')
		print('=       ¡Vuelve pronto!         =')
		print('=================================')

	
	def main_client(self):
		print('=============================================')
		print('=         ¡Te estabmos esperando!           =')
		print('=       ¡Para comenzar la aventura!         =')
		print('=    ¡Conocemos estamos para atenderte!     =')
		print('=   ¡Si eres uno de nuestros supervisores!  =')
		print('=     ¡Digita tu ID seguido de tu clave!    =')
		print('=============================================')
		print('*********************************************')
		print('        * -- ¿Que deseas ver? -- *         	')
		print('*********************************************')
		print('1. Ver estenos')
		print('2. Horarios')
		print('3. Cartelera')
		print('4. Fecha')
		print('5. Hora')
		print('6. Servicios de salas')
		print('7. Horarios')
		print('8. Peliculas')
		print('9. tikets')
		print('10. Salir')

	def main_menu(self):
		print('************************')
		print('* -- Menu Administrador -- *')
		print('************************')
		print('1. Directores')
		print('2. Clasificaciones')
		print('3. Lenguajes')
		print('4. Actores')
		print('5. Generos')
		print('6. Salas')
		print('7. Servicios de salas')
		print('8. Horarios')
		print('9. Peliculas')
		print('10. Projeciones')
		print('11. tikets')
		print('12. Administradores')
		print('13. Salir')

	def option(self, last):
		print('Seleciona una opcion (1-'+last+'):', end = '')

	def not_valid_option(self):
		print('¡Opcion no valida!\nIntenta de nuevo')

	def ask(self, output):
		print(output, end = '')

	def msg(self, output):
		print(output)

	def ok(self, id, op):
		print('+'*(len(str(id))+len(op)+24))
		print('+ ¡'+str(id)+' se '+op+' correctamente! +')
		print('+'*(len(str(id))+len(op)+24))

	def error(self, err):
		print('  ¡ERROR!  '.center(len(err)+4,'-'))
		print('- '+err+' -')
		print('-'*(len(err)+4))

	"""
	***********************
	* Views for directors *
	***********************
	"""
	def directors_menu(self):
		print('****************************')
		print('* -- Submenu Directores -- *')
		print('****************************')
		print('1. Agregar Director')		
		print('2. Mostrar todos los Directores')		
		print('3. Actualizar Director')
		print('4. Borrar Director')
		print('5. Regresar')

	def show_a_director(self, record):
		print('ID:', record[0])
		print('Nombre:', record[1])
		print('A.Paterno:', record[2])
		print('A.Marterno:', record[3])
		

	def show_director_header(self, header):
		print(header.center(48,'*'))
		print('-'*48)

	def show_director_midder(self):
		print('-'*78)

	def show_director_footer(self):
		print('*'*78)

	"""
	*****************************
	* Views for Classifications *
	*****************************
	"""
	def classifications_menu(self):
		print('*********************************')
		print('* -- Submenu Classificacions -- *')
		print('*********************************')
		print('1. Agregar Clasificacion')		
		print('2. Mostrar todas las clasificaciones')		
		print('3. Actualizar una clasificacion')
		print('4. Borrar una clasificacion')
		print('5. Regresar')

	def show_a_classification(self, record):
		print('ID:', record[0])
		print('Descripcion:', record[1])		
		
	def show_classification_header(self, header):
		print(header.center(48,'*'))
		print('-'*48)

	def show_classification_midder(self):
		print('-'*78)

	def show_classification_footer(self):
		print('*'*78)

	"""
	*****************************
	* Views for Lenguages *
	*****************************
	"""
	def languages_menu(self):
		print('***************************')
		print('* -- Submenu Lenguages -- *')
		print('***************************')
		print('1. Agregar lenguaje')		
		print('2. Mostrar todos los lenguajes')		
		print('3. Actualizar un lenguaje')
		print('4. Borrar un lenguaje')
		print('5. Regresar')

	def show_a_language(self, record):
		print('ID:', record[0])
		print('Descripcion:', record[1])		
		
	def show_language_header(self, header):
		print(header.center(48,'*'))
		print('-'*48)

	def show_language_midder(self):
		print('-'*78)

	def show_language_footer(self):
		print('*'*78)

	"""
	********************
	* Views for Actors *
	********************
	"""
	def actors_menu(self):
		print('*************************')
		print('* -- Submenu Actores -- *')
		print('*************************')
		print('1. Agregar Actor')
		print('2. Mostrar todos los Actores')
		print('3. Actualizar Actor')
		print('4. Borrar Actor')
		print('5. Regresar')

	def show_a_actor(self, record):
		print('ID:', record[0])
		print('Nombre:', record[1])
		print('A.Paterno:', record[2])
		print('A.Marterno:', record[3])

	def show_actor_header(self, header):
		print(header.center(48,'*'))
		print('-'*48)

	def show_actor_midder(self):
		print('-'*78)

	def show_actor_footer(self):
		print('*'*78)

	"""
	********************
	* Views for Genres *
	********************
	"""
	def genres_menu(self):
		print('*************************')
		print('* -- Submenu Generos -- *')
		print('*************************')
		print('1. Agregar Genero')
		print('2. Mostrar todos los Generos')
		print('3. Actualizar Genero')
		print('4. Borrar Genero')
		print('5. Regresar')

	def show_a_genre(self, record):
		print('ID:', record[0])
		print('Nombre:', record[1])
		print('Descripcion:', record[2])
		

	def show_genre_header(self, header):
		print(header.center(48,'*'))
		print('-'*48)

	def show_genre_midder(self):
		print('-'*78)

	def show_genre_footer(self):
		print('*'*78)

	"""
	***********************
	* Views for Halls *
	***********************
	"""
	def halls_menu(self):
		print('****************************')
		print('* -- Submenu Salas -- *')
		print('****************************')
		print('1. Agregar sala')		
		print('2. Mostrar todas las salas')		
		print('3. Actualizar sala')
		print('4. Borrar sala')
		print('5. Agregar servicios')
		print('6. Leer las salas con servicios')
		print('7. Regresar')

	def show_a_hall(self, record):
		print('ID:', record[0])
		print('Nombre:', record[1])
		print('No. Asientos:', record[2])
		
		

	def show_hall_header(self, header):
		print(header.center(48,'*'))
		print('-'*48)

	def show_hall_midder(self):
		print('-'*78)

	def show_hall_footer(self):
		print('*'*78)

	"""
	****************************
	* Views for Services-Halls *
	****************************
	"""
	def services_menu(self):
		print('***********************************')
		print('* -- Submenu Servicios a salas -- *')
		print('***********************************')
		print('1. Agregar servicio')		
		print('2. Mostrar todos los servicios')		
		print('3. Actualizar servicio')
		print('4. Borrar servicio')
		print('5. Regresar')

	def show_a_service(self, record):
		print('ID:', record[0])
		print('Nombre:', record[1])
		print('Descripcion:', record[2])
		
		

	def show_service_header(self, header):
		print(header.center(48,'*'))
		print('-'*48)

	def show_service_midder(self):
		print('-'*78)

	def show_service_footer(self):
		print('*'*78)

	"""
	*********************
	* Views for Shedule *
	*********************
	"""
	def shedule_menu(self):
		print('*************************')
		print('* -- Submenu Horarios -- *')
		print('*************************')
		print('1. Agregar horario')
		print('2. Mostrar todos los horarios')
		print('3. Actualizar horario')
		print('4. Borrar horario')
		print('5. Regresar')

	def show_a_shedule(self, record):
		print('ID:', record[0])
		print('Nombre:', record[1])
		print('Descripcion:', record[2])

	
		

	def show_shedule_header(self, header):
		print(header.center(48,'*'))
		print('-'*48)

	def show_shedule_midder(self):
		print('-'*78)

	def show_shedule_footer(self):
		print('*'*78)

	"""
	***********************
	* Views for administrators *
	***********************
	"""
	def admins_menu(self):
		print('*********************************')
		print('* -- Submenu Administradores -- *')
		print('*********************************')
		print('1. Agregar administrador')		
		print('2. Mostrar todos los administradores')		
		print('3. Actualizar administrador')
		print('4. Borrar administrador')
		print('5. Regresar')

	def show_a_admin(self, record):
		print('ID:', record[0])
		print('Nombre:', record[1])
		print('A.Paterno:', record[2])
		print('A.Marterno:', record[3])
		print('Pass:', record[4])
		

	def show_admin_header(self, header):
		print(header.center(48,'*'))
		print('-'*48)

	def show_admin_midder(self):
		print('-'*78)

	def show_admin_footer(self):
		print('*'*78)

	"""
	********************
	* Views for movies *
	********************
	"""
	def movies_menu(self):
		print('*********************************')
		print('* -- Submenu Peliculas -- *')
		print('*********************************')
		print('1. Agregar pelicula')		
		print('2. Mostrar todas las peliculas')		
		print('3. Actualizar pelicula')
		print('4. Borrar pelicula')
		print('5. Agregar actores a pelicula')
		print('6. Leer todos los actores en peliculas')
		print('7. Agregar generos a pelicula')
		print('8. Leer todos los generos y peliculas')
		print('9. Regresar')

	def show_a_movie(self, record):
		print('ID:', record[0])
		print('Nombre:', record[1])
		print('Año:', record[2])
		print('Sinopsis: ', record[3])
		print('Premiere: ', record[4])
		print('Subtitulos: ', record[5])
		print('Duracion: ', record[6])
		print('Director: ', record[7])
		print('Idioma: ', record[8])
		print('Clasificacion: ', record[9])
		

	def show_movie_header(self, header):
		print(header.center(48,'*'))
		print('-'*48)

	def show_movie_midder(self):
		print('-'*78)

	def show_movie_footer(self):
		print('*'*78)


	"""
	****************************
	* Views for union tables *
	****************************
	"""

	def show_a_hall_service(self, record):
		print('Sala:', record[0])
		print('Servicio:', record[1])

	def show_a_movie_actor(self, record):
		print('Pelicula:', record[0])
		print('Actor:', record[1])

	def show_a_movie_genre(self, record):
		print('Pelicula:', record[0])
		print('Genero:', record[1])

	def show_a_admin(self, record):
		print('ID:', record[0])
		print('Nombre:', record[1])
		print('A.Paterno:', record[2])
		print('A.Marterno:', record[3])
		print('pass:', record[4])
	
	"""
	*************************
	* Views for proyections *
	*************************
	"""
	def projections_menu(self):
		print('******************************')
		print('* -- Submenu Proyecciones -- *')
		print('******************************')
		print('1. Agregar proyecion')		
		print('2. Mostrar todas las proyeciones')		
		print('3. Actualizar una proyecion')
		print('4. Borrar una proyecion')
		print('5. Crear proyecciones del dia')
		print('6. Regresar')
		#print('7. Regresar')

	def show_a_projection(self, record):
		print('ID:', record[0])
		print('Fecha:', record[1])
		print('Sala:', record[2])
		print('Pelicula:', record[3])
		print('Horario:', record[4])
		print('Asiento:', record[5])
		print('Ocupado:', record[6])
		
		

	def show_projection_header(self, header):
		print(header.center(48,'*'))
		print('-'*48)

	def show_projection_midder(self):
		print('-'*78)

	def show_projection_footer(self):
		print('*'*78)
		

	"""
	*****************
	* Views Clients *
	*****************
	"""
	def tikets_menu(self):
		print('*************************')
		print('* -- Sub_menu tikets -- *')
		print('*************************')
		print('1. Agregar tiket')		
		print('2. Mostrar todos tikets')		
		print('3. Actualizar Tiket')
		print('4. Borrar tiket')
		print('5. Regresar')

	def show_a_tiket(self, record):
		print('ID:', record[0])
		print('Proyecion:', record[1])
		print('price:', record[2])
		
		

	def show_tiket_header(self, header):
		print(header.center(48,'*'))
		print('-'*48)

	def show_tiket_midder(self):
		print('-'*78)

	def show_tiket_footer(self):
		print('*'*78)