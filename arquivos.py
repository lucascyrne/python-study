#----- ARQUIVOS -----#

# r = somente leitura
# r+ = leitura e escrita
# w = escrita, apagando o que tiver antes
# w+ = leitura e escrita.
# a = escrita, preservando o que tiver antes (append)
# b = modo binário
# + = Atualização - leitura e escrita
# x = abre o arquivo para criação exclusiva, falhando se já existir

# abrindo um arquivo

""" 
manipulador = open(arquivo, modo)

sendo "arquivo" o nome/caminho do arquivo

modo é opcional

(não é necessário importar módulo para usar isso)

método read()
    retorna o conteúdo do arquivo como uma única "string"

método readline()
    retorna uma linha do texto a cada chamada na ordem
    que aparecem no arquivo

método readlines()
    retorna lista de valores de string do arquivo, sendo 
    que cada string corresponde a uma linha do texto 

"""

# testando os métodos read(), readline(), readlines()

def linha():
    print('-=' * 40)

linha()
manipulador = open('arquivo.txt', 'r')
print('\nMétodo read()\n')
print(manipulador.read())
print()
linha()

manipulador.seek(0) # volta para o início do arquivo.txt

print("\nMétodo readline()\n")
print(manipulador.readline())
print('2ª chamada: ', manipulador.readline())
linha()

manipulador.seek(0) # volta para o início do arquivo.txt

print('\nMétodo readlines()\n')
print(manipulador.readlines())
print()

manipulador.close() # fecha conexão "open" com o arquivo.txt

linha()
linha()
linha()
linha()

print()
print('TESTE 001')
print('Abertura de arquivos com FOR em Python\n')

manipulador = open('arquivo.txt', 'r')

for linha in manipulador:
    linha = linha.rstrip()
    print(linha)

manipulador.close()

print()
print('TESTE 002')
print('Contando as linhas do arquivo de texto analisado:\n')

contador = 0
arq = open('arquivo.txt', 'r')
for linha in arq:
    contador += 1
print("Número de linhas no arquivo: ", contador)

arq.close()

print()
print('TESTE 003')
print('Retornando somente as linhas que possuem "Python".\n')

arq = open('arquivo.txt', 'r')
contador = 0
for linha in arq:
    linha = linha.rstrip()
    if 'Python' in linha:
        contador += 1
        print(f'Linhas com "Python": {linha}')
arq.close()

print()
print('TESTE 004')
print('Retorne linhas que contenham palavra inputada.\n')

user = input('Digite a palavra para busca: ')
arq = open('arquivo.txt', 'r')
contador = 0
for linha in arq:
    linha = linha.rstrip()
    if user in linha:
        contador += 1
        print(f'Linhas com "{user}": {linha}')
arq.close()


arq = open('arquivo.txt', 'r')