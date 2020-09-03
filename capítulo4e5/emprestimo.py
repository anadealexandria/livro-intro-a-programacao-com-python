valor_da_casa = float(input("Digite o valor da casa a ser comprada: "))
salário = float(input("Qual o valor do seu salário? "))
quant_de_anos = int(input("Qual a quantidade de anos a pagar? "))

valor_mensal_a_pagar = valor_da_casa/(quant_de_anos * 12)
porcentagem_salario = salário * 0.30

if valor_mensal_a_pagar <= porcentagem_salario:
    print(f"A prestação a ser paga é de {valor_mensal_a_pagar:5.2f}")    
else:
    print("O empréstimo não pode ser concedido.")