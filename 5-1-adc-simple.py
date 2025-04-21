import RPi.GPIO as GPIO
import time as time

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)

def binar(a):
    return [int(i) for i in format(a, '08b')]

def adc():
    for a in range(256):
        GPIO.output(dac, binar(a))
        time.sleep(0.01)
        if GPIO.input(comp) == 1:
            return a
    return 255

try:
    while True:
        a = adc()
        V = a * (3.3 / 255)
        print(a, V)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()