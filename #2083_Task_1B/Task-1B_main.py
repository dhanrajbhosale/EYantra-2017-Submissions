#classes and subclasses to import
import cv2
import numpy as np
import os
path_to_video_mp4_file_with_name="Video.mp4"
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('Video_output.avi',fourcc,16,(1280,720))


filename = 'result1B_2083.csv'
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
#################################################################################################
# DO NOT EDIT!!!
#################################################################################################
def blend_transparent(face_img, overlay_t_img):
    # Split out the transparency mask from the colour info
    overlay_img = overlay_t_img[:,:,:3] # Grab the BRG planes
    overlay_mask = overlay_t_img[:,:,3:]  # And the alpha plane

    # Again calculate the inverse mask
    background_mask = 255 - overlay_mask

    # Turn the masks into three channel, so we can use them as weights
    overlay_mask = cv2.cvtColor(overlay_mask, cv2.COLOR_GRAY2BGR)
    background_mask = cv2.cvtColor(background_mask, cv2.COLOR_GRAY2BGR)

    # Create a masked out face image, and masked out overlay
    # We convert the images to floating point in range 0.0 - 1.0
    face_part = (face_img * (1 / 255.0)) * (background_mask * (1 / 255.0))
    overlay_part = (overlay_img * (1 / 255.0)) * (overlay_mask * (1 / 255.0))

    # And finally just add them together, and rescale it back to an 8bit integer image    
    return np.uint8(cv2.addWeighted(face_part, 255.0, overlay_part, 255.0, 0.0))


def main(video_file_with_path):
    cap = cv2.VideoCapture(video_file_with_path)
    image_red = cv2.imread("Overlay_Images\\yellow_flower.png",-1)
    image_blue = cv2.imread("Overlay_Images\\pink_flower.png",-1)
    image_green = cv2.imread("Overlay_Images\\red_flower.png",-1)

########################################################################################## ###########
    #Write your code here!!!
#####################################################################################################



 
    jprev=1 
    list1=[]
    rise=0
    status=0
    
    while(cap.isOpened()):
       
        ret, img = cap.read()
        if(ret):
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            ret,thresh = cv2.threshold(gray,100,255,0)
            img2,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            j=len(contours)
            if(jprev!=j):
                rise=1                                          ##detecting new contour
                jprev=j
                
            if rise==1:                                          
                for i in range (1,j):                           
                    M = cv2.moments(contours[i])                ##Getting Centroid
                    cx = int(M['m10']/M['m00'])
                    cy = int(M['m01']/M['m00'])
                    
                    cc=[cx,cy]
                    if (j==2):
                        list1.append(cc)                         ## Creating Centroid list and appending first centroid without comparing
                        c=img[cy,cx]
                        i1=i
                        cx1=cx
                        cy1=cy
                    else:
                        for p in range (0,len(list1)):
                            if(list1[p]==cc):                    ##Comparing centroids of new frame with previous frame contours 
                                status=0                         ##Old centroid then Status =0
                                break
                            status=1                             ##New centroid then status =1
                    if(status==1):
                        list1.append(cc)                         ##Appending new centroid  
                        c=img[cy,cx]
                        i1=i
                        cx1=cx                                  
                        cy1=cy
                        status=0
                        
                if c[0]==0 and c[1]==0:
                    k = image_red
                    k1= "RED"                                   ##Detecting Color
                elif c[1]==0 and c[2]==0:
                    k = image_blue
                    k1="BLUE"
                elif c[0]==0 and c[2]==0:
                    k = image_green
                    k1="GREEN"

                approx = cv2.approxPolyDP(contours[i1],0.01*cv2.arcLength(contours[i1],True),True) 
                if len(approx)==5:
                    s = "pentagon"
                    area = cv2.contourArea(contours[i1])
                elif len(approx)==3:                             ##Detecting Shape
                    s = "triangle"
                elif len(approx)==6:
                    s = "hexagon"
                elif len(approx)==4:      
                    (x,y,w,h)=cv2.boundingRect(contours[i1])
                    area = cv2.contourArea(contours[i1])
                    peri=cv2.arcLength(contours[i1],True)
                    l=peri/4
                    d1=img[cy1-(h/2)+10,cx1-(w/2)+10]
                    d2=img[cy1-(h/2)+10,cx1+(w/2)-10]
                    d3=img[cy1+(h/2)-10,cx1+(w/2)-10]
                    d4=img[cy1+(h/2)-10,cx1-(w/2)+10]
                    result=area/peri
                    if result==peri/16:
                        s = "Square"
                    elif  d1[-1]!=d2[-1] and d3[-1]!=d4[-1]:
                        s = "Rhombus"
                    else:
                        s = "Trapazium" 
                elif len(approx) > 10:
                    s = "circle" 

                writecsv(k1,s,(cx1,cy1))                        ##Writing to csv file
                print k1,s,cx1,cy1
                rise=0
            if(j>1): 
                    x,y,w,h = cv2.boundingRect(contours[i1])    ##Overlay function
                    overlay_image = cv2.resize(k,(h,w))
                    img[y:y+w,x:x+h,:] = blend_transparent(img[y:y+w,x:x+h,:], overlay_image)
                    (x,y,w,h)=cv2.boundingRect(contours[i1])
                
                        
                
            ## Show the image
            out.write(img)
            cv2.imshow('image',img)
            
            cv2.waitKey(40)
        else:
            break

        

    cap.release()
    cv2.destroyAllWindows()




#####################################################################################################
    #sample of overlay code for each frame
    #x,y,w,h = cv2.boundingRect(current_contour)
    #overlay_image = cv2.resize(image_red,(h,w))
    #frame[y:y+w,x:x+h,:] = blend_transparent(frame[y:y+w,x:x+h,:], overlay_image)
#######################################################################################################

#################################################################################################
# DO NOT EDIT!!!
#################################################################################################
#main where the path is set for the directory containing the test images
if __name__ == "__main__":
   
    main(path_to_video_mp4_file_with_name)
