
import cv2
import os

frame_file_dir = '/nvme/liuwenran/datasets/caixukun_videos/cxk_xunfa_sort/frames.txt'

cat_result_dir = '/nvme/liuwenran/datasets/caixukun_videos/cxk_xunfa_sort_rename/'

if not os.path.exists(cat_result_dir):
   os.makedirs(cat_result_dir)

img_files = open(frame_file_dir, 'r').readlines()

# resize_height = 512

for ind, line in enumerate(img_files):
    line_strip = line.strip()
    file_name = line_strip.split('/')[-1]

    src = cv2.imread(line_strip)
   #  height, width, c = src.shape
   #  src = cv2.resize(src, (int(resize_height / height * width), resize_height))
   #  src = src[:, 120:120+512, :]

    res_name = os.path.join(cat_result_dir, '{:0>4d}.jpg'.format(ind+1))
    cv2.imwrite(res_name, src)
