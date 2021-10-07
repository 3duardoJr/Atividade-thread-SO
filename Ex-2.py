# Alysson Alcantara.
# Eduardo Ferreira.


# 2) Faca um programa que imprima os números
# primos existentes entre 0 e 99999. UTILIZE THREADS.
# Dica: para cada faixa de mil valores crie um
# thread e dispare o processo para cada uma delas.

# observação:
# cada thread fara a soma de uma faixa de valores primos de forma assincrona
# isso implica que não necessariamente esse calculo sera feito em ordem !

import threading


class ThreadExec(threading.Thread):
    def __init__(self, lower, upper, nome):
        threading.Thread.__init__(self)
        self.lower = lower
        self.upper = upper
        self.nome = nome

    def run(self):
        print("inicio da thread ", self.nome, '\n')
        primeWhile(self.lower, self.upper)
        print("fim da thread ", self.nome, '\n')


def primeWhile(lower, upper):
    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)


def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    loop = 9999  # numeros muito grandes podem levar mais tempo para seram calculados

    clear()
    print("Iniciando a soma de matrizes ... \n")
    max = int(loop / 1000)

    if (loop >= 1000):
        k = ThreadExec(0, 1000, '0')
        k.start()

    if (loop < 1000):
        k = ThreadExec(0, loop, '0')
        k.start()

    for i in range(1, max + 1):
        lower = i * 1000
        upper = lower + 1000

        t = ThreadExec(lower, upper, i)
        t.start()


main()