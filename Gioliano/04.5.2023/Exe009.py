A = []
for i in range(10):
  n = int(input(f"Digite o {i+1}º número: "))
  A.append(n)

quadrado = 0
for n in A:
  quadrado += n ** 2

print(f"A soma dos quadrados dos elementos do vetor A é {quadrado}.")