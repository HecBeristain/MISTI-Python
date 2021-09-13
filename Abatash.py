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
    while True:
        print("\tCIFRADOR ATABASH\n")
        print("¿Que deseas realizar?\n"
          "1. Cifrar\n"
          "2. Descifrar\n"
          "3. Salir\n")
        opcion = input()

        if opcion == "1":
            print("\nTU VAS A CIFRAR UN MENSAJE CON ATABASH")
            #def main():
            mensaje = str(input("\nIngrese tu mensaje a cifrar: ").lower())
            print("Tu mensaje cifrado es: ", atabash(mensaje).upper())
            #if __name__ == '__main__':
            #main()
        elif opcion == "2":
            print("\nTU VAS A DESCIFRAR UN MENSAJE CON ATABASH")
            #def main():
            mensaje = str(input("\nIngrese tu mensaje a descifrar: ").lower())
            print("Tu mensaje descifrado es: ", atabash(mensaje).upper())
            #if __name__ == '__main__':
            #main()
        elif opcion == "3":
            print("Adios")
            break
        input()
        
if __name__ == '__main__':
   main()