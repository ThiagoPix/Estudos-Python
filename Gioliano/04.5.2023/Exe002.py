v = []   
for i in range(10):
  n = int(input("Digite um número: "))
  v.append(n)

print("Os números na ordem inversa, são:")
for i in range(9, -1, -1):
  print(v[i])
