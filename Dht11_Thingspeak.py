
import datetime, time
import urllib.request
import random
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 4
url = "https://api.thingspeak.com/update?api_key=DD12F8GFJC04CBEO&field1="
try:
    while True:
       
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)       
        
        if humidity is not None and temperature is not None:
            #데이타 보내기
            f = urllib.request.urlopen(url+'{0:0.1f}&field2={1:0.1f}'.format(temperature, humidity))
           
            print('Temp={0:0.1f}&Humidity={1:0.1f}'.format(temperature, humidity))
        else:
            print('Failed to get reading. Try again!')
        #thingspeak needs minimum 15 sec delay between updates
        time.sleep(15)
except KeyboardInterrupt:
    pass