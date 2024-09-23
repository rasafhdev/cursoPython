# Métodos de Classe
# São métodos onde self será "cls", ou seja,
# em vez de recevcer a instância no primeiro
# parametro, recebebe

from datetime import datetime as dt

class Pessoa:
    ano = dt.now().year # atributo da classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')
    
    @classmethod
    def criar_pessoa_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls("Anônima", idade)

# Abaxi estamo usando a classe diretamente.
p1 = Pessoa('Rodrigo', 34)
p2 = Pessoa('Anonima', 28)

'''
Abaixo estamos chamado o metodo diramente,
sem precisa instanciar primeiro.
''' 
p3 = Pessoa.criar_pessoa_com_50_anos('Helena')
p4 = Pessoa.criar_sem_nome(23)

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)
