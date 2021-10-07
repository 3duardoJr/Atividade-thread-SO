# Alysson Alcantara.
# Eduardo Ferreira.

# 3) 
# Faça um programa que apresente o menu abaixo. Ao selecionar a
# opção numero 2, o programa deve executar um função
# “chamada_bloqueante” que espera tempo aleatório
# entre 1 a 30 segundos e voltar imediatamente
# o menu principal. Isto é, o programa deve
# continuar responsivo mesmo quando a função esteja sendo executada.
# Caso, o usuário selecione novamente a opção numero 2 e a
# função “chamada_bloqueante” já esteja sendo executada
# o software deverá avisar o usuário que não poderá executar
# mais de uma instancia da função “chamada_bloqueante”
# concorrentemente.

# programa chamada bloqueante
# ---------------------------
# 1) sair
# 2) chamda bloqueante

import threading


class ThreadExec(threading.Thread):
    def __init__(self, running, nome):
        threading.Thread.__init__(self)
        self.nome = nome
        self.running = running

    def run(self):
        self.running = True
        print("inicio da execução: ", self.nome, '\n')
        chamada_bloqueante(self.running)
        print("fim da execução: ", self.nome, '\n')


def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    print("programa chamada bloqueante")
    print("-" * 30)
    print("1) sair")
    print("2) chamada bloqueante\n")


def chamada_bloqueante(running):
    import time
    import random

    if running == True:
        time.sleep(random.randint(1, 30))
        print("\nchamada bloqueante executada")
    else:
        print("chamada bloqueante em execução")



def main():
    running = False
    option = 0
    clear()
    menu()
    while True:
        option = int(input("\nopção: "))
        if (option == 1):
            if (running):
                print("\nchamada bloqueante em execução")
                print("Você precisa aguardar o fim da execução da chamada para sair")
            else:
                break
        elif (option == 2):
            if (running == False and option == 2):
                running = True
                t = ThreadExec(running, 'thread 0')
                t.start()
            else:
                print("\njá está sendo executada em uma thread")
        else:
            print("\nopção inválida")


main()