num = int(input('Digite um número: '))

for x in range (0,num):
    for y in range(0,x+1):
        print(y, end= " ")
    print()