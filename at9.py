combustivel = input("Qual foi o combustível escolhido (digite apenas a inicial do combustível: G para gasolina e E para etanol): ")

qntd = float(input("Quantos litros você abasteceu? "))



if(combustivel == 'G'):
    valor = 5.80 * qntd

else:
     valor = 4.90 * qntd

     print(f"Você gastou {valor: .2f}")