# coding: utf-8

from main import detect_image
from detectors import QRCodeDetector, DumbArUcoDetector, DataMatrixDetector

if __name__ == "__main__":
    print("Detect `qrcode-1.jpg`...")
    text, points, creteria = detect_image("./images/qrcode-1.jpg", QRCodeDetector())
    print(f"Results:\n  {text=},\n  {points=}")
    print(f"Time used: {creteria}")

    print("Detect `ArUco_6x6_1000-711.jpg`...")
    text, points, creteria = detect_image("./images/ArUco_6x6_1000-711.jpg", DumbArUcoDetector())
    print(f"Results:\n  {text=},\n  {points=}")
    print(f"Time used: {creteria}")

    print("Detect `DataMatrix-2.jpg`...")
    text, points, creteria = detect_image("./images/DataMatrix-2.jpg", DataMatrixDetector())
    print(f"Results:\n  {text=},\n  {points=}")
    print(f"Time used: {creteria}")
