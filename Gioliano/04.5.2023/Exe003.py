nota = []

for i in range(4):
  n = float(input("Digite a nota {}: ".format(i+1)))
  nota.append(n)

m = sum(nota) / len(nota)

print("Notas =", nota)
print("Média =", m)