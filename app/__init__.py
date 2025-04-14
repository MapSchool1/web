# Importamos las clases y funciones necesarias de Flask y sus extensiones
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from school_guide.config import config

# Creamos instancias de las extensiones que usaremos en la aplicación
# SQLAlchemy: Para trabajar con la base de datos
db = SQLAlchemy()
# Flask-Migrate: Para manejar las migraciones de la base de datos
migrate = Migrate()

# Función que crea y configura la aplicación Flask
# Esta es la fábrica de la aplicación, que nos permite crear diferentes
# instancias de la aplicación con diferentes configuraciones
def crear_app(config_name='default'):
    # Creamos una nueva instancia de la aplicación Flask
    app = Flask(__name__)
    
    # Cargamos la configuración según el entorno especificado
    # (desarrollo, pruebas o producción)
    app.config.from_object(config[config_name])

    # Inicializamos las extensiones con la aplicación
    # Esto conecta las extensiones con nuestra aplicación Flask
    db.init_app(app)
    migrate.init_app(app, db)

    # Importamos y registramos los blueprints (módulos) de la aplicación
    # Los blueprints son como mini-aplicaciones que organizan el código
    from app.routes import main
    app.register_blueprint(main.bp)

    # Devolvemos la aplicación configurada
    return app 