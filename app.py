from flask import Flask
from flasgger import Swagger
import RPi.GPIO as GPIO
from motor_routes import motor_bp
# from system_routes import system_bp

app = Flask(__name__)
swagger = Swagger(app, config={
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
    "specs_route": "/apiaquario/"
})

app.register_blueprint(motor_bp)

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=os.getenv('PORTA'))
    finally:
        GPIO.cleanup()