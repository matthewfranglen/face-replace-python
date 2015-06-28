""" Handles detecting faces in images """

# pylint: disable=no-member

import cv2
from .settings import IMAGE_CLASSIFIER_FILE

CLASSIFIER = cv2.CascadeClassifier(IMAGE_CLASSIFIER_FILE)

def detect_faces(images):
    """ Detect faces in all provided images """
    for image in images:
        _detect_faces(image)

def _detect_faces(image):
    """ Detect faces in the provided image """
    faces = CLASSIFIER.detectMultiScale(image.cv_image)

    if len(faces) == 0:
        return

    faces[:, 2:] += faces[:, :2]
    image.faces = faces

# vim: set ai et sw=4 syntax=python
