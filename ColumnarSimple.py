filas = 0
columnas = 0
texto = ""

def userInputs ():
    global filas,columnas,texto

    texto = input("¿Cual es el mensaje?: ")     #Recibe instrucciones del usuario
    texto = ''.join(filter(str.isalpha, texto)) #Filtra los caracteres alfabeticos
    filas = int(input("¿Cuantas filas?: "))
    columnas = int(input("¿Cuantas columnas?: "))

    return texto

def columnar (dimension,s):
    matriz = []  # Lista para operar los caracteres

    for i in texto: matriz.append(i) #Texto a lista de caracteres
    matriz = [matriz[i:i+dimension] for i in range(0, len(matriz), dimension)] #Lista 2D con input de usuario
    matriz = [*zip(*matriz)] # Transpone la lista

    print(s.join(map(''.join, matriz))) #Imprime el texto cifrado/descifrado

def cifrar():
    global filas,columnas,texto
    texto = userInputs().upper() #En mayusculas

    #Asegura que el mensaje quepa en la matriz
    if filas*columnas >= len(texto): matrizSize = filas*columnas
    else: matrizSize = len(texto) + (columnas - len(texto) % columnas)
    """ El modulo nos dice si faltan espacios para la matriz cuadrada : (len(texto) % columnas)
        Restar este valor del numero de columnas no da los espacios para rellenar: (columnas - % ) """

    texto = texto.ljust(matrizSize,'X') # Agrega caracteres para completar la matriz cuadrada
    columnar(columnas," ")

def descifrar():
    global filas,texto
    texto = userInputs().casefold() #En minusculas
    columnar(filas,"")

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
