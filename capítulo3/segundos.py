dias = int(input("Digite a quantidade em dias: "))
horas = int(input("Digite a quantidade em horas: "))
minutos = int(input("Digite a quantidade em minutos: "))
segundos = int(input("Digite a quantidade em segundos: "))

total = (dias * 24) * 3600 + horas * 3600 + minutos * 60 + segundos

print(total)