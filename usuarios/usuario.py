from datetime import datetime

class User:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.historial_prestamos = []

    def tomar_prestado(self, libro, csv_manager):
        if libro.is_available():
            libro.prestar()
            self.historial_prestamos.append({
                "libro": libro.titulo,
                "fecha_prestamo": libro.fecha_prestamo,
                "fecha_devolucion": libro.fecha_devolucion
            })
            csv_manager.guardar_prestamo(self, libro)  # Guardar préstamo en CSV
        else:
            raise Exception(f"El libro '{libro.titulo}' no está disponible para préstamo.")
