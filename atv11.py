hora1 = int(input("Digite a hora: "))
minuto1 = int(input("Digite os minutos: "))
hora2 = int(input("Digite a hora: "))
minuto2 = int(input("Digite os minutos: "))



if hora1 > 12:
    hora1 -= 12

if hora2 > 12:
    hora2 -= 12

horaF = hora1 + hora2
minutoF = minuto1 + minuto2

if horaF > 12:
    horaF -= 12

if minutoF > 60:
        minutoF -= 60
        horaF += 1





print(f'{horaF} : {minutoF: 02d}')





