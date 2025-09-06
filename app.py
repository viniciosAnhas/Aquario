import RPi.GPIO as GPIO
import os
import subprocess
from flask import Flask, jsonify
from flasgger import Swagger
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()
LED_PIN = int(os.getenv("LED_PIN"))

# Criar app Flask
app = Flask(__name__)
swagger = Swagger(app)

# Configuração inicial do GPIO (uma vez só)
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

@app.route('/raspberry/status', methods=['GET'])
def system_status():
    """
    Consultar temperatura e voltagem do Raspberry Pi
    ---
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
        app.run(host="0.0.0.0", port=5000, debug=True)
    finally:
        GPIO.cleanup()  # <- só roda quando o processo Flask for encerrado
