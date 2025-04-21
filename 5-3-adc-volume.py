import RPi.GPIO as GPIO
import time as time

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
led = [2, 3, 4, 17, 27, 22, 10, 9]

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)
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
    if l == 256:
        return 255
    return l

try:
    while True:
        l = adc()
        V = l * (3.3 / 255)
        print(l, V)
        if l == 0:
            GPIO.output(led, [0,0,0,0,0,0,0,0])
        if l < 32:
            GPIO.output(led, [0,0,0,0,0,0,0,1])
        if 32<l < 64:
            GPIO.output(led, [0,0,0,0,0,0,1,1])
        if 64<l < 96:
            GPIO.output(led, [0,0,0,0,0,1,1,1])
        if 96<l < 128:
            GPIO.output(led, [0,0,0,0,1,1,1,1])
        if 128<l <160:
            GPIO.output(led, [0,0,0,1,1,1,1,1])
        if 160<l < 192:
            GPIO.output(led, [0,0,1,1,1,1,1,1])
        if 192<l <224:
            GPIO.output(led, [0,1,1,1,1,1,1,1])
        if 224<l < 256:
            GPIO.output(led, [1,1,1,1,1,1,1,1])


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()