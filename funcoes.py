#-------------------- FUNÇÕES ---------------------#

def linha():
    print('-=' * 40)

def mensagem(msg):
    print('-=' * 40)
    print(msg)
    print('-=' * 40)

def soma(a, b):
    s = a + b
    print(f'A soma de {a} e {b} é igual à: {s}')

def contador(*num):
    tam = len(num)
    for valor in num:
        print(f'Vocês escolheu: {valor}.', end=' ')
    print(f'Recebi os valores {num} e são ao todo {tam} números.')
    print()
    
def dobra(lst):
    pos = 0
    while pos<len(lst):
        lst[pos] *= 2
    pos += 1

print() # para pular uma linha da aba do terminal

mensagem('EU AMO MUITO A SUZANA, AF')
mensagem('FUCK BOLSONARO.')
mensagem(' C Y B E R P U N K ')

print() 

soma(1,2)
soma(3,6)
soma(823,1)

print( )

contador(1,2)
contador(2,4,8)
contador(3,6,9)
user = int(input('Digite valores: '))
contador(user)


print()

valores = [6,3,9,1,0,2]
print(f'Os valores são {valores}.')
linha()
dobra(valores)
print(f'Os valores dobrados são {valores}.')

