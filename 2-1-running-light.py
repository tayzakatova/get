import time as time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

leds = [2, 3, 4, 17, 27, 22, 10, 9]
GPIO.setup(leds, GPIO.OUT)

GPIO.output(leds, 0)

k = 3

while k > 0:
        for i in range(len(leds)):
            GPIO.output(leds[i], 1)
            time.sleep(0.2)
            GPIO.output(leds[i], 0)
        k -= 1

GPIO.output(leds, 0)
GPIO.cleanup()






