# main.py
from ultralytics import YOLO

if __name__ == "__main__":
    # just load & verify the model, no prediction call yet
    model = YOLO("yolov8n.pt")
    print("Model loaded successfully")
