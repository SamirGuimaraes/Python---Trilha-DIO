class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {", ".join([f"{chave}= {valor}" for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        super().__init__(**kw)
        self.cor_pelo = cor_pelo



class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico

class Gato(Mamifero):
    pass

class Onintorrinco(Mamifero, Ave):
    pass 

gato = Gato(nro_patas=4, cor_pelo="Laranja")
print(gato)

onintorrinco = Onintorrinco(nro_patas=4, cor_pelo="Marrom", cor_bico="Branca")
print(onintorrinco)