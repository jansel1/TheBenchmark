import time

class FPSCounter:
    def __init__(self):
        self.frame_count = 0
        self.start_time = time.time()
        self.fps = 0

    def update(self):
        self.frame_count += 1
        current_time = time.time()
        if current_time - self.start_time >= 1:
            self.fps = self.frame_count
            self.frame_count = 0
            self.start_time = current_time