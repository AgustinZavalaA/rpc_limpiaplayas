from typing import List, Tuple
from picamera.array import PiRGBArray
from picamera import PiCamera
from multiprocessing import Pipe, Process
import time
import cv2


class CameraProcessing:
    def __init__(
        self,
        show: bool = False,
        resolution: Tuple[int, int] = (128, 96),
        framerate: int = 90,
        video_format: str = "bgr",
    ) -> None:
        # initialize the camera and grab a reference to the raw camera capture
        camera = PiCamera()
        camera.resolution = resolution
        camera.framerate = framerate
        self.raw_capture = PiRGBArray(camera, size=resolution)
        self.stream = camera.capture_continuous(self.raw_capture, format=video_format, use_video_port=True)
        self.show_camera = show
        # allow the camera to warmup
        time.sleep(0.1)

    def process_video_detect_mp(self) -> List[float]:
        # capture frames from the camera
        for frame in self.stream:
            # grab the raw NumPy array representing the image, then initialize the timestamp
            # and occupied/unoccupied text
            image = frame.array
            # show the frame
            if self.show_camera:
                cv2.imshow("Frame", image)
                key = cv2.waitKey(1) & 0xFF
            # clear the stream in preparation for the next frame
            self.raw_capture.truncate(0)
            # if the `q` key was pressed, break from the loop
            if key == ord("q"):
                conn.close()
                break

    def process_video_detect(self, frame):
        # grab the raw NumPy array representing the image, then initialize the timestamp
        # and occupied/unoccupied text
        image = frame.array
        # show the frame
        if self.show_camera:
            cv2.imshow("Frame", image)
            key = cv2.waitKey(1) & 0xFF
        # clear the stream in preparation for the next frame
        self.raw_capture.truncate(0)
        # if the `q` key was pressed, break from the loop
        return key, [0.0]


def main() -> None:
    # Normal way
    camera = CameraProcessing(show=False)
    try:
        for frame in camera.stream:
            key, detect_result = camera.process_video_detect(frame)
            print(detect_result)
            if key == ord("q"):
                break
    except KeyboardInterrupt:
        print("bye bye")
    # camera = CameraProcessing()
    # parent_conn, child_conn = Pipe()
    # p = Process(target=camera.process_video, args=(child_conn,))
    # p.start()
    # # print(parent_conn.recv())
    # p.join()


if __name__ == "__main__":
    main()
