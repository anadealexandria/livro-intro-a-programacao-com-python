salário = float(input("Digite o seu salário: "))
base = salário
imposto = 0

if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)
print(f"O salário é {salário:5.2f} e o imposto a pagar é de {imposto:5.2f}.")