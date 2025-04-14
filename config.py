# Importamos las librerías necesarias para manejar archivos y variables de entorno
import os
from dotenv import load_dotenv

# Definimos la ruta base del proyecto
basedir = os.path.abspath(os.path.dirname(__file__))
# Cargamos las variables de entorno desde el archivo .env
load_dotenv(os.path.join(basedir, '.env'))

# Clase base de configuración que contiene las configuraciones comunes
class Config:
    # Clave secreta para proteger la aplicación de ataques
    # Se puede definir en el archivo .env o usar el valor por defecto
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave-secreta-dificil-de-adivinar'
    
    # Configuración temporal usando SQLite para pruebas
    # SQLite es una base de datos simple que no requiere instalación adicional
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    
    # Desactivamos el seguimiento de modificaciones para mejorar el rendimiento
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Configuración para el entorno de desarrollo
class ConfigDesarrollo(Config):
    # Activamos el modo de depuración para ver errores detallados
    DEBUG = True

# Configuración para el entorno de pruebas
class ConfigPruebas(Config):
    # Activamos el modo de pruebas
    TESTING = True
    # Usamos una base de datos en memoria para pruebas
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

# Configuración para el entorno de producción
class ConfigProduccion(Config):
    # Aquí irían configuraciones específicas para producción
    pass

# Diccionario que mapea los nombres de los entornos a sus clases de configuración
config = {
    'desarrollo': ConfigDesarrollo,  # Entorno de desarrollo local
    'pruebas': ConfigPruebas,        # Entorno para ejecutar pruebas
    'produccion': ConfigProduccion,  # Entorno para el servidor en producción
    'default': ConfigDesarrollo      # Configuración por defecto
} 