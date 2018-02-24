import RPi.GPIO as GPIO
import time as time

GPIO_ECHO = 23
GPIO_TRIG = 17	
GPIO_MOTOR = 18

def gpio_init():
	GPIO.setmode(GPIO.BCM)
	ultrasound_init()
	motorControl = motor_init()
	return motorControl
	
def ultrasound_init():
	GPIO.setup(GPIO_ECHO,GPIO.IN)
	GPIO.setup(GPIO_TRIG,GPIO.OUT)
	GPIO.output(GPIO_TRIG,False)
	time.sleep(2)
	
def motor_init():
	GPIO.setup(GPIO_MOTOR,GPIO.OUT)
	motorControl = GPIO.PWM(GPIO_MOTOR,50)
	motorControl.start(0)
	return motorControl

def destroy( motorControl):
	motorControl.stop()
	GPIO.cleanup()
	
def send_soundwave():
	GPIO.output(GPIO_TRIG,True)
	time.sleep(0.0000001) # 10 microseconds
	GPIO.output(GPIO_TRIG,False)
	
def pulse_duration():
	start_time = time.time()
	GPIO.wait_for_edge(GPIO_ECHO,GPIO.RISING)
	start_time = time.time()
	
	GPIO.wait_for_edge(GPIO_ECHO,GPIO.FALLING)
	end_time = time.time()
	
	return end_time - start_time

def compute_distance():
	send_soundwave()
	return  (pulse_duration() * 34300)/2 	

def compute_vibration(distance):
	vibration = (((distance/100 - 0.5) * -1) /(4-0.5)) +1
	return vibration

	
def distance():
        send_soundwave()
	while GPIO.input(GPIO_ECHO)==0:
		pulse_start = time.time()
		
	while GPIO.input(GPIO_ECHO)==1:
		pulse_stop = time.time()

	pulse_time = pulse_stop - pulse_start
	d = (pulse_time * 34300)/2
	print "Distance is" , d
	return d
	
def prg_start():
	motorControl = gpio_init()
	try:
		while True:
			d = distance()
			duty_cycle = compute_vibration(d)
                        print "distance = " , d
                        print "vibration= " , duty_cycle
			motorControl.ChangeDutyCycle(duty_cycle)
			time.sleep(2)
		
	except KeyboardInterrupt:
		destroy(motorControl)
	
prg_start()


