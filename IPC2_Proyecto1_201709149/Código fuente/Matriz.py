class Matriz:

	frecuence_matrix = []
	pattern_matrix = []

	groups_data = [] #Matriz de la forma: [cardinalidad][patrón de acceso]
	cant_of_groups = None
	reduced_frecuence_matrix = []

	def __init__(self, n, m, name, frecuence_matrix):
		self.next = next
		self.m = m
		self.n = n
		self.name = name
		self.frecuence_matrix = frecuence_matrix

	def print_data(self, matrix_to_print, matrix_name):
		print("")
		pN = len(matrix_to_print)
		pM = len(matrix_to_print[0])

		print(matrix_name + ":")
		print("n: " + str(pN) + ", m: " + str(pM))

		for i in range(pN):
			for j in range(pM):
				element = str(matrix_to_print[i][j])
				print("[" + element + "] ", end = "")
			print("\n")

	def construct_pattern_matrix(self):
		self.pattern_matrix = [[0] * self.m for i in range(self.n)]

		for i in range(self.n):
			for j in range(self.m):
				element = self.frecuence_matrix[i][j]
				if element > 0:
					self.pattern_matrix[i][j] = 1
				else:
					self.pattern_matrix[i][j] = 0

	def construct_reduced_matrix(self):
		self.groups_data = []
		self.cant_of_groups = 0
		aux_matrix = self.pattern_matrix
		pattern_lines = []

		#Convirtiendo filas en cadenas pára comparar entre sí:
		for i in range(self.n):
			aux_string = ""
			for j in range(self.m):
				aux_string += str(self.pattern_matrix[i][j])
			pattern_lines.append(aux_string)
		
		# Creando grupos según patrones
		print("Creando grupos...")

		while True:
			added = False
		#Para crear el primer grupo.
			if self.cant_of_groups == 0:
				first_pattern = str(pattern_lines[0])				
				self.groups_data.append([0, first_pattern])
				self.cant_of_groups += 1
			else:
		 		#recorrerá toda la matriz de patrones, si encuentra uno no agregado, lo agrega.
		 		for i in range(len(pattern_lines)):
		 			added = False
		 			patter_to_ver = str(pattern_lines[i])

		 			for j in range(self.cant_of_groups):
		 				if str(self.groups_data[j][1]) == str(patter_to_ver):
		 					added = True
		 					break
		 				else:
		 					added = False

		 			if added == False:
		 				self.groups_data.append([0, patter_to_ver])
		 				self.cant_of_groups += 1
		 				break
			if added:
		 		break		

		reduced_aux = [[0] * self.m for i in range(self.cant_of_groups)]

		# Agrega la cardinalidad de los grupos:
		for i in range(self.cant_of_groups):
			for j in range(self.n):
				if self.groups_data[i][1] == pattern_lines[j]:
					self.groups_data[i][0] += 1

		# Reduciendo matríz, sumando tuplas:
		print("Realizando suma de tuplas...")
		for i in range(self.cant_of_groups):
			acces_pattern = self.groups_data[i][1]
			
			for j in range(len(pattern_lines)):
				if acces_pattern == pattern_lines[j]:
					#suma una fila
					for l in range(self.m):
						reduced_aux[i][l] += self.frecuence_matrix[j][l]

		self.reduced_frecuence_matrix = reduced_aux

		def get_name(sef):
			return str(self.name)

		def get_n(sef):
			return str(self.n)

		def get_m(sef):
			return str(self.m)

		def get_groups_data(sef):
			return str(self.groups_data)

		def get_g(sef):
			return str(self.cant_of_groups)

		def get_rN(sef):
			return len(self.reduced_frecuence_matrix)
			
