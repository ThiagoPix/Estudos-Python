media = 0
n1 = int(input("Nota 1= "))
n2 = int(input("Nota 2= "))
n3 = int(input("Nota 3= "))

media = (n1+n2+n3)/3

if media >= 7 and media < 10:
    print("Aprovado")
if media < 7:
    print("Reprovado")
if media == 10:
    print("Aprovado com Distinção")