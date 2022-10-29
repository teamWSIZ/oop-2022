import unittest

from src.z1.klasy import Logger, BufferedLogger
from src.z2_dbservice.dbservice import DbService


class ApiTests(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_dbservice_can_be_created(self):
        db = DbService('localhost', 5432)
        assert db is not None

    def test_dbservice_stores_host_and_port(self):
        db = DbService('localhost', 5432)
        assert db.host == 'localhost'
        assert db.port == 5432

    def test_dbservice_is_not_connected_on_startup(self):
        db = DbService('localhost', 5432)
        assert db.connected == False

    def test_can_write_and_read_from_dbservice(self):
        db = DbService('localhost', 5432)
        db.write('kadabra')
        assert db.read() == 'kadabra'

    def test_can_write_overwrites_in_dbservice(self):
        db = DbService('localhost', 5432)
        db.write('kadabra')
        db.write('kadabra')
        assert db.read() == 'kadabra'

    def test_dbservice_is_empty_on_start(self):
        db = DbService('localhost', 5432)
        db.reconnect()
        assert db.read() == ''

    def test_read_on_disconnected_db_raises_runtime_error(self):
        db = DbService('localhost', 5432)
        with self.assertRaises(RuntimeError):  # sprawdza czy ta metoda rzuciła wyjątkiem (jak nie rzuci, to test>fail)
            db.read()

    def test_write_on_disconnected_db_raises_runtime_error(self):
        db = DbService('localhost', 5432)
        with self.assertRaises(RuntimeError):
            db.write('abra kadabra')
