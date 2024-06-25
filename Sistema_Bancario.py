
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))
        
        if valor > 0:
         saldo += valor
         extrato += f"Deposito: R$ {valor:.2f}\n"

        else:
            print("operaçao falhou! o valor informado e invalido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITES_SAQUES

        if excedeu_saldo:
            print("operaçao falhou! voce nao tem saldo suficiente.")
        
        elif excedeu_limite:
            print("operaçao falhou! o valor do saques excede o limite pra hoje.")

        elif excedeu_saques:
            print("Operaçao falhou! numero maximo de saques exedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operaçao falhou! o valor informado e invalido.")

    elif opcao == "e":
        print("\n*********** EXTRATO ************")
        print("nao foram realizados movimentaçoes." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("**********************************")


    elif opcao == "q":
        break

    else:
        print("operaçao invalida, por favor selecione novamente a operacao desejada.")
        