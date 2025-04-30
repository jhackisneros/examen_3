from datetime import datetime, timedelta

class Prestamo:
    def init(self, libro):
         self.libro = libro    
         self.fecha_prestamo = datetime.now() 
         self.fecha_devolucion = self.fecha_prestamo + timedelta(days=30)
def __str__(self):
    return (
        f"Libro: {self.libro.titulo}\n"
        f"Fecha de préstamo: {self.fecha_prestamo.strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"Fecha límite: {self.fecha_devolucion.strftime('%Y-%m-%d %H:%M:%S')}"
    )

         
def tomar_prestado(self, libro, csv_manager):
    if libro.is_available():
        libro.prestar()
        prestamo = Prestamo(libro)
        self.historial_prestamos.append(prestamo)
        csv_manager.guardar_prestamo(self, libro)
    else:
        raise Exception(f"El libro '{libro.titulo}' no está disponible para préstamo.")

def mostrar_historial(self):
    if not self.historial_prestamos:
        return "No hay préstamos en el historial."
    return "\n\n".join(f"{i+1}. {str(prestamo)}" for i, prestamo in enumerate(self.historial_prestamos))
