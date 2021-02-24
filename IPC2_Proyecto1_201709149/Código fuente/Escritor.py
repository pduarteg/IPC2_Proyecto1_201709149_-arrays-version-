import Lector as LectorClass
import re
import os

class Escritor:

	def initial_data_request(self, matrices, output_root):
		self.matrices = matrices
		self.output_root = output_root


	def writeXML(self):
		matrices_l = self.matrices
		
		dirA = self.output_root
		if dirA == "":
			dirA = os.getcwd()
			
		dirB = dirA + "\\IPC2_Proyecto1_Salida.xml"
		
		print("Escribiendo archivo en ruta específicada...")
		try:
			file = open(dirB, "w")
		except:
			print("La ruta específicada ha producido un error.")
			print("Ruta en conflicto: " + str(dirB))
			print("Se escribirá el archivo en la ruta actual...")
			dirA = os.getcwd()
			dirB = dirA + "\\IPC2_Proyecto1_Salida.xml"
			file = open(dirB, "w")

		print("Ruta de salida: " + str(dirB))
		temp_matrix = matrices_l.first

		file.write("<matrices>\n")
		for i in range(matrices_l.cant):			
			reducedN = len(temp_matrix.reduced_frecuence_matrix)
			g = temp_matrix.cant_of_groups

			file.write("	<matriz nombre=\"" + temp_matrix.name + "_Salida\" n=\"" + str(temp_matrix.n) + "\" m=\"" + 
				str(temp_matrix.m) +"\" g=\"" + str(temp_matrix.cant_of_groups) + "\">\n")
			# Escritura de los datos:
			for j in range(reducedN):
				for k in range(temp_matrix.m):
					file.write("		<dato x=\"" + str(j+1) + "\" y=\"" + str(k+1) + "\">"
						+ str(temp_matrix.reduced_frecuence_matrix[j][k]) + "</dato>\n")
			# Escritura de los grupos:
			for j in range(g):
				file.write("		<frecuencia g=\"" + str(j+1) + "\""">" + str(temp_matrix.groups_data[j][0]) + "</frecuencia>\n")
			file.write("	</matriz>\n")
			temp_matrix = temp_matrix.next
		file.write("</matrices>\n")
		# Doc end

		print("Escritura terminada.")
		file.close()
		file = open(dirB)
		dirC = str(dirB)
		#print("Se abrirá el archivo:")
		os.system("IPC2_Proyecto1_Salida.xml")
		print("")

	# Si complete es True, la gráfica es para todo el documento.
	# Si complete es False, la gráfica es para una sola matriz que se pasa como parámetro.
	def writeDOT(self, complete, to_graph_matrix):
		matrices_l = self.matrices			
		dirA = self.output_root
		dirB = dirA + "\\Grafica"
			
		print("Creando gráfica en ruta específicada...")
		try:
			file = open(dirB, "w")
		except:
			print("La ruta específicada ha producido un error.")
			print("Ruta en conflicto: " + str(dirB))
			print("Creando gráfica en la ruta actual...")
			dirA = os.getcwd()
			dirB = dirA + "\\Grafica"
			file = open(dirB, "w")

		print("Ruta de salida: " + str(dirB))

		file.write("digraph Grafica {\n")
		file.write("	{\n")
		file.write("\n")

		if complete:
			temp_matrix = matrices_l.first
			for i in range(matrices_l.cant):
				file.write("		n" + str(i) + " [shape=doublecircle color=red label=\"n=" + str(temp_matrix.n) + "\"]\n")
				file.write("		m" + str(i) + " [shape=doublecircle color=red label=\"m=" + str(temp_matrix.m) + "\"]\n")

				for j in range(temp_matrix.n):
					for k in range(temp_matrix.m):
						file.write("		m" + str(i) + "c" + str(j) + str(k) + " [shape=circle label=\"" + str(temp_matrix.frecuence_matrix[j][k]) + "\"]\n")
				file.write("\n")
				temp_matrix = temp_matrix.next
			file.write("	}\n")

			temp_matrix = matrices_l.first
			for i in range(matrices_l.cant):
				file.write("\n")
				file.write("	Matrices->" + temp_matrix.name + ";\n")
				file.write("\n")
				file.write("		" + temp_matrix.name + "->n" + str(i) + ";\n")
				file.write("		" + temp_matrix.name + "->m" + str(i) + ";\n")

				for j in range(temp_matrix.n):
					file.write("\n")
					for k in range(temp_matrix.m):
						if j == 0:
							file.write("		" + temp_matrix.name + "->" + "m" + str(i) + "c" + str(j) + str(k) + ";\n")
						else:
							file.write("		" + "m" + str(i) + "c" + str(j-1) + str(k) + "->" + "m" + str(i) + "c" + str(j) + str(k) + ";\n")
				temp_matrix = temp_matrix.next
		else:
			file.write("		n [shape=doublecircle color=red label=\"n=" + str(to_graph_matrix.n) + "\"]\n")
			file.write("		m [shape=doublecircle color=red label=\"m=" + str(to_graph_matrix.m) + "\"]\n")
			file.write("	}\n")

			for j in range(to_graph_matrix.n):
					for k in range(to_graph_matrix.m):
						if j == 0:
							file.write("		" + to_graph_matrix.name + "->" + str(to_graph_matrix.frecuence_matrix[j][k]) + ";\n")
						else:
							file.write("		" + str(to_graph_matrix.frecuence_matrix[j-1][k]) + "->" + str(to_graph_matrix.frecuence_matrix[j][k]) + ";\n")
		file.write("}")
		# Doc end

		print("Escritura terminada.")
		file.close()
		file = open(dirB)
		dirC = str(dirB)
		#print("Se abrirá el archivo:")
		os.system("DOT -Tbmp -O Grafica")
		os.system("Grafica.bmp")
		print("")	

