from imutils.face_utils import FaceAligner
from imutils.face_utils import rect_to_bb
import argparse
import imutils
import dlib
import cv2


detector = dlib.get_frontal_face_detector()
predictor_path = "shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor(predictor_path)

fa = FaceAligner(predictor, desiredFaceWidth=256)

for i in range(5):
	filename = "center_" + str(i)+".jpg"
	filename_path = "/Users/dhairyapat/Desktop/SIH/face-alignment/nose/" + filename
	image = cv2.imread(filename_path)

	image = imutils.resize(image, width=800)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	cv2.imshow("Input", image)
	rects = detector(gray, 2)

	# loop over the face detections
	for rect in rects:
		# extract the ROI of the *original* face, then align the face
		# using facial landmarks
		(x, y, w, h) = rect_to_bb(rect)
		faceOrig = imutils.resize(image[y:y + h, x:x + w], width=256)
		faceAligned = fa.align(image, gray, rect)

		cv2.imwrite(filename, faceAligned)

		# To display the output images uncomment the below code
		#cv2.imshow("Original", faceOrig)
		#cv2.imshow("Aligned", faceAligned)
		#cv2.waitKey(0)