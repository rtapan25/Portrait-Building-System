from collections import OrderedDict 
from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2
from resizeimage import resizeimage
import os


detector = dlib.get_frontal_face_detector()
predictor_path = "shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor(predictor_path)

#Save Directory Path # Change the below path
#directory = r'/Users/dhairyapat/Desktop/SIH/CDDATA/BlackBackgroundClusters'
#os.chdir(directory) 

FACIAL_LANDMARKS_IDXS = OrderedDict([
	("mouth", (48, 68)),
	("right_eyebrow", (17, 22)),
	("left_eyebrow", (22, 27)),
	("right_eye", (36, 42)),
	("left_eye", (42, 48)),
	("nose", (27, 35)),
	("jaw", (0, 17))
])

def visualize_facial_landmarks(image, shape, colors=None, alpha=0.75):

    black_image_path = "/Users/dhairyapat/Desktop/SIH/black-resize.jpg"
    output = cv2.imread(black_image_path)

    overlay = output.copy()

    if colors is None:
        colors = [(19, 199, 109), (79, 76, 240), (230, 159, 23),
			(168, 100, 168), (158, 163, 32),
			(163, 38, 32), (180, 42, 220)]

	# loop over the facial landmark regions individually
    for (i, name) in enumerate(FACIAL_LANDMARKS_IDXS.keys()):

        (j, k) = FACIAL_LANDMARKS_IDXS[name]
        pts = shape[j:k]
        if name == "jaw":

            for l in range(1, len(pts)):
                ptA = tuple(pts[l - 1])
                ptB = tuple(pts[l])
                cv2.line(overlay, ptA, ptB, colors[i], 2)

        elif name == "mouth" :
            output = cv2.imread(black_image_path)
            overlay = output.copy()
            directory = r'/Users/dhairyapat/Desktop/SIH/CDDATA/BlackBackgroundLips'
            os.chdir(directory) 
            hull = cv2.convexHull(pts)
            cv2.drawContours(overlay, [hull], -1, colors[i], -1)
            cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)
            cv2.imwrite(filename,output)

        elif name == "left_eyebrow" :
            directory = r'/Users/dhairyapat/Desktop/SIH/CDDATA/BlackBackgroundEyebrows'
            os.chdir(directory) 
            hull = cv2.convexHull(pts)
            cv2.drawContours(overlay, [hull], -1, colors[i], -1)
            cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)
            cv2.imwrite(filename,output)

        elif name == "left_eye" :
            directory = r'/Users/dhairyapat/Desktop/SIH/CDDATA/BlackBackgroundEyes'
            os.chdir(directory) 
            hull = cv2.convexHull(pts)
            cv2.drawContours(overlay, [hull], -1, colors[i], -1)
            cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)
            cv2.imwrite(filename,output)

        elif name == "nose" :
            output = cv2.imread(black_image_path)
            overlay = output.copy()
            directory = r'/Users/dhairyapat/Desktop/SIH/CDDATA/BlackBackgroundNose'
            os.chdir(directory) 
            hull = cv2.convexHull(pts)
            cv2.drawContours(overlay, [hull], -1, colors[i], -1)
            cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)
            cv2.imwrite(filename,output)

        else:
            output = cv2.imread(black_image_path)
            overlay = output.copy()
            hull = cv2.convexHull(pts)
            cv2.drawContours(overlay, [hull], -1, colors[i], -1)
	


for i in range(9600):
	print(i)
	filename = str(i)+".jpg"
	filename_path = "/Users/dhairyapat/Desktop/SIH/CDDATA/FACE/" + filename
	# load the input image, resize it, and convert it to grayscale
	image = cv2.imread(filename_path)
	image = imutils.resize(image, width=250)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# detect faces in the grayscale image
	rects = detector(gray, 1)

	# loop over the face detections
	for (i, rect) in enumerate(rects):

		shape = predictor(gray, rect)
		shape = face_utils.shape_to_np(shape)

		visualize_facial_landmarks(image, shape)
        # To show the image on a window uncomment the below code
		#cv2.imshow("Image", output)
		#cv2.waitKey(0)
		#cv2.imwrite(filename,output)