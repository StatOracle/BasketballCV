# main.py
# from ultralytics import YOLO

from utils.video_utils import read_video, save_video
""" model = YOLO("models/BallDetection.pt")
results = model.track("data/raw_videos/video_1.mp4", save=True)
print(results)
print("====")
for box in results[0].boxes:
    print(box)
"""
def main():
     
    #Read video
     video_frames = read_video("data/raw_videos/video_1.mp4")

     #Save video
     save_video(video_frames, "output_videos/output_video.avi")


if __name__ == '__main__':
    main()