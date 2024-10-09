# @propety + @setter - getter e setter no modo pythonico

class Calculadora:
    def __init__(self, valor1,  valor2):
        self.valor1 = valor1
        self.valor2 = valor2
        self.resultado = None


    @property
    def resultado(self):
        return self.valor1 + self.valor2

    @resultado.setter
    def set_valores(self):
        