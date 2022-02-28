'''
Trains our face-recognition model and saves as an XML file
'''

from utils import *

faces, labels = prepare_training_data("faces")
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(faces, np.array(labels))
face_recognizer.save('model.xml')
