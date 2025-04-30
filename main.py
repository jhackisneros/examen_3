# main.py
from base_datos.csv_manager import CSVManager
from catalogo.book import Book
from catalogo.book_genre import BookGenre
from usuarios.usuario import User

def main():
    # Inicializar el CSVManager con archivos de datos
    csv_manager = CSVManager('libros.csv', 'usuarios.csv', 'prestamos.csv')

    # Cargar libros y usuarios desde CSV
    libros = csv_manager.cargar_libros()
    usuarios = csv_manager.cargar_usuarios()

    # Crear un nuevo usuario
    usuario = User("Carlos Sánchez", 3)
    usuarios.append(usuario)

    # Crear un nuevo libro si no existe en la base de datos
    libro1 = Book("El Quijote", "Miguel de Cervantes", "FICTION")
    libros.append(libro1)

    # Realizar un préstamo
    usuario.tomar_prestado(libro1, csv_manager)

    # Guardar cambios en los archivos CSV
    csv_manager.guardar_libros(libros)
    csv_manager.guardar_usuarios(usuarios)

if __name__ == "__main__":
    main()
