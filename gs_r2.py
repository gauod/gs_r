import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
import glob

def save_all_frames(video_path, dir_path, basename, ext='jpg'):
    

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    n = 0

    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext), frame)
            n += 1

        else:
            return



save_all_frames('gs.mp4', 'report1', 're_video_img')

b=np.zeros(166)
a=glob.glob("report1/re_video_img_*.jpg")


for x in range(166):
    im=cv2.imread(a[x])
    b[x]=im.mean()


y=np.arange(166)

plt.plot(y,b)
plt.savefig('video_g.pdf')
plt.show()
