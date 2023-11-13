m = []

for i in range(10):
  n = [] 
  for j in range(4):
    n2 = float(input(f"Digite a nota {j+1} do aluno {i+1}: "))
    n.append(n2)

m2 = sum(n) / 4
m.append(m2)

num_aprovados = 0
for m2 in m:
  if m2 >= 7.0:
    num_aprovados += 1

print(f"{num_aprovados} alunos têm média maior ou igual a 7.0.")