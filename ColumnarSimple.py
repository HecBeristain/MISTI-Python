
def cifrar():
    matriz = [] # Lista para operar los caracteres

    #Recibe instrucciones del usuario
    textoPlano = input("¿Cual es el mensaje?: ").upper() #En mayusculas
    textoPlano = ''.join(filter(str.isalpha, textoPlano)) #Filtra los caracteres alfabeticos
    filas = int(input("¿Cuantas filas?: "))
    columnas = int(input("¿Cuantas columnas?: "))

    #Asegura que el mensaje quepa en la matriz
    if filas*columnas >= len(textoPlano): matrizSize = filas*columnas
    elif len(textoPlano) % columnas: matrizSize = len(textoPlano) + (columnas - len(textoPlano) % columnas)
    else: matrizSize = len(textoPlano)
    # El modulo nos dice si faltan espacios para la matriz cuadrada : (len(textoPlano) % columnas)
    # Restar este valor del numero de columnas no da los espacios para rellenar: (columnas - % )

    textoPlano = textoPlano.ljust(matrizSize,'X') # Agrega caracteres para completar la matriz cuadrada

    for i in textoPlano: matriz.append(i) #Texto a lista de caracteres
    matriz = [matriz[i:i+columnas] for i in range(0, len(matriz), columnas)] #Lista 2D con columnas de usuario
    matriz = [*zip(*matriz)] # Transpone la lista

    print(' '.join(map(''.join, matriz))) #Imprime el texto cifrado

def descifrar():
    matriz = [] # Lista para operar los caracteres

    #Recibe instrucciones del usuario
    textoCifrado = input("¿Cual es el mensaje?: ").casefold() #En minusculas
    filas = int(input("¿Cuantas filas?: "))
    textoCifrado = ''.join(filter(str.isalpha, textoCifrado)) #Filtra los caracteres alfabeticos

    for i in textoCifrado: matriz.append(i) #Texto a lista de caracteres
    matriz = [matriz[i:i+filas] for i in range(0, len(matriz), filas)] #Lista 2D con columnas de usuario
    matriz = [*zip(*matriz)] # Transpone la lista
    print(''.join(map(''.join, matriz))) #Imprime el texto cifrado

def menu():
    instruccion = ""
    while instruccion != "salir":
        print("\nCifrador Columnar Simple\n")
        instruccion = input("Elige una opción (Cifrar / Descifrar / Salir): ")

        if instruccion.casefold() == "salir": continue
        try: globals()[instruccion.casefold()]()
        except: print("No es una opcion valida, intentalo de nuevo", end="\n")

def main():
    menu()

if __name__ == '__main__':
    main()
