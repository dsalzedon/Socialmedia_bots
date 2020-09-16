"""
Adding white border to a batch of files in a specific folder
requirements:
pip install Pillow
 
"""
import os
from PIL import Image, ImageOps
from random import choice


def add_border(input_image, output_image, border):
    img = Image.open(input_image)

    if isinstance(border, int) or isinstance(border, tuple):
        bimg = ImageOps.expand(img, border=border, fill="white")
    else:
        raise RuntimeError("Border is not an integer or tuple!")

    bimg.save(output_image)


os.chdir("/Users/dsalzedo/Documents/Python/scripts/Random_Code/pic")

border_lst = ["20x60", "45x60", "40x80"]

for f in os.listdir():
    if f == ".DS_Store":
        pass
    else:
        border_select = choice(border_lst).split("x")
        print(border_select)
        # print(str(border_select[0]), str(border_select[1]))
        # print(f)
        add_border(f, f, border=(int(border_select[0]), int(border_select[1])))
