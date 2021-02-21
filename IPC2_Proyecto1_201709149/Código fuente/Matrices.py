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

			for i in range(cant - 1):
				temp = temp.next

			temp.next = matrix
			matrix.next = first
			cat += 1



