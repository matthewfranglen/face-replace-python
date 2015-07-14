Silly Face Replace
==================

This searches for faces within an image and replaces them with the first face
found from an image of your choosing. Some crummy bash scripts have been
written to help convert video to and from images.

### Installation

    sudo apt-get install python-opencv
    git clone git@github.com:matthewfranglen/face-replace-python.git face-replace
    cd face-replace

### Conversion

    python ferris.py REPLACEMENT_IMAGE REPLACEMENT_IMAGE INPUT_FOLDER/ OUTPUT_FOLDER/

This will convert all images in *INPUT_FOLDER*. It will replace any faces with
*REPLACEMENT_IMAGE* and save the updated image to *OUTPUT_FOLDER*.

### Altering the Replacement Image

The replacement face can be detected from one image and then taken from
another, allowing you to alter the replacement face (such as masking it).

    python ferris.py DETECT_IMAGE REPLACE_IMAGE INPUT_FOLDER/ OUTPUT_FOLDER/

Here the *DETECT_IMAGE* is used to find the face, and then the same area is
copied from the *REPLACE_IMAGE*. It is recommended that these be the same size.
The size and position of the detected face is not scaled or moved to match the
dimensions of the replacement image.

### Converting Video

You can use the scripts in the _bin_ folder to handle videos. This requires
ffmpeg. The output video is saved in the mpeg4 format.

    bin/strip INPUT_VIDEO INPUT_FOLDER AUDIO_FILE
    python ferris.py DETECT_IMAGE REPLACE_IMAGE INPUT_FOLDER/ OUTPUT_FOLDER/
    bin/combine OUTPUT_FOLDER AUDIO_FILE OUTPUT_VIDEO

This extracts the video at 25 fps so conversion can take some time. A two
minute video is 3,000 frames.
