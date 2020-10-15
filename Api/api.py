# pip install flask, flask_cours
#python api.py

from flask import Flask, render_template, request
import json
import requests
from flask_cors import CORS, cross_origin
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import flask_cors

count=0

app = Flask(__name__)
cors = CORS(app)

#eye_size=1

@app.route('/all_shapes', methods=['POST','GET'])
def allShapes():
    req = request.args.get('query')
    eyebrows_cluster, eyes_cluster, nose_cluster, lips_cluster, moustache_cluster, beard_cluster = req.split('*')
    oval, circle, square, heart = portrait(eyebrows_cluster,eyes_cluster,nose_cluster,lips_cluster,moustache_cluster,beard_cluster)
    data={}
    data['oval']=oval
    data['round']=circle
    data['square']=square
    data['heart']=heart
    return json.dumps(data)


@app.route('/modify', methods=['POST','GET'])
def modify():
    parameter_string = request.get_json('query')['query']['query']
    #parameter_string = "heart*0*2*0*0*0*0*0*0*1*1"
    print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
    print(parameter_string)
    image_path = resize_portrait(parameter_string)    
    data={}
    data['image_path']= image_path
    return json.dumps(data)


def resize_portrait(parameter_string):
    global count
    param_list = parameter_string.split("*")
    # print(param_list)

    face_shape = param_list[0]
    eyebrow_cluster = param_list[1]
    eyebrow_size = param_list[2]
    eye_cluster = param_list[3]
    eye_size = param_list[4]
    nose_cluster = param_list[5]
    nose_size = param_list[6]
    lips_cluster = param_list[7]
    lips_size = param_list[8]
    moustache_cluster = param_list[9]
    beard_cluster = param_list[10]
    print(beard_cluster)
    print(moustache_cluster)

    general_path = "resize-portrait-images/"

    if face_shape == 'heart' :
        blank_portrait_path = general_path + "face-shape/heart.jpg"
    if face_shape == 'square' :
        blank_portrait_path = general_path + "face-shape/square.jpg"
    if face_shape == 'round' :
        blank_portrait_path = general_path + "face-shape/round.jpg"
    if face_shape == 'oval' :
        blank_portrait_path = general_path + "face-shape/oval.jpg"
        
    back_image = Image.open(blank_portrait_path)
    new_image = back_image.copy()

    left_eyebrow_filename = general_path + "eyebrows-left/" + eyebrow_cluster + "-" + eyebrow_size+ ".jpg"
    right_eyebrow_filename = general_path + "eyebrows-right/" + eyebrow_cluster + "-" + eyebrow_size+ ".jpg"
    left_eye_filename = general_path + "eyes-left/" + eye_cluster + "-" + eye_size + ".jpg"
    right_eye_filename = general_path + "eyes-right/" + eye_cluster + "-" + eye_size + ".jpg"
    nose_filename = general_path + "nose/" + nose_cluster + "-" + nose_size + ".jpg"
    lips_filename = general_path + "lips/" + lips_cluster + "-" + lips_size + ".jpg"

    left_eyebrow = Image.open(left_eyebrow_filename)
    right_eyebrow = Image.open(right_eyebrow_filename)
    left_eye = Image.open(left_eye_filename)
    right_eye = Image.open(right_eye_filename)
    nose = Image.open(nose_filename)
    mouth = Image.open(lips_filename)

    if beard_cluster !='0' :
        beard_filename = general_path + "beard/" + beard_cluster + ".jpg"
        beard = Image.open(beard_filename)
        if face_shape == "heart" :   
            new_image.paste(beard,(45,240))
        if face_shape == "square" :
            new_image.paste(beard,(45,275))
        if face_shape == "round" :
            new_image.paste(beard,(50,205))
        if face_shape == "oval" :
            new_image.paste(beard,(45,290))

    # To generate the new image

    if face_shape == "heart" : 
        new_image.paste(left_eyebrow, (55, 90))
        new_image.paste(right_eyebrow, (135, 90))
        new_image.paste(nose, (100, 155))
        new_image.paste(left_eye, (55, 120))
        new_image.paste(right_eye, (135, 120))
        new_image.paste(mouth, (85, 220))

    if face_shape == "square" : 
        new_image.paste(left_eyebrow, (55, 100))
        new_image.paste(right_eyebrow, (135, 100))
        new_image.paste(nose, (100, 165))
        new_image.paste(left_eye, (55, 130))
        new_image.paste(right_eye, (135, 130))
        new_image.paste(mouth, (85, 230))

    if face_shape == "round" : 
        new_image.paste(left_eyebrow, (55, 88))
        new_image.paste(right_eyebrow, (135, 88))
        new_image.paste(nose, (100, 140))
        new_image.paste(left_eye, (60, 110))
        new_image.paste(right_eye, (140, 110))
        new_image.paste(mouth, (85, 200))

    if face_shape == "oval" : 
        new_image.paste(left_eyebrow, (55, 110))
        new_image.paste(right_eyebrow, (135, 110))
        new_image.paste(nose, (100, 175))
        new_image.paste(left_eye, (55, 140))
        new_image.paste(right_eye, (135, 140))
        new_image.paste(mouth, (85, 240))

    if moustache_cluster != "0" :
        moustache_filename = general_path + "moustache/" + moustache_cluster + ".jpg"
        moustache = Image.open(moustache_filename)
        if face_shape == "heart" :
            new_image.paste(moustache,(88,205))
        if face_shape == "square" :
            new_image.paste(moustache,(88,215))
        if face_shape == "round" :
            new_image.paste(moustache,(88,180))
        if face_shape == "oval" :
            new_image.paste(moustache,(88,220))
    count+=1
    # Return this path to front-end
    image_path = general_path + "image"+str(count)+".jpg"

    new_image.save(image_path,quality=95)
    
    return image_path

def portrait(eyebrows_cluster ,eyes_cluster,nose_cluster,lips_cluster,moustache_cluster,beard_cluster):

    general_path = "default/"

    blank_heart_path = general_path + "face-shape/heart.jpg"
    blank_square_path = general_path + "face-shape/square.jpg"
    blank_round_path = general_path + "face-shape/round.jpg"
    blank_oval_path = general_path + "face-shape/oval.jpg"

    face_heart = Image.open(blank_heart_path)
    heart = face_heart.copy()

    face_square = Image.open(blank_square_path)
    square = face_square.copy()

    face_rounds = Image.open(blank_round_path)
    rounds = face_rounds.copy()

    face_oval = Image.open(blank_oval_path)
    oval = face_oval.copy()

    # beard_cluster = "2"
    # moustache_cluster = "2"
    # eyebrow_cluster = "3"
    # eye_cluster = "3"
    # nose_cluster = "0"
    # lips_cluster = "4"
    
    left_eyebrow_filename = general_path + "eyebrows-left/" + eyebrows_cluster + ".jpg"
    right_eyebrow_filename = general_path + "eyebrows-right/" + eyebrows_cluster + ".jpg"
    left_eye_filename = general_path + "eyes-left/" + eyes_cluster + ".jpg"
    right_eye_filename = general_path + "eyes-right/" + eyes_cluster + ".jpg"
    nose_filename = general_path + "nose/" + nose_cluster + ".jpg"
    lips_filename = general_path + "lips/" + lips_cluster + ".jpg"

    left_eyebrow = Image.open(left_eyebrow_filename)
    right_eyebrow = Image.open(right_eyebrow_filename)
    left_eye = Image.open(left_eye_filename)
    right_eye = Image.open(right_eye_filename)
    nose = Image.open(nose_filename)
    mouth = Image.open(lips_filename)

    if beard_cluster != "0":
        beard_filename = general_path + "beard/" + beard_cluster + ".jpg"
        beard = Image.open(beard_filename)
        heart.paste(beard,(45,240))
        square.paste(beard,(45,275))
        rounds.paste(beard,(50,205))
        oval.paste(beard,(45,290))

    # For Heart shaped portrait
    heart.paste(left_eyebrow, (55, 90))
    heart.paste(right_eyebrow, (135, 90))
    heart.paste(nose, (100, 155))
    heart.paste(left_eye, (55, 120))
    heart.paste(right_eye, (135, 120))
    heart.paste(mouth, (85, 220))

    # For Square shaped portrait
    square.paste(left_eyebrow, (55, 100))
    square.paste(right_eyebrow, (135, 100))
    square.paste(nose, (100, 165))
    square.paste(left_eye, (55, 130))
    square.paste(right_eye, (135, 130))
    square.paste(mouth, (85, 230))

    # For Round shaped portrait
    rounds.paste(left_eyebrow, (55, 75))
    rounds.paste(right_eyebrow, (135, 75))
    rounds.paste(nose, (100, 135))
    rounds.paste(left_eye, (55, 105))
    rounds.paste(right_eye, (135, 105))
    rounds.paste(mouth, (85, 200))

    # For Oval shaped portrait
    oval.paste(left_eyebrow, (55, 110))
    oval.paste(right_eyebrow, (135, 110))
    oval.paste(nose, (100, 175))
    oval.paste(left_eye, (55, 140))
    oval.paste(right_eye, (135, 140))
    oval.paste(mouth, (85, 240))

    if moustache_cluster != "0":
        moustache_filename = general_path + "moustache/" + moustache_cluster + ".jpg"
        moustache = Image.open(moustache_filename)
        heart.paste(moustache,(88,205))
        square.paste(moustache,(88,215))
        rounds.paste(moustache,(88,180))
        oval.paste(moustache,(88,220))

    # Return these 4 paths to front-end
    oval_path = general_path + "image_oval.jpg"
    round_path = general_path + "image_rounds.jpg"
    square_path = general_path + "image_square.jpg"
    heart_path = general_path + "image_heart.jpg"

    oval.save(oval_path,quality=95)
    rounds.save(round_path, quality=95)
    square.save(square_path, quality=95)
    heart.save(heart_path, quality=95)

    return oval_path, round_path, square_path, heart_path

if __name__ == '__main__':
    app.run(debug=True)