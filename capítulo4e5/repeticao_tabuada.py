n = int(input("Digite um número para a tabuada: "))
x = 1
while x <= 10:
    resultado = x * n
    print("{} X {} = {}".format(x, n, resultado))
    x = x + 1