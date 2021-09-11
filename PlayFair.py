# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 03:56:35 2021

@author: jozic
"""

# -*- coding: utf-8 -*-
"""
Developed by Jozic Manuel Espinoza Rivera 
Play fair encode and decode
"""

"""
Function to get encode key
"""


def keyWord():
    validString = False
    global userKeyWord
    while not validString:
        userKeyWord = input("\x1b[7;31mIngresa la llave: ")
        if userKeyWord.isalpha():
            userKeyWord = userKeyWord.replace(" ", "")  # Replace spaces between word in keyword
            userKeyWord = userKeyWord.upper()  # Change all characters in key word for uppercase characters
            createMatrix()
            validString = True
        else:
            print("\n\nLa llave contiene caractares no validos")


"""
Function to define 5x5 matrix started in 0 
"""


def matrix(x, y, initial):
    return [[initial for i in range(x)] for j in range(y)]


"""
Function to construct matrix based in user key word
1.- Filter user keyword(delete duplicate characters)
2.- Filter characters in user key word and alphabet 
3.- Build 5x5 matrix
4.- Show final matrix 
"""


def createMatrix():
    global keyWordMatrix
    flag = 0
    alphabetChar = 0
    matrixList = list()
    for element in userKeyWord:  # Analyse 1 by 1 element in key word
        if element not in matrixList:
            if element == 'J':  # If element is a J do a change for I
                matrixList.append('I')
            else:
                matrixList.append(element)  # If element is in list it does not added
    print("\x1b[7;32m\nLa llave filtrada es:\n", matrixList)

    for i in range(65, 91):  # storing user keyword in ascii uppercase code (65-90)
        if chr(i) not in matrixList:  # convert ascii on char
            if i == 73 and chr(74) not in matrixList:  # If there is I and J not in user Keyword
                matrixList.append("I")
                flag = 1
            elif flag == 0 and i == 73 or i == 74:  # If element = 73(I) or 74(J) do nothing
                pass
            else:
                matrixList.append(chr(i))  # Add characters and convert to char

    keyWordMatrix = matrix(5, 5, 0)
    for raw in range(0, 5):
        for column in range(0, 5):
            keyWordMatrix[raw][column] = matrixList[alphabetChar]  # Build 5x5 matrix
            alphabetChar += 1

    print("\x1b[7;32m\nLa matriz final es:\n\n")
    for rawMatrix in keyWordMatrix:  # Show final matrix
        print(rawMatrix)


"""
Function to get location of each elemnt in message
"""


def locindex(element):
    loc = list()  # If the element is J replace it with I
    if element == 'J':
        element = 'I'
    for i, j in enumerate(keyWordMatrix):  # Search in Keyword matrix
        for k, l in enumerate(j):
            if element == l:
                loc.append(i)  # Add pair of characters
                loc.append(k)
                return loc
    print(loc)  # Show the final pair


"""
Function to encode 
"""


def encode():  # Encryption
    validString = False
    while not validString:  # Validate non alphabetic characters
        encodeText = input("\x1b[7;31m\nIngresa texto a codificar:")
        encodeText = encodeText.upper()  # Convert to uppercase
        encodeText = encodeText.replace(" ", "")  # Replace spaces
        if encodeText.isalpha():
            validString = True
        else:
            print("\n\nLa palabra a codificar contiene caractares no validos")
    print("\x1b[7;32m\nEl texto filtrado es: ", encodeText)
    i = 0
    if len(encodeText) % 2 != 0:  # If message is odd then add X at last
        encodeText = encodeText[:] + 'X'
    print("\x1b[7;32m\nTexto codificado:", end=' ')
    encodeList = list()
    while i < len(encodeText):
        loc = list()
        loc = locindex(encodeText[i])  # Search for the first in pair
        loc1 = list()
        loc1 = locindex(encodeText[i + 1])  # Search for the second in pair
        if loc[1] == loc1[1]:
            encodeList.append(keyWordMatrix[(loc[0] + 1) % 5][loc[1]])
            encodeList.append(keyWordMatrix[(loc1[0] + 1) % 5][loc1[1]])  # Same column condition
        elif loc[0] == loc1[0]:
            encodeList.append(keyWordMatrix[loc[0]][(loc[1] + 1) % 5])
            encodeList.append(keyWordMatrix[loc1[0]][(loc1[1] + 1) % 5])  # Same line condition
        else:
            encodeList.append(keyWordMatrix[loc[0]][loc1[1]])
            encodeList.append(keyWordMatrix[loc1[0]][loc[1]])  # Different both
        i = i + 2  # Location of char
    encodeText = ''.join(encodeList)
    print(encodeText)


"""
Function to decode 
"""


def decode():
    validString = False
    while not validString:  # Validate non alphabetic characters
        decodeText = input("\x1b[7;31m\nIngresa texto a decodificar:")
        decodeText = decodeText.upper()  # Covert to uppercase
        decodeText = decodeText.replace(" ", "")  # Replace spaces
        if decodeText.isalpha():
            validString = True
        else:
            print("\n\nLa palabra codificada contiene caracteres no validos")

    decodeText = decodeText.upper()  # Covert to uppercase
    decodeText = decodeText.replace(" ", "")  # Replace spaces
    print("\x1b[7;32m\nEl texto filtrado es: ", decodeText)
    print("\x1b[7;32m\nTexto decodificado:", end=' ')
    i = 0
    decodeList = list()
    while i < len(decodeText):
        loc = list()
        loc = locindex(decodeText[i])  # Search for first in pair
        loc1 = list()
        loc1 = locindex(decodeText[i + 1])  # Search for second in pair
        if loc[1] == loc1[1]:
            decodeList.append(keyWordMatrix[(loc[0] - 1) % 5][loc[1]])
            decodeList.append(keyWordMatrix[(loc1[0] - 1) % 5][loc1[1]])  # Same column condition
        elif loc[0] == loc1[0]:
            decodeList.append(keyWordMatrix[loc[0]][(loc[1] - 1) % 5])
            decodeList.append(keyWordMatrix[loc1[0]][(loc1[1] - 1) % 5])  # Same line condition
        else:
            decodeList.append(keyWordMatrix[loc[0]][loc1[1]])
            decodeList.append(keyWordMatrix[loc1[0]][loc[1]])  # Differen both
        i = i + 2  # Location of char
    decodeText = ''.join(decodeList)
    decodeText = decodeText.replace("X", "")  # Delete the final char(X)
    print(decodeText)


"""
Function to select an option
"""


def menu():
    exitProgram = False
    while not exitProgram:
        print("\x1b[1;33m" + "\n\n\n===============================")
        print("\x1b[6;36m" + "      CIFRADOR PLAYFAIR")
        print("\x1b[1;33m" + "===============================")
        choice = str(input("\x1b[6;36m" + "\n 1.-Encriptar\n 2.-Desencriptar\n 3-.Salir\n\n" + "\x1b[7;31mOpcion: "))
        if choice == "1":
            keyWord()
            encode()
        elif choice == "2":
            keyWord()
            decode()
        elif choice == "3":
            exitProgram = True
            print("Adios...")
            break
        else:
            print("Selecciona una opcion valida")


"""
Principal function
"""


def main():
    menu()

if __name__ == '__main__':
    main()
