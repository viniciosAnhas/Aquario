import RPi.GPIO as GPIO
import os
from flask import Blueprint, jsonify
from dotenv import load_dotenv

load_dotenv()
MOTOR_PIN = int(os.getenv("MOTOR"))

motor_bp = Blueprint('motor', __name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_PIN, GPIO.OUT)
GPIO.output(MOTOR_PIN, GPIO.LOW)

@motor_bp.route('/motor/on', methods=['POST'])
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
    GPIO.output(MOTOR_PIN, GPIO.HIGH)
    return jsonify({"status": "Motor ligado"})

@motor_bp.route('/motor/off', methods=['POST'])
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
    GPIO.output(MOTOR_PIN, GPIO.LOW)
    return jsonify({"status": "Motor desligado"})

@motor_bp.route('/motor/status', methods=['GET'])
def motor_status():
    """
    Consultar status do Motor
    ---
    tags:
      - Motor
    responses:
      200:
        description: Status do Motor
    """
    status = GPIO.input(MOTOR_PIN)
    return jsonify({"status": "ligado" if status else "desligado"})