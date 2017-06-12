"""
pedroalpacheco  -  12/06/2017

Rules:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Only numbers 3 and 5.

"""

def multiple(pos):
    lista = range(pos)
    portres = lista[::3]
    porcinco = lista[::5]
    somatres = sum(portres)
    somacinco = sum(porcinco)
    return somatres + somacinco
"""
    say = str(pos)

    if pos % 5 == 0 or pos % 3 == 0:
        say = 'mult 3 or 5'

    #Numeros que nao se encaixam acima
    return say
"""
"""
#Testes
if __name__ == '__main__':

    assert multiple(1) == '1'
    assert multiple(2) == '2'
    assert multiple(4) == '4'

    assert multiple(3) == 'mult 3 or 5'
    assert multiple(6) == 'mult 3 or 5'
    assert multiple(9) == 'mult 3 or 5'

    assert multiple(5) == 'mult 3 or 5'
    assert multiple(10) == 'mult 3 or 5'
    assert multiple(15) == 'mult 3 or 5'


"""


"""
In [2]: num = range(10)
In [35]: sum(range(10))
Out[35]: 45

#Falta ver como pegar cada numero que se enquadre nos parametros de 3 e 5
        #soma = sum(range(pos))
        
-----------------------------------------------------------------------
In [3]: num
Out[3]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [4]: for i in num:
   ...:     if i % 3 == 0:
   ...:         print(i)
-----------------------------------------------------------------------
RESULTADO MUUUITO SIMPLES

In [10]: volt = range(10)

In [11]: volt[::3]
Out[11]: [0, 3, 6, 9]

In [12]: volt[::5]
Out[12]: [0, 5]

In [13]: volt[::5]

Total = 266333

Resposta correta:
= 166833 + 99500 - 33165 = 233168 
 

"""