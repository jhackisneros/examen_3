# gestion_datos/csv_manager.py
import csv
from catalogo.book import Book
from usuarios.usuario import User
from datetime import datetime

class CSVManager:
    def __init__(self, libros_file, usuarios_file, prestamos_file):
        self.libros_file = libros_file
        self.usuarios_file = usuarios_file
        self.prestamos_file = prestamos_file

    def guardar_libros(self, libros):
        with open(self.libros_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["titulo", "autor", "genero", "estado"])
            for libro in libros:
                writer.writerow([libro.titulo, libro.autor, libro.genero, libro.estado])

    def cargar_libros(self):
        libros = []
        with open(self.libros_file, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Saltar el encabezado
            for row in reader:
                libro = Book(row[0], row[1], row[2])  # Usamos el genero como string (lo manejaremos más tarde)
                libro.estado = row[3]
                libros.append(libro)
        return libros

    def guardar_usuarios(self, usuarios):
        with open(self.usuarios_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["nombre", "id_usuario"])
            for usuario in usuarios:
                writer.writerow([usuario.nombre, usuario.id_usuario])

    def cargar_usuarios(self):
        usuarios = []
        with open(self.usuarios_file, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Saltar el encabezado
            for row in reader:
                usuario = User(row[0], int(row[1]))
                usuarios.append(usuario)
        return usuarios

    def guardar_prestamo(self, usuario, libro):
        with open(self.prestamos_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([usuario.id_usuario, libro.titulo, "prestado", datetime.now().strftime('%Y-%m-%d %H:%M:%S')])

    def guardar_devolucion(self, usuario, libro):
        with open(self.prestamos_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([usuario.id_usuario, libro.titulo, "devuelto", datetime.now().strftime('%Y-%m-%d %H:%M:%S')])
