#! /usr/bin/python
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)


Q5=7; Q6=11 # Set GPIO Pins
#----------------------------IMPORTANT ------------------------------
#IF Q5 ON THEN Q6 must be OFF
# ELSE transistor short circuit !
#--------------------------------------------------------------------
#Set Starting State
GPIO.setup(Q5, GPIO.OUT)
GPIO.setup(Q6, GPIO.OUT)
GPIO.output(Q5, False)
GPIO.output(Q6, False)
print "Drive motor forwards for 3 seconds"
GPIO.output(Q5, True)
#time.sleep(3)
raw_input()
print "Stop motor"
GPIO.output(Q5, False)
print "Drive motor in reverse for 3 seconds"
GPIO.output(Q6, True)
#time.sleep(3)
raw_input()
print "Stop motor"
GPIO.output(Q5, False)
GPIO.output(Q6, False)
GPIO.cleanup()
