import sys
from datetime import datetime
from random import randint
from time import sleep

def ts():
    return datetime.now().timestamp()


class Logger:
    log_id: int  # pole / field

    def __init__(self, log_id: int):
        self.log_id = log_id

    def log(self, msg: str):
        # to jest "metoda (method)"
        print(f'Logger[{self.log_id}]: {msg}')


class BufferedLogger(Logger):

    def __init__(self, buffer_size: int):
        super().__init__(randint(0, 10 ** 9))   # jakiś losowy ID
        self.buffer_size = buffer_size
        self.buffer = []

    def log(self, msg: str):
        self.buffer.append(msg)
        if len(self.buffer) >= self.buffer_size:
            self.flush()

    def flush(self):
        """
        Drukuje zawartość bufora na konsolę, po czym czyści bufor
        :return:
        """
        for l in self.buffer:
            print(l)
        self.buffer.clear()


class FileBasedBufferedLogger(BufferedLogger):

    def __init__(self, log_file_name: str, buffer_size):
        super().__init__(buffer_size)
        self.log_file_name = log_file_name

    def flush(self):
        with open(self.log_file_name, 'w') as f:
            for line in self.buffer:
                f.write(line + '\n')


if __name__ == '__main__':
    st = ts()
    # ll = Logger(log_id=1)
    # ll = BufferedLogger(buffer_size=10)
    ll = FileBasedBufferedLogger(log_file_name='app.log', buffer_size=1000)
    for i in range(1000):
        ll.log(f'Komunitat {i}')
    en = ts()
    print(f'czas trwania: {en-st:.3f}')
