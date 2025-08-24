# main.py
from ultralytics import YOLO

model = YOLO("yolov8l.pt")
   
results = model.predict("data/raw_videos/video_1.mp4", save=True)
print(results)
print("====")
for box in results[0].boxes:
    print(box)
