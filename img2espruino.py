#!/usr/bin/env python3
import argparse
import numpy as np
from PIL import Image, ImageOps
from bitarray import bitarray
from base64 import b64encode

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert 1-bit image to base64 string for espruino"
    )
    parser.add_argument("--key", help="use object key syntax: '<key>': {...},")
    parser.add_argument("--invert", action="store_true", help="invert image colors")
    parser.add_argument("infile")

    args = parser.parse_args()

    with Image.open(args.infile) as im:
        im = im.convert("1")
        arr = np.asarray(im).flatten().astype(int)
        if args.invert:
            arr = 1 - arr
        ba = bitarray("".join(arr.astype(str)))
        buffer = b64encode(ba.tobytes()).decode()
        if args.key:
            print(f'"{args.key}": ', end="")
        print(
            f'{{width : {im.size[0]}, height : {im.size[1]}, bpp: 1, buffer : E.toArrayBuffer(atob("{buffer}"))}}',
            end="",
        )
        if args.key:
            print(",")
        else:
            print(";")
