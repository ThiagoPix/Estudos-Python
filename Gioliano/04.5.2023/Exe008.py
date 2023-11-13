id = []
a = []

for i in range(5):
  b = int(input(f"Digite a idade {i+1}: "))
  al = float(input(f"Digite a altura {i+1}: "))
  id.append(b)
  a.append(al)

print("Idade na ordem inversa:")
for i in range(4, -1, -1):
  print(id[i])

print("Altura na ordem inversa:")
for i in range(4, -1, -1):
  print(a[i])