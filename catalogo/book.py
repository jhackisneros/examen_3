# catalogo/book.py
from catalogo.book_genre import BookGenre

class Book:
    def __init__(self, titulo, autor, genero: BookGenre, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.disponible = disponible

    def is_available(self):
        return self.disponible

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True
        return False

    def devolver(self):
        self.disponible = True
