m = 1
v = []
for i in range(5):
  n = int(input(f"Digite um numero {i+1}: "))
  v.append(n)

s = sum(v)

for n in v:
  m *= n

print(f"multiplicação: {m}")
print(f"soma: {s}")
print(f"numeros: {v}")