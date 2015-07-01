""" Handles detecting faces in images """

# pylint: disable=no-member, star-args

import cv2
from .models import Face
from .settings import IMAGE_CLASSIFIER_FILE

CLASSIFIER = cv2.CascadeClassifier(IMAGE_CLASSIFIER_FILE)

def detect_faces(images):
    """ Detect faces in all provided images """
    return (_detect_faces(image) for image in images)

def _detect_faces(image):
    """ Detect faces in the provided image """
    faces = CLASSIFIER.detectMultiScale(image.cv_image)

    if len(faces) == 0:
        return image

    faces[:, 2:] += faces[:, :2]
    image.faces = [Face(*face) for face in faces]

    return image

# vim: set ai et sw=4 syntax=python
