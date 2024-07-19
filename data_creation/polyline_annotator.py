import cv2
import numpy as np
import os
import shutil
import pandas as pd
import json

color1 = (100, 100, 100)
color2 = (150, 150, 150)
color3 = (200, 200, 200)
color4 = (220, 220, 220)
color5 = color3  # special case for one image

colors=[color1,color2,color3,color4,color5]

thickness = 3

read_path = 'C:/LaneNet-Train/data/Additional_images/Right_resized'
write_path = 'C:/LaneNet-Train/data/Additional_images/Right_instance'

if os.path.exists(write_path):
	shutil.rmtree(write_path)
os.mkdir(write_path)

orig_size = np.array((512, 256))
new_size = np.array((512, 256))
scale_ratio = new_size / orig_size

data = pd.read_csv('C:/LaneNet-Train/data/Additional_images/Right.csv.csv')

print("Processing images...")
for file in os.listdir(read_path):
	if file == '.DS_Store':
		continue

	instance_image = np.zeros((256, 512, 3), dtype = "uint8")
	
	color_count = 0
	write_img = True

	for index, row in data[data['filename'] == file].iterrows():
		if row['region_count'] == 0:
			write_img = False
			break
		lanes = json.loads((row['region_shape_attributes']))
		x = lanes['all_points_x']
		y = lanes['all_points_y']
		pts = np.array((x, y)).T
		pts = np.int32(np.round(pts * scale_ratio))
		pts = pts.reshape((-1, 1, 2))
		instance_image = cv2.polylines(instance_image, [pts], False, colors[color_count], thickness)
		color_count += 1

		# ensuring the dc264 bug works
		if color_count == 5:
			print(file)
	
	if write_img:
		cv2.imwrite(os.path.join(write_path, file), instance_image)

print("Done!")