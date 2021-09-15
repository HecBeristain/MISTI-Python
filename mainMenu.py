"""
Escriba un programa, que dado un menú,el usuario pueda seleccionar la figura geométrica,
para obtener el área de su selección (rectangulo, triángulo, rombo y trapecio).
"""
#Importar los codificadores
import Abatash
import Cesar
import Bellaso
import PlayFair
import ColumnarSimple

instruccion = 0

#Menu principal
while int(instruccion) != 6:

    # Encabezado
    print("\x1b[1;33m" + "\t====================================================")
    print("\x1b[6;36m" + "\t             PROGRAMACION CON PYTHON")
    print("\x1b[1;33m" + "\t====================================================")
    print("\x1b[1;31m" + "\t====================================================")
    print("\x1b[6;32m" + "\t            Beristain Bermudez Hector")
    print("\x1b[6;32m" + "\t            Del Angel Aquino Eduardo")
    print("\x1b[6;32m" + "\t          Espinoza Rivera Jozic Manuel")
    print("\x1b[6;32m" + "\t         Suarez Rodriguez Daniel Hassan")
    print("\x1b[1;31m" + "\t====================================================")
    print("\x1b[1;33m" + "\t====================================================")
    print("\x1b[6;36m" + "\t                   CIFRADORES")
    print("\x1b[1;33m" + "\t====================================================")
    print("\x1b[6;36m"+"\t\t          SELECCIONA UN CIFRADOR\n")
    print("\x1b[6;32m"+"\t                1.- ABATASH")
    print("\x1b[6;32m"+"\t                2.- CESAR")
    print("\x1b[6;32m"+"\t                3.- BELLASO")
    print("\x1b[6;32m"+"\t                4.- PLAYFAIR")
    print("\x1b[6;32m"+"\t                5.- COLUMNAR SIMPLE")
    print("\x1b[6;32m"+"\t                6.- FIN\n")

    instruccion = input("\x1b[1;31m"+"\t                Opcion: ")
    #try:
    if int(instruccion) == 6: continue     #Salta al condicional del while si recibe una instrucción de paro
    elif int(instruccion) == 5: ColumnarSimple.menu()
    elif int(instruccion) == 4: PlayFair.menu()
    elif int(instruccion) == 3: Bellaso.menu()
    elif int(instruccion) == 2: Cesar.menu()
    elif int(instruccion) == 1: Abatash.menu()
    #except:
    #    print(str(instruccion) + " no es una opcion valida, intentalo de nuevo", end="\n")
    #    instruccion = 0

#Fin del Menu
