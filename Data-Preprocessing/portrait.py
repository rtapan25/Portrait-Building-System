from PIL import Image, ImageDraw, ImageFilter

face_heart = Image.open('/Users/dhairyapat/Desktop/SIH/Portrait/default/face-shape/heart.jpg')
heart = face_heart.copy()

face_square = Image.open('/Users/dhairyapat/Desktop/SIH/Portrait/default/face-shape/square.jpg')
square = face_square.copy()

face_rounds = Image.open('/Users/dhairyapat/Desktop/SIH/Portrait/default/face-shape/round.jpg')
rounds = face_rounds.copy()

face_oval = Image.open('/Users/dhairyapat/Desktop/SIH/Portrait/default/face-shape/oval.jpg')
oval = face_oval.copy()

beard_cluster = "7"
moustache_cluster = "2"
eyebrow_cluster = "3"
eye_cluster = "3"
nose_cluster = "0"
lips_cluster = "4"

general_path = "/Users/dhairyapat/Desktop/SIH/Portrait/default/"
left_eyebrow_filename = general_path + "eyebrows-left/" + eyebrow_cluster + ".jpg"
right_eyebrow_filename = general_path + "eyebrows-right/" + eyebrow_cluster + ".jpg"
left_eye_filename = general_path + "eyes-left/" + eye_cluster + ".jpg"
right_eye_filename = general_path + "eyes-right/" + eye_cluster + ".jpg"
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

save_path = "/Users/dhairyapat/Desktop/SIH/Portrait/default/"

# Return these 4 paths to front-end
oval_path = save_path + "image_oval.jpg"
rounds_path = save_path + "image_rounds.jpg"
square_path = save_path + "image_square.jpg"
heart_path = save_path + "image_heart.jpg"

oval.save(oval_path,quality=95)
rounds.save(rounds_path, quality=95)
square.save(square_path, quality=95)
heart.save(heart_path, quality=95)


