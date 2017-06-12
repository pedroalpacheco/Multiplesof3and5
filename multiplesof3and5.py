"""
pedroalpacheco  -  12/06/2017

Rules:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Only numbers 3 and 5.

"""
import math

def multiple(pos):
    say = str(pos)

    if pos % 5 == 0 or pos % 3 == 0:
        say = 'mult 3 or 5'

    #Numeros que nao se encaixam acima
    return say

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
In [35]: sum(range(10))
Out[35]: 45

#Falta ver como pegar cada numero que se enquadre nos parametros de 3 e 5
        #soma = sum(range(pos))

"""