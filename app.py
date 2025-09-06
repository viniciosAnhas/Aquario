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

@app.route('/motor/on', methods=['POST'])
def motor_on():
    """
    Ligar o Motor
    ---
    tags:
      - Motor
    responses:
      200:
        description: Motor ligado
    """
    GPIO.output(motor, GPIO.HIGH)
    return jsonify({"status": "Motor ligado"})

@app.route('/motor/off', methods=['POST'])
def motor_off():
    """
    Desligar o Motor
    ---
    tags:
      - Motor
    responses:
      200:
        description: Motor desligado
    """
    GPIO.output(motor, GPIO.LOW)
    return jsonify({"status": "Motor desligado"})

@app.route('/motor/status', methods=['GET'])
def get_motor_status():
    """
    Consultar status do Motor
    ---
    tags:
      - Motor
    responses:
      200:
        description: Status atual do Motor
    """
    status = GPIO.input(motor)
    return jsonify({"status": "ligado" if status else "desligado"})

@app.route('/raspberry/status', methods=['GET'])
def raspberry_status():
    """
    Consultar temperatura e voltagem do Raspberry Pi
    ---
    tags:
      - Raspberry
    responses:
      200:
        description: Retorna a temperatura e voltagem atuais
    """
    try:
        temp = subprocess.check_output(["vcgencmd", "measure_temp"]).decode("utf-8").strip()
        volts = subprocess.check_output(["vcgencmd", "measure_volts"]).decode("utf-8").strip()
        return jsonify({
            "temperature": temp,
            "voltage": volts
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=os.getenv('PORTA'))
    finally:
        GPIO.cleanup()