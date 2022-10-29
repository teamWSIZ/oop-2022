from collections.abc import Collection
from uuid import UUID

from src.z3_todo.model import Todo
from src.z3_todo.repo import Repo


class Client:

    def __init__(self, cluster: list[Repo], client_id: int):
        self.todos: Collection[Todo] = set()


    def connect_to_repo_cluster(self, cluster: list[Repo]):
        pass


    def synchronize_messages(self):
        # magic; pull current list of items from repo; replace local set
        pass


    def create_item(self, message: str, day_from_today=7):
        # must send the item to repo
        pass

    def delete_item(self, uuid: UUID):
        pass


    def get_all_items(self, only_active=False):
        # active == not past due date
        pass
