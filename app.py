from flask import Flask, render_template, request
from utils import *
import base64
import cv2
import os
import np
import io
from PIL import Image

app = Flask(__name__)

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('model.xml')
subjects = ["", "Joe Biden", "Donald Trump"]

@app.route('/', methods=['GET', 'POST'])
def index():
    ''' Returns index template '''
    if request.method == 'POST':
        if request.files['image']:
            upload_file = request.files['image']
            pil_img = Image.open(io.BytesIO(upload_file.read())).convert('RGB')
            cv2_img = np.array(pil_img)
            face, rect = detect_face(cv2_img)
            label, conf = face_recognizer.predict(face)
            return "Photo is of " + subjects[label]
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
