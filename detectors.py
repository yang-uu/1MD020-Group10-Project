# coding: utf-8

import cv2
from loguru import logger

class QRCodeDetector:

    def __init__(self):
        self.detector = cv2.QRCodeDetector()

    def detect(self, img_array):
        detectedText, points, _ = self.detector.detectAndDecode(img_array)
        return detectedText, points


class DumbArUcoDetector:

    PREDIFINED_DICT_NAME = {
        cv2.aruco.DICT_4X4_50: "DICT_4X4_50",
        cv2.aruco.DICT_4X4_100: "DICT_4X4_100",
        cv2.aruco.DICT_4X4_250: "DICT_4X4_250",
        cv2.aruco.DICT_4X4_1000: "DICT_4X4_1000",
        cv2.aruco.DICT_5X5_50: "DICT_5X5_50",
        cv2.aruco.DICT_5X5_100: "DICT_5X5_100",
        cv2.aruco.DICT_5X5_250: "DICT_5X5_250",
        cv2.aruco.DICT_5X5_1000: "DICT_5X5_1000",
        cv2.aruco.DICT_6X6_50: "DICT_6X6_50",
        cv2.aruco.DICT_6X6_100: "DICT_6X6_100",
        cv2.aruco.DICT_6X6_250: "DICT_6X6_250",
        cv2.aruco.DICT_6X6_1000: "DICT_6X6_1000",
        cv2.aruco.DICT_7X7_50: "DICT_7X7_50",
        cv2.aruco.DICT_7X7_100: "DICT_7X7_100",
        cv2.aruco.DICT_7X7_250: "DICT_7X7_250",
        cv2.aruco.DICT_7X7_1000: "DICT_7X7_1000",
        cv2.aruco.DICT_ARUCO_ORIGINAL: "DICT_ARUCO_ORIGINAL",
        cv2.aruco.DICT_APRILTAG_16h5: "DICT_APRILTAG_16h5",
        cv2.aruco.DICT_APRILTAG_25h9: "DICT_APRILTAG_25h9",
        cv2.aruco.DICT_APRILTAG_36h10: "DICT_APRILTAG_36h10",
        cv2.aruco.DICT_APRILTAG_36h11: "DICT_APRILTAG_36h11",
    }

    def detect(self, img_array):
        detectedText, points = None, ()
        for id_, name in self.PREDIFINED_DICT_NAME.items():
            results = cv2.aruco.detectMarkers(img_array, cv2.aruco.Dictionary_get(id_))
            if len(results[0]) > 0:
                points, detectedText, _ = results
                logger.debug(f"Found with dict `{name}`.")
        return detectedText, points
