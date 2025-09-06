import RPi.GPIO as GPIO
import os
from flask import Blueprint, jsonify
from dotenv import load_dotenv

load_dotenv()
motor = int(os.getenv("MOTOR"))

motor_bp = Blueprint('motor', __name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor, GPIO.OUT)
GPIO.output(motor, GPIO.LOW)

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
    GPIO.output(motor, GPIO.HIGH)
    return jsonify({"status": "Motor ligado"})