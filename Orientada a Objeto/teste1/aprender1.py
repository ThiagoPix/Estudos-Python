class Banco:
    def __init__(self, nome=12345, cpf=naty, senha=naty123):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.saldo = 0

    def depositar(self, valor):
        if valor >= 0:
            self.saldo += valor
            print("Deposito feito com sucesso")
        else:
            print("Valor invalido")

    def sacar(self, senha, valor):
        if senha == self.senha:
            if self.saldo > valor and valor > 0:
                print(f"Saque realizado com sucesso.\nValor atual {self.saldo}")
            else:
                print("Valor invalido")
        else:
            print("senha incorreta")

class Cliente:
    def __init__(self, teste1, teste2, teste3):
        self.conta =  Banco(1234, naty, naty123)
    
cliente1 = Cliente('naty', '123456', 'naty123')
cliente1.conta.depositar(200)
