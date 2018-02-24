import RPi.GPIO as GPIO
import time

GPIO_MOTOR = 18#22

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
        time.sleep(0.25)
        motor_off()
        time.sleep(0.5)
        motor_on()
        time.sleep(0.25)
        motor_off()
gpio_init()
try:
    loop()
except KeyboardInterrupt:
    destroy()   
