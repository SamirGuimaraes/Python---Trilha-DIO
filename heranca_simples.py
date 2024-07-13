class veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa 
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {", ".join([f"{chave}= {valor}" for chave, valor in self.__dict__.items()])}"

    
class Motocicleta(veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado


    def estar_carragado(self):
        print(f"{"Sim," if self.carregado else "Não"} está carregado")

class Carro(veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado


    def estar_carragado(self):
        print(f"{"Sim," if self.carregado else "Não"} está carregado")

class Caminhao(veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado


    def estar_carragado(self):
        print(f"{"Sim," if self.carregado else "Não"} está carregado")


moto = Motocicleta("Preta", "rdc-1386", 2, True)

carro = Carro("Amarelo", "frg-8745", 4, False)

caminhao = Caminhao("Cinza", "ghi-9067", 8, True)

print(moto)
print(carro)
print(caminhao)