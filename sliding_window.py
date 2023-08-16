import numpy as np

class SlidingWindow:
    win_len: int
    acc_static: float
    buffer: list[float]
    i: int = 0
    def __init__(self, win_len: int, acc_static: float = 0):
        self.win_len = win_len
        self.acc_static = acc_static
        self.buffer = [0] * win_len
    def __call__(self, data: float) -> float:    
        if self.i+1 < self.win_len:
            j = data - self.acc_static
            self.buffer[self.i] = j
            self.i += 1
            return j
        self.__push_back(data)
        return np.mean(self.buffer) - self.acc_static
    def __push_back(self, data: float):
        for i in range(1, len(self.buffer)):
            self.buffer[i-1] = self.buffer[i]
        self.buffer[-1] = data