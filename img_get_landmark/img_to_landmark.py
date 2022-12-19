# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 21:47:20 2021

@author: User
"""

import face_alignment
from skimage import io
import matplotlib.pyplot as plt
import cv2
import csv


csv_save_file = 'E:/RAF-DB_landmark/RAF-DB_landmark_val.csv'          #Your save RAF-DB_landmark_val.csv location
csv_file = 'E:/RAF-DB/basic/Emolabel/list_patition_label_val.csv'    #Your list_patition_label_val.csv location
img = 'E:/RAF-DB/basic/Image/aligned/'    #Your image file 

with open (csv_file) as csvfile:
    with open (csv_save_file, 'w', newline='') as write_file:
        csvwrite = csv.writer(write_file)
        csvRead = csv.DictReader(csvfile)
        for data in csvRead:
            filePath = data['subDirectory_filePath']       # image name
            fil = data['file']                             # image file extension
            expression = data['expression']                # image class
            img_path = img + filePath + '_aligned' + '.' + fil    
            img_name = filePath + '_aligned' + '.' + fil
            input = io.imread(img_path)
            try:
                fa = face_alignment.FaceAlignment(face_alignment.LandmarksType._2D, flip_input=False)
                preds = fa.get_landmarks(input)
                make_str_list = " ".join(str(x) for x in preds)
                img_data = img_name + ';' + make_str_list + ';' + expression + ';' + 'train'
                imgdatatolist = img_data.split(';')
                csvwrite.writerow(imgdatatolist)
            except Exception as e:
                pass
            continue