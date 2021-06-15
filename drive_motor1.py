#!/usr/bin/env python3
import RPi.GPIO as GPIO # using RPi.GPIO module
from time import sleep # import function sleep for delay
GPIO.setmode(GPIO.BCM) # GPIO numbering
GPIO.setwarnings(False) # enable warning from GPIO
AN2 = 25 # set pwm2 pin on MDDS10 to GPIO 25
AN1 = 24 # set pwm1 pin on MDDS10 to GPIO 24
DIG2 = 23 # set dir2 pin on MDDS10 to GPIO 23
DIG1 = 18 # set dir1 pin on MDDS10 to GPIO 18

GPIO.setup(AN2, GPIO.OUT) # set pin as output
GPIO.setup(AN1, GPIO.OUT) # set pin as output
GPIO.setup(DIG2, GPIO.OUT) # set pin as output
GPIO.setup(DIG1, GPIO.OUT) # set pin as output
sleep(1) # delay for 1 seconds
p1 = GPIO.PWM(AN1, 100) # set pwm for M1
p2 = GPIO.PWM(AN2, 100) # set pwm for M2

try:
    while True:
        print("Forward")# display &quot;Forward&quot; when program executed
        GPIO.output(DIG1, GPIO.HIGH) # set DIG1 as high, dir2 = forward
        GPIO.output(DIG2, GPIO.HIGH) # set DIG2 as high, dir1 = forward
        p1.start(50) # set speed for M1, speed=0 – 100
        p2.start(50) # set speed for M2, speed=0 – 100
        sleep(1) # delay for 1 seconds
        
        print("Backward")# display &quot;Backward&quot; when program executed
        GPIO.output(DIG1, GPIO.LOW) # set DIG1 as low, DIR = backward
        GPIO.output(DIG2, GPIO.LOW) # set DIG2 as low, DIR = backward
        p1.start(50) # set speed for M1, speed=0 – 100
        p2.start(50) # set speed for M2, speed=0 – 100
        sleep(1) # delay for 1 seconds

        print("Left")# display &quot;Left&quot; when program executed
        GPIO.output(DIG1, GPIO.LOW) # set DIG1 as low, dir2 = backward
        GPIO.output(DIG2, GPIO.HIGH) # set DIG2 as high, dir1 = forward
        p1.start(25) # set speed for M1
        p2.start(25) # set speed for M2
        sleep(1) # delay for 1 seconds

        print("Right")# display &quot;Right&quot; when program executed
        GPIO.output(DIG1, GPIO.HIGH) # set DIG1 as high, dir1 = forward
        GPIO.output(DIG2, GPIO.LOW) # set DIG2 as low, dir2 = backward
        p1.start(25) # set speed for M1
        p2.start(25) # set speed for M2,
        sleep(1) # delay for 1 seconds

except: # exit program when keyboard interrupt
    p1.start(0) # set speed M1=0
    p2.start(0) # set speed M2=0

