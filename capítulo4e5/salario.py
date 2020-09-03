salário = float(input("Digite o salário: "))

if salário <= 1250:
    aumento = salário * 0.15
else:
    aumento = salário * 0.10    
print("O aumento foi de {}".format(aumento))