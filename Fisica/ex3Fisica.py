d1 = 30
v1 = 90

d2 = 40
v2 = 80

percorridoTotal = 100
horasTotal = 1.5

t1 = d1 / v1
t2 = d2 / v2

tempoTotal = t1 + t2
t3 = horasTotal - tempoTotal

d3 = percorridoTotal - d1 - d2

v3 = d3 / t3

print(f'A velocidade do último trecho foi de {v3}km/h.')
