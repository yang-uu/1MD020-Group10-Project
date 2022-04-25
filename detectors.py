# coding: utf-8

import cv2

class QRCodeDetector:

    def __init__(self):
        self.detector = cv2.QRCodeDetector()

    def detect(self, img_array):
        detectedText, points, _ = self.detector.detectAndDecode(img_array)
        return detectedText, points


class ArUcoDetector:

    def __init__(self, type_):
        self.dict = cv2.aruco.Dictionary_get(getattr(cv2.aruco, type_))

    def detect(self, img_array):
        points, detectedText, _ = cv2.aruco.detectMarkers(img_array, self.dict)
        return detectedText, points
