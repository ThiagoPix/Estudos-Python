class ContaBancaria():
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def sacar(self, valorSaque):
        if valorSaque <= self.saldo:
            self.saldo -= valorSaque
            print(f'Você sacou R$ {valorSaque:.2f}')
        else:
            print('Saldo insuficiente.')

    def depositar(self, valorDeposito):
        self.saldo += valorDeposito
        print(f'Você depositou R$ {valorDeposito:.2f}')

    def extrato(self):
        print(f'Seu extrato = R$ {self.saldo:.2f}')


def cadastrar_cliente():
    cliente = input('\nQual seu nome?\n')
    idade = int(input('\nQual sua idade?\n'))
    if idade < 18:
        print('Desculpe, você não pode abrir uma conta bancária, pois é menor de 18 anos.')
        return None
    banco = input('\nQual banco você gostaria de abrir uma conta?\n')
    saldoInicial = float(input('Qual o valor inicial da conta? R$ '))
    print(f'\n{cliente}, obrigado por abrir uma conta no {banco} com um saldo inicial de R$ {saldoInicial:.2f}!')
    return ContaBancaria(saldoInicial)


def menu(conta):
    while True:
        print('\n-------------------------------------------------------------\n')
        print('MENU:')
        opcao = int(input('ESCOLHAS:\n1 - Visualizar extrato\n2 - Depositar dinheiro\n3 - Sacar dinheiro\n4 - Finalizar o caixa\nESCOLHER = '))

        if opcao == 1:
            conta.extrato()
        elif opcao == 2:
            valorDeposito = float(input('Quanto gostaria de depositar? R$ '))
            conta.depositar(valorDeposito)
        elif opcao == 3:
            valorSaque = float(input('Quanto gostaria de sacar? R$ '))
            conta.sacar(valorSaque)
        elif opcao == 4:
            break


def main():
    perguntaCadastro = input('\nJá tem cadastro em algum banco? (Sim ou Não)\n').lower()

    if perguntaCadastro == 'nao':
        print('Okay, vamos prosseguir com o cadastro!')
        conta = cadastrar_cliente()
        if conta is None:
            return
    else:
        cliente = input('Qual seu nome? ')
        saldoInicial = float(input('Qual o saldo inicial da conta existente? R$ '))
        conta = ContaBancaria(saldoInicial)

    escolhaAcessar = input('Gostaria de acessar sua conta no banco? (Sim ou Não) ').lower()

    if escolhaAcessar == 'sim':
        menu(conta)
    else:
        print('Volte sempre')


main()