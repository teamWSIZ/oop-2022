import unittest
from collections.abc import Collection
from dataclasses import dataclass
from datetime import date, datetime


@dataclass
class TodoMessage:
    content: str
    due_date: date
    message_id: str


class TodoRepo:

    def write(self, message: TodoMessage):
        """
        Stores the `message` in the system.
        :param message:
        :return:
        """
        pass

    def read_all(self) -> Collection[TodoMessage]:
        """
        :return: all messages stored in the system
        """
        pass

    def read_range(self, from_due_date: date, to_due_date=datetime.now().date()) -> Collection[TodoMessage]:
        """
        :param from_due_date:
        :param to_due_date:
        :return: all messages stored with due date between the dates provided
        """
        pass

    def remove(self, message_id: str):
        """
        Removes the massage with provided ID; does nothing if such message is not present in the system.
        :param message_id:
        :return:
        """


class SimpleRepo(TodoRepo):
    def write(self, message: TodoMessage):
        pass

    def read_all(self) -> Collection[TodoMessage]:
        return []

    def remove(self, message_id: str):
        pass


class TodoServerTest(unittest.TestCase):

    def setUp(self) -> None:
        print('creating a new SimpleRepo')
        self.repo: TodoRepo = SimpleRepo()

    def test_can_save_message(self):
        msg = TodoMessage('abra kadabra', date(2012, 1, 15), '0000')
        self.repo.write(msg)
        messages = self.repo.read_all()

        self.assertEqual(len(messages), 1)
        self.assertTrue(msg in messages)

    def test_can_save_two_messages(self):
        msg1 = TodoMessage('abra kadabra', date(2012, 1, 15), '0000')
        msg2 = TodoMessage('deus vult', date(2012, 1, 20), '0001')
        self.repo.write(msg1)
        self.repo.write(msg2)
        messages = self.repo.read_all()

        self.assertEqual(len(messages), 2)
        self.assertTrue(msg1 in messages)
        self.assertTrue(msg2 in messages)

    def test_can_remove_messages(self):
        msg1 = TodoMessage('abra kadabra', date(2012, 1, 15), '0000')
        msg2 = TodoMessage('deus vult', date(2012, 1, 20), '0001')
        self.repo.write(msg1)
        self.repo.write(msg2)
        self.repo.remove(message_id=msg1.message_id)
        messages = self.repo.read_all()

        self.assertEqual(len(messages), 1)
        self.assertTrue(msg2 in messages)

    def test_saving_with_same_id_overwrites(self):
        msg1 = TodoMessage('abra kadabra', date(2012, 1, 15), '0000')
        msg2 = TodoMessage('deus vult', date(2012, 1, 20), '0000')
        self.repo.write(msg1)
        self.repo.write(msg2)
        messages = self.repo.read_all()

        self.assertEqual(len(messages), 1)
        self.assertTrue(msg2 in messages)
