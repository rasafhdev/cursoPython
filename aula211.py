# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌❌cls)

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    '''
    Abaixo é retornado um instância da classe, ou seja,
    em vez de chamar diretamente o metodo contrutor, estamos chamado o metodo de classe, que no final do bloco retorna para a variavel conection a classe construtora
    '''
    @classmethod
    def create_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @classmethod
    def create_auth_admin(cls, user, password, admin_code):
        conection = cls()
        conection.user = user
        conection.password = password
        conection.admin_code = admin_code
        return conection

    @staticmethod
    def log(msg):
        print("Log:", msg)

# c1 = Connection()
# c1.set_user('Rodrigo')
# c1.set_password('Rodrigo')
c1 = Connection.create_auth('Rodrigo', '1234')
admin = Connection.create_auth_admin(
    'Rodrigo',
    '1234',
    'Hipopotomonstrosesquipedaliofobia'
)
print(c1.user)
print(c1.password)
print(admin.user)
print(admin.password)
print(admin.admin_code)
print(Connection.log('Essa é a mensagem de LOG'))