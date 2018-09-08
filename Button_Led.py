import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

GPIO.setup(6, GPIO.OUT)
GPIO.setup(21, GPIO.IN)

try:
    while True:
        input = GPIO.input(21)

        if input == False:
            GPIO.output(6, GPIO.HIGH)
            
        else:
            GPIO.output(6, GPIO.LOW)
            

except KeyboardInterrupt:#ctrl+c
    GPIO.cleanup()