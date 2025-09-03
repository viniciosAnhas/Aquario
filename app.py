import RPi.GPIO as GPIO
import time
import os
from dotenv import load_dotenv

load_dotenv()

GPIO.setmode(GPIO.BCM)

LED_PIN = int(os.getenv("LED_PIN"))

GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.03)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.03)
except KeyboardInterrupt:
    print("Encerrando o programa...")
finally:
    GPIO.cleanup()
