from typing import Deque, Any, Iterator
from collections import deque
from fila_com_deque import Queue
import numpy as np

K = int(input('Tamanho do estacionamento: '))
V = []
while True:
    n = input('Sequência de instantes:[Aperte enter ao terminar] ')
    if n == '':#adicionando no vetor de comandos
        break
    else:
        n = int(n)
        V.append(n)
T = int(input('Instante T:'))
#print(V)
def estado_atual(K, V, T):
    R = Queue(K)#fila de tamanho K
    for i in range(1, K+1):#adicionando zeros na fila
        R.push(0)
    #print(R)
    for i in range(1, T+1):#adicionando a posição do vetor na fila
        if i in V:
            R.push(V.index(i)+1)
        else:
            R.push(0)
        #print(R)

    #print(R)
    P = []
    for i in R: #colocando os elementos em uma fila para invertê-la
        P.append(i)
    P.reverse()
    return P
print(estado_atual(K, V, T))
'''fila = Queue(K)

listav = []
while True: #pegar os instantes que os carros entram
    p = input(f'Entrada: ')
    if p == '':
        break
    p = int(p)
    listav.append(p) #adiciona o instante numa lista

print(listav)
carro = (listav.index(7)+1) #pega o número do carro(1, 2, 3, etc)
print(carro)
V = np.zeros(K)#vetor de zeros

print(V)

T = int(input('Instante: '))
print(T)
'''