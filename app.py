import RPi.GPIO as GPIO
import time
import os
from dotenv import load_dotenv
from decimal import Decimal

load_dotenv()

GPIO.setmode(GPIO.BCM)

LED_PIN = int(os.getenv("LED_PIN"))
TEMPO = Decimal(os.getenv("TEMPO"))

GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(TEMPO)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(TEMPO)
except KeyboardInterrupt:
    print("Encerrando o programa...")
finally:
    GPIO.cleanup()
