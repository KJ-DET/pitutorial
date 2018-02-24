import RPi.GPIO as GPIO
import time

GPIO_MOTOR = 22

def gpio_init():
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(GPIO_MOTOR,GPIO.OUT)
   GPIO.output(GPIO_MOTOR,False)
   time.sleep(2)

def destroy():
    GPIO.cleanup()

def motor_on():
    GPIO.output(GPIO_MOTOR,GPIO.HIGH)

def motor_off():
    GPIO.output(GPIO_MOTOR,GPIO.LOW)

def loop():
    while True:
        motor_on()
        time.sleep(2)
        motor_off()
        time.sleep(1)
        

gpio_init()
try:
    loop()
except KeyboardInterrupt:
    destroy()   
