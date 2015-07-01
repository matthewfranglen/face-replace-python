""" Handles changing images """

import PIL.ImageDraw

def box_faces(images):
    """ Add borders to all detected faces """
    return (_box_faces(image) for image in images)

def _box_faces(image):
    """ Add borders to all detected faces """
    for face in image.faces:
        _box_face(image, face)
    return image

def _box_face(image, face):
    """ Add borders to detected face """
    draw = PIL.ImageDraw.Draw(image.image)
    draw.rectangle(face.as_box(), outline="yellow")

def get_faces(image):
    """ Returns images reduced to just the face """
    return (image.crop(face) for face in image.faces)

def merge_faces(merge, images):
    """ Merge image onto all detected faces """
    return (_merge_faces(merge, image) for image in images)

def _merge_faces(merge, image):
    """ Merge image onto all detected faces """
    for face in image.faces:
        _merge_face(merge, image, face)
    return image

def _merge_face(merge, image, face):
    """ Merge image onto detected face """
    scaled = merge.image.resize(face.as_dimension())
    image.image.paste(scaled, face.as_box(), mask=scaled)

# vim: set ai et sw=4 syntax=python
