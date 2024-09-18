cont = 1

while cont !=2:

    A = int(input("Digte o valor de A: "))
    B = int(input("Digte o valor de B: "))

    if A == B:
        C = A + B
    else:
        C = A * B

    print(C)
    cont = int(input("Deseja continuar?\n"
                    "1 - Sim\n"
                    "2 - Não\n"))