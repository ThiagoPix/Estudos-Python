totalAbono = 0
funcionariototal = 0
maiorAbono = 0
minimoAbono = 0


while True:
    salario = float (input("Digite o salario. (Aperte 0 e de enter para cancelar!)"))
    if salario == 0: 
        break
    else:   
        abono = salario * 0.2
        if abono < 100 and abono >0:
            abono = 100

        totalAbono = totalAbono + abono
        if abono == 100:
            minimoAbono += 1
        
        if abono > maiorAbono:
            maiorAbono = abono

        print ('Salario - Abono ')
        print("R$", salario, "- R$",abono )

print("\nProjeção de Gastos com Abono")
print("============================")
print("\nTotal gasto com abono: R$", totalAbono)
print("Valor mínimo pago a", minimoAbono, "colaboradores" )
print("Maior valor de abono pago: R$", maiorAbono)