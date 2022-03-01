'''
Flask app main file
'''

import io
from flask import Flask, render_template, request
from PIL import Image
import np
import utils

server = Flask(__name__)

face_recognizer = utils.cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('model.xml')
subjects = ["", "Joe Biden", "Donald Trump"]

@server.route('/', methods=['GET', 'POST'])
def index():
    ''' Returns index template '''
    if request.method == 'POST':
        if request.files['image']:
            upload_file = request.files['image']
            try:
                pil_img = Image.open(io.BytesIO(upload_file.read())).convert('RGB')
                cv2_img = np.array(pil_img)
                face, _ = utils.detect_face(cv2_img)
                label, _ = face_recognizer.predict(face)
                return "Photo is of " + subjects[label]
            except:
                return "Please ensure your file uploaded is an image"
    return render_template('index.html')

