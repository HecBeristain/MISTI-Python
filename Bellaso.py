# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 21:44:18 2021

@author: Daniel
"""

import os

from IPython.display import clear_output
from IPython import get_ipython
import numpy as np
import time
import math
from numpy import array

get_ipython().magic('clear')
os.system('cls')
clear_output(wait=True)

Dict = {"A": "a", "B": "b", "C": "c", "D": "d", "E": "e", "F": "f", "G": "g",
        "H": "h", "I": "i", "J": "j", "K": "k", "L": "l", "M": "m", "N": "n",
        "O": "o", "P": "p", "Q": "q", "R": "r", "S": "s", "T": "t", "U": "u",
        "V": "v", "W": "w", "X": "x", "Y": "y", "Z": "z", " ": " "}

Dict1 = {"a": "A", "b": "B", "c": "C", "d": "D", "e": "E", "f": "F", "g": "G",
         "h": "H", "i": "I", "j": "J", "k": "K", "l": "L", "m": "M", "n": "N",
         "o": "O", "p": "P", "q": "Q", "r": "R", "s": "S", "t": "T", "u": "U",
         "v": "V", "w": "W", "x": "X", "y": "Y", "z": "Z", " ": " "}


def Clear_Screen():
    get_ipython().magic('clear')
    os.system('cls')
    clear_output(wait=True)


def May2Min(Word0):  ###  Convertidor de Mayusculas a minusculas
    Word1 = ""
    for i in range(0, len(Word0)):
        # print(i)
        if ((Word0[i] in Dict) == True):
            Word1 = Word1 + Dict[Word0[i]]
            # print("hola")
        else:
            Word1 = Word1 + Word0[i]
            # print("no")
    return Word1


def Min2May(Word1):  #####  Convertidor de inusculas a Mayusculas
    Word0 = ""
    for i in range(0, len(Word1)):
        # print(i)
        if ((Word1[i] in Dict1) == True):
            Word0 = Word0 + Dict1[Word1[i]]
            # print("hola")
        else:
            Word0 = Word0 + Word1[i]
            # print("no")
    return Word0


def Alphas():  ########  Construir alfabetos desde los diccionarios
    global Alpha_0, Alpha_1
    Alpha_0 = list(Dict.keys())  ##### A. Mayusculas
    Alpha_0.remove(" ")  ######## Eliminar elemento " "
    Alpha_1 = list(Dict.values())  ##### A. Minusculas
    Alpha_1.remove(" ")


def Build_Alpha():
    global up, down, Alpha_m, min_pass, Alpha_temp, Alpha_R, Alpha_L
    NN, MM = 2, 13

    Alpha_R = [["" for x in range(26)] for i in range(5)]  ### Alfabeto derecha (min)
    # print(a)
    Alpha_L = [["" for x in range(6)] for i in range(5)]
    up = math.ceil(len(Password[0]) / 2)
    down = len(Password[0]) - up
    min_pass = May2Min(Password[0])

    ################ COMPLETAR ALFABETOS DERECHOS   (Alpha_R)
    space_down = 0
    for j in range(5):
        # print("j es: %d" % j)
        Alpha_temp = list(Alpha_1)
        # print(Alpha_temp)
        for i in range(len(min_pass)):
            # print(i)
            # print(min_pass[i])
            Alpha_temp.remove(min_pass[i])  ##### Remover password del alfabeto completo

        # Alpha_R [j][i]
        for i in range(13):
            # print(i)
            if i <= (up - 1):  ##  Rango de la primer mitad de la pass1
                Alpha_R[j][i] = min_pass[i]
            else:
                Alpha_R[j][i] = Alpha_temp[i - up]
                # Alpha_R = A

        #             Password
        # index2 = 26 - len(min_pass)
        for i in range(13, 26):
            # print(space_down)
            # print("hola")
            # print(i)
            if ((i >= 13 + space_down) & (i <= (13 + space_down + down - 1))):
                # print("here")
                Alpha_R[j][i] = min_pass[i - 13 - space_down + up]

            elif ((space_down >= 1) & (i < 13 + space_down)):

                Alpha_R[j][i] = Alpha_temp[len(Alpha_temp) - 13 + i - space_down]

            elif ((space_down >= 1) & (i > (13 + space_down + down - 1))):

                Alpha_R[j][i] = Alpha_temp[i - down - up - space_down]


            else:
                Alpha_R[j][i] = Alpha_temp[i - down - up]
        space_down = space_down + 1
        ########   COMPLETAR ALFABETO IZQUIERDO  (Alpha_L)
    desplazar = 0;
    N_Letra = 0;
    for j in range(6):
        for i in range(5):
            if N_Letra <= 25:
                Alpha_L[i][j] = Min2May(Alpha_R[0][N_Letra])
                N_Letra = N_Letra + 1


def Pass1_Fix():
    global Pass1_F
    Pass1_F = ""
    for i in range(len(Password[1])):
        if (Password[1][i] != " "):
            Pass1_F = Pass1_F + Password[1][i]
    # print(Pass1_F)


def Codec1():
    global Word, Word_May, Word_Min, Translation, Word_len, Letter_1, index, space

    print("Entrada:")
    Word = str(input());
    Word_May = Min2May(Word)
    Word_Min = May2Min(Word)
    # print(Word_May)
    # print(Word_Min)
    Word_len = len(Word)

    Translation = ""
    Letter_1 = 1

    index = 0
    space = 0

    I_Pass1 = 0
    # index_Pass1 = 0

    for i in range(Word_len):

        # print(Word_len)
        if (Letter_1 == 1) & (Word_May[i] != " "):  ### letra inicial =! espacio

            # print(Letter_Pass1)
            Letter_1 = 0

            for j in range(5):
                if (Pass1_F[I_Pass1] in Alpha_L[j]) == True:
                    # print (Pass1_F[I_Pass1])
                    index = j

                    # print(index)
                    Codec2(index, Word_Min[i])
                    Letter_1 = 0



        elif Word_May[i] == " ":
            Translation = Translation + " "
            Letter_1 = 1
            I_Pass1 = I_Pass1 + 1
        else:
            index = index + 1
            if index >= 5:
                index = 0
            # print(index)
            Codec2(index, Word_Min[i])

        if I_Pass1 >= len(Pass1_F):
            I_Pass1 = 0


def Codec2(N_Alfabeto, Letter):
    global Translation
    position = Alpha_R[N_Alfabeto].index(Letter)
    pos = 0
    if position < 13:
        pos = position + 13

    else:
        pos = position - 13
    Translation = Translation + Alpha_R[N_Alfabeto][pos]
    # print(position)


def P_Translate():
    global Translation, Translation1
    if sel == 1:  #####   Codificar
        Translation = Min2May(Translation)
    elif sel == 2:  #####   Decodificar
        Translation = May2Min(Translation)
        # print("Prueba")
        # print(Translation)
        Translation1 = ""
        for i in range(len(Translation)):
            # print(i)

            if i == 0:
                Translation1 = Translation1 + Min2May(Translation[i])
                # print(Translation1)
            else:
                Translation1 = Translation1 + Translation[i]
        Translation = Translation1

    print("")
    print("Salida:")
    print("")
    print(Translation)
    # print(Translation1)


def menu():
    global sel
    fin = 0
    while fin == 0:
        print("         Codificador Bellasco       ")
        print("Seleccione una opcion:")
        print("1. Codificar")
        print("2. Decodificar")
        print("3. Salir")
        seleccion = int(input())

        if (isinstance(seleccion, int) == False) | (seleccion < 1) | (seleccion > 3):
            print("Opción no válida")
        elif seleccion == 1:
            sel = seleccion
            Clear_Screen()
            print("Codificar con Bellasco")
            Codec1()
            P_Translate()

        elif seleccion == 2:
            sel = seleccion
            Clear_Screen()
            print("Decodificar con Bellasco")
            Codec1()
            P_Translate()
        elif seleccion == 3:
            fin = 1
            Clear_Screen()
            print("Hasta pronto")

        print("")


# Password = ("IOVe","OSCILLATE WILDLY")
Password = ("IOVe", "AVE MARIA GRATIA PLENA")

Alphas()
Build_Alpha()
Pass1_Fix()
# print(Alpha_R)
# print(Alpha_temp)
Menu_Inicial()
# Codec1()
# P_Translate()


# print(Alpha_R[0][0:13])
# print(Alpha_R[0][13:26])
# print("")
# print(Alpha_R[1][0:13])
# print(Alpha_R[1][13:26])
# print("")
# print(Alpha_R[2][0:13])
# print(Alpha_R[2][13:26])
# print("")
# print(Alpha_R[3][0:13])
# print(Alpha_R[3][13:26])
# print("")
# print(Alpha_R[4][0:13])
# print(Alpha_R[4][13:26])

