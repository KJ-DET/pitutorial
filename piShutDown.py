import RPi.GPIO as GPIO
import subprocess

ButtonPin = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ButtonPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

GPIO.wait_for_edge(ButtonPin,GPIO.FALLING)
print("Open, initiate Shutdown")
subprocess.call(['shutdown' , '-h', 'now'], shell=False)
