# Depositar valor positivo na conta bancária.
# Precisa conter os valores de depósitos e saque
# 3 saques por dia sendo que o valor maximo por saque deve ser até 500 reais. 
# Armazenar os valores de saque e depósito para extrato.
# Não pode sacar se o valor de saldo for menor que o valor do saque.

operacoes = """

[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Sair
"""

valor_conta = 0.0
extrato_deposito = ''
num_saques = 0
while True:
    escolha = input(operacoes)
    if escolha == '1':
       valor_Deposito = float(input("Entre com o valor que deseja depoditar "))
       if valor_Deposito >= 0.01:
        deposito_moeda = "R$ {:,.2f}".format(valor_Deposito)
        extrato_deposito += 'deposito realizado de: '
        extrato_deposito +=  f'{deposito_moeda} \n'
        print(f"Deposito de {deposito_moeda} realizado com sucesso.")
        valor_conta += valor_Deposito
       else:
        print("Valor de deposito precisa ser maior que 0.01")  

    elif escolha == '2':
        while num_saques < 3:
            valor_saque = float(input("Entre com o valor que deseja sacar: "))
            if valor_saque >= 0.01 and valor_saque <= 500 and valor_saque <= valor_conta:
                saque_moeda = "R$ {:,.2f}".format(valor_saque)
                extrato_deposito += "Saque realizado de: "
                extrato_deposito += f"{saque_moeda} \n"
                print(f"Saque de {saque_moeda} realizado com sucesso.")
                valor_conta -= valor_saque
                num_saques += 1
            else:
                print("Saque inválido.")
        
        print("Seu número de saques diários foi atingido tente outro dia.")
    elif escolha == '3':
       print(f"{extrato_deposito}")
       saldo_conta = "R$ {:,.2f}".format(valor_conta)
       print(f"Seu saldo em conta é de: {saldo_conta}")

    elif escolha == '4':
       break
    else:
       print("Opção invalida")
