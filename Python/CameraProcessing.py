from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2


class CameraProcessing:
    def __init__(self, height: int = 96, width: int = 128, framerate: int = 90, video_format: str = "bgr") -> None:
        # initialize the camera and grab a reference to the raw camera capture
        camera = PiCamera()
        camera.resolution = (width, height)
        camera.framerate = framerate
        self.raw_capture = PiRGBArray(camera, size=(width, height))
        self.stream = camera.capture_continuous(self.raw_capture, format=video_format, use_video_port=True)
        # allow the camera to warmup
        time.sleep(0.1)

    def process_video(self):
        # capture frames from the camera
        for frame in self.stream:
            # grab the raw NumPy array representing the image, then initialize the timestamp
            # and occupied/unoccupied text
            image = frame.array
            # show the frame
            cv2.imshow("Frame", image)
            key = cv2.waitKey(1) & 0xFF
            # clear the stream in preparation for the next frame
            self.raw_capture.truncate(0)
            # if the `q` key was pressed, break from the loop
            if key == ord("q"):
                break


def main() -> None:
    camera = CameraProcessing()
    camera.process_video()


if __name__ == "__main__":
    main()
