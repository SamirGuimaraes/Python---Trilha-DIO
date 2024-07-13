import textwrap

def mostrar_menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar_valor(saldo_atual, valor_deposito, extrato_atual, /):
    if valor_deposito > 0:
        saldo_atual += valor_deposito
        extrato_atual += f"Depósito:\tR$ {valor_deposito:.2f}\n"
        print("\nDepósito realizado com sucesso!")
    else:
        print("\nOperação falhou! O valor informado é inválido.")

    return saldo_atual, extrato_atual

def realizar_saque(*, saldo_atual, valor_saque, extrato_atual, limite_saque, saques_realizados, max_saques):
    saldo_insuficiente = valor_saque > saldo_atual
    acima_do_limite = valor_saque > limite_saque
    saques_excedidos = saques_realizados >= max_saques

    if saldo_insuficiente:
        print("\nOperação falhou! Saldo insuficiente.")
    elif acima_do_limite:
        print("\nOperação falhou! Valor do saque acima do limite.")
    elif saques_excedidos:
        print("\nOperação falhou! Número máximo de saques excedido.")
    elif valor_saque > 0:
        saldo_atual -= valor_saque
        extrato_atual += f"Saque:\t\tR$ {valor_saque:.2f}\n"
        saques_realizados += 1
        print("\nSaque realizado com sucesso!")
    else:
        print("\nOperação falhou! O valor informado é inválido.")

    return saldo_atual, extrato_atual

def exibir_extrato(saldo_atual, /, *, extrato_atual):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato_atual else extrato_atual)
    print(f"\nSaldo:\t\tR$ {saldo_atual:.2f}")
    print("==========================================")

def criar_novo_usuario(lista_usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario_existente = encontrar_usuario(cpf, lista_usuarios)

    if usuario_existente:
        print("\nJá existe um usuário com esse CPF!")
        return

    nome_completo = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco_completo = input("Informe o endereço (logradouro, número - bairro - cidade/estado): ")

    lista_usuarios.append({"nome": nome_completo, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco_completo})
    print("Usuário criado com sucesso!")

def encontrar_usuario(cpf, lista_usuarios):
    usuarios_encontrados = [usuario for usuario in lista_usuarios if usuario["cpf"] == cpf]
    return usuarios_encontrados[0] if usuarios_encontrados else None

def criar_nova_conta(agencia_banco, num_conta, lista_usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario_encontrado = encontrar_usuario(cpf, lista_usuarios)

    if usuario_encontrado:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia_banco, "numero_conta": num_conta, "usuario": usuario_encontrado}

    print("\nUsuário não encontrado, criação de conta cancelada!")

def listar_todas_contas(lista_contas):
    for conta in lista_contas:
        detalhes_conta = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(detalhes_conta))

def main():
    MAX_SAQUES = 3
    AGENCIA_PADRAO = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    saques_realizados = 0
    usuarios = []
    contas = []

    while True:
        opcao = mostrar_menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar_valor(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = realizar_saque(
                saldo_atual=saldo,
                valor_saque=valor,
                extrato_atual=extrato,
                limite_saque=limite,
                saques_realizados=saques_realizados,
                max_saques=MAX_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato_atual=extrato)

        elif opcao == "nu":
            criar_novo_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_nova_conta(AGENCIA_PADRAO, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_todas_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
