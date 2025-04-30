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

    def prestar(self, usuario, libro):
        """Marca el libro como prestado y registra el préstamo."""
        if self.is_available():
            self.estado = "prestado"
            self.fecha_prestamo = datetime.now()
            self.fecha_devolucion = self.fecha_prestamo + timedelta(days=30)
            if usuario:
                if hasattr(usuario, 'nombre'):
                    self.historial_prestamos.append({
                        'usuario': usuario.nombre,
                        'libro': libro.titulo,
                        'fecha_prestamo': self.fecha_prestamo,
                        'fecha_devolucion': self.fecha_devolucion
                    })
                else:
                    raise AttributeError("El objeto usuario no tiene un atributo 'nombre'.")
            return True
        else:
            raise Exception(f"El libro '{self.titulo}' no está disponible para préstamo.")

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