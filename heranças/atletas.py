from abc import ABC


class Atleta(ABC):
    nome: str
    idade: int
    peso: float

    def __init__(self, n, i, p):
        self.nome = n
        self.idade = i
        self.peso = p

    def __str__(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}\nPeso: {self.peso}\n"

    def aquecer(self):
        return f"{self.nome} se aqueçeu!\n"


class Corredor(Atleta):
    def correr(self):
        return f"{self.nome} correu!\n"


class Nadador(Atleta):
    def nadar(self):
        return f"{self.nome} nadou!\n"


class Ciclista(Atleta):
    def pedalar(self):
        return f"{self.nome} pedalou!\n"


class Triatleta(Corredor, Nadador, Ciclista):
    def realizar_maratona(self):
        info = self.aquecer()
        info += self.correr()
        info += self.nadar()
        info += self.pedalar()
        return info
