opcao = 1

while opcao != 2:
    alunos = int(input("Digite a quantidade de alunos: "))

    n = 0
    notas = 0

    while n < alunos:
        nota = float(input("Digite as notas dos alunos: "))
        n = n + 1
        notas = notas + nota
        media = notas / alunos

    print(f"a média da turma é{media: .2f}")

    opcao = int(input("Deseja continuar?\n"
                      "1 para sim\n"
                      "2 para não "))
