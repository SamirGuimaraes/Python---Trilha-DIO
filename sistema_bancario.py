saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = str(input("Digite a opção que deseja realizar \n[d] Depositar \n[s] Sacar \n[e] Extrato \n[x] Sair \n"))


    if opcao == "d":
        valor = int(input("Qual o valor que deseja depositar: "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito de R${valor} concluido com sucesso \nSeu saldo atual é de R${saldo}.\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES:
            print("Número de saques diários atingidos.")
        else:
            valor = int(input("Qual valor deseja sacar: "))
            if valor > limite:
                print("Limite maiores que R$500,00 não são permitidos")
            elif valor > saldo:
                print("Saque requerido maior que o saldo na conta.")
            else:
                saldo -= valor
                numero_saques += 1
                extrato += f"Com um saque de R${valor} o seu saldo atual é de R${saldo}.\n"

    elif opcao == "e":
        if extrato == "":
            print("Não foram realizados transações bancárias.")
        else:
            print("-" * 5 + "EXTRATO" + "-" * 5)
            print(extrato)
            print("-"*17)
    
    elif opcao == "x":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação.")



