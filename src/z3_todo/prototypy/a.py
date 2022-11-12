from uuid import uuid4


class Server:

    def __init__(self):
        self.sid = uuid4()

    def __repr__(self):
        return f'[Server: {self.sid}]'


if __name__ == '__main__':
    s1 = Server()
    s2 = Server()
    print(s1)

    servers = [s1,s2]
    print(servers)

    gg = set()
    gg.add(s2)
    gg.add(s1)
    gg.add(s1)
    gg.add(s1)
    gg.add(s1)
    gg.remove(s1)
    print(gg)
