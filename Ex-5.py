# Alysson Alcantara
# Eduardo Ferreira

# 5) Crie um software que terá duas threads.
# Uma thread Produtora que sorteia um numero e coloque
# este número no topo da pilha shared. Este sorteio deverá acontecer
# em um tempo aleatório.
# A segunda thread chamada de consumidor deverá remover o item do topo de pilha e imprimir na tela.
# Para evitar inconsistências no programa e possíveis travamentos as duas threads
# não podem acessar a pilha shared ao mesmo tempo.

import threading
sem = threading.Semaphore() # Implementação do semaforo 

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def produtora(shared):
    import random
    from time import sleep

    while True:
        randomTime = random.randint(1, 5)
        sleep(randomTime)

        sem.acquire()
        shared.push(random.randint(0, 100))

        print('adicionando item', shared.items[-1], '\n')

        sem.release()


def consumidora(shared):
    import random
    from time import sleep

    while True:
        randomTime = random.randint(1, 5)
        sleep(randomTime)

        if (shared.size() == 0):
            print('Pilha vazia \n')

        else:
            sem.acquire()
            print('Removendo item', shared.pop(), '\n')
            sem.release()
            print("| Tamanho atual da pilha", shared.size(), '\n')


def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    clear()
    shared = Stack()

    t1 = threading.Thread(target=produtora, args=(shared,))
    t2 = threading.Thread(target=consumidora, args=(shared,))

    t2.start()
    t1.start()


main()