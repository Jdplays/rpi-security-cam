import cv2

class VideoStream:
    def __init__(self, source=0):
        self.cap = cv2.VideoCapture(source)

    def start(self):
        pass  # The video stream is already started when the object is created

    def read(self):
        ret, frame = self.cap.read()
        if not ret:
            raise Exception("Error: Could not read a frame.")
        return frame

    def stop(self):
        self.cap.release()

    def release(self):
        self.cap.release()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.release()
