# gestion_empleado/employee.py
from gestion_usuario.user import User
from catalogo.book import Book
from typing import List

class Employee:
    def __init__(self, nombre, id_empleado):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.usuarios: List[User] = []  # Lista de usuarios gestionados

    def registrar_usuario(self, usuario: User):
        """Registrar un nuevo usuario en el sistema."""
        self.usuarios.append(usuario)
        print(f"Usuario {usuario.nombre} registrado exitosamente.")

    def gestionar_libros(self, libro: Book, accion: str):
        """Gestiona libros: 'añadir' o 'eliminar'."""
        if accion == "añadir":
            print(f"El libro {libro.titulo} ha sido añadido a la biblioteca.")
        elif accion == "eliminar":
            print(f"El libro {libro.titulo} ha sido eliminado de la biblioteca.")
        else:
            print("Acción no válida.")
