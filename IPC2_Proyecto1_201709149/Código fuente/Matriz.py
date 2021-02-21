class Matriz:

	data_list = []

	def __init__(self, n, m, name, data_list):
		self.next = next
		self.m = m
		self.n = n
		self.name = name
		self.data_list = data_list
		self.print_data()

	def print_data(self):
		print("")
		print("Se imprimirá la matriz: ")
		print("")
		for i in range(self.n):
			for j in range(self.m):
				element = str(self.data_list[i][j])
				print(element + " ", end = "")
			print("\n")

