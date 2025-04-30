# prestamos/gestor_prestamos.py

from datetime import datetime, timedelta

class Prestamo:
    def __init__(self, libro):
        self.libro = libro
        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion = self.fecha_prestamo + timedelta(days=30)

    def __str__(self):
        return f"{self.libro.titulo} - Prestado: {self.fecha_prestamo.strftime('%Y-%m-%d %H:%M:%S')} - Dev: {self.fecha_devolucion.strftime('%Y-%m-%d')}"

class GestorPrestamos:
    def __init__(self, csv_manager):
        self.csv_manager = csv_manager

    def realizar_prestamo(self, usuario, libro):
        if not libro.is_available():
            raise Exception(f"El libro '{libro.titulo}' no está disponible para préstamo.")

        prestamo = Prestamo(libro)
        libro.prestar(prestamo.fecha_prestamo, prestamo.fecha_devolucion)

        usuario.historial_prestamos.append(prestamo)

        self.csv_manager.guardar_prestamo(usuario, libro)
        self.csv_manager.actualizar_libros()
