prim = int(input('Qual número você quer saber se é primo? '))
res = 0
for i in range(1, prim+1):
    if prim % i == 0:
        res+= 1

if res == 2:
    print("\n", prim, "É um número primo")
else:
    print("\n", prim, "Não é um número primo")
