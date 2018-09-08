import Adafruit_DHT
import pymysql
import time

sensor = Adafruit_DHT.DHT11
pin = 4

try:
    
    conn = pymysql.connect(host='localhost',user='iot', password='iot',db='iot_schema', port=3306,charset='utf8',cursorclass=pymysql.cursors.DictCursor)
    cur = conn.cursor()  
  
                   
    while True:
       
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)       
        
        if humidity is not None and temperature is not None:
          
             cur.execute('INSERT INTO sensors(temperature,humidity) VALUES('+str(temperature)+','+str(humidity)+')')
             conn.commit()
        else:
            print('Failed to get reading. Try again!')      
       
        time.sleep(15)
except KeyboardInterrupt:
    
    print('error ')    
finally:
    conn.close()
    cur.close()
    