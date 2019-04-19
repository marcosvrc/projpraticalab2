'''
Classe Conta

@author: marcos
'''

class Conta:
   
    def __init__(self, numero, saldo, limite=1000.0, totalSaque=0.0, totalDeposito=0.0):
        self.numero = numero
        self.saldo = saldo
        self.limite = limite
        self.totalSaque = totalSaque
        self.totalDeposito = totalDeposito
        
    def setNumero(self, numero):
        self.numero = numero

    def getNumero(self):
        return self.numero
    
    def setSaldo(self, saldo):
        self.saldo = saldo
        
    def getSaldo(self):
        return self.saldo
    
    def setLimite(self, limite):
        self.limite = limite
        
    def getLimite(self):
        return self.limite
    
    
    def setTotalSaque(self, totalSaque):
        self.totalSaque = totalSaque
    
    def getTotalSaque(self):
        return self.totalSaque
    
    def setTotalDeposito(self, totalDeposito):
        self.totalDeposito = totalDeposito
        
    def getTotalDeposito(self):
        return self.totalDeposito