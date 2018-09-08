import webiopi
GPIO = webiopi.GPIO
led=17

def setup():
	GPIO.setFunction(led, GPIO.OUT)
    GPIO.output(led, GPIO.LOW)	
def destroy():    
	GPIO.setFunction(LED, GPIO.IN)
@webiopi.macro
def led_on():
	GPIO.output(led, GPIO.HIGH)
 
@webiopi.macro
def led_off():
	GPIO.output(led, GPIO.LOW)

