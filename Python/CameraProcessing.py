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

    def process_video_detect_mp(self, child_conn: Pipe):
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
            child_conn.send([0.0])
            # if the `q` key was pressed, break from the loop
            if key == ord("q"):
                child_conn.close()
                break

    def process_video_detect_mp_handler(self, parent_conn: Pipe):
        while True:
            if not parent_conn.empty():
                print(parent_conn.recv())

    def process_video_detect(self, frame):
        key = None
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
    # camera = CameraProcessing(show=False)
    # try:
    #     for frame in camera.stream:
    #         key, detect_result = camera.process_video_detect(frame)
    #         print(detect_result)
    #         if key == ord("q"):
    #             break
    # except KeyboardInterrupt:
    #     print("bye bye")

    # With multiprocessing
    camera = CameraProcessing(show=True)
    parent_conn, child_conn = Pipe()
    process1 = Process(target=camera.process_video_detect_mp, args=(child_conn,))
    process2 = Process(target=camera.process_video_detect_mp_handler, args=(parent_conn,))
    try:
        process1.start()
        process2.start()
        process1.join()
        process2.join()
    except KeyboardInterrupt:
        print("bye bye")


if __name__ == "__main__":
    main()
