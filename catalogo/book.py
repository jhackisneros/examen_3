# catalogo/book.py
from catalogo.book_genre import BookGenre

class Book:
    def __init__(self, titulo, autor, genero, estado="disponible"):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero  # Ahora usamos BookGenre
        self.estado = estado

    def is_available(self):
        return self.estado == "disponible"

    def prestar(self):
        if self.is_available():
            self.estado = "prestado"
            return True
        return False

    def devolver(self):
        if not self.is_available():
            self.estado = "disponible"
            return True
        return False
