import cv2
import os

cur_dir = os.path.dirname(os.path.realpath(__file__))
#/home/hanqing/walabot_Research/walabotResearch/python/cutAvi.py

root_path = os.path.dirname(os.path.dirname(cur_dir))
#/home/hanqing/walabot_Research/walabotResearch


dataset_name = "test_dataset"
dataset = os.path.join(root_path, dataset_name)

out_dataset_name = "cut_dataset"
out_dataset = os.path.join(root_path, out_dataset_name)




def cutAvi(activity, video_name, cut_from, cut_length):


    video_dataset = os.path.join(dataset, activity)
    video_path = os.path.join(video_dataset, video_name)
    out_name = video_name[:-4]+"_cut.avi"
    out_video_dataset = os.path.join(out_dataset, activity)
    out_path = os.path.join(out_video_dataset, out_name)

    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter(out_path, fourcc, 1.0, (703, 576))

    cap = cv2.VideoCapture(video_path)
    n = 0
    while cap.isOpened() and n<cut_from+cut_length+1:
        if(n>cut_from and n<cut_from+cut_length):
            _, frame = cap.read()
            out.write(frame)
        n = n + 1

activity = 'walk'
video_name = "1.avi"
cut_