import csv
from catalogo.book import Book
from datetime import datetime
from usuarios.usuario import Usuario

class CSVManager:
    def __init__(self, libros_file, usuarios_file, prestamos_file):
        self.libros_file = libros_file
        self.usuarios_file = usuarios_file
        self.prestamos_file = prestamos_file

        self.libros = self.cargar_libros()
        self.usuarios = self.cargar_usuarios()

    def cargar_libros(self):
        libros = []
        with open(self.libros_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    libro = Book(row[0], row[1], row[2])
                    if len(row) > 3:
                        libro.estado = row[3]
                    if len(row) > 4 and row[4]:
                        libro.fecha_prestamo = datetime.strptime(row[4], '%Y-%m-%d %H:%M:%S')
                    if len(row) > 5 and row[5]:
                        libro.fecha_devolucion = datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S')
                    libros.append(libro)
        return libros

    def cargar_usuarios(self):
        usuarios = []
        with open(self.usuarios_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    usuario = Usuario(row[0], row[1])
                    usuarios.append(usuario)
        return usuarios

    def guardar_prestamo(self, usuario, libro):
        with open(self.prestamos_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                usuario.nombre,
                libro.titulo,
                libro.fecha_prestamo.strftime('%Y-%m-%d %H:%M:%S'),
                libro.fecha_devolucion.strftime('%Y-%m-%d %H:%M:%S')
            ])

    def actualizar_libros(self):
        with open(self.libros_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            for libro in self.libros:
                writer.writerow([
                    libro.titulo,
                    libro.autor,
                    libro.genero,
                    libro.estado,
                    libro.fecha_prestamo.strftime('%Y-%m-%d %H:%M:%S') if libro.fecha_prestamo else '',
                    libro.fecha_devolucion.strftime('%Y-%m-%d %H:%M:%S') if libro.fecha_devolucion else ''
                ])
