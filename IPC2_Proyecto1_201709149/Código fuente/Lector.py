from tkinter import filedialog
from tkinter import *
from lxml import etree
import re

class Lector:

    file_root = None
    file = None
    file_lines = None

    def open_a_file(self):        
        print("Se cargará un archivo: ")
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
        print("Se cargará el archivo. . .")
        try:
            file = open(self.file_root)
            archivo = etree.parse(self.file_root)
        except:
            print("Archivo no encontrado.")
            print("")
            load_correctly = False

        if load_correctly:
            self.file_lines = file.readlines()

        return load_correctly

    def reset_all_r(self):
        self.file_root = None
        self.file = None        