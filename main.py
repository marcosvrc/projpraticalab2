'''

Classe Main para rodar a aplicacao

@author: marcos
'''

from contaservice import ContaService
from conta import Conta
from cliente import Cliente


conta = Conta('34993', 0)
cliente = Cliente('MARCOS VINICIO RAMOS CAMARA', '99999999', conta)

contaService = ContaService()

opcao = ''
repete = True
while (repete):

    print "\n\nOpcoes:\n"
    print "[1] Deposito" 
    print "[2] Saque" 
    print "[3] Extrato" 
    print "[4] Sair" 

    opcao = raw_input('\nDigite a sua opcao: ')
    if (opcao == '1'):
        valor = float(raw_input('Digite o valor do deposito: R$ '))
        contaService.deposito(valor, conta)
    elif (opcao == '2'):
        valor = float(raw_input('Digite o valor do saque: R$ '))
        contaService.saque(valor, conta)
    elif (opcao == '3'):
        contaService.extrato(conta)
    elif (opcao == '4'):
        print 'Programa encerrado!' 
        repete = False
        exit()
    else:
        print 'Opcao Invalida: '


        
        