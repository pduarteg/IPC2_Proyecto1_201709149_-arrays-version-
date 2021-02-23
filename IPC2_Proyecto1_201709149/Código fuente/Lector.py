from tkinter import filedialog
from tkinter import *
from xml.dom import minidom
import re
import Matrices
import Matriz

class Lector:

    file_root = None
    file = None
    read_done = False
    procesed_data = False

    circular_list_of_matrices = None

    first_load = True

    def open_a_file(self):
        print("Se cargará un archivo...")
        open_correctly = True
        try:
            root = Tk()
            root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                filetypes=(("Input Files [IPC2]", "*.xml"), ("all files", "*.*")))            
            self.file_root = root.filename            
        except:
            print("Error de directorio")
            open_correctly = False

        if open_correctly == True:
            if self.file_root == "":
                print("Dirección vacía.")
                print("")

        return open_correctly
    
    def read_file(self):
        load_correctly = True
        print("")
        print("Se leerá el directorio...")
        try:
            self.file = minidom.parse(self.file_root)
        except:
            print("Archivo no encontrado.")
            print("")
            load_correctly = False

        return load_correctly

    def proces_file(self):
        if self.procesed_data == False:
            print("Se leerán las matrices...")
            list_of_matrices = self.file.getElementsByTagName("matriz")        
            cant_of_matrices = len(list_of_matrices)

            if cant_of_matrices != 0:
                print("Creando matrices de frecuencia de accesos...")
                self.circular_list_of_matrices = Matrices.Matrices()

                for i in range(cant_of_matrices):
                    matrix_name = list_of_matrices[i].attributes["nombre"].value
                    n = int(list_of_matrices[i].attributes["n"].value)
                    m = int(list_of_matrices[i].attributes["m"].value)

                    print("Creando la matriz: #" + str(i+1) + "...")            

                    matrix_base = [[0] * m for i in range(n)]
                    data_list = list_of_matrices[i].getElementsByTagName("dato")

                    for j in range(n*m):
                        #Valores de fila y columna (menos uno para ajustar el índice)
                        x = int(data_list[j].attributes["x"].value) - 1
                        y = int(data_list[j].attributes["y"].value) - 1

                        if x > (n-1) or y > (m-1):
                            print("")
                            print("Se ha encontrado un parámetro que excede el tamaño permitido en la matriz #"
                                + str(i) + ", se cancelará el proceso de esta matríz.")
                            print("")
                            break

                        dato = int(data_list[j].childNodes[0].data)
                        
                        #print("dato = " + str(dato))

                        #print("n*m = " + str(n*m))
                        #print("j: " + str(j))
                        #print("x: " + str(x))
                        #print("y: " + str(y))
                        matrix_base[x][y] = dato

                    self.circular_list_of_matrices.add_matrix(Matriz.Matriz(n, m, matrix_name, matrix_base))
                print("Matrices creadas.")
                print("Creando matrices de patrón de accesos...")
                self.circular_list_of_matrices.construct_pattern_matrices()
                print("Creando matrices reducidas...")
                self.circular_list_of_matrices.construct_reduced_matrices()
                self.procesed_data = True
                print("Procesado de datos finalizado.")
                print("")
                print("Se imprimirán los datos de las matrices:")
                self.circular_list_of_matrices.print_matrices_data()
                print("")
            else:
                print("")
                print("No se han encontrado matrices.")
                print("")
        else:
            print("Ya se han procesado los datos para el actual archivo cargado en memoria.")
            print("")

    def reset_all_r(self):
        self.file_root = None
        self.file = None
        self.read_done = False
        self.circular_list_of_matrices = None
        self.procesed_data = False
