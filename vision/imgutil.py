from PIL import Image

def to_grayscale(filepath):
    return Image.open(filepath).convert('L')
