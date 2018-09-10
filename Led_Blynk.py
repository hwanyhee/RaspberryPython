#! /usr/bin/python
# _*_ coding:utf-8 _*_

import BlynkLib
import time
import RPi.GPIO as GPIO
#이메일로 받은 토큰을 아래에 추가
BLYNK_AUTH = '이메일에서 받은 토큰'
# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)
# GPIO set
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
# Register Virtual Pins
# blynk앱에서 버튼 누를 경우 동작 (Virtual Pins 1)
@blynk.VIRTUAL_WRITE(1)
def my_write_handler(value):

  print('Current V1 value: {}'.format(value))
  if(value == '1'):
    GPIO.output(17, 1)
  else:
    GPIO.output(17, 0)
@blynk.VIRTUAL_READ(2)
def my_read_handler():
    # this widget will show some time in seconds..
    blynk.virtual_write(2, time.ticks_ms() // 1000)

# Start Blynk (this call should never return)
blynk.run()
