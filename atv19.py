cont = 0
cont_neg = 0
for x in range(11):
    num = int(input("Digite um número: "))
    if num >= 10 and num <=20:
        cont += 1
    else:
        cont_neg += 1

print(f'{cont} números estão no intervalo e \n {cont_neg} números estão fora do intervalo')


