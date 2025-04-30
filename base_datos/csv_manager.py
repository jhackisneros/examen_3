import csv
from catalogo.book import Book
from usuarios.usuario import Usuario
from datetime import datetime

class CSVManager:
    def __init__(self, libros_file, usuarios_file, prestamos_file):
        self.libros_file = libros_file
        self.usuarios_file = usuarios_file
        self.prestamos_file = prestamos_file

    def cargar_libros(self):
        libros = []
        with open(self.libros_file, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    libro = Book(row[0], row[1], row[2])
                    libros.append(libro)
        return libros

    def cargar_usuarios(self):
        usuarios = []
        with open(self.usuarios_file, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    usuario = Usuario(row[0], row[1])
                    usuarios.append(usuario)
        return usuarios

    def guardar_prestamo(self, usuario, libro):
        with open(self.prestamos_file, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([usuario.nombre, libro.titulo, libro.fecha_prestamo.strftime('%Y-%m-%d'), libro.fecha_devolucion.strftime('%Y-%m-%d')])
