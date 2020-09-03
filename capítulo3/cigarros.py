cigarrosFumados = int(input("Quantos cigarros são fumados por dia? "))
quantAnosFumando = int(input("Fumou durante quantos anos? "))

totalCigarrosFumados = (cigarrosFumados * 10/60)/24 
totalDeDias = quantAnosFumando * 365

total = totalCigarrosFumados * totalDeDias

print("O total de dias perdidos será de {}".format(total))