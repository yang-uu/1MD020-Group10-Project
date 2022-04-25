# coding: utf-8

import cv2
import datetime


def detect_image(filename, detector):
    img = cv2.imread(filename)

    start_time = datetime.datetime.now()
    detectedText, points = detector.detect(img)
    time_used = datetime.datetime.now() - start_time

    return detectedText, points, time_used
