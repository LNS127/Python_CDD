soma = 0
num = int(input("Digite a quantidade de alunos: "))
for i in range(1,num+1):
    nota1 = int(input("Digite as notas: "))
    soma = soma + nota1

media = soma/num
print(media)

