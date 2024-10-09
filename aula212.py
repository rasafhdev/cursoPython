# @Propery - é um getter no modo Pythonico!
# getter - é um methodo para obter um atributo.
# cor -> get_cor()
# Modo Pythônico - Modo Python de fazer as coisas
# @propety é uma propriedade do objeto, ela
# é um método que se comporta como um atributo.
# Geralmente é usada mas seguintes situações;
# - como geter
# p/ evitar quebrar o código cliente
# p/ habilitar o Setter
# p/ executar ações ao obter um atributo.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def get_nome(self):
        print('Estou usando propety para obter o nome')
        return self.nome

    @property
    def get_idade(self):
        return self.idade


pessoa = Pessoa(
    'Rodrigo',
    '28'
)

print(pessoa.get_nome)
print(pessoa.get_idade)