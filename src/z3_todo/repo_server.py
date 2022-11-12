from uuid import uuid4


class RepoServer:

    def __init__(self):
        self.id = uuid4()
        self.cluster: set[RepoServer] = {self}  # wszystkie RepoServer'y
        self.is_leader = True
        self.leader: 'RepoServer' = self
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
        for oth in self.cluster:
            oth.follower_write(message)

    def follower_write(self, message: str):
        """
        Funkcja do wywołania tylko przez leadera
        """
        self.data.append(message)

    def add_other(self, candidate: 'RepoServer'):
        self.cluster.add(candidate)

    def extend_cluster(self, candidate: 'RepoServer'):
        """
        Add an extra node 'candidate' to the cluster represented by self.cluster
        :param candidate: just a new 'RepoServer'
        :return:
        """

        # cluster membership
        for node in self.cluster.copy():
            node.add_other(candidate)
        candidate.cluster = self.cluster.copy()

        # clone leader info from self
        candidate.leader = self.leader
        candidate.is_leader = False

        # clone data from self
        candidate.data = self.data.copy()

    def elect_leader(self):
        print(f'electing leader on {self.id}')
        all_ids = [n.id for n in self.cluster]
        leader_id = min(all_ids)
        leader_ref = None

        for node in self.cluster:
            if node.id == leader_id:
                node.is_leader = True
                node.leader = node
                leader_ref = node

        for node in self.cluster:
            node.is_leader = (node.id == leader_id)
            node.leader = leader_ref



    def __repr__(self):
        return f'Candidate(id={self.id}, is_leader={self.is_leader})'


if __name__ == '__main__':
    N = 3
    candidates = [RepoServer() for _ in range(N)]
    for c in candidates:
        for ca in candidates:
            c.add_other(ca)

    candidates[0].elect_leader()
    print(candidates)
    print('-' * 10)

    # klient wykonuje zapisy
    candidates[1].write('aaa')
    candidates[0].write('bbb')
    candidates[2].write('ccc')
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
