from frota import *


def operar_carro(carro):
    try:
        print("1- Ligar motor")
        print("2- Desligar motor")
        print("3- Acelerar")

        op = 0
        while op not in (1, 2, 3):
            op = int(input("Digite as opcoes[1-3]: "))

        if op == 1:
            carro.ligar()
        elif op == 2:
            carro.desligar()
        elif op == 3:
            v = float(input("Informe a velocidade: "))
            t = float(input("Informe o tempo: "))
            carro.acelerar(v, t)

        print('Infos atuais do carro')
        print(carro)
    except Exception as e:
        print("Erro!")
        print(e)


def intro():
    modelo = input("Digite o modelo do carro: ")
    marca = input("Digite a marca do carro: ")
    cor = input("Digite a cor do carro: ")
    consumo = float(input("Consumo médio em km/l: "))
    litros = float(input("Nivel do tanque em litros: "))
    carro = Carro(modelo, marca, cor, 0, False, litros, consumo)
    return carro


if __name__ == "__main__":
    print("Cadastre um carro")

    print("--Carro 1--")
    carro1 = intro()
    # intro(carro1)
    print("--Carro 2--")
    carro2 = intro()
    # intro(carro2)

    '''
    Controlando os carros até ele atingir 600 Km
    '''
    while (carro1.odometro < 600 and carro2.odometro < 600) and (carro1.tanque > 0 or carro2.tanque > 0):
        try:
            print('Escolhe o carro para controlar:')
            print('1- Carro 1')
            print('2- Carro 2')

            op = 0
            while op not in (1, 2):
                op = int(input("Digite as opçoes[1-2]: "))

            if op == 1:
                operar_carro(carro1)
            elif op == 2:
                operar_carro(carro2)
        except Exception as e:
            print("Erro!")
            print(e)

    carro1.desligar()
    carro2.desligar()

    print(carro1)
    print(carro2)

    if carro1.odometro > carro2.odometro:
        print("Carro 1 ganhou!")
    else:
        print("Carro 2 ganhou!")
