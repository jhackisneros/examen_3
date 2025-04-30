from datetime import datetime, timedelta
from enum import Enum

class BookGenre(Enum):
    FICTION = "Ficción"
    NONFICTION = "No Ficción"
    SCIENCE = "Ciencia"
    ART = "Arte"

class Book:
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.estado = "disponible"  # "disponible" o "prestado"
        self.fecha_prestamo = None
        self.fecha_devolucion = None

    def is_available(self):
        return self.estado == "disponible"

    def prestar(self):
        if self.estado == "disponible":
            self.estado = "prestado"
            self.fecha_prestamo = datetime.now()
            self.fecha_devolucion = self.fecha_prestamo + timedelta(days=30)  # 30 días de préstamo
        else:
            raise Exception(f"El libro '{self.titulo}' ya está prestado.")

    def devolver(self):
        if self.estado == "prestado":
            self.estado = "disponible"
            self.fecha_prestamo = None
            self.fecha_devolucion = None
        else:
            raise Exception(f"El libro '{self.titulo}' no está prestado.")
