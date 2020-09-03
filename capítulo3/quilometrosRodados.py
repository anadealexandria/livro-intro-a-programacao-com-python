kmRodados = int(input("Quantos km o carro percorreu? "))
diasAlugados = int(input("Durante quantos dias o carro foi alugado? "))

preçoApagar = kmRodados * 0.15 + diasAlugados * 60

print("O preço a pagar pelo aluguel do carro é de {}".format(preçoApagar))