from atletas import *
from lutadores import *

if __name__ == "__main__":
    keller = Triatleta("Fernanda Keller", 40, 55.8)
    print(keller)
    print(keller.realizar_maratona())

    Maeda = MMA("Mitsuyo Maeda")
    Jailton = MMA("Jailton Almeida")
    Maeda.superman_punch(Jailton)
