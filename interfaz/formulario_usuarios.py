# interfaz/formulario_usuarios.py
import tkinter as tk
from usuarios.usuario import Usuario

usuario = Usuario("Juan Perez", 1)

class FormularioUsuarios(tk.Frame):
    def __init__(self, parent, usuarios, callback):
        super().__init__(parent)
        self.usuarios = usuarios
        self.callback = callback
        self.create_widgets()

    def create_widgets(self):
        self.usuario_label = tk.Label(self, text="Selecciona un usuario:")
        self.usuario_label.pack()

        self.usuario_listbox = tk.Listbox(self, height=10, width=50)
        for usuario in self.usuarios:
            self.usuario_listbox.insert(tk.END, usuario.nombre)
        self.usuario_listbox.pack()

        self.usuario_seleccionado_label = tk.Label(self, text="Usuario seleccionado:")
        self.usuario_seleccionado_label.pack()

        self.usuario_seleccionado_text = tk.Label(self, text="", width=50)
        self.usuario_seleccionado_text.pack()

        # Vincular el evento de selección
        self.usuario_listbox.bind("<<ListboxSelect>>", self.actualizar_usuario)

    def actualizar_usuario(self, event):
        selected_usuario_index = self.usuario_listbox.curselection()
        if selected_usuario_index:
            usuario_seleccionado = self.usuarios[selected_usuario_index[0]]
            self.usuario_seleccionado_text.config(text=f"{usuario_seleccionado.nombre}")
            self.callback(usuario_seleccionado)  # Actualiza el usuario seleccionado en la ventana principal
