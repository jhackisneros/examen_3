from datetime import datetime, timedelta

class Book:
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.estado = "disponible"
        self.fecha_prestamo = None
        self.fecha_devolucion = None

    def is_available(self):
        return self.estado == "disponible"

    def prestar(self):
        if self.is_available():
            self.estado = "prestado"
            self.fecha_prestamo = datetime.now()
            self.fecha_devolucion = self.fecha_prestamo + timedelta(days=30)
        else:
            raise Exception(f"El libro '{self.titulo}' no está disponible para préstamo.")

    def devolver(self):
        if self.estado == "prestado":
            self.estado = "disponible"
            self.fecha_prestamo = None
            self.fecha_devolucion = None
        else:
            raise Exception(f"El libro '{self.titulo}' no está prestado actualmente.")

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.estado})"
