# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 14:35:18 2018

@author: Sriram
"""

import urllib.request
import cv2
import numpy as np
import os
neg_image_urls = open("urls.txt").read().strip().split("\n")
pic_num = 1
    
if not os.path.exists('VadaPav'):
    os.makedirs('VadaPav')
        
for i in neg_image_urls:
    try:
        print(i)
        urllib.request.urlretrieve(i, "VadaPav/"+str(pic_num)+".jpg")
        img = cv2.imread("VadaPav/"+str(pic_num)+".jpg")
        # should be larger than samples / pos pic (so we can place our image on it)
        resized_image = cv2.resize(img, (500, 500))
        cv2.imwrite("VadaPav/"+str(pic_num)+".jpg",resized_image)
        pic_num += 1
            
    except Exception as e:
        print(str(e)) 