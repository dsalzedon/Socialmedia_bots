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
f = args.path

# en border_lst cambias los valores para los marcos y puedes añadir más
border_lst = ["20x60", "45x60", "40x80"]

# escoge un pseudo-aleatorio entre la lista de bordes
border_select = choice(border_lst).split("x")

add_border(f, f, border=(int(border_select[0]), int(border_select[1])))
