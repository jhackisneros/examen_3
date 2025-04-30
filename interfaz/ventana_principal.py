import tkinter as tk
from tkinter import messagebox
from prestamos.gestor_prestamos import GestorPrestamos
from base_datos.csv_manager import CSVManager
from .formulario_libros import FormularioLibros
from .formulario_usuarios import FormularioUsuarios

class VentanaPrincipal(tk.Tk):
    def __init__(self, libros, usuarios):
        super().__init__()
        self.title("Sistema de Gestión de Biblioteca")
        self.geometry("800x500")

        # Guardar libros y usuarios como atributos
        self.libros = libros
        self.usuarios = usuarios

        self.libro_seleccionado = None
        self.usuario_seleccionado = None

        # CSV Manager y Gestor de Préstamos
        self.csv_manager = CSVManager('libros.csv', 'usuarios.csv', 'prestamos.csv')
        self.gestor_prestamos = GestorPrestamos(self.csv_manager)

        # Formulario de libros
        self.formulario_libros = FormularioLibros(self, self.libros, self.set_libro_seleccionado)
        self.formulario_libros.pack(side=tk.LEFT, padx=10)

        # Formulario de usuarios
        self.formulario_usuarios = FormularioUsuarios(self, self.usuarios, self.set_usuario_seleccionado)
        self.formulario_usuarios.pack(side=tk.LEFT, padx=10)

        # Botón de préstamo
        self.prestamo_button = tk.Button(self, text="Realizar préstamo", command=self.realizar_prestamo, state=tk.DISABLED)
        self.prestamo_button.pack(pady=10)

        # Libros no disponibles
        self.libros_no_disponibles_label = tk.Label(self, text="Libros no disponibles:", font=("Helvetica", 12))
        self.libros_no_disponibles_label.pack()

        self.libros_no_disponibles_listbox = tk.Listbox(self, height=5, width=50)
        self.libros_no_disponibles_listbox.pack(pady=10)

        # Historial de préstamos
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

        try:
            self.gestor_prestamos.realizar_prestamo(self.usuario_seleccionado, self.libro_seleccionado)
            messagebox.showinfo("Préstamo realizado", f"{self.usuario_seleccionado.nombre} ha tomado prestado '{self.libro_seleccionado.titulo}'.")

            self.actualizar_libros_no_disponibles()
            self.actualizar_historial()
            self.prestamo_button.config(state=tk.DISABLED)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def actualizar_libros_no_disponibles(self):
        self.libros_no_disponibles_listbox.delete(0, tk.END)
        for libro in self.libros:
            if libro.estado == "prestado":
                self.libros_no_disponibles_listbox.insert(tk.END, f"{libro.titulo} (Dev. {libro.fecha_devolucion.strftime('%Y-%m-%d')})")

    def actualizar_historial(self):
        self.historial_listbox.delete(0, tk.END)
        for usuario in self.usuarios:
            for prestamo in usuario.historial_prestamos:
                self.historial_listbox.insert(tk.END, f"{prestamo['usuario']} - {prestamo['fecha_prestamo'].strftime('%Y-%m-%d')} - {prestamo['fecha_devolucion'].strftime('%Y-%m-%d')}")
