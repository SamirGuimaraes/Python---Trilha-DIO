"""
Vamos agora, adicionar uma funcionalidade à classe UsuarioTelefone, 
que realizar chamadas para outros usuários. Cada chamada terá uma duração
em minutos e o custo será deduzido do saldo do usuário, suponha o custo
de $0.10 por minuto. Você pode criar um método fazer_chamada que vai 
permitir que o usuário faça a chamada, ele vai receber o destinatario 
e duracao como parâmetros. Calcule o custo da chamada usando o método 
'custo_chamada' do objeto 'plano', além de adicionar o método deduzir_saldo 
para deduzir o valor do saldo do plano e depois retorne uma mensagem 
adequada como mostra no exemplo a baixo.

Entrada
Número do usuário, número do telefone, saldo inicial, número do destinatário e a duração da chamada em minutos.

Saída
Mensagem indicando o sucesso da chamada ou saldo insuficiente para fazer a chamada.
"""

class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano

    def fazer_chamada(self, destinatario, duracao):
        custo_chamada = self.plano.custo_chamada(duracao)
        if self.plano.verificar_saldo() >= custo_chamada:
            self.plano.deduzir_saldo(custo_chamada)
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${self.plano.verificar_saldo():.2f}"
        else:
            return "Saldo insuficiente para fazer a chamada."


class Plano:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def verificar_saldo(self):
        return self.saldo

    def custo_chamada(self, duracao):
        return duracao * 0.10

    def deduzir_saldo(self, valor):
        self.saldo -= valor


class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))


nome = input()
numero = input()
saldo_inicial = float(input())

usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = input()
duracao = int(input())

print(usuario_pre_pago.fazer_chamada(destinatario, duracao))