#-------- MATRIZ ---------#


#"""
matriz = []

m = int(input("Digite o número de linhas da matriz: "))
n = int(input("Digite o número de colunas da matriz: "))

def constróiMatriz(m, n, matriz):
    for i in range(1, m+1):
        linha = [] 
        for j in range(1, n+1):
            x = int(input("Digite o elemento %i%i da matriz: "%(i,j)))
            linha.append(x)
        
        matriz.append(linha)

def TrocaElemento(pos1, pos2, matriz):
    elemento1 = matriz[pos1//10][pos1%10]
    elemento2 = matriz[pos2//10][pos2%10]
    matriz[pos1//10][pos1%10] = elemento2
    matriz[pos2//10][pos2%10] = elemento1


constróiMatriz(m, n, matriz)
print(matriz)
pos1 = int(input("Digite a posição do elemento 1: "))
pos2 = int(input("Digite a posição do elemento 2: "))
TrocaElemento(pos1, pos2, matriz)
print(matriz)
"""

import random 

matriz = []

def geraMatriz(matriz):
    lista = list(range(16))
    for j in range(4):
        linha = []
        for i in range(4):
            x = random.choice(lista)
            linha.append(x)
            lista.remove(x)
        matriz.append(linha)

for i in range(3):
    matriz = []
    geraMatriz(matriz)
    print(matriz)