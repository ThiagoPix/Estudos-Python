n1 = 1
n2 = 1
n3 = 0
guardar = 0
nf = int(input("Quer fazer quantas vezes? "))

if nf == 0:
    print("Tudo bem, acabou!")
if nf == 1:
    print(n1)
if nf == 2:
    print(n1)
    print(n2)
if nf >= 3:
    print(n1)
    print(n2)
    for i in range(1,nf-1):
        g = n2
        n3 = n1 + n2
        print(n3)
        n2 = n3
        n1 = g