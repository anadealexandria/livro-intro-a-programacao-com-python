distância = int(input("Qual a distância que deseja percorrer? "))

if distância <= 200:
    preco = distância * 0.50
else:
    preco = distância * 0.45
print("O preço é de {}".format(preco))
