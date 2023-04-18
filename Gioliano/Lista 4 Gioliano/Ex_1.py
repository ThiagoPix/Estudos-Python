x = 3
y = 4
z = 0.6

print(x + x * x ** (y * x) / z)

# Primeiro será feito o que está em parenteses, em seguida fara a potência
# Depois fará a multiplicação pois vem antes da divisão na equação, depois a divisão e em seguida, a soma

print(((not(x + z < y)) or (x + x * z >= y )) and True)

# Apenas um dos que estão sendo comparados no "OR" precisam ser true para que o print digite True, pois false and true da false.
# (not(x + z < y) é falso. x + z é sim menor que y, porém, o not reverte o valor booleano dele, transformando em false
# x + x * z >= y  é true pois x + x * z == 4.8 que é maior que y, logo é verdadeiro.
# Dessa forma, true and true, da true.