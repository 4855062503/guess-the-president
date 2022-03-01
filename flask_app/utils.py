'''
Utils module for Flask app and train script
'''

import os
import cv2

def draw_rectangle(img, rect):
    ''' draws rectangle '''
    (x_dimension, y_dimension, width, height) = rect
    cv2.rectangle(
            img, (x_dimension, y_dimension), (x_dimension+width, y_dimension+height), (0, 255, 0), 2
            )

def draw_text(img, text, x_dimension, y_dimension):
    ''' draws text '''
    cv2.putText(img, text, (x_dimension, y_dimension), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)

def detect_face(img):
    ''' detects face '''
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
            )
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    if len(faces) == 0:
        return None, None
    (x_dimension, y_dimension, width, height) = faces[0]
    return gray[y_dimension:y_dimension+width, x_dimension:x_dimension+height], faces[0]

def prepare_training_data(data_folder_path):
    ''' prepares training data '''
    dirs = os.listdir(data_folder_path)
    #list to hold all subject faces
    faces = []
    #list to hold labels for all subjects
    labels = []

    #let's go through each directory and read images within it
    for dir_name in dirs:
        if not dir_name.startswith("s"):
            continue

        label = int(dir_name.replace("s", ""))
        subject_dir_path = data_folder_path + "/" + dir_name
        subject_images_names = os.listdir(subject_dir_path)
        for image_name in subject_images_names:
            #ignore system files like .DS_Store
            if image_name.startswith("."):
                continue

            image_path = subject_dir_path + "/" + image_name
            image = cv2.imread(image_path)
            face, _ = detect_face(image)
            if face is not None:
                faces.append(face)
                labels.append(label)

    return faces, labels
