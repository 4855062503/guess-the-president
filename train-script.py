from utils import *

faces, labels = prepare_training_data("faces")
# Instantiate the face_recognizer
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(faces, np.array(labels))

def predict(test_img):
    subjects = ["", "Joe Biden", "Donald Trump"]
    img = test_img.copy()
    face, rect = detect_face(img)
    label, conf = face_recognizer.predict(face)
    label_text = subjects[label]
    print("President predicted is " + label_text)
    draw_rectangle(img, rect)
    draw_text(img, label_text, rect[0], rect[1]-5)
    return img

test_img = cv2.imread('test-img.jpg')
predicted_img = predict(test_img)
face_recognizer.save('model.xml')
