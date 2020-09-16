"""
Adding white border, from "service menu" on apple or as a "other app" in capture one
On automator,
shell: bin/bass         pass input: as argument
/usr/local/bin/python3 <python script path> "$1"
"""

import os
import argparse
from sys import argv
from PIL import Image, ImageOps
from random import choice


def check_size(image_path):
    img = Image.open(image_path)
    img_size = img.size
    if img_size[0] > img_size[1]:
        border_select = choice(border_hor).split("x")
        add_border(
            image_path,
            image_path,
            border=(int(border_select[0]), int(border_select[1])),
        )
    else:
        border_select = choice(border_ver).split("x")
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


parser = argparse.ArgumentParser()
parser.add_argument("path", type=str)
args = parser.parse_args()
img_file = args.path

# En border_x cambias los valores para los marcos y puedes añadir más
# Para añadir otro marco, ponle una coma(,) al ultimo y usa el formato VALORxVALOR entre comillas("")
# e.g. ["4x4", 50x10, "50x100", "60x100"]

border_hor = ["30x70", "20x80", "40x80"]

border_ver = ["20x60", "45x60", "10x30"]


check_size(img_file)
