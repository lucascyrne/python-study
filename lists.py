#-=-=-=-=-=-= LISTAS =-=-=-=-=-=-=-=-#
def linha():
    print('-=' * 30)

print()
linha()
num = ['1', '2', '3', '4', '5']
print('Lista Original: ', num)
linha()

print()
num.append('6')
print('Adicionando elemento "6" ao final da lista: ', num)


print()
num.insert(7,'7')
print('Inserindo "7" na sétima casa: ', num)

print()
del num[2]
print('Deletando o elemento do index "2": ', num)

print()
num.pop()
print('Deletando o ultimo elemento: ', num)

print()
num.remove('5')
print('Removendo o número "5" da lista: ', num)

print()
num.insert(2, 3)
num.insert(4, 5)
print('Reinserindo elementos e voltando a lista original: ', num)
print()

for pos, valor in enumerate(num):
    print(f'Na posição {pos} encontrei o valor {valor}.')
print('Cheguei ao fim.')