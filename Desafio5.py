"""
Agora, vamos Adicionar uma funcionalidade à classe 
UsuarioTelefone para que possa ser verificado o saldo 
disponível em seu plano. Para essa solução, você pode 
criar uma classe PlanoTelefone, o seu método de 
inicialização e encapsular os atributos, 'nome' e 'saldo' 
dentro da classe. Adicione também um método 'verificar_saldo' 
para verificar o saldo do plano e uma  'mensagem_personalizada' 
para gerar uma mensagem personalizada.

Condições da verificação do saldo:
- Caso o saldo seja menor do que 10, retorne: "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
- Caso o saldo seja maior ou igual a 50, retorne: "Parabéns! Continue aproveitando seu plano sem preocupações."
- Caso contrário, retorne: "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

Entrada
Como entrada, será solicitado o nome, plano (Essencial, Prata, Premium) e saldo atual do cliente.

Saída
Mensagem personalizada de acordo o saldo do cliente.
"""

class PlanoTelefone:
    def __init__(self, nome, saldo):
        self.__nome = nome
        self.__saldo = saldo

    def verificar_saldo(self):
        return self.__saldo

    def mensagem_personalizada(self):
        if self.__saldo <= 10:
            return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif 10 < self.__saldo <= 20:
            return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."
        else:
            return "Parabéns! Continue aproveitando seu plano sem preocupações."


class UsuarioTelefone:
    def __init__(self, nome, plano):
        self.nome = nome
        self.plano = plano

    def verificar_saldo(self):
        mensagem_usuario = self.plano.mensagem_personalizada()
        return mensagem_usuario


nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())

plano_usuario = PlanoTelefone(nome_plano, saldo_inicial) 
usuario = UsuarioTelefone(nome_usuario, plano_usuario)  

mensagem_usuario = usuario.verificar_saldo()  
print(mensagem_usuario)