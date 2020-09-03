velocidade = int(input("Digite a velocidade do seu carro: "))

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print("Você pagará {} de multa.".format(multa))
if velocidade <= 80:
    print("Você não pagará multa!")