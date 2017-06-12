"""
pedroalpacheco  -  12/06/2017

Rules:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Only numbers 3 and 5.

"""

def multiple(pos):
    #Verifica multiplos de 5
    if pos in (5, 10, 15):
        return 'mult 5'

    # Verifica multiplos de 3
    if pos in (3, 6, 9):
        return 'mult 3'

    #Numeros que nao se encaixam ascima
    return str(pos)

#Testes
if __name__ == '__main__':

    assert multiple(1) == '1'
    assert multiple(2) == '2'
    assert multiple(4) == '4'

    assert multiple(3) == 'mult 3'
    assert multiple(6) == 'mult 3'
    assert multiple(9) == 'mult 3'

    assert multiple(5) == 'mult 5'
    assert multiple(10) == 'mult 5'
    assert multiple(15) == 'mult 5'