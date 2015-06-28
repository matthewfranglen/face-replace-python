""" Detect and manipulate faces """

from sys import argv
from ferris.io import load_images, save_images
from ferris.cv import detect_faces
from ferris.manipulate_image import box_faces, get_faces, merge_faces

# pylint: disable=invalid-name

if __name__ == "__main__":
    if len(argv) < 2:
        print "Requires source and destination directories"

    source_directory = argv[1]
    destination_directory = argv[2]

    images = load_images(source_directory)
    detect_faces(images)
    box_faces(images)
    save_images(images, destination_directory)

# vim: set ai et sw=4 syntax=python
