# Abstração
# Herança é um

from pathlib import Path

# um caminho do log usando a lib pathlib
# uma classe principal protegida
#   um metodo de log erro
#   um metodo de log success
# uma classe para herdar a principal LogFileMixin
# uma classe para herdar a principal LogPrintMixin
# chamada dos métodos.




LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg): # Assinatura do método
        raise NotImplementedError('Implemente o método log')

    def log_error(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')


# Mixin é para adicionar funcionalidades na sua herança multipla
class LogFileMixin(Log): #é um LOG
    def _log(self, msg):
        print(msg)

class LogPrintMixin(Log): #é um LOG
    def _log(self, msg):
        print(f'{msg}')


if __name__ == '__main__':
    l = LogPrintMixin()
    l.log_error('qualquer coisa')
    l.log_success('Qualquer coisa')
    print(LOG_FILE)