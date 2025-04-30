from datetime import datetime, timedelta

class Book:
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.disponible = True
        self.historial_prestamos = []  # Para almacenar el historial de préstamos
        self.fecha_prestamo = None
        self.fecha_devolucion = None

    def is_available(self):
        return self.disponible

    def prestar(self, usuario):
        if self.disponible:
            self.disponible = False
            self.fecha_prestamo = datetime.now()
            self.fecha_devolucion = self.fecha_prestamo + timedelta(days=30)  # Un mes para devolverlo
            # Añadir el préstamo al historial
            self.historial_prestamos.append({
                'usuario': usuario.nombre,
                'fecha_prestamo': self.fecha_prestamo,
                'fecha_devolucion': self.fecha_devolucion
            })
            return True
        return False

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            self.fecha_prestamo = None
            self.fecha_devolucion = None
            return True
        return False
