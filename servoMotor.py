import RPi.GPIO as GPIO
import time

SERVOPIN = 15 #output from servo

def servo_init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(SERVOPIN,GPIO.OUT)
    servo = GPIO.PWM(SERVOPIN,50) # pulse width modulation where pulse has 50Htz frequency
    return servo

def destroy(servo):
    servo.stop()
    GPIO.cleanup()


servo = servo_init()
servo.start(7.5)

try:
    while True:
        servo.ChangeDutyCycle(7.5) #goes to Neutral (center)
        time.sleep(1)
        servo.ChangeDutyCycle(12.5) #goes to 180 (right)
        time.sleep(1)
        servo.ChangeDutyCycle(2.5) #goes to zero =(left)
        time.sleep(1)
except KeyboardInterrupt:
        destroy(servo)



