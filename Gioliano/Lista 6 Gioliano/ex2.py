salarioInicial = float(input("Digite seu primeiro salário: "))
anosTrabalhados = int(input("Digite quantos anos você trabalhou na empresa: "))
percentual = 0.015
for i in range(anosTrabalhados) :
    
    print(f"Seu salario atualmente é de {salarioInicial + (salarioInicial * percentual)}")
    percentual = percentual * 2