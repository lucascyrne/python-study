#---------- C.e.V MUNDO 3 - DICIONÁRIOS -----------#

# dados = {}  -> Uma das formas de adicionar um dicionário

dados = {'nome':'Benny', 'idade':'19'}
print('-=' * 30)
print('Chamando o nome adicionado ao dicionário:', dados['nome'])
print('-=' * 30)
dados['sexo'] = 'M'
print('Adicionando dados ao sexo:', dados['sexo'])
print('-=' * 30)
del dados['idade']
print('idade deletada:', dados)
print('-=' * 30)

# usando dicionário em outra estrutura:

filme = {
    'titulo':'Star Wars',
    'ano':1977,
    'diretor':'George Lucas'
}

print('Printando valores de "filme":', filme.values())
print('-=' * 30)
print('Printando chaves de "filme":', filme.keys())
print('-=' * 30)
print('Printando valores e chaves de "filme":', filme.items())
print('-=' * 30)

print('Montando FOR para retornar valores e chaves: ')
print()
for k,v in filme.items():
    print(f'O {k} é {v}')