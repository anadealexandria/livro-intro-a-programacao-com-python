numero1 = int(input("Digite o número 1: "))
numero2 = int(input("Digite o número 2: "))
adição = numero1 + numero2
subtração = numero1 - numero2
multiplicação = numero1 * numero2
divisão = numero1/numero2
escolha_da_operação = str(input("Escolha entre as quatro operações (adição, subtração, multiplicação e divisão): "))

if escolha_da_operação == "adição":
    print("A soma é igual a {}".format(adição))
elif escolha_da_operação == "subtração":
    print("A subtração é igual a {}".format(subtração))
elif escolha_da_operação == "multiplicação":
    print("A multiplicação é igual a {}".format(multiplicação))
else:
    print("A divisão é igual a {}".format(divisão))
