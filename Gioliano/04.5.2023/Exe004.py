v = [] 
con = []

for i in range(10):
  c = input("Digite um caractere: ")
  v.append(c)

for c in v:
  if c.isalpha() and c.lower() not in "aeiou":
    con.append(c)

print("Número de consoantes digitadas: ", len(con))
print("As consoantes digitadas foram: ", con)