soma = 0
media = 0

for i in range(1, 9):
    n = int(input("Digite um número: "))
    soma = soma + n

media = soma/i
print("A soma dos números = ", soma)
print("A média dos números= ", media)