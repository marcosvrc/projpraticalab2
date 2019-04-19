'''

Classe Main para rodar a aplicacao

@author: marcos
'''

from contaservice import ContaService
from conta import Conta
from cliente import Cliente


class Main:
  
    def __init__(self, params):
        pass
    
    conta = Conta('23443', 0.0, 1000.0, 1000.0, 2.0, 3.0)
    cliente = Cliente('Marcos Vinicio', '23323232332', conta)
    
    contaService = ContaService()
    
    contaService.extrato(cliente.getConta())
        