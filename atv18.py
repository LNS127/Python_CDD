
cont = 0

for x in range(11):
    num = int(input("Digite um número: "))
    if num < 0:
        cont += 1

print(f'{cont} números são negativos')

