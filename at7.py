n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
n3 = float(input("Digite sua terceira nota: "))

media = (n1+n2+n3)/3


if(media >=7):
         print(f"Sua média é{media: .1f}. Você está aprovado.")
else:
    if (media >= 4):
        print(f"Sua média é {media: .1f}. Você está de recuperação.")
    else:
        print(f"Sua média é {media: .1f}.Você está reprovado")