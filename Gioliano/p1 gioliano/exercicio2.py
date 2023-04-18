quantidade = 0

for i in range(10):
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        quantidade = quantidade + 1

print("A quantidade de números pares inseridos é= ", quantidade)