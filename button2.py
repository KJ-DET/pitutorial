import RPi.GPIO as GPIO

ButtonPin = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ButtonPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

try:
    while True:
        if GPIO.input(ButtonPin) == GPIO.LOW:
            print("Open")
        else:
            print("Closed")
except KeyboardInterrupt:
    GPIO.cleanup()
