import RPi.GPIO as GPIO
import time

GPIO_TRIG = 16 #output from pi
GPIO_ECHO = 18 #input to pi
GPIO_LED = 11 #output from pi 

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
    GPIO.setup(GPIO_LED,GPIO.OUT)
    GPIO.output(GPIO_LED,False)

def destroy():
    GPIO.cleanup()
    

def led_on():
    GPIO.output(GPIO_LED,GPIO.HIGH)

def led_off():
    GPIO.output(GPIO_LED,GPIO.LOW)

#Main Program
gpio_init()

try:

    while True:
        distance = measure_distance()
        print "Distance:" , distance , "cm"
        if distance > 50 :
            led_on()
        else:
            led_off()
        time.sleep(1)

except KeyboardInterrupt:
    destroy()
