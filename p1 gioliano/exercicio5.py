salario = float(input("Qual é o seu salario? "))

if salario <= 2800:
    print("Seu aumento salarial é de: ", salario * 0.20)
    print("Seu novo salario é = ", salario*1.20)

if salario > 2800 and salario < 7000:
    print("Seu aumento salarial é de: ", salario * 0.15)
    print("Seu novo salario é = ", salario*1.15)

if salario > 7000 and salario < 15000:
    print("Seu aumento salarial é de: ", salario * 0.10)
    print("Seu novo salario é = ", salario*1.10)

if salario >= 15000:
    print("Seu aumento salarial é de: ", salario * 0.05)
    print("Seu novo salario é = ", salario*1.05)