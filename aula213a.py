# teste com @propety

class Connection:
    def __init__(self,):
        self._user = None
        self._password = None

    @property
    def auth(self):
        return self._user, self._password

    @auth.setter
    def auth(self, values):
        self._user, self._password = values

if __name__ == '__main__':
    connection = Connection()
    connection.auth = ('teste', 'teste')
    print(connection._user)
    print(connection._password)