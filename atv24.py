tentativa = 3

senha = 5111

while tentativa > 0:
    receba = int(input("Digite sua senha: "))
    if receba == senha:
        print("Acesso liberado")
        break
    else:
        print("Acesso negado, digite novamete:")
        tentativa -= 1
if tentativa == 0:
      print("Acesso bloqueado")
