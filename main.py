# main.py
from catalogo.book import Book
from catalogo.book_genre import BookGenre

def main():
    # Crear libros
    libro1 = Book("Cien Años de Soledad", "Gabriel García Márquez", BookGenre.FICTION)
    libro2 = Book("Breve Historia del Tiempo", "Stephen Hawking", BookGenre.SCIENCE)

    # Verificar disponibilidad
    print(libro1.is_available())  # True
    print(libro2.is_available())  # True

    # Prestar un libro
    libro1.prestar()
    print(libro1.is_available())  # False

    # Devolver un libro
    libro1.devolver()
    print(libro1.is_available())  # True

if __name__ == "__main__":
    main()
