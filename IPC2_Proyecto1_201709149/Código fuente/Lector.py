from tkinter import filedialog
from tkinter import *
import re

class Lector:

    file_root = None
    file = None

    def open_a_file(self):        
        print("Se cargará un archivo: ")
        error_viewer = False
        try:
            root = Tk()
            root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                filetypes=(("Input Files [LFP]", "*.lfp"), ("all files", "*.*")))            
            self.file_root = root.filename            
        except:
            print("Error de directorio")
            error_viewer = True

        if error_viewer == False:
            if self.file_root == "":
                print("Dirección vacía.")

    # Lee todas las lineas, y clasifica en lsitas para odenar, buscar y ambas.
    def read_file(self):
        print("")
        print("Se leerán todas las listas. . .")
        file = open(self.file_root)
        self.lines_list = file.readlines()

        # Filtrar: elimina todas las lineas leidas que no se consideren una lista.
        changes = True
        while changes:
            changes = False
            for i in range(len(self.lines_list)):
                if re.search(r"ORDENAR", str(self.lines_list[i])) or re.search("BUSCAR", str(self.lines_list[i])):
                    continue
                else:
                    changes = True
                    self.lines_list.pop(i)
                    break
        # ---

        self.cantidad_filas = len(self.lines_list)
        file.close()

        for i in range(self.cantidad_filas):            
                if re.search(self.pattern_order, str(self.lines_list[i])) or re.search(self.pattern_search, str(self.lines_list[i])):
                    self.order_and_search_list.append(self.lines_list[i])

                if re.search(self.pattern_search, str(self.lines_list[i])):
                    self.to_search_list.append(self.lines_list[i])

                if re.search(self.pattern_order, str(self.lines_list[i])):
                    self.to_order_list.append(self.lines_list[i])            

        self.ordered = False
        self.searched = False
        self.all_results = False
        print("Listas cargadas.")
        print("---")


    def reset_all_r(self):
        self.file_root = None
        self.file = None        