# python modules
import time
import threading

class Interval:
    def __init__(self, action, interval):
        self.action = action
        self.interval = interval
        self.stop_event = threading.Event()

    def __setInterval(self):
        nextTime = time.time() + self.interval
        while not self.stop_event.wait(nextTime - time.time()):
            nextTime += self.interval
            self.action()
    
    def start(self):
        thread = threading.Thread(target=self.__setInterval)
        thread.start()

    def end(self):
        self.stop_event.set()