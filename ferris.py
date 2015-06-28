import cv2
import sys
import PIL.Image

def detect_faces(image_file):
    image = cv2.imread(image_file)
    classifier = cv2.CascadeClassifier("resources/haarcascade_frontalface_alt.xml")
    faces = classifier.detectMultiScale(image)

    if len(faces) == 0:
        return [], image

    faces[:, 2:] += faces[:, :2]
    return faces, image

def box_faces(image, faces):
    for x1, y1, x2, y2 in faces:
        cv2.rectangle(image, (x1, y1), (x2, y2), (127, 255, 0), 2)
    return image

def overlay_faces(image_path, faces, replacement_path):
    image = PIL.Image.open(image_path)
    replacement_image = crop_face(replacement_path)

    for x1, y1, x2, y2 in faces:
        resized = replacement_image.resize((x2 - x1, y2 - y1))
        image.paste(resized, (x1, y1, x2, y2))

    return image

def crop_face(image_path):
    faces, _ = detect_faces(image_path)
    image = PIL.Image.open(image_path)
    return image.crop(faces[0])

def write_image_cv2(image, path):
    cv2.imwrite(path, image)

def write_image_pil(image, path):
    image.save(path)

def boxed_image_name(path):
    last_dot = path.rfind('.')
    output_path = image_path[:last_dot] + "_boxed" + image_path[last_dot:]
    return output_path

def replaced_image_name(path):
    last_slash = path.rfind('/') or 0
    output_path = "output/" + image_path[last_slash:]
    return output_path

def box_all_faces(image_path):
    faces, image = detect_faces(image_path)
    if len(faces):
        boxed_image = box_faces(image, faces)
        write_image(boxed_image, boxed_image_name(image_path))
    else:
        print "No faces found for {0}".format(image_path)

if __name__ == "__main__":
    for image_path in sys.argv[1:]:
        faces, cv_image = detect_faces(image_path)
        image = overlay_faces(image_path, faces, "glenn.jpg")
        write_image_pil(image, replaced_image_name(image_path))

