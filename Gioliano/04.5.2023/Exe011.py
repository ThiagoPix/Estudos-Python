A = []
for i in range(10):
  n = int(input(f"Digite o {i+1}º número do vetor A: "))
  A.append(n)

B = []
for i in range(10):
  n = int(input(f"Digite o {i+1}º número do vetor B: "))
  B.append(n)

C = []
for i in range(10):
  n = int(input(f"Digite o {i+1}º número do vetor C: "))
  C.append(n)

D = []
for i in range(10):
  D.append(A[i])
  D.append(B[i])
  D.append(C[i])

print("O vetor D é:")
print(D)