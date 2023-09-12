
import cv2
import numpy as np
import os

frame_file_dir = '/nvme/liuwenran/datasets/forrestgan/running_frames_rename/frames.txt'

cat_result_dir = '/nvme/liuwenran/datasets/forrestgan/running_frames_rename_resized/'

if not os.path.exists(cat_result_dir):
   os.makedirs(cat_result_dir)

img_files = open(frame_file_dir, 'r').readlines()

height = 512

for line in img_files:
    line_strip = line.strip()
    file_name = line_strip.split('/')[-1]

    src = cv2.imread(line_strip)
    new_width = int(height / src.shape[0] * src.shape[1])

    res = cv2.resize(src, (new_width, height))

    part = (new_width - height) // 2

    res = res[:, part:(part + height), :]

    res_name = cat_result_dir + file_name

    cv2.imwrite(res_name, res)
