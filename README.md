# Flask School Guide

A Flask application following best practices and modern development standards.

## Project Structure

```
school_guide/
├── app/                    # Application package
│   ├── __init__.py        # Application factory
│   ├── models/            # Database models
│   ├── routes/            # Route blueprints
│   ├── static/            # Static files
│   └── templates/         # Jinja2 templates
├── config.py              # Configuration
├── requirements.txt       # Project dependencies
└── run.py                # Application entry point
```

## Setup

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. Initialize the database:
```bash
flask db init
flask db migrate
flask db upgrade
```

5. Run the development server:
```bash
flask run
```

## Development

- Run tests: `pytest`
- Format code: `black .`
- Lint code: `flake8`

## License

MIT 