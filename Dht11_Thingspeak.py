
import datetime, time
import urllib.request
import random
import Adafruit_DHT


sensor = Adafruit_DHT.DHT11
pin = 4
url = "https://api.thingspeak.com/update?api_key=AXIQQULTJUR031QJ&field1="

seq=0   
try:
    while True:
        seq+=1
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)       
        
        if humidity is not None and temperature is not None:
            f = urllib.request.urlopen(url+seq+'&Temp={0:0.1f}&Humidity={1:0.1f}'.format(temperature, humidity))
            print(url+seq+'&Temp={0:0.1f}&Humidity={1:0.1f}'.format(temperature, humidity))
            data = str(f.read())
            print("data : ", data)
            print('Temp={0:0.1f}&Humidity={1:0.1f}'.format(temperature, humidity))
        else:
            print('Failed to get reading. Try again!')
        
        time.sleep(10)
except KeyboardInterrupt:
    pass