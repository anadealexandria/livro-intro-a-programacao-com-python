kWh = int(input("Qual o kWh gasto? "))
instalação = str(input("Qual o tipo de instalação: Residência (R), Comercial (C) ou Industrial (I)? "))

if instalação == "R":
    if kWh <= 500:
        total_a_pagar = kWh * 0.40        
    else:
        total_a_pagar = kWh * 0.65
elif instalação == "C":
    if kWh <= 1000:
        total_a_pagar = kWh * 0.55
    else:
        total_a_pagar = kWh * 0.60
elif instalação == "I":
    if kWh <= 5000:
        total_a_pagar = kWh * 0.55
    else:
        total_a_pagar = kWh * 0.60
else:
    print("Tipo de instalação inválida!")
    total_a_pagar = "inválido"

print("O total a pagar é: {}".format(total_a_pagar))