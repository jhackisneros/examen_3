# prestamos/gestor_prestamos.py

class GestorPrestamos:
    def __init__(self, csv_manager):
        self.csv_manager = csv_manager

    def realizar_prestamo(self, usuario, libro):
        if not libro.is_available():
            raise Exception(f"El libro '{libro.titulo}' no está disponible para préstamo.")

        # Marcar libro como prestado
        libro.prestar()

        # Registrar en historial del usuario como diccionario
        usuario.historial_prestamos.append({
            'usuario': usuario.nombre,
            'libro': libro.titulo,
            'fecha_prestamo': libro.fecha_prestamo,
            'fecha_devolucion': libro.fecha_devolucion
        })

        # Guardar en CSV
        self.csv_manager.guardar_prestamo(usuario, libro)

        # Si tienes método para actualizar libros, descomenta esta línea:
        # self.csv_manager.actualizar_libros()
