'''
Classe Cliente

@author: marcos
'''
from conta import Conta

class Cliente:
   

    def __init__(self, nome, telefone, conta):
        
        self.nome = nome
        self.telefone = telefone
        self.conta = conta
    
    def setNome(self, nome):
        self.nome = nome
    
    def getNome(self):
        return self.nome
    
    def setTelefone(self,telefone):
        self.telefone = telefone
        
    def getTelefone(self):
        return self.telefone
    
    def setConta(self, conta):
        self.conta = conta
    
    def getConta(self):
        return self.conta