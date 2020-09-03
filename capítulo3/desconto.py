valorDaMercadoria = float(input("Qual o valor da mercadoria?"))
percentualDeDesconto = int(input("Qual o percentual de desconto?"))

valorDeDesconto = valorDaMercadoria * percentualDeDesconto/100

precoApagar = valorDaMercadoria - valorDeDesconto

print(valorDeDesconto)
print(precoApagar)