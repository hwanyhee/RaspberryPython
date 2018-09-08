#! /usr/bin/python
# _*_ coding:utf-8 _*_

import RPi.GPIO as GPIO
import time
from flask import Flask,render_template

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
app = Flask(__name__)
@app.route('/')
def hello():
	return '<h1>Hello Flask!</h1>'

@app.route('/index/<title>')
def view(title):
	return render_template('Led_Flask.html', title=title)

@app.route('/ledcontrol/<action>')
def led_onoff(action):
	if (action == "on"):
        	GPIO.output(17, GPIO.HIGH)
	if (action == "off"):
             	GPIO.output(17, GPIO.LOW)
        if (action == "toggle"):
        	toggle= not GPIO.input(17)
                GPIO.output(17, toggle)
		if(toggle==True):
			action='ON'
		else:
			action='OFF'
	return render_template('Led_Flask.html',title='LED:'+action.upper()) 
if __name__ == "__main__":
	app.run(host='0.0.0.0',port=10003,debug=True)

