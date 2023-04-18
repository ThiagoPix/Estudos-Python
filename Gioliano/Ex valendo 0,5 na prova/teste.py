# Função para calcular o abono
def calcular_abono(salario):
    abono = salario * 0.2  # Calcula 20% do salário
    if abono < 100:  # Define o valor mínimo de R$ 100,00
        abono = 100
    return abono

# Variáveis para armazenar os resultados
total_funcionarios = 0
total_abono = 0
total_minimo = 0
maior_abono = 0

# Loop para digitação dos salários
while True:
    salario = float(input("Digite o salário do funcionário (ou 0 para encerrar): "))
    if salario == 0:
        break  # Encerra o loop quando o valor digitado for 0
    abono = calcular_abono(salario)  # Chama a função para calcular o abono
    total_funcionarios += 1  # Incrementa o contador de funcionários
    total_abono += abono  # Soma o abono ao total
    if abono == 100:
        total_minimo += 1  # Incrementa o contador de funcionários que receberão o valor mínimo
    if abono > maior_abono:
        maior_abono = abono  # Atualiza o maior valor pago como abono
    print(f"Salário: R$ {salario:.2f} | Abono: R$ {abono:.2f}")

# Exibe o relatório com os resultados
print("\nRelatório de Cálculo de Abono:")
print("Salário     | Abono")
print("-------------------------")
print(f"Número total de funcionários processados: {total_funcionarios}")
print(f"Valor total a ser gasto com o pagamento do abono: R$ {total_abono:.2f}")
print(f"Número de funcionários que receberão o valor mínimo de R$ 100,00: {total_minimo}")
print(f"Maior valor pago como abono: R$ {maior_abono:.2f}")
