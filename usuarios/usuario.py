# usuarios/usuario.py
from catalogo.book import Book

class User:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.historial_prestamos = []  # Lista de libros prestados

    def tomar_prestado(self, libro: Book, csv_manager):
        if libro.is_available():
            libro.prestar()
            self.historial_prestamos.append(libro)
            csv_manager.guardar_prestamo(self, libro)
            print(f"{self.nombre} ha tomado prestado {libro.titulo}.")
        else:
            print(f"{libro.titulo} no está disponible para préstamo.")

    def devolver_libro(self, libro: Book, csv_manager):
        if libro in self.historial_prestamos:
            libro.devolver()
            self.historial_prestamos.remove(libro)
            csv_manager.guardar_devolucion(self, libro)
            print(f"{self.nombre} ha devuelto {libro.titulo}.")
        else:
            print(f"{self.nombre} no tiene {libro.titulo} prestado.")
