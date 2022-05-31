import cv2
import numpy as np
import os
import io
from picamera import PiCamera
from picamera.array import PiRGBArray
import RPi.GPIO as GPIO    
import time
s='obj'
obj=1

zone=1    
zone1=[(350,250),(400,250),(450,250),(500,250)]
zone2=[(120,197),(160,202),(85,230),(130,240)]
zone3=[(230,172),(270,172),(310,172),(350,172)]
zone4=[(500,179),(540,182),(580,183),(620,186)]

def colorDetect():
    global zone
    cam.resolution = (640,480)
    raw_cap = PiRGBArray(cam,(640,480))
    time.sleep(1.0)
    
    for frame in cam.capture_continuous(raw_cap,format="bgr",use_video_port=True,splitter_port=3,resize=(640,480)):
        color_image1 = frame.array
        cv2.waitKey(1)
        raw_cap.truncate(0)
        
        gray=cv2.cvtColor(color_image1,cv2.COLOR_BGR2GRAY)#convert each frame to grayscale.
        blur=cv2.medianBlur(gray,5)
        ret,th1 = cv2.threshold(blur,100,255,cv2.THRESH_BINARY)#using threshold remave noise
        ret1,th2 = cv2.threshold(th1,127,255,cv2.THRESH_BINARY_INV)# invert the pixels of the image frame
        a,contours1, hierarchy = cv2.findContours(th2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #find the contours
        #cv2.drawContours(color_image1,contours1,-1,(255,0,0),1)   
        
        print len(contours1)
        j=len(contours1)
        mn=0
        for cnt in contours1:
            obj=0
                       
            area1 = cv2.contourArea(cnt)
            
            if area1>=2000 and area1<7000:
             
                print area1
                M = cv2.moments(cnt)
                if (M['m00']!=0):
                    cx = int(M['m10']/M['m00'])
                    cy = int(M['m01']/M['m00'])                                    ##Finding Centroid
                    c=color_image1[cy,cx]
                    print c
                    #cv2.circle(color_image1,(cx,cy), 7, (0,0,255), -1)
                    if c[2]>c[0] and c[2]>c[1]:
                        k = "red"
                    elif c[0]>c[1] and c[0]>c[2]:
                        k = "blue"                                                 ##Finding Color
                    elif c[1]>c[0] and c[1]>c[2]:
                        k = "green"     
        
                    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)   ##Finding Shape
                    
                    if len(approx)==4:      
                       s = "square"
                    elif len(approx) > 10:
                       s = "circle"
                    else: 
                       s="triangle"

                mn=mn+1

                if(zone==1):
                    for i in range(mn):
                        if(k=='red' and s=='triangle'):
                            result = transparentOverlay(bImg,pngImage,zone1[i],1)
                        elif(k=='red' and s=='square'):
                            result = transparentOverlay(bImg,pngImage2,zone1[i],1)
                        elif(k=='red' and s=='circle'):
                            result = transparentOverlay(bImg,pngImage1,zone1[i],1)
                        elif(k=='blue' and s=='triangle'):
                            result = transparentOverlay(bImg,pngImage7,zone1[i],1)
                        elif(k=='blue' and s=='square'):
                            result = transparentOverlay(bImg,pngImage8,zone1[i],1)
                        elif(k=='blue' and s=='circle'):
                            result = transparentOverlay(bImg,pngImage6,zone1[i],1)
                        elif(k=='green' and s=='triangle'):
                            result = transparentOverlay(bImg,pngImage4,zone1[i],1)
                        elif(k=='green' and s=='square'):
                            result = transparentOverlay(bImg,pngImage5,zone1[i],1)
                        elif(k=='green' and s=='circle'):
                            result = transparentOverlay(bImg,pngImage3,zone1[i],1)
                        i=i+1

                if(zone==2):
                    for i in range(mn):
                        if(k=='red' and s=='triangle'):
                            result = transparentOverlay(bImg,pngImage,zone2[i],1)
                        elif(k=='red' and s=='square'):
                            result = transparentOverlay(bImg,pngImage2,zone2[i],1)
                        elif(k=='red' and s=='circle'):
                            result = transparentOverlay(bImg,pngImage1,zone2[i],1)
                        elif(k=='blue' and s=='triangle'):
                            result = transparentOverlay(bImg,pngImage7,zone2[i],1)
                        elif(k=='blue' and s=='square'):
                            result = transparentOverlay(bImg,pngImage8,zone2[i],1)
                        elif(k=='blue' and s=='circle'):
                            result = transparentOverlay(bImg,pngImage6,zone2[i],1)
                        elif(k=='green' and s=='triangle'):
                            result = transparentOverlay(bImg,pngImage4,zone2[i],1)
                        elif(k=='green' and s=='square'):
                            result = transparentOverlay(bImg,pngImage5,zone2[i],1)
                        elif(k=='green' and s=='circle'):
                            result = transparentOverlay(bImg,pngImage3,zone2[i],1)
                        i=i+1

                if(zone==3):
                    for i in range(mn):
                        if(k=='red' and s=='triangle'):
                            result = transparentOverlay(bImg,pngImage,zone3[i],1)
                        elif(k=='red' and s=='square'):
                            result = transparentOverlay(bImg,pngImage2,zone3[i],1)
                        elif(k=='red' and s=='circle'):
                            result = transparentOverlay(bImg,pngImage1,zone3[i],1)
                        elif(k=='blue' and s=='triangle'):
                            result = transparentOverlay(bImg,pngImage7,zone3[i],1)
                        elif(k=='blue' and s=='square'):
                            result = transparentOverlay(bImg,pngImage8,zone3[i],1)
                        elif(k=='blue' and s=='circle'):
                            result = transparentOverlay(bImg,pngImage6,zone3[i],1)
                        elif(k=='green' and s=='triangle'):
                            result = transparentOverlay(bImg,pngImage4,zone3[i],1)
                        elif(k=='green' and s=='square'):
                            result = transparentOverlay(bImg,pngImage5,zone3[i],1)
                        elif(k=='green' and s=='circle'):
                            result = transparentOverlay(bImg,pngImage3,zone3[i],1)
                        i=i+1

                if(zone==4):
                    for i in range(mn):
                        if(k=='red' and s=='triangle'):
                            result = transparentOverlay(bImg,pngImage,zone4[i],1)
                        elif(k=='red' and s=='square'):
                            result = transparentOverlay(bImg,pngImage2,zone4[i],1)
                        elif(k=='red' and s=='circle'):
                            result = transparentOverlay(bImg,pngImage1,zone4[i],1)
                        elif(k=='blue' and s=='triangle'):
                            result = transparentOverlay(bImg,pngImage7,zone4[i],1)
                        elif(k=='blue' and s=='square'):
                            result = transparentOverlay(bImg,pngImage8,zone4[i],1)
                        elif(k=='blue' and s=='circle'):
                            result = transparentOverlay(bImg,pngImage6,zone4[i],1)
                        elif(k=='green' and s=='triangle'):
                            result = transparentOverlay(bImg,pngImage4,zone4[i],1)
                        elif(k=='green' and s=='square'):
                            result = transparentOverlay(bImg,pngImage5,zone4[i],1)
                        elif(k=='green' and s=='circle'):
                            result = transparentOverlay(bImg,pngImage3,zone4[i],1)
                        i=i+1

                                    
                zone=zone+1                                        ##Writing to csv file
                cv2.imshow("Result",result)
       
        cam.resolution = (320,240)
        raw_cap = PiRGBArray(cam,(320,240))
        time.sleep(1.0)
        break            
            #cn=cn+1
            #cv2.drawContours(color_image1,contours1,-1,(0,255,0),2)
            #cv2.imshow("Video",color_image1)
    

def transparentOverlay(src , overlay , pos,scale = 1):
    """
    :param src: Input Color Background Image
    :param overlay: transparent Image (BGRA)
    :param pos:  position where the image to be blit.
    :param scale : scale factor of transparent image.
    :return: Resultant Image
    """
    overlay = cv2.resize(overlay,(30,30),fx=scale,fy=scale)
    h,w,_ = overlay.shape  # Size of pngImg
    rows,cols,_ = src.shape  # Size of background Image
    y,x = pos[0],pos[1]    # Position of PngImage
    
    #loop over all pixels and apply the blending equation
    for i in range(h):
        for j in range(w):
            if x+i >= rows or y+j >= cols:
                continue
            alpha = float(overlay[i][j][3]/255.0) # read the alpha channel 
            src[x+i][y+j] = alpha*overlay[i][j][:3]+(1-alpha)*src[x+i][y+j]
    return src




bImg = cv2.imread("plantation.png")
# cv2.imshow("aa",bImg)

# KeyPoint : Remember to use cv2.IMREAD_UNCHANGED flag to load the image with alpha channel
pngImage = cv2.imread("tulipred.png", cv2.IMREAD_UNCHANGED)
pngImage1 = cv2.imread("carnation.png" , cv2.IMREAD_UNCHANGED)
pngImage2 = cv2.imread("gerber.png" , cv2.IMREAD_UNCHANGED)
pngImage3 = cv2.imread("lily.png" , cv2.IMREAD_UNCHANGED)
pngImage4 = cv2.imread("hydrangeayellow.png" , cv2.IMREAD_UNCHANGED)
pngImage5 = cv2.imread("sunflower.png" , cv2.IMREAD_UNCHANGED)
pngImage6 = cv2.imread("orchid.png" , cv2.IMREAD_UNCHANGED)
pngImage7 = cv2.imread("tulipblue.png" , cv2.IMREAD_UNCHANGED)
pngImage8 = cv2.imread("hydrangeablue.png" , cv2.IMREAD_UNCHANGED)   
redb = 11
greenb = 15
blueb = 13
#set the GPIO pins of raspberry pi.
GPIO.setmode (GPIO.BOARD)
GPIO.setwarnings (False)
#enable
GPIO.setup(37, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
#setting the GPIO pin as Output
GPIO.setup (33, GPIO.OUT)
GPIO.setup (35, GPIO.OUT)
GPIO.setup (36, GPIO.OUT)
GPIO.setup (38, GPIO.OUT)

GPIO.setup (redb, GPIO.OUT)
GPIO.setup (greenb, GPIO.OUT)
GPIO.setup (blueb, GPIO.OUT)
#GPIO.PWM( pin, frequency ) it generates software PWM
left= GPIO.PWM(37, 100)
right = GPIO.PWM(40, 100)

left.start(0)
right.start(0)

#enable pins of the motor
GPIO.output(33,GPIO.LOW)
GPIO.output(35,GPIO.HIGH)

GPIO.output(36,GPIO.HIGH)
GPIO.output(38,GPIO.LOW)




#initialize a PiCam object
cam = PiCamera()
#set the resolution of the video to be captured// storage type
#set the resolution of the video to be captured
cam.resolution = (320,240)
#create a RGB Array of PiCam storage type
raw_cap = PiRGBArray(cam,(320,240))
#initialize the frame count
frame_cnt = 0
#to capture video coninuously create a video object
time.sleep(1.0)
for frame in cam.capture_continuous(raw_cap,format="bgr",use_video_port=True,splitter_port=2,resize=(320,240)):
#add some sleep to warm up PiCam
    
#print "done warming up"
#capture continuously
#while(True):
    #grab a frame
    #image = frame.next()
    #extract opencv bgr array of color frame
    color_image = frame.array
    #cv2.imshow("Video",color_image)
    cv2.waitKey(1)
    raw_cap.truncate(0)



##capture = cv2.VideoCapture(0)  #read the video
##capture.set(3,320.0) #set the size
##capture.set(4,240.0)  #set the size
##capture.set(5,15)  #set the frame rate
##for i in range(0,2):
##    flag, trash = capture.read() #starting unwanted null value
 

##PROCESSING OF THE IMAGE


    #flag, frame = cam.read() #read the video in frames
    gray=cv2.cvtColor(color_image,cv2.COLOR_BGR2GRAY)#convert each frame to grayscale.
    blur=cv2.medianBlur(gray,7)#blur the grayscale image
    ret,th1 = cv2.threshold(blur,81,255,cv2.THRESH_BINARY)#using threshold remave noise
    ret1,th2 = cv2.threshold(th1,127,255,cv2.THRESH_BINARY_INV)# invert the pixels of the image frame
    a,contours, hierarchy = cv2.findContours(th2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #find the contours
    cv2.drawContours(color_image,contours,-1,(0,255,0),1)
    #cv2.imshow("Video",color_image)
    print len(contours) 
    '''for i in range(0,len(contours)-1):
       area = cv2.contourArea(i)
       print area '''
#01     cv2.imshow('frame',frame) #show video 
    for cnt in contours:
       
      
       if cnt is not None:
           area = cv2.contourArea(cnt)# find the area of contour
           print area
            
           if area>=6000 and area<25000:   ##upper range was 16000
            # find moment and centroid
                M = cv2.moments(cnt)
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                cv2.circle(color_image,(cx,cy), 7, (0,0,255), -1) 
                cv2.circle(color_image,(160,120), 7, (255,0,0), -1)
                
                ##SET DIRECTION BASED ON CENTROID(X) ONLY
                if cx<160 and cy>140:    
                    #PWMR.start (0)
                    #PWML.start (0)
                    right.ChangeDutyCycle (25)
                    GPIO.output(33,GPIO.HIGH)
                    GPIO.output(35,GPIO.LOW)
                    left.ChangeDutyCycle (28)
                    time.sleep(.1)
                    GPIO.output(33,GPIO.LOW)
                    GPIO.output(35,GPIO.HIGH)
                    right.ChangeDutyCycle(0)
                    left.ChangeDutyCycle (0)
                    
                elif cx>=160 and cy>140:    
                    #PWMR.start (0)
                    #PWML.start (0)
                    left.ChangeDutyCycle (28)
                    GPIO.output(38,GPIO.HIGH)
                    GPIO.output(36,GPIO.LOW)
                    right.ChangeDutyCycle (25)
                    time.sleep(.1)
                    GPIO.output(38,GPIO.LOW)
                    GPIO.output(36,GPIO.HIGH)
                    right.ChangeDutyCycle(0)
                    left.ChangeDutyCycle (0)
                    
                
                elif cx<=120:    
                    #PWMR.start (0)
                    #PWML.start (0)
                    right.ChangeDutyCycle (25)
                    left.ChangeDutyCycle (0)
                    time.sleep(.1)
                    right.ChangeDutyCycle(0)
                    left.ChangeDutyCycle (0)
                 
                elif cx>120 and cx<200:
                    #PWMR.start (0)
                    #PWML.start (0)
                    right.ChangeDutyCycle (25)
                    left.ChangeDutyCycle (28)
                    time.sleep(.15)
                    right.ChangeDutyCycle(0)
                    left.ChangeDutyCycle (0)
                  
                  
                elif cx>=220:
                    #PWMR.start (0)
                    #PWML.start (0)
                    right.ChangeDutyCycle (0)
                    left.ChangeDutyCycle (28)
                    time.sleep(.1)
                    right.ChangeDutyCycle(0)
                    left.ChangeDutyCycle (0)
                    
           elif area>=25000 and area<=32000 :
                right.ChangeDutyCycle (25)
                left.ChangeDutyCycle (28)
                time.sleep(.3)
                right.ChangeDutyCycle(0)
                left.ChangeDutyCycle (0)
                time.sleep(2)
                colorDetect()
            
                right.ChangeDutyCycle(0)
                left.ChangeDutyCycle (0)
                time.sleep(2)                   

                if(obj):
                   print s
                break          
            
           elif area>32000 :
                right.ChangeDutyCycle (25)
                left.ChangeDutyCycle (28)
                time.sleep(.1)
                right.ChangeDutyCycle(0)
                left.ChangeDutyCycle (0)          
            
            
    cv2.imshow("Video",color_image)
   
PWMR.start (0)
PWMR1.start (0)                 
PWML.start (0)                 
PWML1.start (0)

print "Stopping motor"
GPIO.output(Motor1E,GPIO.LOW)
GPIO.output(Motor2E,GPIO.LOW)
 
GPIO.cleanup()
cam.release()
cv2.destroyAllWindows()


