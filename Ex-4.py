# Alysson Alcantara
# Eduardo Ferreira

# 4) Desenvolva um software que terá duas threads.
# Uma thread chamada Produtora que sorteia um
# número aleatório e coloca na variável shared.
# Este sorteio acontece em um tempo também aleatório.
# A segunda thread chamada monitor deverá imprimir
# na tela sempre que houver um valor novo em shared.

import threading

class ThreadExec(threading.Thread):
    def __init__(self, nome, function):
        threading.Thread.__init__(self)
        self.nome = nome
        self.function = function

    def run(self):
        print("inicio da execução: ", self.nome)
        self.function()


def produtora():
    import random
    from time import sleep
    sleep(random.randint(1, 10))
    shared = random.randint(1, 100)
    return shared

def monitor():
    print('\n')
    while True:
        print("Monitorando...")
        print("Shared encontrado: ", produtora(), "\n")

def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')        

def main():
    clear()
    t1 = ThreadExec('Produtora', produtora)
    t2 = ThreadExec('Monitor', monitor)
    
    t1.start()
    t2.start()


main()