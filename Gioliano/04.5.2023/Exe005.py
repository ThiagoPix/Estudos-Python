v = []
par = []
impa = [] 

for i in range(20):
  n = int(input("Digite um número: "))
  v.append(n)

for n in v:
  if n % 2 == 0:
    par.append(n)
  else:
    impa.append(n)

print("ímpares: ", impa)
print("pares: ", par)
print("Todos: ", v)