from datetime import datetime, timedelta

class Book: 
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo 
        self.autor = autor 
        self.genero = genero 
        self.estado = "disponible"  # Puede ser "disponible" o "prestado"
        self.historial_prestamos = []  # Lista para registrar los préstamos
        self.fecha_prestamo = None
        self.fecha_devolucion = None

    def is_available(self):
        """Verifica si el libro está disponible para préstamo."""
        return self.estado == "disponible"

    def realizar_prestamo(self, usuario, libro):
        if not libro.is_available():
            raise Exception(f"El libro '{libro.titulo}' no está disponible para préstamo.")

        # Registrar el préstamo
        libro.prestar(usuario)

        # Crear un objeto Prestamo y agregarlo al historial del usuario
        prestamo = prestamo(libro)
        usuario.historial_prestamos.append(prestamo)

        # Guardar el préstamo en el archivo CSV
        self.csv_manager.guardar_prestamo(usuario, libro)

    def devolver(self):
        """Marca el libro como disponible."""
        if self.estado == "prestado":
            self.estado = "disponible"
            self.fecha_prestamo = None
            self.fecha_devolucion = None
            return True
        else:
            raise Exception(f"El libro '{self.titulo}' no está prestado actualmente.")

    def __str__(self):
        """Devuelve una representación en texto del libro."""
        return f"{self.titulo} - {self.autor} ({self.estado})"