# MATRIZ COMUM 3X3
matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()


# MATRIZ PARES COM TOTAL 3X3 
matriz = [[0,0,0], [0,0,0], [0,0,0]]
totPar = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range(0,3):
    for c in range(0,3):
        if matriz[l][c] % 2 == 0:
            totPar += 1
            print(f'[~{matriz[l][c]:^3}~]', end='')
        else:
            print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'Ao todos foram {totPar} valores PARES.')

# MATRIZ IDENTIDADE DE 3ª ORDEM
mID = [[0,0,0], [0,0,0], [0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        if i == j:
            mID[i][j] = 1
        else:
            mID[i][j] = 0
        
for i in range(0,3):
    for j in range(0,3):
       print(f'[{mID[i][j]:^5}]', end='')
    print()


# PREENCHER MATRIZ DE 4ª ORDEM
sDP = 0
p2L = 1
mai3C = 0
m = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
for i in range(0,4):
    for j in range(0,4):
        m[i][j] = int(input(f'Digite o valor para [{i}, {j}]: '))
        if i == j:
            sDP += m[i][j]

for j in range(0,4):
    p2L = p2L * m[1][j]

for i in range(0,4):
    if m[i][2] > mai3C:
        mai3C = m[i][2]

for i in range(0,4):
    for j in range(0,4):
        print(f'[{m[i][j]:5^}]', end='')
    print()

print(f'A soma da diagonal principal é {sDP}.')
print(f'O produto dos valores da segunda linha é {p2L}.')
print(f'O maior valor da terceira coluna é {mai3C}.')





