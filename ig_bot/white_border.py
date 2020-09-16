"""
Adding white border to a batch of files in a specific folder
requirements:
pip install Pillow
 
"""
import os
from PIL import Image, ImageOps
from random import choice


def check_size(image_path):
    img = Image.open(image_path)
    img_size = img.size
    if img_size[0] > img_size[1]:
        border_select = choice(border_lst_hor).split("x")
        add_border(
            image_path,
            image_path,
            border=(int(border_select[0]), int(border_select[1])),
        )
    else:
        border_select = choice(border_lst_ver).split("x")
        add_border(
            image_path,
            image_path,
            border=(int(border_select[0]), int(border_select[1])),
        )


def add_border(input_image, output_image, border):
    img = Image.open(input_image)

    if isinstance(border, int) or isinstance(border, tuple):
        bimg = ImageOps.expand(img, border=border, fill="white")
    else:
        raise RuntimeError("Border is not an integer or tuple!")

    bimg.save(output_image)


os.chdir("/Users/dsalzedo/Documents/Python/scripts/Random_Code/pic")

border_lst_hor = ["30x70", "20x80", "40x80"]
border_lst_ver = ["20x60", "45x60", "10x30"]

for f in os.listdir():
    if f == ".DS_Store":
        pass
    else:
        check_size(f)
