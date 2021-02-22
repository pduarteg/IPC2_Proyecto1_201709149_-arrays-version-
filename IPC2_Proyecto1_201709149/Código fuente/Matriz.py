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

	def print_data(self, matrix_to_print):
		print("")
		pN = len(matrix_to_print)
		pM = len(matrix_to_print[0])

		print("pN: " + str(pN) + ", pM: " + str(pM))

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
		self.cant_of_groups = 0
		aux_matrix = self.pattern_matrix
		pattern_lines = []

		#Convirtiendo filas en cadenas pára comparar entre sí:
		for i in range(self.n):
			aux_string = ""
			for j in range(self.m):
				aux_string += str(self.pattern_matrix[i][j])
			pattern_lines.append(aux_string)

		# Creando información de grupos:
		for i in range(self.n):
			acces_pattern = pattern_lines[i]
			if self.cant_of_groups == 0:
				self.groups_data.append([1, acces_pattern])
				self.cant_of_groups += 1
			else:
				for j in range(self.cant_of_groups):
					if acces_pattern == self.groups_data[i-1][1]:
						self.groups_data[i-1][0] += 1
					else:
						self.groups_data.append([1, acces_pattern])
						self.cant_of_groups += 1

		reduced_aux = [[0] * self.m for i in range(self.cant_of_groups)]

		# Reduciendo matríz, sumando tuplas:
		for i in range(len(self.groups_data)):
			acces_pattern = self.groups_data[i][1]
			
			for j in range(len(pattern_lines)):
				if acces_pattern == pattern_lines[j]:
					for l in range(self.m):
						reduced_aux[i][l] += self.frecuence_matrix[j][l]

		self.reduced_frecuence_matrix = reduced_aux

					



						