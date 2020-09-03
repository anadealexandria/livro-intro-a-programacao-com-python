n = int(input("Digite um número para a tabuada: "))
início = int(input("Digite o número inicial para a contagem: "))
fim = int(input("Digite o número final para a contagem: "))
while início <= fim:
    resultado = início * n
    print("{} X {} = {}".format(início, n, resultado))
    início = início + 1
