import RPi.GPIO as GPIO
import subprocess

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(40,GPIO.FALLING)

print("Hello")
