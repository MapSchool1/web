# Importamos las clases y funciones necesarias de Flask
from flask import Blueprint, render_template, jsonify
# Importamos el modelo Prueba y la instancia de la base de datos
from app.models.test import Prueba
from app import db

# Creamos un Blueprint llamado 'principal'
# Los Blueprints son como mini-aplicaciones que organizan el código
bp = Blueprint('principal', __name__)

# Definimos la ruta principal ('/')
# Esta función se ejecuta cuando alguien visita la página principal
@bp.route('/')
def inicio():
    # Renderiza la plantilla index.html
    return render_template('index.html')

# Definimos la ruta para probar la conexión a la base de datos
# Esta función se ejecuta cuando alguien visita /prueba-bd
@bp.route('/prueba-bd')
def prueba_bd():
    try:
        # Creamos un nuevo registro de prueba en la base de datos
        prueba = Prueba(nombre='Prueba de Base de Datos')
        # Agregamos el registro a la sesión de la base de datos
        db.session.add(prueba)
        # Guardamos los cambios en la base de datos
        db.session.commit()
        
        # Obtenemos todos los registros de la tabla Prueba
        pruebas = Prueba.query.all()
        
        # Devolvemos una respuesta JSON con:
        # - estado: indica si la operación fue exitosa
        # - mensaje: describe el resultado
        # - pruebas: lista de todos los registros encontrados
        return jsonify({
            'estado': 'éxito',
            'mensaje': 'Conexión a la base de datos exitosa',
            'pruebas': [{'id': p.id, 'nombre': p.nombre, 'fecha_creacion': p.fecha_creacion.isoformat()} for p in pruebas]
        })
    except Exception as e:
        # Si ocurre algún error, devolvemos un mensaje de error
        return jsonify({
            'estado': 'error',
            'mensaje': f'Error en la conexión a la base de datos: {str(e)}'
        }), 500 