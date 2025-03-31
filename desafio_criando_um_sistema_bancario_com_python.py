menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
extrato = ""
numero_saques = 0
VALOR_LIMITE_SAQUE = 500
QUANTIDADE_LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    elif opcao == "s":
        print("Saque")
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > VALOR_LIMITE_SAQUE
        excedeu_saques = numero_saques >= QUANTIDADE_LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente.")
        elif excedeu_limite:
            print("Valor do saque excede o limite.")
        elif excedeu_saques:
            print("Número máximo de saques diários atingido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para saque.")

    elif opcao == "e":
        print("Extrato")

        if not extrato:
            print("Nenhuma movimentação realizada.")
        else:
            print(extrato)
        print(f"Saldo: R$ {saldo:.2f}")

    elif opcao == "q":
        print("Saindo...")
        break

    else:
        print("Opção inválida. Tente novamente.")