import random
import os

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b)
    return s


def run():
    with open('./DATA.txt' , 'r' , encoding='utf-8') as data:
        lista = [i.strip() for i in data]

    palabra = random.choice(lista) 
    palabra_oculta_lista = ['_' for i in range( len(palabra) )  ]
    string_palabra_oculta = "".join(palabra_oculta_lista)
    contador = 0
    letras_repetidas = []


    while len(palabra)  != contador:
        os.system("clear")
        print(f'Juguemos ahorcado, tu palabra es de {len(palabra)}  letras \n   ')
        print(string_palabra_oculta)

        letra = input('Escribe una letra:    ').lower()
        if letra in letras_repetidas:
            print(f'La letra {letra} ya la introdujiste, favor de no repetir')
            continue
        letras_repetidas.append(letra)

        if letra.isnumeric():
            print('No ingresar numeros ')
            continue

        if len(letra) != 1:
            print('No ingresar mas de una letra por favor ')
            continue
        
        iterador = 0
        for i in palabra:   
            if normalize(i) == letra:
                palabra_oculta_lista[iterador] = i
                contador += 1
            iterador += 1
   

        string_palabra_oculta = "".join(palabra_oculta_lista)

    print(f'Felicidades la palabra era {string_palabra_oculta}')
        

if __name__ == '__main__':
    run()