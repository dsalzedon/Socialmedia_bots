"""
Adding white border, from "service menu" on apple or as a "other app" in capture one
"""

import os
import argparse
from sys import argv
from PIL import Image, ImageOps


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
add_border(f, f, border=(100, 30))
