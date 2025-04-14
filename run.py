# Importamos la función crear_app desde nuestro paquete app
from school_guide.app import crear_app

# Creamos una instancia de la aplicación usando la configuración por defecto
app = crear_app()

# Este bloque se ejecuta solo si el archivo se ejecuta directamente
# (no cuando se importa como módulo)
if __name__ == '__main__':
    # Iniciamos el servidor de desarrollo de Flask
    # Por defecto, la aplicación estará disponible en http://localhost:5000
    app.run() 