# import RPi.GPIO as GPIO
# import time
# import os
# from dotenv import load_dotenv

# load_dotenv()

# GPIO.setmode(GPIO.BCM)

# LED_PIN = int(os.getenv("LED_PIN"))
# TEMPO = float(os.getenv("TEMPO"))

# GPIO.setup(LED_PIN, GPIO.OUT)

# try:
#     while True:
#         GPIO.output(LED_PIN, GPIO.HIGH)
#         time.sleep(TEMPO)
#         GPIO.output(LED_PIN, GPIO.LOW)
#         time.sleep(TEMPO)
# except KeyboardInterrupt:
#     print("Encerrando o programa...")
# finally:
#     GPIO.cleanup()

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

def setup_gpio():
    """Configura o GPIO e garante que o LED comece apagado"""
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.LOW)  # LED apagado ao iniciar

@app.route('/led/on', methods=['POST'])
def led_on():
    """
    Ligar o LED
    ---
    responses:
      200:
        description: LED ligado
    """
    setup_gpio()
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
    setup_gpio()
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
    setup_gpio()
    status = GPIO.input(LED_PIN)
    return jsonify({"status": "ligado" if status else "desligado"})

@app.teardown_appcontext
def cleanup_gpio(exception=None):
    GPIO.cleanup()

if __name__ == "__main__":
    setup_gpio()
    app.run(host="0.0.0.0", port=5000, debug=True)
