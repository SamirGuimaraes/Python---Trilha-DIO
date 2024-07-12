"""
Este código é um exemplo de um sistema bancário mais elaborado e totalmente modularizado em Python. Ele permite que usuários depositem e saquem dinheiro, exibam o extrato, criem novas contas, listem contas existentes e criem novos usuários. Aqui está uma explicação detalhada do que cada parte do código faz:

1. Menu de Opções
A função menu exibe um menu de opções para o usuário e retorna a opção escolhida. O menu inclui opções para depositar, sacar, exibir o extrato, criar uma nova conta, listar contas, criar um novo usuário e sair do programa.

2. Funções de Operações Bancárias
Depositar (depositar):
Esta função recebe o saldo atual, o valor do depósito e o extrato. Se o valor for maior que zero, ele é adicionado ao saldo e a transação é registrada no extrato.

Sacar (sacar):
Esta função recebe o saldo atual, o valor do saque, o extrato, o limite de saque, o número de saques realizados e o limite de saques diários. Ela verifica se o valor do saque excede o saldo, o limite ou o número de saques permitidos. Se todas as condições forem satisfeitas, o valor é subtraído do saldo, o número de saques é incrementado e a transação é registrada no extrato.

Exibir Extrato (exibir_extrato):
Esta função imprime o extrato de transações e o saldo atual. Se não houver transações, uma mensagem indicando que não foram realizadas movimentações é exibida.

3. Funções de Gestão de Usuários e Contas
Criar Usuário (criar_usuario):
Esta função permite criar um novo usuário. O usuário é identificado por um CPF único. Se um usuário com o mesmo CPF já existir, uma mensagem de erro é exibida. Caso contrário, o novo usuário é adicionado à lista de usuários.

Filtrar Usuário (filtrar_usuario):
Esta função procura um usuário na lista de usuários pelo CPF. Se encontrado, o usuário é retornado, caso contrário, retorna None.

Criar Conta (criar_conta):
Esta função permite criar uma nova conta associada a um usuário existente. Ela recebe a agência, o número da conta e a lista de usuários. Se o CPF do usuário for encontrado na lista, uma nova conta é criada e retornada. Caso contrário, uma mensagem de erro é exibida.

Listar Contas (listar_contas):
Esta função exibe uma lista de todas as contas criadas, incluindo a agência, número da conta e nome do titular.

4. Função Principal (main)
A função main inicializa variáveis importantes como o saldo, limite de saque, extrato, número de saques, lista de usuários e lista de contas. Ela entra em um loop infinito onde exibe o menu e realiza a operação escolhida pelo usuário. Dependendo da opção selecionada, a função correspondente é chamada. O loop continua até que o usuário escolha a opção de sair.
"""

import textwrap

def menu():
    menu = """\n
    ====== MENU ======
    [d]\tDepositar 
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [x]\tSair
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor 
        extrato + f"Depósito de R${valor}, saldo atual de R${saldo}"
        print("Depósito realizado com sucesso.")
    else:
        print("Insira um valor maior que zero para realizar o depósito.")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print("\nValor de saque maior que saldo disponível.")
    elif excedeu_limite:
        print("\nValor de saque maior que limite permitido por vez.")
    elif excedeu_saques:
        print("\nNúmero de saques diários ultrapassado.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque de R${valor}, saldo atual de R${saldo}"
        numero_saques += 1
        print("\nSaque realizado com sucesso.")
    else:
        print("Erro no saque, tente realizar a operação novamente.")
    
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n========== EXTRATO ===========")
    print("Não foram realizadass movimentações." if not extrato else extrato)
    print(f"Saldo:\t\tR${saldo:.2f}")
    print("================================")


def criar_usuario(usuarios):
    cpf = input("Digite seu CPF (apenas número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario: 
        print("Um usuário já existe com esse CPF.")
        return 
    
    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Digite sua data de nascimento Ex- 14.02.2005")
    endereco = input("Digite seu endereço (logradouro, numero - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso.")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso.")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\nO usuário não foi encontrado, texte criar uma conta de um usuário já cadastrado")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Quanto deseja depositar: "))
            
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Quando deseja sacar: "))

            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato = extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, selecione novamente a operação que deseja realizar.")


main ()




