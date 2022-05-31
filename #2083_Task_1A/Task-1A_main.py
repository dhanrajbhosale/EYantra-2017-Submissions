#classes and subclasses to import
import cv2
import numpy as np
import os

ix=0
filename = 'results1A_2083.csv'
#################################################################################################
# DO NOT EDIT!!!
#################################################################################################
#subroutine to write results to a csv
def writecsv(color,shape,(cx,cy)):
    global filename
    #open csv file in append mode
    filep = open(filename,'a')
    # create string data to write per image
    datastr = "," + color + "-" + shape + "-" + str(cx) + "-" + str(cy)
    #write to csv
    filep.write(datastr)
    filep.close()

def main(path):
#####################################################################################################
    #Write your code here!!!
#####################################################################################################

    s="Object Not Found"                       
    obj=1
    global ix
    ix=ix+1
    img = cv2.imread(path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,127,255,1)
    img2,contours,h = cv2.findContours(thresh,1,2)
    j=len(contours)                                    
    i=0

    for cnt in contours:
        obj=0
        if(i<j):
            M = cv2.moments(contours[i])
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])                                    ##Finding Centroid
            c=img[cy,cx]
            if c[2]>c[0] and c[2]>c[1]:
                k = "RED"
            elif c[0]>c[1] and c[0]>c[2]:
                k = "BLUE"                                                 ##Finding Color
            elif c[1]>c[0] and c[1]>c[2]:
                k = "GREEN"     
            i=i+1       
        approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)   ##Finding Shape
        if len(approx)==5:
            s = "pentagon"
        elif len(approx)==3:
            s = "triangle"                                         
        elif len(approx)==6:
            s = "hexagon"
        elif len(approx)==4:      
            (x,y,w,h)=cv2.boundingRect(cnt)
            area = cv2.contourArea(cnt)
            peri=cv2.arcLength(cnt,True)
            l=peri/4
            d1=img[cy-(h/2)+10,cx-(w/2)+10]
            d2=img[cy-(h/2)+10,cx+(w/2)-10]
            d3=img[cy+(h/2)-10,cx+(w/2)-10]
            d4=img[cy+(h/2)-10,cx-(w/2)+10]
            result=area/peri
            if result==peri/16:
                s = "Square"
            elif  d1[-1]!=d2[-1] and d3[-1]!=d4[-1]:
                s = "Rhombus"
            else:
                s = "Trapezium" 
        elif len(approx) > 10:
            s = "circle" 
        print k
        print cx,cy,s
        cv2.putText(img,k, (cx,cy), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.75, 0)
        d=cy+15
        cv2.putText(img,s, (cx,d), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.75, 0)
        d=d+15
        cv2.putText(img,"("+str(cx)+","+str(cy)+")", (cx,d), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.75, 0)   ##Printing on contours
        cv2.circle(img,(cx,cy), 2, (255,255,255), -1)                            ##Pointing centroid
        writecsv(k,s,(cx,cy))                                                    ##Writing to csv file
    if(obj):
        print s
    cv2.imwrite('test'+str(ix)+'output'+'.png',img)                              ##Saving Output Images 
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
#################################################################################################
# DO NOT EDIT!!!
#################################################################################################
#main where the path is set for the directory containing the test images
if __name__ == "__main__":
    global filename
    mypath = '.'
    #getting all files in the directory
    onlyfiles = [os.path.join(mypath,f) for f in os.listdir(mypath) if f.endswith(".png")]
    #iterate over each file in the directory
    for fp in onlyfiles:
        #Open the csv to write in append mode
        filep = open(filename,'a')
        #this csv will later be used to save processed data, thus write the file name of the image 
        filep.write(fp)
        #close the file so that it can be reopened again later
        filep.close()
        #process the image
        data = main(fp)
        print data
        #open the csv
        filep = open(filename,'a')
        #make a newline entry so that the next image data is written on a newline
        filep.write('\n')
        #close the file
        filep.close()
