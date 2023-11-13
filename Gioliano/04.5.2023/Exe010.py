A = []
for i in range(10):
  n = int(input(f"Digite o {i+1}º número do vetor 1: "))
  A.append(n)

B = []
for i in range(10):
  n = int(input(f"Digite o {i+1}º número do vetor 2: "))
  B.append(n)

C = []
for i in range(10):
  C.append(A[i])
  C.append(B[i])

print("O vetor C é:")
print(C)