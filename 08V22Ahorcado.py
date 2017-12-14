#-*- coding: utf-8 -*-
import random

IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

LISTA  = ['paracaidas']
TAMANO_LISTA=len(LISTA)
SELECCION_LISTA=random.randint(0,TAMANO_LISTA-1)
TAMANO_PALABRA=len(LISTA[SELECCION_LISTA])
preliminar=[' * ']
preliminar=preliminar*TAMANO_PALABRA

def lineas(entrada_lineas):
    unidad_linea='*___'
    total_lineas=unidad_linea*entrada_lineas
    print(total_lineas)

def rellenar(entrada):
    "para buscar dentro de la palabra"
    aux =0
    while aux<TAMANO_PALABRA:
        if LISTA[SELECCION_LISTA][aux]==entrada:
            preliminar[aux]=entrada
        aux+=1
    return preliminar

def coincidencia(arg):
    i=0
    while i<TAMANO_PALABRA:
        if LISTA[SELECCION_LISTA][i]==arg:
            return True
        else:
            i+=1
    return False

def fin_juego ():
    aux=0
    while LISTA[SELECCION_LISTA][aux]==preliminar[aux] and aux<TAMANO_PALABRA:
        aux+=1
        if aux==TAMANO_PALABRA:
            return True
    else:
        return False


if __name__=='__main__':
    print('****************A H O R C A D O****************')
    print('Palabra de {} letras \n'.format(TAMANO_PALABRA))
    print(''.join(preliminar))
    Finalizo=False
    aux1=0


    while Finalizo==False and aux1<6:
        entrada=str(input('\n\nletra ->: '))
        coincidencia(entrada)
        if coincidencia(entrada):
            rellenar(entrada)
        else:
            aux1+=1

        Finalizo=fin_juego()

        if Finalizo:
            print('{}\n{}\n \nCorrecto, {}'.format(IMAGES[aux1],''.join(preliminar),LISTA[SELECCION_LISTA]))
        elif aux1==6:
            print('\n\nTu parabla era: {} \nYUO ARE DEAD\n{}'.format(LISTA[SELECCION_LISTA], IMAGES[aux1]))
        else:
            print('{}\n{}'.format(IMAGES[aux1],''.join(preliminar)))

'''
listas
http://www.mclibre.org/consultar/python/lecciones/python-listas.html#Paso28
http://www.mclibre.org/consultar/python/lecciones/python-for.html

'''
