""" Handles loading and saving images """

# pylint: disable=no-self-use

from os import listdir
from .models import Image

class IO(object):
    """ Handles loading and saving images """

    def load_images(self, source_directory):
        """ Loads the images from the source_directory """
        return [
            Image(filename, source_directory)
            for filename
            in listdir(source_directory)
        ]

    def save_images(self, images, destination_directory):
        """ Saves the images to the destination_directory """
        for image in images:
            image.save(destination_directory)

# vim: set ai et sw=4 syntax=python
