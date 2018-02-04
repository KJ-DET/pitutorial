import RPi.GPIO as GPIO
import time

GPIO_TRIG = 16 #output from pi
GPIO_ECHO = 18 #input to pi
GPIO_SERVO = 15 #output from pi 

def measure_distance():
    #send a soundwave by sending singal to TRIGGER
    print "measuring distance"
    GPIO.output(GPIO_TRIG, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIG,False)
    start =time.time()

    while GPIO.input(GPIO_ECHO)==0:
        start_time = time.time()

    while GPIO.input(GPIO_ECHO)==1:
        stop_time = time.time()

    time_taken = stop_time - start_time
    distance = (time_taken * 34300)/2
    print "distance is:" ,distance
    return distance

def gpio_init():
    GPIO.setmode(GPIO.BOARD)

def ultrasound_init():
    GPIO.setup(GPIO_TRIG,GPIO.OUT)
    GPIO.setup(GPIO_ECHO,GPIO.IN)
    GPIO.output(GPIO_TRIG,False)
    print "reseting trigger"

def servo_init():
    GPIO.setup(GPIO_SERVO,GPIO.OUT)
    servo = GPIO.PWM(GPIO_SERVO,50)
    return servo

def destroy(servo):
    servo.stop()
    GPIO.cleanup()

def move_to_neutral(servo):
    servo.ChangeDutyCycle(7.5)

def move_to_left(servo):
    servo.ChangeDutyCycle(2.5)

def move_to_right(servo):
    servo.ChangeDutyCycle(12.5)

#Main Program
gpio_init()
ultrasound_init()
servo = servo_init() 
servo.start(7.5)
#move_to_right(servo)
move_to_neutral(servo)
try:

    while True:
        distance = measure_distance()
        print "Distance:" , distance , "cm"
   #     if distance < 10 :
   #         move_to_left(servo)
   #     elif distance > 10 and distance < 50 :
   #         move_to_right(servo)
   #     else: 
   #         move_to_neutral(servo)
        if distance < 20 :
            #move_to_neutral(servo)
            move_to_right(servo)
            move_to_left(servo)
            move_to_neutral(servo)
            move_to_right(servo)
            move_to_left(servo)
        else :
            move_to_neutral(servo)
          #  move_to_right(servo)
        time.sleep(1)

except KeyboardInterrupt:
    destroy(servo)
