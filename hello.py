# -*- coding: utf-8 -*-
# pep8

"""
Script de hello world criativo
Desafio lançado pelo Mateus Schwede
@see https://titotheworld.blogspot.com.br/2017/07/codinamizando-python-stage-1.html
@author Eric S. Lucinger Ruiz <eu@ericruiz.com.br>
@version 10/07/2017

testado no Ubuntu 16.04.2 LTS
com python 2.7.12
e python 3.5.2
"""
import random

# usando frase parcial para diminuir as probabilidades ;)
x = 'Hello wor'
y = ''.join(random.sample(x, len(x)))
loops = 0
limit = 1000000

print('Hello word criativo, rodando loops, aguarde..')
while True:
    if x == y or loops >= limit:
        break

    y = ''.join(random.sample(x, len(x)))
    loops += 1

print('Hello: ' + y + 'ld!!!')
print('Loops: ' + str(loops))
