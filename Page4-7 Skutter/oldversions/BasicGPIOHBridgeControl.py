#! /usr/bin/python
import time
import RPi.GPIO as GPIO

#----------------------------IMPORTANT -----------------------------------
#IF GPIO 0, 1 is "1" THEN GPIO 2, 3 must be "0" ELSE transistor short circuit !
#-------------------------------------------------------------------------

GPIO.setup(1, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

#Drive motor forwards for 3 seconds
GPIO.output(1, True)
GPIO.output(2, True)
time.sleep(3)
#Stop motor
GPIO.output(1, False)
GPIO.output(2, False)
#Drive motor in reverse for 3 seconds
GPIO.output(3, True)
GPIO.output(4, True)
time.sleep(3)
#Stop motor
GPIO.output(3, False)
GPIO.output(4, False)
