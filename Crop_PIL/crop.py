#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 16:57:04 2022

@author: lukas
"""
#Python Imaging Library
from PIL import Image
import os

for i in range(51):
    if i > 0:
        i = str(i)
        path = os.path.join("/xxxx/"+i+".jpg")
        im = Image.open(path)
        
        width, height = im.size
        # Setting the points for cropped image
        left = 1
        top = height / 5.4
        right = width
        bottom = 3 * height / 3.4
        
        # print(path)
        im1 = im.crop((left, top, right, bottom))
        im1.show()
        # im1.save(i+".jpg")


