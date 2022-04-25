# coding: utf-8

from main import detect_image
from detectors import QRCodeDetector, ArUcoDetector

if __name__ == "__main__":
    print("Detect `qrcode-1.jpg`...")
    text, points, time_used = detect_image("./images/qrcode-1.jpg", QRCodeDetector())
    print(f"Results: {text=}, {points=}")
    print(f"Time used: {time_used}")

    print("Detect `ArUco_6x6_1000-711.jpg`...")
    text, points, time_used = detect_image("./images/ArUco_6x6_1000-711.jpg", ArUcoDetector("DICT_6X6_1000"))
    print(f"Results: {text=}, {points=}")
    print(f"Time used: {time_used}")
