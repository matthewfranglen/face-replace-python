""" Handles storing image data """

# pylint: disable=no-self-use, too-few-public-methods, no-member, invalid-name

from os.path import join
import PIL.Image
import cv2


class Image(object):
    """ A single picture """

    def __init__(self, name, folder=None, path=None):
        self.name = name

        if folder and not path:
            path = join(folder, name)

        if path:
            self.image = PIL.Image.open(path)
            self.cv_image = cv2.imread(path)

        self.faces = []

    def crop(self, face):
        """ Return a new Image cropped to the face """
        result = Image(self.name)
        result.image = self.image.crop(face.as_box())

        return result

    def save(self, folder):
        """ Saves image to the folder """
        path = join(folder, self.name)
        self.image.save(path)


class Face(object):
    """ A detected face in a picture """

    def __init__(self, left, top, right, bottom):
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom

    def as_box(self):
        """ Returns a box for PIL.Image use """
        return (self.left, self.top, self.right, self.bottom)

    def as_dimension(self):
        """ Returns the width and height """
        return (self.right - self.left, self.bottom - self.top)


# vim: set ai et sw=4 syntax=python
