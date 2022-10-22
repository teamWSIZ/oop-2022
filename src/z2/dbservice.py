class DbService:

    def __init__(self, host, port):
        self.port = port
        self.host = host  # field / pole --> związane z instancją
        self.connected = False
        print(f'tworzę instancję DbService, do hosta {self.host}')

    def check_connectivity(self) -> bool:  # metoda, która ma _dostęp_ do instancji
        # sprawdź połączenie z bazą
        return True

    def reconnect(self):
        print(f'reconnecting to {self.host}:{self.port}')
        self.connected = True
        print(f'connected to {self.host}:{self.port}')


if __name__ == '__main__':
    # tworzenie instancji
    db1 = DbService('localhost', 5432)
    db2 = DbService('quicksight.us-east-2.amazonaws.com', 5432)
    print(db1.connected)
    db1.reconnect()
    print(db1.connected)
    print(db2.connected)
