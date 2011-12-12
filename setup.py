#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Public Domain

"""
CairoSVG - A Simple SVG Converter for Cairo
===========================================

CairoSVG is a SVG converter based on Cairo. It can export SVG files to PDF,
PostScript and PNG files.

For further information, please visit the `CairoSVG Website
<http://www.cairosvg.org/>`_.

"""

from distutils.core import setup

import cairosvg


# When the version is updated, ``cairosvg.VERSION`` must be modified.
# A new section in the ``NEWS`` file must be added too.
setup(
    name="CairoSVG",
    version=cairosvg.VERSION,
    description="A Simple SVG Converter for Cairo",
    long_description=__doc__,
    author="Kozea",
    author_email="guillaume.ayoub@kozea.fr",
    url="http://www.cairosvg.org/",
    download_url="http://www.cairosvg.org/src/cairosvg/CairoSVG-%s.tar.gz" % \
        cairosvg.VERSION,
    license="GNU GPL v3",
    platforms="Any",
    packages=["cairosvg"],
    provides=["cairosvg"],
    scripts=["bin/cairosvg"],
    requires={"pycairo": ["pycairo>=1.8"]},
    keywords=["svg", "cairo", "pdf", "png", "postscript"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion"])