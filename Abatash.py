# La cifra ATABASH
Alfabeto = {'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v',
            'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q',
            'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l',
            'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g',
            'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a'}

def atabash(mensaje):
    cifrar = ''
    for letra in mensaje:
        if (letra != ' '):
            cifrar += Alfabeto[letra]
        else:
            cifrar += ' '
    return cifrar

def menu():
    mensaje = str(input("\nIngrese tu mensaje a cifrar: ").lower())
    print("Tu mensaje cifrado es: ", atabash(mensaje).upper())

if __name__ == '__main__':
   main()