num = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

while num2 == 0:
    num2 = int(input("Número inválido, Digite o segundo número: "))

div = num/num2

print(div)