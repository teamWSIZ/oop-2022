class Logger:
    log_id: int # pole / field

    def __init__(self, log_id: int):
        print('konstruktor działa')
        self.log_id = log_id

    def log_it(self, msg: str):
        # to jest "metoda (method)"
        print(f'Logger[{self.log_id}]: {msg}')


if __name__ == '__main__':
    ll = Logger(log_id=17)
    ll.log_it('Komunikat')
    l7 = Logger(7)
    l7.log_it('Komunikat')

