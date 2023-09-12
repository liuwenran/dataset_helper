
import cv2
import numpy as np
import os

# frame_file_dir = '/nvme/liuwenran/datasets/zhou_zenmela_fps10_frames_resized/frames.txt'
frame_file_dir = '/nvme/liuwenran/datasets/playground/huangbo_fps10/frames.txt'
# output_img_dir = '/nvme/liuwenran/branches/liuwenran/dev-sdi/mmediting/resources/demo_results/controlnet_hed/zhou_zenmela_fps10_frames_resized/'
# output_img_dir = '/nvme/liuwenran/datasets/results/run_forrest_any3/'
output_img_dir = '/nvme/liuwenran/branches/liuwenran/dev-sdi/mmediting/resources/demo_results/controlnet_hed/huangbo_fps10'
output_img_dir_third = '/nvme/liuwenran/branches/liuwenran/dev-sdi/mmediting/resources/demo_results/controlnet_hed/huangbo_fps10_playground_party_fixloc'

cat_result_dir = '/nvme/liuwenran/branches/liuwenran/dev-sdi/mmediting/resources/demo_results/controlnet_hed/huangbo_fps10_playground_party_fixloc_cat/'

if not os.path.exists(cat_result_dir):
   os.makedirs(cat_result_dir)

img_files = open(frame_file_dir, 'r').readlines()

for ind, line in enumerate(img_files):
    # if ind > 19:
    #     break
    line_strip = line.strip()
    file_name = line_strip.split('/')[-1]

    src = cv2.imread(line_strip)

    output_name = os.path.join(output_img_dir, file_name)
    print(output_name)

    output = cv2.imread(output_name)

    src = cv2.resize(src, (output.shape[1], output.shape[0]))

    res = np.hstack([src, output])

    output_third_name = os.path.join(output_img_dir_third, file_name)
    output_third = cv2.imread(output_third_name)
    output_third = cv2.resize(output_third, (output.shape[1], output.shape[0]))
    res = np.hstack([res, output_third])

    res_name = os.path.join(cat_result_dir, file_name)

    cv2.imwrite(res_name, res)


cmd = 'ffmpeg -r 10 -i ' + cat_result_dir + '%04d.jpg -b:v 30M -vf fps=10 ' + cat_result_dir[:-1] + '.mp4'
os.system(cmd)
