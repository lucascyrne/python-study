#------------- t u p l a s -------------#

lanche = 'hamburguer', 'suco', 'pizza', 'pudim', 'batata frita' # As Tuplas são imutáveis

print()

for comida in lanche:
    print(f'Eu vou comer {comida}')
print()

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print()

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print()

print('Comi pra caramba.')
print()

print('organizado: ', sorted(lanche))
print()

a = (2,5,4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(f'O tamanho é de {len(c)}')
print(f'Aparecem {c.count(5)} vezes o número "5"')
print(f'Em que posição está o ultimo 5: {c.index(5, 1)}')

