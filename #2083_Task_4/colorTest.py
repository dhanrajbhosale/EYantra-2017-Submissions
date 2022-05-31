import cv2
import numpy as np
import os
import io
from picamera import PiCamera
from picamera.array import PiRGBArray
import RPi.GPIO as GPIO    
import time

redb = 11
greenb = 15
blueb = 13
obj=1
i=0
s="Object Not Found"
#set the GPIO pins of raspberry pi.
GPIO.setmode (GPIO.BOARD)
GPIO.setwarnings (False)

GPIO.setup (redb, GPIO.OUT)
GPIO.setup (greenb, GPIO.OUT)
GPIO.setup (blueb, GPIO.OUT)

#initialize a PiCam object
cam = PiCamera()
cam.resolution = (640,480)
raw_cap = PiRGBArray(cam,(640,480))
time.sleep(1.0)
for frame in cam.capture_continuous(raw_cap,format="bgr",use_video_port=True,splitter_port=3,resize=(640,480)):
    color_image1 = frame.array
    cv2.waitKey(1)
    raw_cap.truncate(0)
    gray=cv2.cvtColor(color_image1,cv2.COLOR_BGR2GRAY)#convert each frame to grayscale.
    blur=cv2.bilateralFilter(gray,9,75,75)
    ret,th1 = cv2.threshold(blur,50,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)#using threshold remave noise
    ret1,th2 = cv2.threshold(th1,50,255,cv2.THRESH_BINARY_INV)# invert the pixels of the image frame
    a,contours1, hierarchy = cv2.findContours(th2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #find the contours
    cv2.drawContours(color_image1,contours1,-1,(0,255,0),1)
    cv2.imshow("Video",color_image1) 

    print len(contours1)
    j=len(contours1)

    for cnt in contours1:
        obj=0
        cn=0
        area1 = cv2.contourArea(cnt)
        print area1
        if area1>=120 and area1<400:
            M = cv2.moments(contours1[cn])
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])                                    ##Finding Centroid
            c=color_image1[cy,cx]
            if c[2]>c[0] and c[2]>c[1]:
                k = "red"
            elif c[0]>c[1] and c[0]>c[2]:
                k = "blue"                                                 ##Finding Color
            elif c[1]>c[0] and c[1]>c[2]:
                k = "green"     

            approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)   ##Finding Shape
            if len(approx)==3:
               s = "triangle"                                         
            elif len(approx)==4:      
               s = "Square"
            elif len(approx) > 10:
               s = "circle"
        


  
            if(k=='red' and s=='triangle'):
                GPIO.output(redb,GPIO.HIGH)
                print "RED Tringle"
                time.sleep(2.0)
                GPIO.output(redb,GPIO.LOW)
                time.sleep(2.0)
            elif(k=='red' and s=='square'):
                GPIO.output(redb,GPIO.HIGH)
                print "RED Square"
                time.sleep(2.0)
                GPIO.output(redb,GPIO.LOW)
                time.sleep(2.0)
            elif(k=='red' and s=='circle'):
                GPIO.output(redb,GPIO.HIGH)
                print "RED Square"
                time.sleep(2.0)
                GPIO.output(redb,GPIO.LOW)
                time.sleep(2.0)

            elif(k=='blue' and s=='triangle'):
                GPIO.output(blueb,GPIO.HIGH)
                print "blue Tringle"
                time.sleep(2.0)
                GPIO.output(blueb,GPIO.LOW)
                time.sleep(2.0)
            elif(k=='blue' and s=='square'):
                GPIO.output(blueb,GPIO.HIGH)
                print "blue Square"
                time.sleep(2.0)
                GPIO.output(blueb,GPIO.LOW)
                time.sleep(2.0)
            elif(k=='blue' and s=='circle'):
                GPIO.output(blueb,GPIO.HIGH)
                print "blue Square"
                time.sleep(2.0)
                GPIO.output(blueb,GPIO.LOW)
                time.sleep(2.0)

            elif(k=='green' and s=='triangle'):
                GPIO.output(greenb,GPIO.HIGH)
                print "green Tringle"
                time.sleep(2.0)
                GPIO.output(greenb,GPIO.LOW)
                time.sleep(2.0)
            elif(k=='green' and s=='square'):
                GPIO.output(greenb,GPIO.HIGH)
                print "green Square"
                time.sleep(2.0)
                GPIO.output(greenb,GPIO.LOW)
                time.sleep(2.0)
            elif(k=='green' and s=='circle'):
                GPIO.output(greenb,GPIO.HIGH)
                print "green Square"
                time.sleep(2.0)
                GPIO.output(greenb,GPIO.LOW)
                time.sleep(2.0)
        cn=cn+1
GPIO.cleanup()
cam.release()
cv2.destroyAllWindows()
