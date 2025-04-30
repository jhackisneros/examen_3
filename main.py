# main.py
from interfaz.ventana_principal import VentanaPrincipal
from base_datos.csv_manager import CSVManager

def run_app():
    csv_manager = CSVManager("libros.csv","usuarios.csv","prestamos.csv")
    libros = csv_manager.cargar_libros()
    usuarios = csv_manager.cargar_usuarios()

    app = VentanaPrincipal(libros, usuarios)
    app.mainloop()

if __name__ == "__main__":
    run_app()