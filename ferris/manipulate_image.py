""" Handles changing images """

import PIL.ImageDraw

# pylint: disable=no-self-use, no-member

class ImageManipulator(object):
    """ Handles changing images """

    def box_faces(self, images):
        """ Add borders to all detected faces """
        for image in images:
            self._box_faces(image)

    def _box_faces(self, image):
        """ Add borders to all detected faces """
        for face in image.faces:
            self._box_face(image, face)

    def _box_face(self, image, face):
        """ Add borders to detected face """
        draw = PIL.ImageDraw.Draw(image.image)
        draw.rectangle(face, outline=(127, 255, 0))

    def get_faces(self, image):
        """ Returns images reduced to just the face """
        return [image.crop(face) for face in image.faces]

    def merge_faces(self, merge, images):
        """ Merge image onto all detected faces """
        for image in images:
            self._merge_faces(merge, image)

    def _merge_faces(self, merge, image):
        """ Merge image onto all detected faces """
        for face in image.faces:
            self._merge_face(merge, image, face)

    def _merge_face(self, merge, image, face):
        """ Merge image onto detected face """
        scaled = merge.image.resize((face.width, face.height))
        image.image.paste(scaled, face.as_tuple())

# vim: set ai et sw=4 syntax=python
