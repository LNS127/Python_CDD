time1 = input("Digite  o nome do time 1: ")
time2 = input("Digite  o nome do time 2: ")

placar1 = int(input("Digite quantos gols o time 1 marcou: "))
placar2 = int(input("Digite quantos gols o time 2 marcou: "))

if(placar1 == placar2):
    print("A partida foi empate.")
else:
    if(placar1 > placar2):
        print(f"O {time1} venceu.")
    else:
        print(f"O  {time2} venceu.")