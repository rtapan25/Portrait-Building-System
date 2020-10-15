import dlib
import numpy as np
from skimage import io


predictor_path = "shape_predictor_68_face_landmarks.dat"

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)

attributes = []

for i in range(9600):
    filename = str(i)+".jpg"
    filename_path = "/Users/dhairyapat/Desktop/SIH/CDDATA/FACE/" + filename
    img = io.imread(filename_path)

    dets = detector(img)

    #output face landmark points inside retangle
    for k, d in enumerate(dets):
        shape = predictor(img, d)

    vec = np.empty([68, 2], dtype = int)
    for b in range(68):
        vec[b][0] = shape.part(b).x
        vec[b][1] = shape.part(b).y
    
    d = {}

    lips_width = abs(vec[54][0]-vec[48][0]) 
    lips_height = (abs(vec[50][1]-vec[58][1]) + abs(vec[51][1]-vec[57][1]) + abs(vec[52][1]-vec[56][1])) / 3
    left_eyebrow_length = abs(vec[21][0]-vec[17][0])
    right_eyebrow_length = abs(vec[26][0]-vec[22][0])
    left_eye_width = abs(vec[39][0]-vec[36][0])
    left_eye_height = (abs(vec[37][1]-vec[41][1]) + abs(vec[40][1]-vec[38][1])) / 2 
    right_eye_height = (abs(vec[47][1]-vec[43][1]) + abs(vec[46][1]-vec[44][1])) / 2    
    right_eye_width = abs(vec[45][0]-vec[42][0])
    nose_height = abs(vec[33][1]-vec[27][1]) 
    nose_width = abs(vec[35][0]-vec[31][0])

    d["image-name"] = filename
    d["lips_width"] = lips_width
    d["lips_height"] = round(lips_height,2)
    d["left_eyebrow_length"] = left_eyebrow_length
    d["right_eyebrow_length"] = right_eyebrow_length
    d["left_eye_width"] = left_eye_width
    d["left_eye_height"] = left_eye_height
    d["right_eye_height"] = right_eye_height
    d["right_eye_width"] = right_eye_width
    d["nose_height"] = nose_height
    d["nose_width"] = nose_width 
    
    attributes.append(d)
   

with open('attributes.txt', 'w+') as f:
    for attribute in attributes:
        f.write("%s\n" % attribute)

