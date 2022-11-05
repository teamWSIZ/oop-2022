from uuid import uuid4


class Candidate:

    def __init__(self):
        self.id = uuid4()
        self.others: list[Candidate] = []
        self.is_leader = None
        self.leader = None
        self.data = []


    def write(self, message: str):
        """
        Funkcja do wywołania przez klientów
        """
        self.leader.leader_write(message)

    def leader_write(self, message: str):
        """
        Funkcja do wywołania tylko przez leadera
        """
        self.data.append(message)
        for oth in self.others:
            oth.follower_write(message)

    def follower_write(self, message: str):
        """
        Funkcja do wywołania tylko przez leadera
        """
        self.data.append(message)


    def add_other(self, candidate: 'Candidate'):
        self.others.append(candidate)

    def elect_leader(self):
        print(f'electing leader on {self.id}')

        # przerobić tą funkcję tak by self.is_leader było True, jeśli nasz id jest najmniejszy z wszystkich
        min_id = self.id
        for oth in self.others:
            min_id = min(min_id, oth.id)

        if self.id == min_id:
            self.is_leader = True
            self.leader = self
        else:
            self.is_leader = False

        # czy to wystarczy ↓↓ by wybory odbyły się na wszystkich Candidate'ach?
        for oth in self.others:
            if oth.is_leader is None:
                oth.elect_leader()
            if oth.is_leader is True:
                self.leader = oth

    def __repr__(self):
        return f'Candidate(id={self.id}, is_leader={self.is_leader})'


if __name__ == '__main__':
    N = 9
    candidates = [Candidate() for _ in range(N)]
    for c in candidates:
        for ca in candidates:
            if c != ca:
                c.add_other(ca)


    candidates[0].elect_leader()
    print(candidates)
    print('-' * 10)

    # klient wykonuje zapisy
    candidates[1].write('aaa')
    candidates[0].write('bbb')
    candidates[4].write('ccc')
    candidates[2].write('ddd')

    for c in candidates[:3]:
        print(c.data)


# dla dwóch:

# cand1 = Candidate()
# cand2 = Candidate()
# print(cand1)
# print(cand2)
#
#
# cand1.other = cand2
# cand2.other = cand1
#
# cand1.elect_leader()
#
# print(cand1)
# print(cand2)


"""
1) Kandydaci powinni wiedzieć o sobie, 
2) Powinni mieć pole is_leader: bool
3) Powinni mieć metodę elect_leader(), która ustawi self.is_leader=True, jeśli aktualny Candidate ma najmniejszy .id, 
   lub self.is_leader=False w przeciwnym przypadku
4) Chcemy mieć możliwość uruchomienia tych wyborów z pojedynczego Candidate (nie tak byśmy musieli mieć referencje do wszystkich)
"""
