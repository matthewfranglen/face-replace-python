""" Detect and manipulate faces """

from sys import argv, exit
from ferris.io import load_images, save_images
from ferris.cv import detect_faces
from ferris.manipulate_image import box_faces, get_faces, merge_faces
from ferris.models import Image

# pylint: disable=invalid-name

if __name__ == "__main__":
    if len(argv) < 5:
        print "Requires merge face and image, source directory and destination directory"
        exit(1)

    merge_face_path = argv[1]
    merge_image_path = argv[2]
    source_directory = argv[3]
    destination_directory = argv[4]

    print "Loading images..."
    merge_face = Image('merge', path=merge_face_path)
    merge_image = Image('merge', path=merge_image_path)
    images = load_images(source_directory)

    print "Detecting faces..."
    detect_faces(images + [merge_face])

    merge_face = merge_image.crop(merge_face.faces[0])

    print "Changing faces..."
    merge_faces(merge_face, images)

    print "Saving results..."
    save_images(images, destination_directory)
    print "Done!"

# vim: set ai et sw=4 syntax=python
