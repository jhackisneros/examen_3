# interfaz/ventana_principal.py
import tkinter as tk
from tkinter import messagebox
from base_datos.csv_manager import CSVManager
from .formulario_libros import FormularioLibros  # Cambié la importación
from .formulario_usuarios import FormularioUsuarios  # Cambié la importación

class VentanaPrincipal(tk.Tk):
    def __init__(self, libros, usuarios):
        super().__init__()
        self.title("Sistema de Gestión de Biblioteca")
        self.geometry("600x400")

        self.libro_seleccionado = None
        self.usuario_seleccionado = None

        self.csv_manager = CSVManager('libros.csv', 'usuarios.csv', 'prestamos.csv')
        
        # Formulario de libros
        self.formulario_libros = FormularioLibros(self, libros, self.set_libro_seleccionado)
        self.formulario_libros.pack(side=tk.LEFT, padx=10)

        # Formulario de usuarios
        self.formulario_usuarios = FormularioUsuarios(self, usuarios, self.set_usuario_seleccionado)
        self.formulario_usuarios.pack(side=tk.LEFT, padx=10)

        # Botón de préstamo
        self.prestamo_button = tk.Button(self, text="Realizar préstamo", command=self.realizar_prestamo, state=tk.DISABLED)
        self.prestamo_button.pack(pady=10)

    def set_libro_seleccionado(self, libro):
        self.libro_seleccionado = libro

    def set_usuario_seleccionado(self, usuario):
        self.usuario_seleccionado = usuario

    def realizar_prestamo(self):
        if not self.libro_seleccionado or not self.usuario_seleccionado:
            messagebox.showerror("Error", "Debe seleccionar un libro y un usuario.")
            return

        if self.libro_seleccionado.estado == "prestado":
            messagebox.showerror("Error", f"El libro '{self.libro_seleccionado.titulo}' ya está prestado.")
            return

        respuesta = messagebox.askyesno("Confirmar préstamo", f"¿Deseas prestar '{self.libro_seleccionado.titulo}' a {self.usuario_seleccionado.nombre}?")
        
        if respuesta:
            self.usuario_seleccionado.tomar_prestado(self.libro_seleccionado, self.csv_manager)
            messagebox.showinfo("Préstamo realizado", f"{self.usuario_seleccionado.nombre} ha tomado prestado '{self.libro_seleccionado.titulo}'.")
            self.prestamo_button.config(state=tk.DISABLED)
#







