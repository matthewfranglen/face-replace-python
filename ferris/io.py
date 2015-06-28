""" Handles loading and saving images """

from os import listdir
from .models import Image

def load_images(source_directory):
    """ Loads the images from the source_directory """
    return [
        Image(filename, source_directory)
        for filename
        in listdir(source_directory)
    ]

def save_images(images, destination_directory):
    """ Saves the images to the destination_directory """
    for image in images:
        image.save(destination_directory)

# vim: set ai et sw=4 syntax=python
