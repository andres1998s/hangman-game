import random
import os
from errores import intentos

def run():
    with open('./DATA.txt' , 'r' , encoding='utf-8') as data:
        lista = [i.strip() for i in data]
 
    palabra = random.choice(lista) 
    palabra_oculta_lista = ['_' for i in range( len(palabra) )  ]
    string_palabra_oculta = "".join(palabra_oculta_lista)
    errores = 0

    while palabra  != string_palabra_oculta and errores != 5:

        os.system("clear")
        print(f'Juguemos ahorcado, adivina la palabra, {len(palabra)} letras')
        print(intentos(errores))
        print(string_palabra_oculta) 
        letra = input('Presiona una tecla y despues enter    ').lower()

        iterador = 0
        for i in palabra:   
            if i == letra:
                palabra_oculta_lista[iterador] = i
            iterador += 1  
        
        version_anterior = string_palabra_oculta
        string_palabra_oculta = "".join(palabra_oculta_lista)

        if version_anterior == string_palabra_oculta:
            errores += 1
          
    if palabra == string_palabra_oculta:
        os.system("clear")
        print(f'Felicidades la palabra era  {string_palabra_oculta}')
    else:
        os.system("clear")
        print(intentos(errores))


if __name__ == '__main__':
    run()

#a partir de la linea 22 tenemos in ciclo que recorre un string y una variable que itera acompañando al 
#string pero que es independiente, de tal manera que cuando hay una coincidencia con una letra escrita por el 
#usuario accedemos a un indice de una lista y le reasignamos su valor, esto gracias a la variable iterador que va sumandose
#a si misma en cada ciclo de tal forma que coincide con los valores del objeto palabra 