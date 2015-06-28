""" Handles detecting faces in images """

# pylint: disable=no-self-use, too-few-public-methods

import cv2
from .settings import IMAGE_CLASSIFIER_FILE

CLASSIFIER = cv2.CascadeClassifier(IMAGE_CLASSIFIER_FILE)

class CV(object):
    """ Handles detecting faces in images """

    def detect_faces(self, images):
        """ Detect faces in all provided images """
        for image in images:
            self._detect_faces(image)

    def _detect_faces(self, image):
        """ Detect faces in the provided image """
        faces = CLASSIFIER.detectMultiScale(image.cv_image)

        if len(faces) == 0:
            return

        faces[:, 2:] += faces[:, :2]
        image.faces = faces

# vim: set ai et sw=4 syntax=python
