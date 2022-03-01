'''
Trains our face-recognition model and saves as an XML file
'''

import np
import utils

faces, labels = utils.prepare_training_data("faces")
face_recognizer = utils.cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(faces, np.array(labels))
face_recognizer.save('model.xml')
