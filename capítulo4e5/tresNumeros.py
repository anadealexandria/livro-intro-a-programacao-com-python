numero1 = int(input("Digite o número 1: "))
numero2 = int(input("Digite o número 2: "))
numero3 = int(input("Digite o número 3: "))

maior = numero1
if numero2 > maior:
    maior = numero2
if numero3 > maior:
    maior = numero3  
print("O maior número é {}".format(maior))

menor = numero1
if numero2 < menor:
    menor = numero2
if numero3 < menor:
    menor = numero3
print("O menor número é {}".format(menor))