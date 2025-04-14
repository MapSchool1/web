# Guía Escolar - Aplicación Flask

Una aplicación web moderna desarrollada con Flask, siguiendo las mejores prácticas de desarrollo.

## 📋 Tabla de Contenidos

1. [¿Qué es este proyecto?](#qué-es-este-proyecto)
2. [Estructura del Proyecto](#estructura-del-proyecto)
3. [Conceptos Importantes](#conceptos-importantes)
4. [Configuración del Entorno](#configuración-del-entorno)
5. [Instalación y Uso](#instalación-y-uso)
6. [Desarrollo](#desarrollo)
7. [Base de Datos](#base-de-datos)
8. [Rutas y Vistas](#rutas-y-vistas)
9. [Plantillas](#plantillas)
10. [Estilos CSS](#estilos-css)

## ¿Qué es este proyecto?

Este es un proyecto de ejemplo que demuestra cómo construir una aplicación web moderna usando Flask, un framework web de Python. La aplicación está diseñada para ser una guía escolar, pero puede ser adaptada para cualquier propósito.

## Estructura del Proyecto

```
guia_escolar/
├── app/                    # Paquete principal de la aplicación
│   ├── __init__.py        # Fábrica de la aplicación y configuración inicial
│   ├── models/            # Modelos de la base de datos
│   │   ├── __init__.py    # Inicialización de los modelos
│   │   └── test.py        # Modelo de prueba
│   ├── routes/            # Rutas y controladores
│   │   └── main.py        # Rutas principales
│   ├── static/            # Archivos estáticos (CSS, JS, imágenes)
│   │   └── css/
│   │       └── style.css  # Estilos CSS
│   └── templates/         # Plantillas HTML
│       └── index.html     # Plantilla principal
├── config.py              # Configuración de la aplicación
├── requirements.txt       # Dependencias del proyecto
└── run.py                # Punto de entrada de la aplicación
```

## Conceptos Importantes

### Blueprints (Planos)
Los Blueprints son como mini-aplicaciones dentro de tu aplicación principal. Ayudan a organizar el código en módulos más pequeños y manejables. En este proyecto, usamos un Blueprint llamado 'principal' que maneja las rutas principales.

### Modelos
Los modelos representan las tablas en la base de datos. Cada modelo es una clase Python que hereda de `db.Model`. Por ejemplo, el modelo `Prueba` representa una tabla con columnas para id, nombre y fecha de creación.

### Rutas
Las rutas son las URLs que los usuarios pueden visitar. Cada ruta está asociada a una función que maneja la petición y devuelve una respuesta. Por ejemplo, la ruta '/' muestra la página principal.

### Plantillas
Las plantillas son archivos HTML que contienen el diseño de las páginas. Usamos el motor de plantillas Jinja2, que permite incluir lógica y variables en el HTML.

## Configuración del Entorno

La aplicación usa un archivo `.env` para configurar variables importantes:

```env
FLASK_APP=run.py          # Archivo principal de la aplicación
FLASK_ENV=development     # Entorno de desarrollo
SECRET_KEY=tu-clave-secreta  # Clave para seguridad
DATABASE_URL=sqlite:///app.db  # URL de la base de datos
```

## Instalación y Uso

1. **Crear un entorno virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar la base de datos**:
   ```bash
   flask db init
   flask db migrate -m "Migración inicial"
   flask db upgrade
   ```

4. **Ejecutar la aplicación**:
   ```bash
   flask run
   ```

La aplicación estará disponible en http://localhost:5000

## Desarrollo

### Herramientas de Desarrollo
- **pytest**: Para ejecutar pruebas
- **black**: Para formatear el código
- **flake8**: Para verificar la calidad del código

### Comandos útiles
```bash
# Ejecutar pruebas
pytest

# Formatear código
black .

# Verificar calidad del código
flake8
```

## Base de Datos

La aplicación usa SQLAlchemy para interactuar con la base de datos. Actualmente está configurada para usar SQLite, pero puede ser cambiada a MySQL u otra base de datos.

### Modelo de Ejemplo
```python
class Prueba(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
```

## Rutas y Vistas

Las rutas están definidas en `app/routes/main.py`. Cada ruta es una función decorada con `@bp.route()`.

### Ejemplo de Ruta
```python
@bp.route('/')
def inicio():
    return render_template('index.html')
```

## Plantillas

Las plantillas están en la carpeta `app/templates/`. Usan el motor de plantillas Jinja2.

### Características de las Plantillas
- Herencia de plantillas
- Inclusión de archivos estáticos
- Variables y lógica condicional
- Bucles y estructuras de control

## Estilos CSS

Los estilos están en `app/static/css/style.css`. La aplicación usa CSS moderno con variables y un diseño responsive.

### Características del CSS
- Variables CSS para colores y estilos
- Diseño responsive
- Estilos modernos y limpios
- Compatibilidad con diferentes navegadores

## Licencia

MIT 