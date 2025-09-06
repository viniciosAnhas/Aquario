import RPi.GPIO as GPIO
import os
from flask import Blueprint, jsonify
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()
LED_PIN = int(os.getenv("LED_PIN"))

# Blueprint para rotas do LED
led_bp = Blueprint('led', __name__)

# Configuração do GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)  # LED começa apagado

@led_bp.route('/led/on', methods=['POST'])
def led_on():
    """
    Ligar o LED
    ---
    tags:
      - Motor
    responses:
      200:
        description: LED ligado
    """
    GPIO.output(LED_PIN, GPIO.HIGH)
    return jsonify({"status": "LED ligado"})

@led_bp.route('/led/off', methods=['POST'])
def led_off():
    """
    Desligar o LED
    ---
    tags:
      - Motor
    responses:
      200:
        description: LED desligado
    """
    GPIO.output(LED_PIN, GPIO.LOW)
    return jsonify({"status": "LED desligado"})

@led_bp.route('/led/status', methods=['GET'])
def led_status():
    """
    Consultar status do LED
    ---
    tags:
      - Motor
    responses:
      200:
        description: Status do LED
    """
    status = GPIO.input(LED_PIN)
    return jsonify({"status": "ligado" if status else "desligado"})
