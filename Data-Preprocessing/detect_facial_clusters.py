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

#Save Directory Path
directory = directory = r'/Users/dhairyapat/Desktop/SIH/CDDATA/BlackBackgroundClusters'
os.chdir(directory) 

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
    #output = imutils.resize(output, height=250)

    overlay = output.copy()

    if colors is None:
        colors = [(19, 199, 109), (79, 76, 240), (230, 159, 23),
			(168, 100, 168), (158, 163, 32),
			(163, 38, 32), (180, 42, 220)]

	# loop over the facial landmark regions individually
    for (i, name) in enumerate(FACIAL_LANDMARKS_IDXS.keys()):

        (j, k) = FACIAL_LANDMARKS_IDXS[name]
        pts = shape[j:k]
=        if name == "jaw":

            for l in range(1, len(pts)):
                ptA = tuple(pts[l - 1])
                ptB = tuple(pts[l])
                cv2.line(overlay, ptA, ptB, colors[i], 2)

        else:
            hull = cv2.convexHull(pts)
            cv2.drawContours(overlay, [hull], -1, colors[i], -1)
	
    cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)
	# return the output image
    return output

for i in range(9600):
	
	filename = str(i)+".jpg"
	filename_path = "/Users/dhairyapat/Desktop/SIH/CDDATA/FACE/" + filename
	image = cv2.imread(filename_path)
	image = imutils.resize(image, width=250)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# detect faces in the grayscale image
	rects = detector(gray, 1)

	# loop over the face detections
	for (i, rect) in enumerate(rects):

		shape = predictor(gray, rect)
		shape = face_utils.shape_to_np(shape)

		# visualize all facial landmarks with a transparent overlay
		output = visualize_facial_landmarks(image, shape)

		cv2.imwrite(filename,output)