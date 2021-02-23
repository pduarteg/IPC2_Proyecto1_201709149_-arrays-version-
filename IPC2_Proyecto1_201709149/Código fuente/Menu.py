import Lector as LectorClass
import Escritor as WriterClass
import sys
from tkinter import filedialog
from tkinter import *
import re

class Menu:

    lector_obj = LectorClass.Lector()
    writer_obj = WriterClass.Escritor()

    def __init__(self, exit):
        self.exit = exit

    def imprimir_menu(self):
        print("------------------------- MENÚ PRINCIPAL -------------------------")
        print("")
        print(" [1] Cargar archivo")
        print(" [2] Procesar archivo")
        print(" [3] Escribir archivo de salida")
        print(" [4] Mostrar datos del estudiante")
        print(" [5] Generar gráfica")
        print(" [6] Salida")
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
                    try:
                        selected_option_l = int(input())
                    except:
                        print("Error de entrada. Intente de nuevo")
                        print("")
                        continue

                    # Reseteo de datos antes de cualquier intento de carga.
                    if selected_option_l == 1 or selected_option == 2:
                        if self.lector_obj.first_load and self.lector_obj.read_done:
                            self.lector_obj.first_load = False
                        if self.lector_obj.first_load == False:
                            print("Borrando datos anterioes...")
                            self.lector_obj.reset_all_r()

                    if selected_option_l == 1:
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
                    output_root = input()

                    if output_root == "":
                        print("La ruta está vacía.")
                        print("")
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
                print("----------------------------- DATOS -----------------------------")
                print("")
                print("     Nombre: Percy Juventino Duarte Gálvez")
                print("     Carnet: 201709149")
                print("     Curso: Introducción a la Programación y Computación 2")
                print("     Sección: D ")
                print("     Cuarto semestre")
                print("")
                print("-----------------------------------------------------------------")
                print("")
            elif selected_option == 5:
                print("opción 5 elegida")
            elif selected_option == 6:
                self.exit = True
            elif selected_option == 7:
                self.lector_obj.circular_list_of_matrices.print_matrices_data()
            else:
                print("La opción no es válida, intente de nuevo.")
                print("")

