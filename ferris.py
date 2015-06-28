""" Detect and manipulate faces """

from sys import argv, exit
from ferris.io import load_images, save_images
from ferris.cv import detect_faces
from ferris.manipulate_image import box_faces, get_faces, merge_faces

# pylint: disable=invalid-name

if __name__ == "__main__":
    if len(argv) < 3:
        print "Requires source and destination directories"
        exit(1)

    source_directory = argv[1]
    destination_directory = argv[2]

    print "Loading images..."
    images = load_images(source_directory)

    print "Detecting faces..."
    detect_faces(images)

    print "Changing faces..."
    box_faces(images)

    print "Saving results..."
    save_images(images, destination_directory)
    print "Done!"

# vim: set ai et sw=4 syntax=python
