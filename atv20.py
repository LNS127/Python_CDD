n = 0
notas = 0
while n <10:
    nota = float(input("Digite sua nota: "))
    n = n+1
    notas = notas + nota

media = notas/10

print(f"{media: .2f}")
