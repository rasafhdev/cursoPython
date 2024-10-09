# Encapsulamento (modificadores de acessos: public, protected, private)
# Python não tem modificadores de acesso nativo.
# Usa-se então uma convenção:
#   (Sem underline) = Public
#   (Um underline) = Protected
#   (Dois underlines) = Private
#       "name manglig" (desfiguração de nomes) em Python
#       só DEVE ser usado na classe em que foi declarado.

class Foo:
    def __init__(self):
        self.publico = 'Isso é publico'
        self._protected = 'Isso é privado'
        self.__private = 'Isso é privado' # somente nessa classe

    def metodo_publico(self):
        self._metodo_protected()
        return 'metodo_publico'

    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'

    def __metodo_private(self):
        print('__metodo_private')
        return '__metodo_private'


f = Foo()
print(f.metodo_publico())