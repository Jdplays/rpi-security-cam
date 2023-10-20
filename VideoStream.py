import cv2

class VideoStream:
    def __init__(self, source=0):
        self.cap = cv2.VideoCapture(source)
        if not self.cap.isOpened():
            raise Exception("Error: Could not open the camera.")

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

if __name__ == "__main__":
    with VideoStream() as vs:
        while True:
            frame = vs.read()
            cv2.imshow("USB Camera Stream", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
