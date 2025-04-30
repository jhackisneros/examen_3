import csv
from catalogo.book import Book
from datetime import datetime
from catalogo.book import Book  # Importar la clase Book
from usuarios.usuario import Usuario  # Importar la clase User

class CSVManager:
    def __init__(self, libros_file, usuarios_file, prestamos_file):
        self.libros_file = libros_file
        self.usuarios_file = usuarios_file
        self.prestamos_file = prestamos_file

        # Cargar datos de los archivos CSV
        self.libros = self.cargar_libros()
        self.usuarios = self.cargar_usuarios()

    def cargar_libros(self):
        libros = []
        with open(self.libros_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  # Verifica que la fila no esté vacía
                    libro = Book(row[0], row[1], row[2])  # Crear libro con la información cargada del CSV
                    libros.append(libro)
        return libros

    def cargar_usuarios(self):
        usuarios = []
        with open(self.usuarios_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  # Verifica que la fila no esté vacía
                    usuario = Usuario(row[0], row[1])  # Crear usuario con nombre e ID
                    usuarios.append(usuario)
        return usuarios

    def guardar_prestamo(self, usuario, libro):
        with open(self.prestamos_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([usuario.nombre, libro.titulo, libro.fecha_prestamo, libro.fecha_devolucion])
