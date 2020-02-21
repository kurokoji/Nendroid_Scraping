import os, glob
import numpy as np
import argparse
from tqdm import tqdm
import cv2

parser = argparse.ArgumentParser(description='face')
parser.add_argument('--dir', help='dir')

args = parser.parse_args()


def to_gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def main():

    cascade = cv2.CascadeClassifier('./lbpcascade_animeface/lbpcascade_animeface.xml')

    files = glob.glob(os.path.join(args.dir, "*.jpg"))
    for i, f in enumerate(tqdm(files)):
        im = cv2.imread(f)
        gray = to_gray(im)
        face_rect = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1, minSize=(64, 64))

        rect_images = []

        for j, rect in enumerate(face_rect):
            x = rect[0]
            y = rect[1]
            x_len = rect[2]
            y_len = rect[3]
            img = im[y : y + y_len, x : x + x_len]

            n, e = os.path.splitext(os.path.basename(f))
            name = os.path.join(args.dir, 'face', '{}_{:02}.jpg'.format(n, j))
            cv2.imwrite(name, img)

if __name__ == '__main__':
    main()
