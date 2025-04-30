# interfaz/ventana_principal.py
import tkinter as tk
from tkinter import messagebox
from base_datos.csv_manager import CSVManager
from .formulario_libros import FormularioLibros
from .formulario_usuarios import FormularioUsuarios
from datetime import datetime

class VentanaPrincipal(tk.Tk):
    def __init__(self, libros, usuarios):
        super().__init__()
        self.title("Sistema de Gestión de Biblioteca")
        self.geometry("800x500")

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

        # Mostrar libros no disponibles
        self.libros_no_disponibles_label = tk.Label(self, text="Libros no disponibles:", font=("Helvetica", 12))
        self.libros_no_disponibles_label.pack()

        self.libros_no_disponibles_listbox = tk.Listbox(self, height=5, width=50)
        self.libros_no_disponibles_listbox.pack(pady=10)

        # Mostrar historial de préstamos
        self.historial_label = tk.Label(self, text="Historial de Préstamos:", font=("Helvetica", 12))
        self.historial_label.pack()

        self.historial_listbox = tk.Listbox(self, height=5, width=50)
        self.historial_listbox.pack(pady=10)

    def set_libro_seleccionado(self, libro):
        self.libro_seleccionado = libro
        self.check_button_state()

    def set_usuario_seleccionado(self, usuario):
        self.usuario_seleccionado = usuario
        self.check_button_state()

    def check_button_state(self):
        if self.libro_seleccionado and self.usuario_seleccionado:
            self.prestamo_button.config(state=tk.NORMAL)
        else:
            self.prestamo_button.config(state=tk.DISABLED)

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

            # Actualizar libros no disponibles
            self.actualizar_libros_no_disponibles()

            # Actualizar historial
            self.actualizar_historial()

            self.prestamo_button.config(state=tk.DISABLED)

    def actualizar_libros_no_disponibles(self):
        # Limpiar la lista
        self.libros_no_disponibles_listbox.delete(0, tk.END)
        for libro in self.csv_manager.libros:
            if libro.estado == "prestado":
                self.libros_no_disponibles_listbox.insert(tk.END, f"{libro.titulo} (Dev. {libro.fecha_devolucion.strftime('%Y-%m-%d')})")

    def actualizar_historial(self):
        # Limpiar la lista
        self.historial_listbox.delete(0, tk.END)
        for usuario in self.csv_manager.usuarios:
            for prestamo in usuario.historial_prestamos:
                self.historial_listbox.insert(tk.END, f"{prestamo['libro']} - {prestamo['fecha_prestamo'].strftime('%Y-%m-%d %H:%M:%S')} - Entrega: {prestamo['fecha_devolucion'].strftime('%Y-%m-%d')}")
