from flask import Flask
from flasgger import Swagger
import RPi.GPIO as GPIO
from led_routes import led_bp
from system_routes import system_bp

app = Flask(__name__)
swagger = Swagger(app)

# Registrar blueprints
app.register_blueprint(led_bp)
app.register_blueprint(system_bp)

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=5000, debug=True)
    finally:
        GPIO.cleanup()
