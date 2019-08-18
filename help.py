#-------------- AJUDA INTERATIVA --------------#

#help(print) # Interactive help
'''
def contador(i,f,p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')

contador(2, 10, 2)
help(contador)
'''

def somar(a=0,b=0,c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    """

    s = a + b + c
    print(f'A soma vale {s}.')

somar(3, 2 )


 