# Código com DRY (Don't Repeat Yourself)

class Connection:
    def __init__(self, host='localhost'): # Is private
        self._host = host
        self._user = None
        self._password = None
        self._admin_code = None

    '''
    def set_user(self, user):
        self._user = user

    def set_password(self, password):
        self._password = password

    def set_admin_code(self, admin_code):
        self._admin_code = admin_code
    '''

    @classmethod
    def _create_connection(cls, user, password, admin_code=None):
        connection = cls()
        connection.user = user
        connection.password = password
        connection.admin_code = admin_code
        return connection

    @classmethod
    def create_auth(cls, user, password):
        return cls._create_connection(user, password)

    @classmethod
    def create_auth_admin(cls, user, password, admin_code):
        return cls._create_connection(user, password, admin_code)


c1 = Connection.create_auth(
    'Rodrigo',
    '1234',
)

c1_admin = Connection.create_auth_admin(
    'Rodrigo',
    '1234',
    'Hipopotomonstrosesquipedaliofobia',
)

print(f'Call whith classmethod create_auth:\n User: {c1.user}\n Password: {c1.password}\n')
print(f'Call whith classmethod create_auth_admin:\n User: {c1_admin.user}\n Password: {c1_admin.password}\n Admin Code: {c1_admin.admin_code}')
