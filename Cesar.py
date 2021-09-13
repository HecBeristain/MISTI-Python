# La cifra de Cesar

alfabeto = ["a", "b", "c", "d", "e", "f", "g",
            "h", "i", "j", "k", "l", "m", "n",
            "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]



def menu():
    
    while True:
            print("\tCIFRADOR CESAR\n")
            print("¿Que deseas realizar?\n"
                  "1. Cifrar\n"
                  "2. Descifrar\n"
                  "3. Salir\n")
            opcion = input()

            if opcion == "1":
                def cifrado_cesar(alfabeto, texto):
                    texto_cifrado = ""

                    while True:
                        print("Ingrese el nivel de cifrado del 3 al 6: \n")
                        cifrado = int(input())
                        if cifrado > 3 and cifrado < 6:
                            break

                    for letra in texto:
                        if letra in alfabeto:
                            indice_actual = alfabeto.index(letra)
                            indice_cesar = indice_actual + cifrado
                            if indice_cesar > 25:
                                indice_cesar -= 25
                            texto_cifrado += alfabeto[indice_cesar]
                        else:
                            texto_cifrado += letra
                    return texto_cifrado


                print("Introduce el texto a cifrar: ")
                frase = str(input().lower())
                frase_cifrada = print("Tu texto cifrado es: ", cifrado_cesar(alfabeto, frase).upper())
                input()
            elif opcion == "2":
                def cifrado_cesar(alfabeto, texto):
                    texto_cifrado = ""

                    while True:
                        print("Ingrese el nivel para descifrar del 3 al 6: \n")
                        cifrado = int(input())
                        if cifrado > 3 and cifrado < 6:
                            break

                    for letra in texto:
                        if letra in alfabeto:
                            indice_actual = alfabeto.index(letra)
                            indice_cesar = indice_actual - cifrado
                            if indice_cesar > 25:
                                indice_cesar -= 25
                            texto_cifrado += alfabeto[indice_cesar]
                        else:
                            texto_cifrado += letra
                    return texto_cifrado


                print("Introduce tu texto para descifrar: ")
                frase = str(input().lower())
                frase_cifrada = print("Tu texto descifrado es: ", cifrado_cesar(alfabeto, frase).upper())
                input()
            elif opcion == "3":
                print("Adios")
                break
                input()