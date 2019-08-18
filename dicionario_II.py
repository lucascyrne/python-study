#---------- C.e.V MUNDO 3 - DICIONÁRIOS - PARTE II -----------#

pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade':22}
pessoas['peso'] = 98.5
print('-=' * 30)
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print('-=' * 30)

for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-=' * 30) 

for v in pessoas.values():
    print(v)   
print('-=' * 30)


