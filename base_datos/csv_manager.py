# gestion_datos/csv_manager.py
import csv
import os
from catalogo.book import Book
from usuarios.usuario import User
from datetime import datetime

class CSVManager:
    def __init__(self, libros_file, usuarios_file, prestamos_file):
        self.libros_file = libros_file
        self.usuarios_file = usuarios_file
        self.prestamos_file = prestamos_file

        # Verificar si los archivos existen, si no, crearlos con datos iniciales
        self.crear_archivos_iniciales()

    def crear_archivos_iniciales(self):
        if not os.path.exists(self.libros_file):
            with open(self.libros_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["titulo", "autor", "genero", "estado"])  # Encabezados de los libros
                # Datos de ejemplo
                libros_iniciales = [
                    Book("Cien Años de Soledad", "Gabriel García Márquez", "FICTION", "disponible"),
                    Book("Breve Historia del Tiempo", "Stephen Hawking", "SCIENCE", "disponible")
                ]
                for libro in libros_iniciales:
                    writer.writerow([libro.titulo, libro.autor, libro.genero, libro.estado])

        if not os.path.exists(self.usuarios_file):
            with open(self.usuarios_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["nombre", "id_usuario"])  # Encabezados de los usuarios
                # Datos de ejemplo
                usuarios_iniciales = [
                    User("Juan Pérez", 1),
                    User("Ana Gómez", 2)
                ]
                for usuario in usuarios_iniciales:
                    writer.writerow([usuario.nombre, usuario.id_usuario])

        if not os.path.exists(self.prestamos_file):
            with open(self.prestamos_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["id_usuario", "titulo_libro", "estado", "fecha"])  # Encabezados de los préstamos

    def guardar_libros(self, libros):
        with open(self.libros_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["titulo", "autor", "genero", "estado"])  # Encabezados
            for libro in libros:
                writer.writerow([libro.titulo, libro.autor, libro.genero, libro.estado])

    def cargar_libros(self):
        libros = []
        with open(self.libros_file, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Saltar el encabezado
            for row in reader:
                libro = Book(row[0], row[1], row[2], row[3])  # Usamos el genero como string
                libros.append(libro)
        return libros

    def guardar_usuarios(self, usuarios):
        with open(self.usuarios_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["nombre", "id_usuario"])  # Encabezados
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
