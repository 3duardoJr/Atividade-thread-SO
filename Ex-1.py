# Alysson Alcantara.
# Eduardo Ferreira.

# 1 ) Escreva um programa que realize o cálculo das
# somas dos valores das linhas de uma matriz
# qualquer de números inteiros e imprima o resultado na tela.
# Faça com que o cálculo do somatório de
# cada linha seja realizado em paralelo por uma thread.

import threading


def sumInThread(response, i, j, A, B):
    response[i][j] = A[i][j] + B[i][j]
    print('Calculando linha', j, '\nResposta: ', response, '\n\n')


def somar(A, B):
    response = []
    nLineA, nLineB = len(A), len(B)
    nColA, nColB = len(A[0]), len(B[0])

    if (nLineA == nLineB) and (nColA == nColB):
        for i in range(nLineA):
            line = [0] * nColA
            response.append(line)
            for j in range(nColA):
                threading.Thread(target=sumInThread, args=(
                    response, i, j, A, B)).start()

    else:
        print("Matrizes não tem a mesma ordem")

    return response


def main():
    matriz_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matriz_2 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

    somar(matriz_1, matriz_2)


main()