# -*- coding: utf-8 -*-

def funcion_primo(arg):
    if arg<=1:
        return False
    else:
        for i in range(2,arg):
            if arg % i == 0 and arg != i:
                return False
    return True

def User_Interface():
    print('PRIME NUMBER')

    numeroAevaluar=int(input('What is the number?  '))

    resultado=funcion_primo(numeroAevaluar)

    if resultado is True:
        print(' {} is prime.'.format(numeroAevaluar))
    else:
        print('No bunny!, {} it is not prime.'.format(numeroAevaluar))


if __name__ == '__main__':
    User_Interface()
