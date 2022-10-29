from src.z3_todo.model import Todo
from collections.abc import Collection


class Repo:

    def __init__(self):
        self.todolists: Collection[Todo] = set()
        # self.todos = dict[str, list[Todo]]    # gdybyśmy chcieli mieć więcej "kanałów" todo's
        self.cluster = {self}
        self.highest_id = 0

    def add_node(self, node: 'Repo'):
        self.cluster.add(node)

    def join_repo(self, repo: 'Repo'):
        # połączenie się z clusterem, do którego należy już `repo`
        repo.add_node(self)
        self.add_node(repo)
