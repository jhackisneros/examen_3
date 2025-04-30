from datetime import datetime, timedelta

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.historial_prestamos = []

    def tomar_prestado(self, libro, csv_manager):
        if libro.is_available():
            libro.prestar()

            prestamo_info = {
                'usuario': self.nombre,
                'libro': libro.titulo,
                'fecha_prestamo': libro.fecha_prestamo,
                'fecha_devolucion': libro.fecha_devolucion
            }

            self.historial_prestamos.append(prestamo_info)
            csv_manager.guardar_prestamo(self, libro)
        else:
            raise Exception(f"El libro '{libro.titulo}' no está disponible para préstamo.")

    def mostrar_historial(self):
        if not self.historial_prestamos:
            return "No hay préstamos en el historial."
        return "\n".join(
            f"{i+1}. Libro: {p['libro']}, Desde: {p['fecha_prestamo'].strftime('%Y-%m-%d')}, Hasta: {p['fecha_devolucion'].strftime('%Y-%m-%d')}"
            for i, p in enumerate(self.historial_prestamos)
        )
