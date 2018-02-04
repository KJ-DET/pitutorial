from gpiozero import Button

button = Button(21)

try:
    
    while True:
        if button.is_pressed:
            print("Button is pressed")
        else:
            print("Button not pressed")

except KeyboardInterrupt:
    GPIO.cleanup()
