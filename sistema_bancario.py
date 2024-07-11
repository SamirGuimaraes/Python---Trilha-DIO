"""
Este código implementa um sistema simples de operações bancárias em Python. Ele permite que o usuário realize depósitos, saques, visualize o extrato das transações realizadas e saia do programa.

O usuário interage com o sistema por meio de um menu que oferece quatro opções: Depositar (d), Sacar (s), Extrato (e) e Sair (x).
O saldo inicial da conta é definido como zero, e há um limite máximo de saque de R$500,00 por transação e um limite diário de três saques.
Quando o usuário escolhe depositar, ele é solicitado a inserir um valor que, se válido, é adicionado ao saldo da conta e registrado no extrato.
Para sacar, o usuário deve inserir um valor que não exceda o saldo da conta, o limite de saque ou o número máximo de saques diários permitidos. Se todas as condições forem satisfeitas, o valor é subtraído do saldo e registrado no extrato.

A opção de extrato permite que o usuário veja um histórico de todas as transações realizadas.
A opção de sair encerra o programa.

Esse código fornece uma interface básica para gerenciar transações financeiras de maneira interativa.
"""
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



