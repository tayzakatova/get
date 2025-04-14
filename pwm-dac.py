import time as time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
pwm = GPIO.PWM(24, 60)
pwm.start(0)
try:
    while 1 > 0:
        c = float(input('Введите коэффициент заполнения'))
        if c >= 0 and c <= 100:
            pwm.ChangeDutyCycle(c)
            U = 3.3 * c / 100
            print(f'напряжение в ауте {U}В')
        else:
            print('Ваш коэффициент не подходит по госту')

except ValueError:
    print('не то')

  
finally:
    time.sleep(15)
    pwm.stop()
    GPIO.cleanup()    
