'''
Classe service para manipular a classe Conta

@author: marcos
'''

class ContaService:
    
   
    def __init__(self):
        pass
        
    def deposito(self, valor, Conta):
        totalDeposito = Conta.getTotalDepositori() + valor
        Conta.setTotalDeposito(totalDeposito)
        
        if (Conta.getLimiteInicial() != Conta.getLimite()):
            reposicao = Conta.getLimiteInicial() - Conta.getLimite()
            
            limite = Conta.getLimite() + reposicao
            Conta.setLimite(limite)
            
            saldo = Conta.getSaldo() + valor
            saldoTotal = saldo - reposicao
            
            Conta.setSaldo(saldoTotal)
            
        else:
            saldoTot = Conta.getSaldo() + valor
            Conta.setSaldo(saldoTot)

    def getSaldoTotal(self, conta):
        return conta.getSaldo() + conta.getLimite()

    def saque(self, valor, Conta):

        if (valor <= Conta.getSaldoTotal()):
            self.totalSaque += valor;
            if (valor <= self.getSaldo()):
                self.saldo -= valor
                print('Saldo atual (Saldo + Limite): R$ {:.2f}'.format(self.getSaldoTotal()))
            elif (valor <= self.getSaldoTotal()):
                valor_saca_limite = valor - self.getSaldo()
                self.limite -= valor_saca_limite
                self.saldo = 0
        else:
            print('\n\nSaldo insuficiente!\n\n')
            print('Pressione qualquer tecla para continuar...')
            input('')

    def valorDeposito(self):
        return

    def extrato(self, conta):
        print 'Extrato CC No.' + conta.getNumero() + '\n' 
        print 'Deposito: R$ {:.2f}'.format(conta.getTotalDeposito()) + '\n'
        if (conta.getTotalSaque() > 0):
            print 'Saque: R$ {:.2f}'.format(conta.getTotalSaque()) + '\n'

        print 'Saldo: R$ {:.2f}'.format(conta.getSaldo()) + '\n' 
        print 'Limite: R$ {:.2f}'.format(conta.getLimite()) + '\n'
        print 'Disponivel: R$ {:.2f}'.format(self.getSaldoTotal(conta)) + '\n'   
    