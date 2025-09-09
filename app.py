# from flask import Flask
# from flasgger import Swagger
# import RPi.GPIO as GPIO
# import os
# from routes import motor_bp, raspberry_bp, sensor_bp
# from flask_apscheduler import APScheduler
# from scheduler import iniciar_agendamentos

# app = Flask(__name__)

# class Config:
#     SCHEDULER_API_ENABLED = False
#     SCHEDULER_TIMEZONE = "America/Sao_Paulo"

# app.config.from_object(Config)

# scheduler = APScheduler()
# scheduler.init_app(app)

# GPIO.setwarnings(False)

# swagger = Swagger(app, config={
#     "headers": [],
#     "specs": [
#         {
#             "endpoint": 'apispec_1',
#             "route": '/apiaquario/apispec_1.json',
#             "rule_filter": lambda rule: True,
#             "model_filter": lambda tag: True,
#         }
#     ],
#     "static_url_path": "/flasgger_static",
#     "swagger_ui": True,
#     "specs_route": "/apiaquario/",
#     "title": "APIAQUARIO"
# })

# app.register_blueprint(motor_bp)
# app.register_blueprint(raspberry_bp)
# app.register_blueprint(sensor_bp)

# if __name__ == "__main__":
#     try:
#         scheduler.start()
#         iniciar_agendamentos(scheduler, app)
#         app.run(host="0.0.0.0", port=os.getenv('PORTA'))
#     finally:
#         GPIO.cleanup()

from flask import Flask
from flasgger import Swagger
import RPi.GPIO as GPIO
import os
from routes import motor_bp, raspberry_bp, sensor_bp
from flask_apscheduler import APScheduler
from scheduler.motor_scheduler import iniciar_agendamentos

app = Flask(__name__)

# Configuração do APScheduler
class Config:
    SCHEDULER_API_ENABLED = False
    SCHEDULER_TIMEZONE = "America/Sao_Paulo"

app.config.from_object(Config)

# Inicializa o scheduler
scheduler = APScheduler()
scheduler.init_app(app)

# Remove warnings do GPIO
GPIO.setwarnings(False)

# Configuração SIMPLIFICADA do Swagger
swagger_template = {
    "info": {
        "title": "APIAQUARIO",
        "version": "1.0.0",
        "description": "API para controle do aquário",
        "termsOfService": "",
        "contact": {
            "name": "Vinicios Anhas",
            "url": "https://github.com/seu-usuario"
        }
    },
    "host": "localhost:5000",
    "basePath": "/",
    "schemes": [
        "http",
        "https"
    ],
}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apiaquario/apispec_1.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apiaquario/",
    "title": "APIAQUARIO",  # Título na aba do navegador
}

swagger = Swagger(app, config=swagger_config, template=swagger_template)

app.register_blueprint(motor_bp)
app.register_blueprint(raspberry_bp)
app.register_blueprint(sensor_bp)

# Rota para customizar o footer dinamicamente
@app.after_request
def alterar_footer_swagger(response):
    if response.content_type and 'text/html' in response.content_type:
        if hasattr(response, 'get_data'):
            content = response.get_data(as_text=True)
            # Altera o footer
            content = content.replace('powered by Flasgger', 'Powered by Vinicios Anhas')
            content = content.replace('Flasgger', 'Swagger UI')
            content = content.replace('A swagger API', 'APIAQUARIO')
            response.set_data(content)
    return response

if __name__ == "__main__":
    try:
        # Inicia o scheduler
        scheduler.start()
        
        # Configura os agendamentos
        iniciar_agendamentos(scheduler, app)
        
        # Inicia o servidor Flask
        app.run(host="0.0.0.0", port=os.getenv('PORTA'))
    finally:
        GPIO.cleanup()