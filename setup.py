#!/usr/bin/env python

from distutils.core import setup

setup(
    name="img2espruino",
    version="0.1",
    description="Convert 1 bit images to espruino strings",
    author="Iakov Davydov",
    author_email="gward@python.net",
    url="https://github.com/idavydov/img2espruino",
    install_requieres=["numpy>=1.17.0", "Pillow>=8.0.0", "bitarray>=2.0.0"],
    scripts=["img2espruino.py"],
)
