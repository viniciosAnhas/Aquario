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
import time
import threading
from flask import Flask, request, jsonify
from flasgger import Swagger
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()
LED_PIN = int(os.getenv("LED_PIN"))
TEMPO = float(os.getenv("TEMPO"))

# Criar app Flask
app = Flask(__name__)
swagger = Swagger(app)

# Controle de thread do piscar
blinking = False
blink_thread = None

def setup_gpio():
    """Configura o GPIO se ainda não foi configurado"""
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LED_PIN, GPIO.OUT)
    except RuntimeError:
        # Se já estiver configurado, ignoramos
        pass

# def blink_led():
#     """Thread para piscar LED"""
#     global blinking
#     setup_gpio()
#     while blinking:
#         GPIO.output(LED_PIN, GPIO.HIGH)
#         time.sleep(TEMPO)
#         GPIO.output(LED_PIN, GPIO.LOW)
#         time.sleep(TEMPO)

@app.route('/led', methods=['POST'])
def set_led():
    """
    Ligar ou desligar o LED
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            state:
              type: boolean
              example: true
    responses:
      200:
        description: Status do LED
    """
    global blinking
    setup_gpio()   # <- garante que GPIO está pronto
    blinking = False
    data = request.get_json()
    if data and data.get("state"):
        GPIO.output(LED_PIN, GPIO.HIGH)
        return jsonify({"status": "LED ligado"})
    else:
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

# @app.route('/led/blink', methods=['POST'])
# def start_blink():
#     """
#     Fazer o LED piscar no intervalo definido em TEMPO (.env)
#     ---
#     responses:
#       200:
#         description: Inicia o piscar do LED
#     """
#     global blinking, blink_thread
#     setup_gpio()
#     if not blinking:
#         blinking = True
#         blink_thread = threading.Thread(target=blink_led, daemon=True)
#         blink_thread.start()
#         return jsonify({"status": f"LED piscando a cada {TEMPO} segundos"})
#     else:
#         return jsonify({"status": "LED já está piscando"})

@app.route('/led/blink/stop', methods=['POST'])
def stop_blink():
    """
    Parar o piscar do LED
    ---
    responses:
      200:
        description: Para o piscar do LED
    """
    global blinking
    setup_gpio()
    blinking = False
    GPIO.output(LED_PIN, GPIO.LOW)
    return jsonify({"status": "Piscar parado e LED desligado"})

@app.teardown_appcontext
def cleanup_gpio(exception=None):
    GPIO.cleanup()

if __name__ == "__main__":
    setup_gpio()
    app.run(host="0.0.0.0", port=5000, debug=True)
