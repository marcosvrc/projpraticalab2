'''
Classe service para manipular a classe Conta

@author: marcos
'''

class ContaService:
    
   
    def __init__(self):
        pass
        
    #Faz o deposito na conta do cliente
    def deposito(self, valor, conta):
       
        conta.setTotalDeposito(valor)
        conta.setSaldo(conta.getSaldo() + conta.getTotalDeposito())

    #Obtem o saldo total do cliente
    def getSaldoTotal(self, conta):
        return conta.getSaldo() + conta.getLimite()

    
    #Processa o saque do cliente
    def saque(self, valor, conta):

        if (valor <= self.getSaldoTotal(conta)):
            conta.setTotalSaque(conta.getTotalSaque() + valor)
            if (valor <= conta.getSaldo() or valor <= self.getSaldoTotal(conta)):
                conta.setSaldo(conta.getSaldo() - valor)
        else:
            print "\n\nSaldo insuficiente!\n\n"
            print "Pressione qualquer tecla para continuar..."
            raw_input('')


    # Emite o extrato do cliente
    def extrato(self, conta):
        print 'Extrato CC No.' + conta.getNumero() + '\n' 
        print 'Deposito: ' + self.formatarValorMonetario(conta.getTotalDeposito()) + '\n'
        if (conta.getTotalSaque() > 0):
            print 'Saque: ' + self.formatarValorMonetario(conta.getTotalSaque()) + '\n'

        print 'Saldo: ' + self.formatarValorMonetario(conta.getSaldo()) + '\n' 
        print 'Limite: ' + self.formatarValorMonetario(conta.getLimite()) + '\n'
        print 'Disponivel: ' + self.formatarValorMonetario(self.getSaldoTotal(conta)) + '\n'   
    
    # Formata valor monetario
    def formatarValorMonetario(self , valor):
        return 'R$ {:.2f}'.format(valor)
    