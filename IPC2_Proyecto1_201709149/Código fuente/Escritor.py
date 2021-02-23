import Lector as LectorClass
import re
import os

class Escritor:

	def initial_data_request(self, matrices, output_root):
		self.matrices = matrices
		self.output_root = output_root


	def writeXML(self):
		matrices_l = self.matrices
		#dirA = os.getcwd()
		dirA = self.output_root
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
		#os.system("IPC2_Proyecto1_Salida.xml")
		print("")

	def reset_all_w(self):
		self.table_content = []		
		self.lines_list = []