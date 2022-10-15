import unittest

from src.z1.klasy import Logger, BufferedLogger


class ApiTests(unittest.TestCase):

    def setUp(self) -> None:
        self.logger = BufferedLogger(buffer_size=10)

    def test_is_created(self):
        pass
        # assert self.logger.log_id == 17

