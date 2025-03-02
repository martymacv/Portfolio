import sys
import traceback


class ConnectionError(Exception):
    def __init__(self):
        pass


class DatabaseConnection:
    def __init__(self):
        self._fl_connection_open = None
        self.login = None
        self.password = None

    def connect(self, login, password):
        self.login = login
        self.password = password
        self._fl_connection_open = True

    def close(self):
        self._fl_connection_open = False

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(exc_type)
            self.close()
            return False
        self.close()
        return True



db = DatabaseConnection()


sys.exit(999)
# здесь объявляйте класс PrimaryKey
class PrimaryKey:
    def __init__(self):
        pass

    def __enter__(self):
        print('вход')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(exc_type)
            return True


with PrimaryKey() as pk:
    raise ValueError
