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
    l = 0
    r = 255
    while l <= r:
        m = (l + r)//2
        GPIO.output(dac, binar(m))
        #print(binar(m))
        time.sleep(0.001)
        if GPIO.input(comp) == 1:
            r = m - 1
        else:
            l = m + 1
    return l

try:
    while True:
        l = adc()
        V = l * (3.3 / 255)
        print(l, V)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()