
import cv2
import numpy as np
import os

# frame_file_dir = '/nvme/liuwenran/datasets/zhou_zenmela_fps10_frames_resized/frames.txt'
frame_file_dir = '/nvme/liuwenran/datasets/caixukun_videos/cxk_xunfa_sort_rename/frames.txt'
# output_img_dir = '/nvme/liuwenran/branches/liuwenran/dev-sdi/mmediting/resources/demo_results/controlnet_hed/zhou_zenmela_fps10_frames_resized/'
output_img_dir = '/nvme/liuwenran/branches/liuwenran/dev-sdi/mmediting/resources/demo_results/controlnet_hed/cxk_xunfa_sort_rename/'

cat_result_dir = '/nvme/liuwenran/branches/liuwenran/dev-sdi/mmediting/resources/demo_results/controlnet_hed/cxk_xunfa_sort_rename_cat/'

if not os.path.exists(cat_result_dir):
   os.makedirs(cat_result_dir)

img_files = open(frame_file_dir, 'r').readlines()

for ind, line in enumerate(img_files):
    # if ind > 19:
    #     break
    line_strip = line.strip()
    file_name = line_strip.split('/')[-1]

    src = cv2.imread(line_strip)

    # file_ind = int(file_name.split('.')[0])
    # output_name = output_img_dir + '{:0>4d}.jpg'.format(file_ind)
    # print(output_name)

    output_name = os.path.join(output_img_dir, file_name)

    output = cv2.imread(output_name)

    src = cv2.resize(src, (output.shape[1], output.shape[0]))

    res = np.hstack([src, output])

    res_name = cat_result_dir + file_name

    cv2.imwrite(res_name, res)


cmd = 'ffmpeg -r 10 -i ' + cat_result_dir + '%04d.jpg -b:v 30M -vf fps=10 ' + cat_result_dir[:-1] + '.mp4'
os.system(cmd)
