import Lector as LectorClass
import Escritor as Writer
import sys
from tkinter import filedialog
from tkinter import *

class Menu:

    lector_obj = LectorClass.Lector()

    def __init__(self, exit):
        self.exit = exit

    def imprimir_menu(self):
        print("----------- MENÚ PRINCIPAL -----------")
        print("")
        print(" [1] Cargar archivo")
        print(" [2] Procesar archivo")
        print(" [3] Escribir archivo de salida")
        print(" [4] Mostrar datos del estudiante")
        print(" [5] Generar gráfica")
        print(" [6] Salida")
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
                self.lector_obj.reset_all_r()               
                self.lector_obj.open_a_file()
            elif selected_option == 2:                
                
            elif selected_option == 3:
                
            elif selected_option == 4:
                print("-------------------------------------------------------")
                print("------------------------ DATOS ------------------------")
                print("")
                print("     Nombre: Percy Juventino Duarte Gálvez")
                print("     Carnet: 201709149")
                print("     Curso: Introducción a la Programación y Computación 2")
                print("     Sección: D ")
                print("     Cuarto semestre")
                print("")
                print("-------------------------------------------------------")
                print("")
            elif selected_option == 5:
                
            elif selected_option == 6:
                self.exit = True
            else:
                print("La opción no es válida, intente de nuevo.")
                print("")

