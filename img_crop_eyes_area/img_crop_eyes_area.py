# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 20:14:02 2021

@author: User
"""

import csv
import os
from PIL import Image
import numpy as np
import shutil
import cv2

csv_file = 'E:/RAF-DB_landmark/RAF-DB_landmark_val.csv'      #Your landmark.csv file
img_file = 'E:/RAF-DB/basic_val_image/'                      #Your image file
img_save_file = 'E:/RAF-DB_eyes/test/'                       #Your eyes_image save file

with open(csv_file) as csv_raed:
    csvRead = csv.DictReader(csv_raed)
    for data in csvRead:
        file_name = data['subDirectory_filePath']
        landmark = data['landmark']
        landmark = landmark.replace(" ",'')
        landmark = landmark.replace("\n", "")
        landmark = landmark.replace(".", ";")
        landmarkstolist = landmark.split(';')
        #print(landmarkstolist)
        onone_x = landmarkstolist[0]
        onone_x = int(onone_x)
        nosey = landmarkstolist[59]
        nosey = int(nosey)
        seventeen_x =landmarkstolist[32]
        seventeen_x = int(seventeen_x)
        reyebrowy = landmarkstolist[53]
        reyebrowy = int(reyebrowy)
        h = abs(nosey) 
        w = abs(seventeen_x)
        x = abs(onone_x)
        y = abs(reyebrowy)
        expression = data['expression']
        img = img_file + expression + '/' + file_name
        image = cv2.imread(img)
        image_eye = image[y:h,x:w]
        image_eye_save_file = img_save_file + expression + '/' + file_name
        try:
            cv2.imwrite(image_eye_save_file , image_eye)
            print(file_name)
        except Exception as e:
            pass
        continue