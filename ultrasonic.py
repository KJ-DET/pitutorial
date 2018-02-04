import RPi.GPIO as GPIO
import time

GPIO_TRIG = 16 #output from pi
GPIO_ECHO = 18 #input to pi

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
    GPIO.setup(GPIO_TRIG,GPIO.OUT)
    GPIO.setup(GPIO_ECHO,GPIO.IN)
    GPIO.output(GPIO_TRIG,False)
    print "reseting trigger"
    time.sleep(2)


gpio_init()

try:

    while True:
        distance = measure_distance()
        print "Distance:" , distance , "cm"
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
