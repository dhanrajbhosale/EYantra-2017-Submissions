import cv2
import numpy as np
import os
import io
from picamera import PiCamera`
from picamera.array import PiRGBArray
import RPi.GPIO as GPIO    
import time

redb = 11
greenb = 15
blueb = 13
while (1):
    GPIO.setup (redb, GPIO.OUT)
    GPIO.setup (greenb, GPIO.OUT)
    GPIO.setup (blueb, GPIO.OUT)

    GPIO.output(redb,GPIO.HIGH)
    GPIO.output(greenb,GPIO.LOW)
    GPIO.output(blueb,GPIO.LOW)
    time.sleep(2.0)

    GPIO.output(redb,GPIO.LOW)
    GPIO.output(greenb,GPIO.LOW)
    GPIO.output(blueb,GPIO.LOW)
    time.sleep(2.0)

    GPIO.output(redb,GPIO.LOW)
    GPIO.output(greenb,GPIO.HIGH)
    GPIO.output(blueb,GPIO.LOW)
    time.sleep(2.0)

    GPIO.output(redb,GPIO.LOW)
    GPIO.output(greenb,GPIO.LOW)
    GPIO.output(blueb,GPIO.LOW)
    time.sleep(2.0)

    GPIO.output(redb,GPIO.LOW)
    GPIO.output(greenb,GPIO.LOW)
    GPIO.output(blueb,GPIO.HIGH)
    time.sleep(2.0)

    GPIO.output(redb,GPIO.LOW)
    GPIO.output(greenb,GPIO.LOW)
    GPIO.output(blueb,GPIO.LOW)
    time.sleep(2.0)

GPIO.cleanup()
cam.release()
cv2.destroyAllWindows()
