import sys
import io
import pandas as pd
import glob
import os
from shutil import move
from os.path import join
from os import listdir, rmdir
import cv2
import numpy as np

mean = [0.0, 0.0, 0.0]
std = [0.0, 0.0, 0.0]
img_h, img_w = 64, 64

# obtain all images in this dataset
target_folder = join(os.path.dirname(__file__), 'train')
paths = glob.glob(target_folder + "/*")
print (paths)
num_images = 0

for class_name in paths:
    images_path = glob.glob(class_name + "/*")
    for img_path in images_path:
        print (img_path)
        if 'jpeg' in img_path.lower():
            print (img_path)
            img = cv2.imread(img_path)
            img = np.asarray(img)
            if num_images <=10:
                print (img)
            img = img.astype(np.float32) / 255.0
            for i in range(3):
                mean[i] += img[:, :, i].mean()
                std[i] += img[:, :, i].std()
            num_images += 1


# BGR --> RGB 
mean.reverse()
std.reverse()

mean = np.asarray(mean) / num_images
std = np.asarray(std) / num_images

print ("mean {}".format(mean))
print ("std {}".format(std))
