import os.path as osp
import json

llm_caption_path = '/mnt/petrelfs/liuwenran/datasets/llm-midjourney/midjourney_ksj.jsonl'

haodong_caption_path = '/mnt/petrelfs/liuwenran/datasets/aigcmm/AIGCMM_TRAIN_SAMPLE/train_anno.jsonl'

llm_file = open(llm_caption_path, 'r')
llm_anno_list = list(llm_file)

haodong_file = open(haodong_caption_path, 'r')
haodong_anno_list = list(haodong_file)

all_haodong_names = []
for haodong_anno in haodong_anno_list:
    haodong_anno = json.loads(haodong_anno)
    img_name = haodong_anno['img_path'].split('_')[-1].split('.')[0]
    all_haodong_names.append(img_name)


all_llm_names = []
for llm_anno in llm_anno_list:
    llm_anno = json.loads(llm_anno)
    img_name = llm_anno['img_list'][0].split('_')[-1].split('.')[0]
    all_llm_names.append(img_name)

print('haodong length ' + str(len(all_haodong_names)))
print('llm length ' + str(len(all_llm_names)))

count = 0
overlap_names = []
for name in all_haodong_names:
    if name in all_llm_names:
        overlap_names.append(name)
        print(name)
        count += 1

print('overlap count ' + str(count))
