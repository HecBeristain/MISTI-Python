# La cifra de Cesar
alfabeto = ["a", "b", "c", "d", "e", "f", "g",
            "h", "i", "j", "k", "l", "m", "n",
            "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]

def cifrado_cesar(alfabeto,texto):
    texto_cifrado = ""

    while True:
        print("Ingrese el nivel de cifrado del 3 al 6: ")
        cifrado = int(input())
        if cifrado >3 and cifrado <6:
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

def menu():
    print("Introduce el texto a cifrar: ")
    frase = str(input().lower())
    frase_cifrada = print("Tu texto cifrado es: ", cifrado_cesar(alfabeto, frase).upper())