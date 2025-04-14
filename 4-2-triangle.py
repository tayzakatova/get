import time as time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setup(dac, GPIO.OUT)

def dac2bin(a):
    b = list(bin(a))
    b.remove(b[0])
    b.remove(b[0])
    s = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(b)):
        b[i] = int(b[i])
        s[8 - len(b) + i] = b[i]
    return s

try:
    T = float(input('Период сигнала'))
    t = T / (2 * 255)
    while 1 > 0:
        for a in range(256):
            GPIO.output(dac, dac2bin(a))
            time.sleep(t)
        for a in range(254, -1, -1):
            GPIO.output(dac, dac2bin(a))
            time.sleep(t)


finally:
    time.sleep(15)
    GPIO.output(dac, 0)
    GPIO.cleanup()