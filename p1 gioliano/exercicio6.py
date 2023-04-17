ganho = float(input("Quanto voce ganha por hora? "))
hora = int(input("Quantas horas você trabalha por mês? "))

total = ganho*hora
renda = total*0.17
inss = total*0.09
sindicato = total*0.03

print("---------------------------------")
print("O seu salario bruto é= R$", total)
print("O valor pago ao inss= R$", inss)
print("Valor pago de Imposto de Renda= R$", renda)
print("Valor pago de sindicato= R$", sindicato)
print("O valor liquido recebido= R$", total-renda-inss-sindicato)