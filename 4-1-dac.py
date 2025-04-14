import time as time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setup(dac, GPIO.OUT)
s = [0, 0, 0, 0, 0, 0, 0, 0]
b = []
try:
    while True:
        k = input('Введите число от 0 до 255')
        if k.lower() == 'q':
            break
        
    
        a = int(k)
        
        if a < 0:
            print('Вы ввели отрицательное число')
            continue
        if a > 255:
            print('вы ввели слишком большое число')
            continue
    
        b = list(bin(a))
        b.remove(b[0])
        b.remove(b[0])

        for i in range(len(b)):
            b[i] = int(b[i])
            s[8 - len(b) + i] = b[i]
        GPIO.output(dac, s)

        U = 3.3 * a / 255
        print(f'напряжение {U} В')
except ValueError:
    print('не то')


finally:
    time.sleep(15)
    GPIO.output(dac, 0)
    GPIO.cleanup()