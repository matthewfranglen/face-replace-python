""" Detect and manipulate faces """

from sys import argv, exit
from ferris.io import load_images, save_images
from ferris.cv import detect_faces
from ferris.manipulate_image import box_faces, get_faces, merge_faces
from ferris.models import Image

# pylint: disable=invalid-name

def _load_merge_face(merge_face_path, merge_image_path):
    """ Loads the two images,
        uses the merge_face to detect the face region
        and then crops that area from the image.
        This allows the image to be altered to merge better. """

    face = Image('merge', path=merge_face_path)
    image = Image('merge', path=merge_image_path)
    list(detect_faces([face])) # force evaluation

    return image.crop(face.faces[0])

if __name__ == "__main__":
    if len(argv) < 5:
        print "Requires merge face and image,"
        print "source and destination directories"
        exit(1)

    print "Loading merge images..."
    merge_face = _load_merge_face(argv[1], argv[2])

    source_directory = argv[3]
    destination_directory = argv[4]

    print "Starting..."
    io_pipe = load_images(source_directory)
    detect_pipe = detect_faces(io_pipe)
    merge_pipe = merge_faces(merge_face, detect_pipe)
    save_images(merge_pipe, destination_directory)
    print "Done!"

# vim: set ai et sw=4 syntax=python
