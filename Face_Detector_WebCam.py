import cv2
from random import randrange
# Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Choose an image to detect faces in
webcam = cv2.VideoCapture(0)

while True:
    
    successful_frame_read, frame = webcam.read()
# Must convert to grayscale
    grayscaled_img = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
# Detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    # Draw rectangles around the faces
    for(x,y,w,h) in face_coordinates:
        cv2.rectangle(grayscaled_img , (x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow('Rishi',grayscaled_img)
    cv2.waitKey(1)

print("Code Completed ")

