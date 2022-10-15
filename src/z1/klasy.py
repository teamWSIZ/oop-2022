from random import randint
from time import sleep


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
        #todo: co jeśli w "buffer" już jest linii tyle ile on może pomieścić, czyli self.buffer_size?
        # wtedy trzeba automatycznie wykonać self.flush()
        # a potem wyczyścić buffer

    def flush(self):
        for l in self.buffer:
            print(l)


if __name__ == '__main__':
    ll = BufferedLogger(log_id=17, buffer_size=100)
    ll.log('Komunikat')
    l7 = Logger(7)
    l7.log('Komunikat')
    l7.log('Zaczynam dlugie obliczenia')
    sleep(1)
    l7.log('Koniec obliczen')
