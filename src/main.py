from frota import *


def operar_carro(carro):
    try:
        print('1- Ligar motor')
        print('2- Desligar motor')
        print('3- Acelerar')

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


if __name__ == "__main__":
    print('Cadastre um carro')
    nm_modelo1 = input('Digite o modelo para carro 1: ')
    nm_marca1 = input('Digite a marca para carro 1: ')
    nm_cor1 = input('Digite a cor para carro 1: ')
    nm_modelo2 = input('Digite o modelo para carro 2: ')
    nm_marca2 = input('Digite a marca para carro 2: ')
    nm_cor2 = input('Digite a cor para carro 2: ')

    carro1 = Carro(nm_modelo1, nm_marca1, nm_cor1, 0, False)
    carro2 = Carro(nm_modelo2, nm_marca2, nm_cor2, 0, False)

    '''
    Controlando os carros até ele atingir 600 Km
    '''
    while carro1.odometro < 600 or carro2.odometro < 600:
        try:
            print('Escolhe o carro para controlar:')
            print('1- Carro 1')
            print('2- Carro 2')

            op = 0
            while op not in (1,2):
                op = int(input("Digite as opcoes[1-2]: "))

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

    if carro1.odometro >= 600:
        print("Carro 1 foi o primeiro a atingir 600 kilometros")
    if carro2.odometro >= 600:
        print("Carro 2 foi o primeiro a atingir 600 kilometros")