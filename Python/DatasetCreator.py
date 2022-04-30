import cv2
import datetime


class DatasetCreator:
    def __init__(self, camera_id) -> None:
        self.cap = cv2.VideoCapture(camera_id)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 416)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 416)

    def release(self):
        self.cap.release()

    def update(self):
        _, self.frame = self.cap.read()

    def save_frame(self):
        cv2.imwrite(f"dataset_raspi/{datetime.datetime.now()}.jpg", self.frame)
