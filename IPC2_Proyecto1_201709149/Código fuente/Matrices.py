import Matriz

class Matrices:

	#Nodos tipo Matriz
	first = None
	last = None

	cant = 0

	def add_matrix(self, matrix):
		if self.first == None:
			self.first = matrix
			self.last = matrix
			self.cant += 1
		else:
			temp = self.first

			for i in range(self.cant - 1):
				temp = temp.next

			temp.next = matrix
			matrix.next = self.first
			self.cant += 1

	def construct_pattern_matrices(self):
		aux_matrix = self.first
		for i in range(self.cant):
			aux_matrix.construct_pattern_matrix()
			aux_matrix = aux_matrix.next

	def print_matrices_data(self):
		aux_matrix = self.first
		for i in range(self.cant):
			print("Matíz #" + str(i+1) + ":")
			print("Nombre: " + str(aux_matrix.name))
			print("n: " + str(aux_matrix.n) + ", m: " + str(aux_matrix.m))
			print("Cantidad de grupos: " + str(aux_matrix.cant_of_groups))
			aux_matrix.print_data(aux_matrix.frecuence_matrix, "Matríz de frecuencias")
			aux_matrix.print_data(aux_matrix.pattern_matrix, "Matríz de patrones de acceso")
			aux_matrix.print_data(aux_matrix.reduced_frecuence_matrix, "Matríz reducida")
			aux_matrix = aux_matrix.next

	def construct_reduced_matrices(self):
		aux_matrix = self.first
		for i in range(self.cant):
			aux_matrix.construct_reduced_matrix()
			aux_matrix = aux_matrix.next