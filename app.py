import RPi.GPIO as GPIO
import os
import subprocess
from flask import Flask, jsonify
from flasgger import Swagger
from dotenv import load_dotenv

load_dotenv()
motor = int(os.getenv("MOTOR"))

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor, GPIO.OUT)
GPIO.output(motor, GPIO.LOW)

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

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=os.getenv('PORTA'))
    finally:
        GPIO.cleanup()