# interfaz/formulario_libros.py
import tkinter as tk
from catalogo.book import Book

class FormularioLibros(tk.Frame):
    def __init__(self, parent, libros, callback):
        super().__init__(parent)
        self.libros = libros
        self.callback = callback
        self.create_widgets()

    def create_widgets(self):
        self.libro_label = tk.Label(self, text="Selecciona un libro:")
        self.libro_label.pack()

        self.libro_listbox = tk.Listbox(self, height=10, width=50)
        for libro in self.libros:
            if libro.estado == "disponible":
                self.libro_listbox.insert(tk.END, libro.titulo)
        self.libro_listbox.pack()

        self.libro_seleccionado_label = tk.Label(self, text="Libro seleccionado:")
        self.libro_seleccionado_label.pack()

        self.libro_seleccionado_text = tk.Label(self, text="", width=50)
        self.libro_seleccionado_text.pack()

        # Vincular el evento de selección
        self.libro_listbox.bind("<<ListboxSelect>>", self.actualizar_libro)

    def actualizar_libro(self, event):
        selected_libro_index = self.libro_listbox.curselection()
        if selected_libro_index:
            libro_seleccionado = self.libros[selected_libro_index[0]]
            if libro_seleccionado.estado == "disponible":
                self.libro_seleccionado_text.config(text=f"{libro_seleccionado.titulo} de {libro_seleccionado.autor}")
                self.callback(libro_seleccionado)  # Actualiza el libro seleccionado en la ventana principal
