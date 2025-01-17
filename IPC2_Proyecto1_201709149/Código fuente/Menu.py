import Lector as LectorClass
import Escritor as WriterClass
import sys
from tkinter import filedialog
from tkinter import *
import re
import os

class Menu:

    lector_obj = LectorClass.Lector()
    writer_obj = WriterClass.Escritor()

    def __init__(self, exit):
        self.exit = exit

    def imprimir_menu(self):
        print(" ****************************************************************************")
        print(" *                              MENÚ PRINCIPAL                              *")
        print(" ****************************************************************************")
        print("")
        print("  [1] Cargar archivo")
        print("  [2] Procesar archivo")
        print("  [3] Escribir archivo de salida")
        print("  [4] Mostrar datos del estudiante")
        print("  [5] Generar gráfica")
        print("  [6] Salir")
        print("")
        print("Escriba el número de acuerdo a la opción que desee: ")

    def imprimir_menu_de_carga(self):
        print("")
        print("---------------- Carga de archivos: ----------------")
        print("")
        print(" [1] Escribir dirección")
        print(" [2] Seleccionar archivo")
        print(" [3] Regresar al menú principal")
        print("")
        print("Escriba el número de acuerdo a la opción que desee: ")

    def print_graph_menu(self):
        print("")
        print("--------------- Creación de gráficas: ---------------")
        print("")
        print("Matrices actuales en memoria:")
        print("")
        last = self.lector_obj.print_matrices_names()
        print(" [" + str(last) + "] Graficar todas")
        print(" [" + str(last + 1) + "] Regresar al menú principal")
        print("")
        print("Escriba el número de acuerdo a la matríz que desee graficar, todas o para cancelar.")

    def request_of_graph(self):
            m_cant = self.lector_obj.circular_list_of_matrices.cant
            while True:
                self.print_graph_menu()
                selected_option_g = 0
                try:
                    selected_option_g = int(input())
                except:
                    print("Error de entrada. Intente de nuevo.")
                    print("")
                    continue

                print("La opcion a graficar fue: " + str(selected_option_g))
                if selected_option_g > 0 and selected_option_g <= m_cant:
                    to_graph_matrix = self.lector_obj.circular_list_of_matrices.first

                    for i in range(selected_option_g - 1):
                        to_graph_matrix = to_graph_matrix.next
                    print("Se iniciará la escritura del archivo DOT...")
                    self.writer_obj.writeDOT(False, to_graph_matrix)
                elif selected_option_g == (m_cant + 1):
                    print("Se graficarán todas")
                    print("Se iniciará la escritura del archivo DOT...")
                    self.writer_obj.writeDOT(True, None)
                    break
                elif selected_option_g == (m_cant + 2):
                    print("")
                    break

    def iniciar_menu(self):
        while(self.exit == False):
            self.imprimir_menu()
            try:
                selected_option = int(input())
            except:
                print("Error de entrada. Intente de nuevo")
                print("")
                continue
            if selected_option == 1:
                back = False
                while back == False:
                    self.imprimir_menu_de_carga()
                    selected_option_l = 0
                    try:
                        selected_option_l = int(input())
                    except:
                        print("Error de entrada. Intente de nuevo")
                        print("")
                        continue

                    if selected_option_l == 1:
                        if self.lector_obj.read_done:
                            print("Borrando datos anterioes...")
                        self.lector_obj.reset_all_r()

                        print("Escriba una ruta específica:")
                        root = input()
                        if root == "":
                            print("Dirección vacía.")
                            print("")
                        else:
                            self.lector_obj.file_root = root
                            if self.lector_obj.read_file():
                                print("Carga realizada exitosamente.")
                                print("")
                                self.lector_obj.read_done = True                                
                                back = True
                    elif selected_option_l == 2:
                        if self.lector_obj.read_done:
                            print("Borrando datos anterioes...")
                        self.lector_obj.reset_all_r()

                        print("Elija el archivo para cargarlo:")
                        if self.lector_obj.open_a_file():
                            if self.lector_obj.read_file():
                                print("Carga realizada exitosamente.")
                                print("")
                                self.lector_obj.read_done = True
                                back = True
                    elif selected_option_l == 3:
                        print("Regresando al menú principal.")
                        print("")
                        back = True
                    else:
                        print("La opción no es válida, intente de nuevo.")
                        print("")                
            elif selected_option == 2:                
                print("Se leerán los datos del archivo cargado...")
                if self.lector_obj.read_done:
                    self.lector_obj.proces_file()
                else:
                    print("No se ha cargado un archivo.")
                    print("")
            elif selected_option == 3:
                print("Se solicitará la escritura de archivo de salida...")
                if self.lector_obj.request_output_file_write():
                    print("Se iniciará la escritura del archivo...")
                    print("Ingrese un directorio específico: ")
                    print("* Nota: deje vacío para escribir en ruta actual.")
                    output_root = input()

                    if output_root == "":
                        print("La ruta está vacía.")
                        print("Se creará el archivo en el direcotrio actual.")
                        self.writer_obj.initial_data_request(self.lector_obj.circular_list_of_matrices, output_root)
                        self.writer_obj.writeXML()
                    elif re.search(r"[*?<>|]", output_root):
                        print("Se encontraron carácteres no permitidos.")
                    else:
                        print("Se escribirá el archivo en la ruta: ")
                        print(output_root)
                        self.writer_obj.initial_data_request(self.lector_obj.circular_list_of_matrices, output_root)
                        self.writer_obj.writeXML()
                else:
                    print("No hay datos cargados o procesados para crear un archivo de salida.")
                    print("")
            elif selected_option == 4:
                print("")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DATOS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("|                                                                 |")
                print("|     Nombre: Percy Juventino Duarte Gálvez                       |")
                print("|     Carnet: 201709149                                           |")
                print("|     Curso: Introducción a la Programación y Computación 2       |")
                print("|     Sección: \"D\"                                                |")
                print("|     Cuarto semestre de Ingeniería en Ciencias y Sistemas        |")
                print("|     Primer semestre 2021                                        |")
                print("|                                                                 |")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("")
            elif selected_option == 5:
                print("Se solicitará la escritura de gráfica...")
                if self.lector_obj.request_output_file_write():
                    # Solicitud de ruta iniciada
                    # print("Se iniciará la escritura del archivo DOT...")
                    # print("Ingrese un directorio específico: ")
                    # print("* Nota: deje vacío para escribir en ruta actual.")
                    # output_root = input()

                    # if output_root == "":
                    #     print("La ruta está vacía.")
                    #     print("Se creará el archivo en el directorio actual.")
                    #     self.writer_obj.initial_data_request(self.lector_obj.circular_list_of_matrices, output_root)
                    #     self.request_of_graph()
                    # elif re.search(r"[*?<>|]", output_root):
                    #     print("Se encontraron carácteres no permitidos.")
                    # else:
                    #     print("Se escribirá el archivo en la ruta: ")
                    #     print(output_root)
                    #     self.writer_obj.initial_data_request(self.lector_obj.circular_list_of_matrices, output_root)
                    #     self.request_of_graph()
                    # Solicitud de ruta fin.
                    self.writer_obj.initial_data_request(self.lector_obj.circular_list_of_matrices, "")
                    self.request_of_graph()
                else:
                    print("No hay datos cargados o procesados para crear un archivo de salida.")
                    print("")
            elif selected_option == 6:
                self.exit = True
            elif selected_option == 7:
                self.lector_obj.circular_list_of_matrices.print_matrices_data()
            else:
                print("La opción no es válida, intente de nuevo.")
                print("")