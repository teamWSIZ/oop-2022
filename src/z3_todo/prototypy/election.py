from uuid import uuid4


class Candidate:

    def __init__(self):
        self.id = uuid4()
        self.others: list[Candidate] = []
        self.is_leader = None

    def elect_leader(self):
        print(f'electing leader on {self.id}')

        # przerobić tą funkcję tak by self.is_leader było True, jeśli nasz id jest najmniejszy z wszystkich
        if self.id < self.other.id:
            self.is_leader = True
        else:
            self.is_leader = False

        # czy to wystarczy ↓↓ by wybory odbyły się na wszystkich Candidate'ach?
        if self.other.is_leader is None:
            self.other.elect_leader()


    def __str__(self):
        return f'Candidate(id={self.id}, is_leader={self.is_leader})'



if __name__ == '__main__':
    N = 3
    candidates = [Candidate() for _  in range(N)]
    for c in candidates:
        print(c)

    candidates[0].elect_leader()


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

