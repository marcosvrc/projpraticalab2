'''
Classe Conta

@author: marcos
'''

class Conta:
   
    def __init__(self, numero, saldo, limite, limiteInicial, totalSaque, totalDeposito):
        self.numero = numero
        self.saldo = saldo
        self.limite = limite
        self.limiteInicial = limiteInicial
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
    
    def setLimiteInicial(self, limiteInicial):
        self.limiteInicial = limiteInicial
        
    def getLimiteInicial(self):
        return self.limiteInicial
    
    def setTotalSaque(self, totalSaque):
        self.totalSaque = totalSaque
    
    def getTotalSaque(self):
        return self.totalSaque
    
    def setTotalDeposito(self, totalDeposito):
        self.totalDeposito = totalDeposito
        
    def getTotalDeposito(self):
        return self.totalDeposito