
# reorganize the training folder into a pytorch style.
import io
import pandas as pd
import glob
import os
from shutil import move
from os.path import join
from os import listdir, rmdir

target_folder = './train/'
train_dict = {}

classes = glob.glob(target_folder + '/*')
print (classes)

for class_path in classes:
	paths = glob.glob(class_path + '/*')
	for path in paths:
		print (path)
		if 'txt'in path:
			os.remove(path)
		elif 'images' in path:
			for f in os.listdir(path):
				move(os.path.join(path, f), class_path)
			os.rmdir(path)


