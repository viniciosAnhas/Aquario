import RPi.GPIO as GPIO
import os
from flask import Flask, jsonify
from flasgger import Swagger
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()
LED_PIN = int(os.getenv("LED_PIN"))

# Criar app Flask
app = Flask(__name__)
swagger = Swagger(app)

# Configuração inicial do GPIO (apenas uma vez)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)  # LED começa apagado

@app.route('/led/on', methods=['POST'])
def led_on():
    """
    Ligar o LED
    ---
    responses:
      200:
        description: LED ligado
    """
    GPIO.output(LED_PIN, GPIO.HIGH)
    return jsonify({"status": "LED ligado"})

@app.route('/led/off', methods=['POST'])
def led_off():
    """
    Desligar o LED
    ---
    responses:
      200:
        description: LED desligado
    """
    GPIO.output(LED_PIN, GPIO.LOW)
    return jsonify({"status": "LED desligado"})

@app.route('/led/status', methods=['GET'])
def get_led_status():
    """
    Consultar status do LED
    ---
    responses:
      200:
        description: Status atual do LED
    """
    status = GPIO.input(LED_PIN)
    return jsonify({"status": "ligado" if status else "desligado"})

@app.teardown_appcontext
def cleanup_gpio(exception=None):
    GPIO.cleanup()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
