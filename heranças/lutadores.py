from abc import ABC


class Lutador(ABC):
    nome: str
    energia = 100.0

    def __init__(self, n):
        self.nome = n

    def __str__(self):
        return f"Nome: {self.nome}\nEnergia: {self.energia}"

    def soco(self, oponente):
        oponente.energia -= 5.5
        print(f"{self.nome} usou Soco contra {oponente.nome}\n{oponente.nome} tem {oponente.energia} restando!")


class Boxeador(Lutador):
    def cruzado(self, oponente: Lutador):
        oponente.energia -= 10.2

    def gancho(self, oponente: Lutador):
        oponente.energia -= 20.8
        print(f"{self.nome} usou Gancho contra {oponente.nome}\n{oponente.nome} tem {oponente.energia} restando!")


class MuayThai(Boxeador):
    def chute_alto(self, oponente: Lutador):
        oponente.energia -= 15.4
        print(f"{self.nome} usou Chute Alto contra {oponente.nome}\n{oponente.nome} tem {oponente.energia} restando!")


class JiuJitsu(Lutador):
    def chave_braco(self, oponente: Lutador):
        oponente.energia -= 100
        print(f"{self.nome} usou chave de braço contra {oponente.nome}\n{oponente.nome} tem {oponente.energia} restando!")


class MMA(MuayThai, JiuJitsu):

    def superman_punch(self, oponente: Lutador):
        oponente.energia -= 53.2
        print(f"{self.nome} usou Superman Punch contra {oponente.nome}\n{oponente.nome} tem {oponente.energia} restando!")
