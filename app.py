from flask import Flask
from flasgger import Swagger
import RPi.GPIO as GPIO
import os
from routes import motor_bp, raspberry_bp, sensor_bp
from flask_apscheduler import APScheduler
from scheduler import iniciar_agendamentos

app = Flask(__name__)

class Config:
    SCHEDULER_API_ENABLED = False
    SCHEDULER_TIMEZONE = "America/Sao_Paulo"

app.config.from_object(Config)

scheduler = APScheduler()
scheduler.init_app(app)

GPIO.setwarnings(False)


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
    "title": "APIAQUARIO",
    "version": "1.0.0",
    "description": "API para controle do aquario",
    "termsOfService": "",
    "ui_params": {
        "displayRequestDuration": True,
        "docExpansion": "none"
    }
}

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

app.register_blueprint(motor_bp)
app.register_blueprint(raspberry_bp)
app.register_blueprint(sensor_bp)

if __name__ == "__main__":
    try:
        scheduler.start()
        iniciar_agendamentos(scheduler, app)
        app.run(host="0.0.0.0", port=os.getenv('PORTA'))
    finally:
        GPIO.cleanup()