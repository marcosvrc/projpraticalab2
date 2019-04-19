'''
Classe service para manipular a classe Conta

@author: marcos
'''

class ContaService:
    
   
    def __init__(self):
        pass
        
    def deposito(self, valor, conta):
       
        conta.setTotalDeposito(valor)
        conta.setSaldo(conta.getSaldo() + conta.getTotalDeposito())

    def getSaldoTotal(self, conta):
        return conta.getSaldo() + conta.getLimite()

    def saque(self, valor, conta):

        if (valor <= self.getSaldoTotal(conta)):
            conta.setTotalSaque(conta.getTotalSaque() + valor)
            if (valor <= conta.getSaldo() or valor <= self.getSaldoTotal(conta)):
                conta.setSaldo(conta.getSaldo() - valor)
        else:
            print "\n\nSaldo insuficiente!\n\n"
            print "Pressione qualquer tecla para continuar..."
            raw_input('')


    def extrato(self, conta):
        print 'Extrato CC No.' + conta.getNumero() + '\n' 
        print 'Deposito: R$ {:.2f}'.format(conta.getTotalDeposito()) + '\n'
        if (conta.getTotalSaque() > 0):
            print 'Saque: R$ {:.2f}'.format(conta.getTotalSaque()) + '\n'

        print 'Saldo: R$ {:.2f}'.format(conta.getSaldo()) + '\n' 
        print 'Limite: R$ {:.2f}'.format(conta.getLimite()) + '\n'
        print 'Disponivel: R$ {:.2f}'.format(self.getSaldoTotal(conta)) + '\n'   
    