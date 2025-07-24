from flask import Flask
from rutas.auth import auth_bp
from rutas.panel_admin import admin_bp
from rutas.test_tema import test_tema_bp
from rutas.test_global import test_global_bp
from rutas.test_personalizado import test_personalizado_bp
from rutas.subida_pdf import pdf_bp
from rutas.generador_justificaciones import justificaciones_bp
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'clave_secreta_para_tests')

# Registro de Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(test_tema_bp)
app.register_blueprint(test_global_bp)
app.register_blueprint(test_personalizado_bp)
app.register_blueprint(pdf_bp)
app.register_blueprint(justificaciones_bp)

@app.route('/')
def home():
    return "¡Bienvenido a la web de tests para Policía Nacional!"

if __name__ == '__main__':
    app.run(debug=True)

app = app  # Necesario para Gunicorn
