idades = []
alturas = []

for i in range(30):
  idade = int(input(f"Digite a idade do {i+1}º aluno: "))
  altura = float(input(f"Digite a altura do {i+1}º aluno: "))
  idades.append(idade)
  alturas.append(altura)

soma_alturas = 0
num_alunos = 0
for i in range(30):
  if idades[i] > 13:
    soma_alturas += alturas[i]
    num_alunos += 1

media_alturas = soma_alturas / num_alunos

num_alunos_baixa_altura = 0
for i in range(30):
  if idades[i] > 13 and alturas[i] < media_alturas:
    num_alunos_baixa_altura += 1

print(f"Há {num_alunos_baixa_altura} alunos com mais de 13 anos e altura inferior à média de altura desses alunos.")