from datetime import datetime, timedelta

class Book: 
    def init(self, titulo, autor, genero):
         self.titulo = titulo 
         self.autor = autor 
         self.genero = genero 
         self.estado = "disponible" # puede ser "disponible" o "prestado" self.historial_prestamos = [] self.fecha_prestamo = None self.fecha_devolucion = None
def is_available(self):
    return self.estado == "disponible"

def prestar(self, usuario=None):
    if self.is_available():
        self.estado = "prestado"
        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion = self.fecha_prestamo + timedelta(days=30)
        if usuario:
            self.historial_prestamos.append({
                'usuario': usuario.nombre,
                'fecha_prestamo': self.fecha_prestamo,
                'fecha_devolucion': self.fecha_devolucion
            })
        return True
    return False

def devolver(self):
    if self.estado == "prestado":
        self.estado = "disponible"
        self.fecha_prestamo = None
        self.fecha_devolucion = None
        return True
    return False

def __str__(self):
    return f"{self.titulo} - {self.autor} ({self.estado})"
