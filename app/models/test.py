# Importamos la instancia de la base de datos y la clase datetime
from app import db
from datetime import datetime

# Definimos la clase Prueba que representa una tabla en la base de datos
# Esta clase hereda de db.Model, que es parte de SQLAlchemy
class Prueba(db.Model):
    # Definimos las columnas de la tabla
    
    # Columna id: Es la clave primaria, se incrementa automáticamente
    id = db.Column(db.Integer, primary_key=True)
    
    # Columna nombre: Almacena texto de hasta 100 caracteres, no puede ser nulo
    nombre = db.Column(db.String(100), nullable=False)
    
    # Columna fecha_creacion: Almacena la fecha y hora de creación
    # Se establece automáticamente al crear un nuevo registro
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)

    # Método que define cómo se representa el objeto como string
    # Útil para depuración y mostrar información en la consola
    def __repr__(self):
        return f'<Prueba {self.nombre}>' 