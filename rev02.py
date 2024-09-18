cont =1
while cont !=2:
    num = int(input("Digite um número: "))

    if num > 0 and num%2 ==0:
        print(f"{num} é Par e positivo")
    elif num > 0 and num%2 !=0:
        print(f"{num} é Impar e positivo")
    elif num < 0 and num%2 == 0:
        print(f"{num} é Par e negativo")
    else:
        print(f"{num} é impar e negativo")
    cont= int(input("Você deseja fazer novamente?\n "
                "1 - para sim\n"
                " 2 - não \n"))