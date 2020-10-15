# We import the necessary packages 
from imutils import face_utils 
import numpy as np 
import argparse 
import imutils 
import dlib 
import cv2 
import os

  
detector = dlib.get_frontal_face_detector()
predictor_path = "shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor(predictor_path)
  
#Save Directory Path
directory = directory = r'/Users/dhairyapat/Desktop/SIH/CDDATA/try'
os.chdir(directory) 

for i in range(2):
    # We then load the input image, resize it, and convert it to grayscale 
    # filename = str(i)+".jpg"
    filename_path = "/Users/dhairyapat/Desktop/SIH/CDDATA/FACE/30.jpg" #+ filename
	# load the input image, resize it, and convert it to grayscale
    image = cv2.imread(filename_path)
    image = imutils.resize(image, width=250)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# detect faces in the grayscale image
    rects = detector(gray, 1)

    
    for (i, rect) in enumerate(rects): 

        shape = predictor(gray, rect) 
        shape = face_utils.shape_to_np(shape) 
    
        for (x, y) in shape: 
            cv2.circle(image, (x, y), 2, (0, 0, 255), -1) 

    cv2.imwrite("output.jpg",image)
    