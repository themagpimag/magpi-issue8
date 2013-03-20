#! /usr/bin/python
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

# Top Transistors are active LOW, Bottom active HIGH
T_ACTIVE = 0; B_ACTIVE = 1; T_DEACTIVE = 1; B_DEACTIVE = 0
T1=7; T2=11; T3=13; T4=15 # Set GPIO Pins
#----------------------------IMPORTANT ------------------------------
#IF T1, T2 are "ACTIVE" THEN GPIO T3, T4 must be "DEACTIVE"
# ELSE transistor short circuit !
#--------------------------------------------------------------------
#Set Starting State
GPIO.setup(T1, GPIO.OUT); GPIO.setup(T2, GPIO.OUT)
GPIO.setup(T3, GPIO.OUT); GPIO.setup(T4, GPIO.OUT)
GPIO.output(T1, T_DEACTIVE); GPIO.output(T2, B_DEACTIVE)
GPIO.output(T3, T_DEACTIVE); GPIO.output(T4, B_DEACTIVE)
print "Connect Motor Power and Press Enter"
raw_input()
print "Drive motor forwards for 3 seconds"
GPIO.output(T1, T_ACTIVE); GPIO.output(T2, B_ACTIVE)
time.sleep(3)
print "Stop motor"
GPIO.output(T1, T_DEACTIVE); GPIO.output(T2, B_DEACTIVE)
print "Drive motor in reverse for 3 seconds"
GPIO.output(T3, T_ACTIVE); GPIO.output(T4, B_ACTIVE)
time.sleep(3)
print "Stop motor"
GPIO.output(T3, T_DEACTIVE); GPIO.output(T4, B_DEACTIVE)
print "Disconnect Motor Power and Press Enter"
raw_input()
GPIO.cleanup()
