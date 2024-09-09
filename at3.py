nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))
acrescimo = salario * 1.1
idade2 = idade * 12

print(f"Meu nome é {nome}, tenho {idade} anos e recebo R${acrescimo: .2f} por mês. E a minha idade em meses são {idade2} meses. ")