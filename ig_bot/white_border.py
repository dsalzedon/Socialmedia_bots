"""
Adding white border to a batch of files in a specific folder

requirements:
pip install Pillow
 
"""
import os
from PIL import Image, ImageOps



def add_border(input_image, output_image, border):
    img = Image.open(input_image)

    if isinstance(border, int) or isinstance(border, tuple):
        bimg = ImageOps.expand(img, border=border, fill="white")
    else:
        raise RuntimeError("Border is not an integer or tuple!")

    bimg.save(output_image)


os.chdir("/Users/dsalzedo/Documents/Python/PyInsta/ivaninthemusic/Monday")

for f in os.listdir():
    if f == ".DS_Store":
        pass
    else:
        print(f)
        add_border(f, f, border=(100, 30))

