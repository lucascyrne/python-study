#----------- CURSO #009 - MANIPULATING TEXT --------------#

def linha():
    print('-=' * 40)

def j():
    print()


frase = "Curso em Vídeo Python"
linha()

print(frase)
linha()
print('retorna 10º espaço: ', frase[9])
print('retorna entre 9º espaço e 12º: ', frase[9:13])
print('retorna entre 9º espaço e 21º, pulando de 2 em 2 espaços: ', frase[9:21:2])
print('retorna 9º espaço até o fim, pulando de 3 em 3 espaços: ', frase[9::3])

print()
print('quantos espaços possuem a frase: ', len(frase))
print('quantas letras "o" existem na frase: ', frase.count('o'))
print('quantas letras "o" existem na frase de seu início até a 12º letra: ', frase.count('o',0,13))
print('verifica se existe "deo" dentro de frase: ', frase.find('deo'))
print('verifica se existe "Android" dentro de frase: ', frase.find('Android'))
print("verifica se há Curso em frase: ", 'Curso' in frase)
print('troca de lugar "Python" por "Android": ', frase.replace('Python','Android'))
print('torna maiúscula todas as letras: ', frase.upper())
print('torna minúscula todas as letras: ', frase.lower())
print('torna maiúscula a primeira letra da frase: ', frase.capitalize())
print('torna maiúscula a primeira letra de cada palavra na frase: ', frase.title())
linha()

frase = "                   Aprenda Python            " 

print('por padrão (que pode ser definido) apaga todos os espaços em branco antes e depois da string: ', frase.strip())
print('por padrão (que pode ser definido) apaga todos os espaços em branco à direita da string: ', frase.rstrip())
print('por padrão (que pode ser definido) apaga todos os espaços em branco à esquerda da string: ', frase.lstrip())

frase = "Curso em Vídeo Python"

print('divide em pedaços: ', frase.split())
print("unifica os pedaços: ", ','.join(frase))

#----------------------------------------------------------#
