from PIL import Image
from pylab import array, uint8
import os

def to_grayscale(filepath):
    return Image.open(filepath).convert('L')


def get_img_list(dirpath, extension):
    img_list = []
    for f in os.listdir(dirpath):
        if f.endswith(extension):
            img_list.append(os.path.join(dirpath, f))
    return img_list


def resize(img_array, width, height):
    img = Image.fromarray(uint8(img_array))
    return array(img.resize((width, height)))
