salario = float(input("Qual o valor do salário? "))
PorcentagemDoAumento = int(input("Qual a porcentagem do aumento salarial?"))

aumento = salario * PorcentagemDoAumento/100

novoSalario = salario + aumento

print("O valor do aumento é de {} e o valor do novo salário é de {}".format(aumento ,novoSalario))
