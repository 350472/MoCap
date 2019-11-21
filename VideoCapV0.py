"""
11/19/19
Alex Fryer
Code to Capture Joint Angle
"""

#import libraries
import cv2
key = 0

#Request min/max angles
cap = cv2.VideoCapture("obrism.gif")

while (key != 27):
    
#Capture image from camera
    ret, frame = cap.read()
#Create window
    cv2.namedWindow("Vid",cv2.WINDOW_NORMAL)

#Display images in window
    cv2.imshow("Vid",frame)

#Wait for button press
    key = cv2.waitKey(1)
#Destroy windows/save
    if key == 27:
        cv2.destroyAllWindows()