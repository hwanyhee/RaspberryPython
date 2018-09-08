import webiopi

GPIO = webiopi.GPIO
LED=17


		
@webiopi.macro
def led_on():
	GPIO.output(LED, GPIO.HIGH)
	 
@webiopi.macro
def led_off():
	GPIO.output(LED, GPIO.LOW)
