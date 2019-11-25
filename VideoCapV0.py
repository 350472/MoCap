"""
11/19/19
Alex Fryer
Code to Capture Joint Angle
"""

#import libraries
import cv2
import numpy
key = 0

cv2.namedWindow('Color Sliders',cv2.WINDOW_NORMAL)

cv2.createTrackbar('CSliderB0','Color Sliders',0,0,lambda x:None) 
cv2.createTrackbar('CSliderG0','Color Sliders',0,0,lambda x:None) 
cv2.createTrackbar('CSliderR0','Color Sliders',0,0,lambda x:None) 

#Request min/max angles
cap = cv2.VideoCapture(0)

while (key != 27):
    
    B = cv2.getTrackbarPos('CSliderB0','Color Sliders')
    G = cv2.getTrackbarPos('CSliderG0','Color Sliders')
    R = cv2.getTrackbarPos('CSliderR0','Color Sliders')
    
#Capture image from camera
    ret, frame = cap.read()
#Create window
    cv2.namedWindow("Vid",cv2.WINDOW_NORMAL)
    
    ImgH = frame.shape[0]
    ImgW = frame.shape[1]
    ImgC = frame.shape[2]
    
    Pap = numpy.zeros((ImgH,ImgW,ImgC), numpy.uint8)
    
    Pap[0:ImgH,0:ImgW, 0:ImgC] = [B,G,R]
    
    COut0 = cv2.inRange(frame, B , 255)
    
    Img = cv2.bitwise_or(Pap, Pap, mask = COut0) 
#Display images in window
    cv2.imshow("Vid",Img)

#Wait for button press
    key = cv2.waitKey(1)
#Destroy windows/save
    if key == 27:
        cv2.destroyAllWindows()